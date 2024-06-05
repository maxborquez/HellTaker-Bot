import time
import csv
import keyboard
import tkinter as tk
import pygetwindow as gw
import win32gui

def read_key_sequence(file_name):
    sequence = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            key, time_str = row
            sequence.append((key, time_str))
    return sequence

def play_sequence(sequence):
    for key, time_str in sequence:
        millis = float(time_str) / 1000
        print(f"'{key}' - {millis * 1000} milliseconds...")
        keyboard.press(key)
        time.sleep(0.1)
        keyboard.release(key)
        time.sleep(millis)

def start_sequence(file_name):
    window = gw.getWindowsWithTitle("Helltaker")
    if window:
        hwnd = win32gui.FindWindow(None, window[0].title)
        win32gui.SetForegroundWindow(hwnd)
        time.sleep(1)
        sequence = read_key_sequence(file_name)
        play_sequence(sequence)
    else:
        print("Helltaker window not found.")

def show_buttons(tipo):
    if 'helltaker_button' in globals():
        window.geometry("200x400")
        helltaker_button.pack_forget()
    if 'examtaker_button' in globals():
        window.geometry("200x400")
        examtaker_button.pack_forget()

    if tipo == "HellTaker":
        buttons_info = [
            ("I", "./data/I.csv"),
            ("II", "./data/II.csv"),
            ("III", "./data/III.csv"),
            ("IV", "./data/IV.csv"),
            ("V", "./data/V.csv"),
            ("VI", "./data/VI.csv"),
            ("VII", "./data/VII.csv"),
            ("VIII", "./data/VIII.csv"),
            ("IX", "./data/IX.csv"),
            ("Judgement", "./data/Judgement.csv")
        ]
    elif tipo == "ExamTaker":
        buttons_info = [
            ("I", "./data/EX-I.csv"),
            ("II", "./data/EX-II.csv"),
            ("III", "./data/EX-III.csv"),
            ("IV", "./data/EX-IV.csv"),
            ("V", "./data/EX-V.csv"),
            ("VI", "./data/EX-VI.csv"),
            ("Examtaker Boss Complete", "./data/EXB-complete.csv"),
            ("Boss Phase 1", "./data/EXB-1phase.csv"),
            ("Boss Phase 2", "./data/EXB-2phase.csv"),
            ("Boss Phase 3", "./data/EXB-3phase.csv")
        ]

    for texto, archivo in buttons_info:
        boton = tk.Button(window, text=texto, command=lambda archivo=archivo: start_sequence(archivo), bg="#3B3A4F", fg="white")
        boton.pack(pady=5)
        additional_buttons.append(boton)

    back_button = tk.Button(window, text="Back", command=show_home, bg="white", fg="black")
    back_button.pack(pady=5)
    additional_buttons.append(back_button)

def show_home():
    for boton in additional_buttons:
        window.geometry("200x150")
        boton.pack_forget()
    helltaker_button.pack(pady=20)
    examtaker_button.pack(pady=20)

def create_window():
    global window, helltaker_button, examtaker_button, additional_buttons
    window = tk.Tk()
    window.title("HellBot")
    window.geometry("240x150")
    window.configure(bg="#AB333E")
    window.iconbitmap('./assets/icon.ico')

    additional_buttons = []

    helltaker_button = tk.Button(window, text="HellTaker", command=lambda: show_buttons("HellTaker"), bg="#3B3A4F", fg="white")
    helltaker_button.pack(pady=20)

    examtaker_button = tk.Button(window, text="ExamTaker", command=lambda: show_buttons("ExamTaker"), bg="#3B3A4F", fg="white")
    examtaker_button.pack(pady=20)

    window.mainloop()

if __name__ == "__main__":
    create_window()
