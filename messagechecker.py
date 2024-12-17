import tkinter as tk
from tkinter import messagebox
from textblob import TextBlob

def spelling_check():
    text = input_text.get("1.0","end-1c")
    if not text.strip():
        messagebox.showwarning("Warning","Enter the text to check the spelling")
        return
    try:
        blob = TextBlob(text)
        correct_text = blob.correct()
        output_text.delete("1.0",tk.END)
        output_text.insert(tk.END,correct_text)
    except Exception as e:
        messagebox.showerror("error{e}")

root=tk.Tk()
root.title("Spelling checker")
root.geometry("500x400")
root.resizable(False,False)
root.configure(bg="Black")

title_label = tk.Label(root,text="Spelling checker",font=("Arial",18,"bold"), bg="Black")
title_label.pack(pady=10)

input_label = tk.Label(root, text="ENter the text")
input_label.pack()

input_text=tk.Text(root)
input_text.pack()


check_button = tk.Button(root , text="Check spelling", command=spelling_check)
check_button.pack()

output_label = tk.Label(root, text="Corrected Text:", font=("Arial", 12), bg="#f0f0f0")
output_label.pack()

# Output Text Box
output_text = tk.Text(root, height=7, width=55, font=("Arial", 12), bg="#e6e6e6")
output_text.pack(pady=5)

# Run the Application
root.mainloop()
