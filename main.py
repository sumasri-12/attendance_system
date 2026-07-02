import tkinter as tk
from tkinter import messagebox
import os

def register():
    os.system("python register.py")

def train():
    os.system("python train.py")
    messagebox.showinfo("Success", "Training Completed!")

def attendance():
    os.system("python attendance.py")

def view_attendance():
    if os.path.exists("attendance.csv"):
        os.system("notepad attendance.csv")
    else:
        messagebox.showerror("Error", "Attendance file not found!")

root = tk.Tk()
root.title("Face Recognition Attendance System")
root.geometry("500x400")

title = tk.Label(
    root,
    text="Attendance Management System",
    font=("Arial", 18, "bold")
)
title.pack(pady=20)

btn1 = tk.Button(
    root,
    text="Register Student",
    width=25,
    height=2,
    command=register
)
btn1.pack(pady=10)

btn2 = tk.Button(
    root,
    text="Train Model",
    width=25,
    height=2,
    command=train
)
btn2.pack(pady=10)

btn3 = tk.Button(
    root,
    text="Take Attendance",
    width=25,
    height=2,
    command=attendance
)
btn3.pack(pady=10)

btn4 = tk.Button(
    root,
    text="View Attendance",
    width=25,
    height=2,
    command=view_attendance
)
btn4.pack(pady=10)

btn5 = tk.Button(
    root,
    text="Exit",
    width=25,
    height=2,
    command=root.destroy
)
btn5.pack(pady=10)

root.mainloop()