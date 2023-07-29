import os
import tkinter as tk
from tkinter import filedialog


def get_clipboard_text():
    root =tk.Tk()
    root.withdraw()
    return root.clipboard_get()


def save_text_to_file(text):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path,"w",encoding="utf-8") as file:
            file.write(text)


if __name__ == "__main__":
    try:
        copied_text = get_clipboard_text()
        if copied_text:
            save_text_to_file(copied_text)
            print("Text has been successfully saved to a file.")
        else:
            print("Clipboard is empty. Nothing to save.")
    except Exception as e:
        print(f"An error occurred: {e}")