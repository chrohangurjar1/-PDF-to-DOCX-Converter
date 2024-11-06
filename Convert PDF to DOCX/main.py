import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2docx import Converter

# Function to convert PDF to DOCX
def convert_pdf_to_docx(pdf_path, docx_path):
    cv = Converter(pdf_path)
    cv.convert(docx_path, start=0, end=None)
    cv.close()
    messagebox.showinfo("Success", f"PDF converted successfully to {docx_path}!")

# Function to handle file selection and conversion
def select_pdf():
    pdf_path = filedialog.askopenfilename(
        title="Select PDF File",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if pdf_path:
        docx_path = filedialog.asksaveasfilename(
            title="Save DOCX File",
            defaultextension=".docx",
            filetypes=[("Word Documents", "*.docx")]
        )
        if docx_path:
            convert_pdf_to_docx(pdf_path, docx_path)

# Initialize the main window
root = tk.Tk()
root.title("PDF to DOCX Converter")
root.geometry("300x150")

# Create a button to select and convert the PDF
convert_button = tk.Button(
    root, text="Select PDF to Convert", command=select_pdf, padx=10, pady=10
)
convert_button.pack(pady=20)

# Run the GUI
root.mainloop()
