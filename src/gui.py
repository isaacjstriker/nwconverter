import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES
from converter import convert_csv

class CSVConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV Converter")

        self.label = tk.Label(root, text="Drag and drop a CSV file here or click to select")
        self.label.pack(pady=20)

        self.label.bind("<Button-1>", self.select_file)
        self.root.drop_target_register(DND_FILES)
        self.root.dnd_bind('<<Drop>>', self.drop_file)

    def select_file(self, event):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.convert_file(file_path)

    def drop_file(self, event):
        file_path = event.data.strip('{}')
        if file_path:
            self.convert_file(file_path)

    def convert_file(self, file_path):
        output_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if output_path:
            convert_csv(file_path, output_path)
            messagebox.showinfo("Success", "File converted successfully!")

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = CSVConverterApp(root)
    root.mainloop()