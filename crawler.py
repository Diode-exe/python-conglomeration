import os
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

visited = set()

def download(url, folder):
    local_path = safe_filename(url)
    full_path = os.path.join(folder, local_path)

    # If the path exists and is a file but we need a folder, fix it
    dir_name = os.path.dirname(full_path)
    if os.path.isfile(dir_name):
        print(f"Warning: {dir_name} is a file, but a directory is needed. Removing the file.")
        os.remove(dir_name)

    os.makedirs(dir_name, exist_ok=True)

    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(full_path, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {url} -> {full_path}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")
    return full_path




def download(url, folder):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return None
    local_path = os.path.join(folder, safe_filename(url).lstrip("/"))
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    with open(local_path, "wb") as f:
        f.write(response.content)
    print(f"Saved {url} -> {local_path}")
    return local_path if "text/html" in response.headers.get("Content-Type", "") else None

def rewrite_html(file_path, folder):
    with open(file_path, "rb") as f:
        soup = BeautifulSoup(f, "html.parser")
    tags = {"img": "src", "script": "src", "link": "href", "a": "href"}
    for tag, attr in tags.items():
        for element in soup.find_all(tag):
            link = element.get(attr)
            if not link:
                continue
            full_url = urljoin(f"file://{file_path}", link)
            parsed = urlparse(full_url)
            if parsed.netloc:  # Only rewrite links that were downloaded
                local_file = safe_filename(full_url).lstrip("/")
                element[attr] = os.path.relpath(local_file, start=os.path.dirname(file_path))
    with open(file_path, "wb") as f:
        f.write(soup.prettify("utf-8"))

def crawl(url, folder, domain):
    if url in visited:
        return
    visited.add(url)
    html_path = download(url, folder)
    if not html_path:
        return
    with open(html_path, "rb") as f:
        soup = BeautifulSoup(f, "html.parser")
    tags = {"img": "src", "script": "src", "link": "href", "a": "href"}
    for tag, attr in tags.items():
        for element in soup.find_all(tag):
            link = element.get(attr)
            if not link:
                continue
            full_url = urljoin(url, link)
            parsed_full = urlparse(full_url)
            if parsed_full.netloc != domain:
                continue  # Stay inside the same site
            if tag == "a":
                crawl(full_url, folder, domain)
            else:
                download(full_url, folder)
    rewrite_html(html_path, folder)

if __name__ == "__main__":
    start_url = input("Enter the URL to mirror: ").strip()
    if not start_url.startswith("http"):
        start_url = "http://" + start_url
    domain = urlparse(start_url).netloc
    folder = domain.replace(".", "_")
    os.makedirs(folder, exist_ok=True)
    crawl(start_url, folder, domain)
