import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile
import os

def zip_files():
    files = filedialog.askopenfilenames(title="Select Files to Zip")
    if not files:
        return

    zip_path = filedialog.asksaveasfilename(defaultextension=".zip", filetypes=[("Zip files", "*.zip")])
    if not zip_path:
        return

    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))
    
    messagebox.showinfo("Success", f"Files zipped to {zip_path}")

def zip_folder():
    folder = filedialog.askdirectory(title="Select Folder to Zip")
    if not folder:
        return

    zip_path = filedialog.asksaveasfilename(defaultextension=".zip", filetypes=[("Zip files", "*.zip")])
    if not zip_path:
        return

    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, _, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder)
                zipf.write(file_path, arcname)
    
    messagebox.showinfo("Success", f"Folder zipped to {zip_path}")

def unzip_file():
    zip_path = filedialog.askopenfilename(filetypes=[("Zip files", "*.zip")], title="Select ZIP File to Extract")
    if not zip_path:
        return

    extract_path = filedialog.askdirectory(title="Select Destination Folder")
    if not extract_path:
        return

    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(extract_path)
    
    messagebox.showinfo("Success", f"Extracted to {extract_path}")

# UI Setup
root = tk.Tk()
root.title("ZIP/UNZIP Tool")
root.geometry("300x200")
root.resizable(False, False)

tk.Label(root, text="ZIP / UNZIP Tool", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="📁 Zip Files", width=25, command=zip_files).pack(pady=5)
tk.Button(root, text="📂 Zip Folder", width=25, command=zip_folder).pack(pady=5)
tk.Button(root, text="📦 Unzip File", width=25, command=unzip_file).pack(pady=5)

root.mainloop()
