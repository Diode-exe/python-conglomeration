import speedtest
import tkinter as tk
from tkinter import simpledialog, messagebox
import threading
import datetime

global download_speed, upload_speed, ping, server_name

download_speed = 0
upload_speed = 0
ping = 0
server_name = "Unknown"

# Create the main window
root = tk.Tk()
root.title("Speedtest")
root.geometry("310x250")
try:
    icon = tk.PhotoImage(file="speedometer.gif")
    root.iconphoto(True, icon)
except tk.TclError:
    messagebox.showerror("Program error!", "Program icon not found! Program will still run...")

# Labels for displaying results (using StringVar for dynamic updates)
download_var = tk.StringVar()
upload_var = tk.StringVar()
server_var = tk.StringVar()
ping_var = tk.StringVar()

tk.Label(root, text="Speedtest", font=("Arial", 18)).pack(pady=5)
tk.Label(root, textvariable=download_var, font=("Arial", 12)).pack()
tk.Label(root, textvariable=upload_var, font=("Arial", 12)).pack()
tk.Label(root, textvariable=server_var, font=("Arial", 10)).pack()
tk.Label(root, textvariable=ping_var, font=("Arial", 10)).pack()

download_var.set("Download Speed: Press 'Start Speedtest'...")
upload_var.set(f"Upload Speed: Press 'Start Speedtest'...")

def run_speedtest():
    download_var.set("Connecting...")
    upload_var.set("Connecting...")
    try:
        wifi = speedtest.Speedtest(secure=True)
    except speedtest.ConfigRetrievalError:
        messagebox.showerror("Connection error", "Connection error. Make sure you're connected to the internet and that " \
        "the speedtester isn't blocked.")
        start_button.config(text="Start Speedtest", state="normal")
    global download_speed, upload_speed, ping, server_name
    server_var.set("Getting best server... (May take a while, sorry)")
    try:
        server = wifi.get_best_server()
        server_name = f"{server['sponsor']} ({server['name']}, {server['country']})"
    except Exception as e:
        server_name = "Error finding server"
        messagebox.showerror("Server Error", f"Could not find best server. Error: {e}")
        server_var.set("Server: Error finding server")
        download_var.set("Download Speed: Test aborted")
        upload_var.set("Upload Speed: Test aborted")
        ping_var.set("Ping: Test aborted")
        start_button.config(text="Start Speedtest", state="normal")
        return
    server_var.set(f"Server: {server_name}")
    download_var.set("Download Speed: Testing...")
    upload_var.set(f"Upload Speed: Testing...")
    ping_var.set(f"Ping: Testing...")
    root.update_idletasks()
    try:
        download_speed = wifi.download() / 1_000_000  # Convert to Mbit/s
        upload_speed = wifi.upload() / 1_000_000
        ping = wifi.results.ping
    except Exception as e:
        download_var.set(f"Download Speed: Error - {e}")
        upload_var.set(f"Upload Speed: Error - {e}")
        ping_var.set("Ping: Test aborted")
        start_button.config(text="Start Speedtest", state="normal")
        return


    download_var.set(f"Download Speed: {download_speed:.2f} Mbps")
    upload_var.set(f"Upload Speed: {upload_speed:.2f} Mbps")
    ping_var.set(f"Ping: {ping} ms")
    start_button.config(text="Start Speedtest", state="normal")

def speedtest_func():
    start_button.config(text="Testing...", state="disabled")
    threading.Thread(target=run_speedtest).start()


def save_results_to_file():
    if server_name == "Unknown":
        messagebox.showerror("Saving error", "No data to save. Run the speedtest first.")
        return
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    try:
        with open ("speedtest_results.txt", "a") as file:
                file.write(f"Time/Date: {timestamp}\n")
                file.write(f"Server: {server_name}\n")
                file.write(f"Download Speed: {download_speed:.2f} Mbps\n")
                file.write(f"Upload Speed: {upload_speed:.2f} Mbps\n")
                file.write(f"Ping: {ping} ms\n")
                file.write("-" * 30 + "\n")
        messagebox.showinfo(f"Saved", "Saved results to speedtest_results.txt")
    except Exception as e:
        messagebox.showerror(f"Error", "Error: {e}")
# Button to start the test
start_button = tk.Button(root, text="Start Speedtest", command=speedtest_func)
start_button.pack(pady=10)
tk.Button(root, text="Save to file", command=save_results_to_file).pack(pady=10)


root.mainloop()