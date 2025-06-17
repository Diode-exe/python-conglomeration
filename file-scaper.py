import os

def search_files(root_dir, search_string):
    for foldername, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            if "collected_html" in file_path:
                print("collected_html, not reading")
            if "html" in filename:
                print(f"[FOUND] {filename}")
            try:
                if "collected_html" not in file_path:
                    with open("scraper_name_results.txt", 'a') as file:
                        file.write(f"{filename}\n")
                else:
                    print("Collected HTML, not reading")
            except Exception as e:
                print(f"Error : {e}")
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    for line_num, line in enumerate(file, start=1):
                        if search_string in line:
                            print(f"[FOUND] {file_path} (Line {line_num}): {line.strip()}")
            except Exception as e:
                print(f"[ERROR] Cannot read {file_path}: {e}")

if __name__ == "__main__":
    root = "/home/rohan/web.archive.org/"
    query = input("Enter the string to search for: ").strip()
    search_files(root, query)
