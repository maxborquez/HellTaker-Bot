import time
import csv
import keyboard
import tkinter as tk
import pygetwindow as gw
import win32gui
import threading

stop_sequence = False

def read_key_sequence(file_name):
    sequence = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            key, time_str = row
            sequence.append((key, time_str))
    return sequence

def play_sequence(sequence):
    global stop_sequence
    stop_sequence = False

    def play():
        global stop_sequence
        for key, time_str in sequence:
            if stop_sequence:
                stop_sequence = False
                break
            millis = float(time_str) / 1000
            print(f"'{key}' - {millis * 1000} milliseconds...")
            keyboard.press(key)
            time.sleep(0.1)
            keyboard.release(key)
            time.sleep(millis)

    threading.Thread(target=play).start()

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

def stop_sequence():
    global stop_sequence
    stop_sequence = True

def show_buttons(tipo):
    global additional_labels

    if tipo == "HellTaker":
        helltaker_button.pack_forget()
        examtaker_button.pack_forget()
        window.geometry("240x600")
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
            ("Judgement complete", "./data/Judgement.csv"),
            ("Judgement stage 1", "./data/Judgement-stage1.csv"),
            ("Judgement stage 2", "./data/Judgement-stage2.csv"),
            ("Judgement stage 3", "./data/Judgement-stage3.csv"),
            ("Judgement stage 4", "./data/Judgement-stage4.csv")
        ]
    elif tipo == "ExamTaker":
        helltaker_button.pack_forget()
        examtaker_button.pack_forget()
        window.geometry("240x450")
        buttons_info = [
            ("I", "./data/EX-I.csv"),
            ("II", "./data/EX-II.csv"),
            ("III", "./data/EX-III.csv"),
            ("IV", "./data/EX-IV.csv"),
            ("V", "./data/EX-V.csv"),
            ("VI", "./data/EX-VI.csv"),
            ("Examtaker Boss Complete", "./data/EXB-complete.csv"),
            ("Boss stage 1", "./data/EXB-stage1.csv"),
            ("Boss stage 2", "./data/EXB-stage2.csv"),
            ("Boss stage 3", "./data/EXB-stage3.csv")
        ]

    for texto, archivo in buttons_info:
        boton = tk.Button(window, text=texto, command=lambda archivo=archivo: start_sequence(archivo), bg="#3B3A4F", fg="white")
        boton.pack(pady=5)
        additional_buttons.append(boton)

        if texto in ["Judgement complete", "Examtaker Boss Complete"]:
            label = tk.Label(window, text="Or", bg="#AB333E", fg="white")
            label.pack()
            or_labels.append(label)

    back_button = tk.Button(window, text="Back", command=show_home, bg="white", fg="black")
    back_button.pack(pady=5)
    additional_buttons.append(back_button)

    stop_button = tk.Button(window, text="Stop", command=stop_sequence, bg="red", fg="white")
    stop_button.pack(pady=5)
    additional_buttons.append(stop_button)

def show_home():
    for boton in additional_buttons:
        window.geometry("240x150")
        boton.pack_forget()
    for label in or_labels:
        label.pack_forget()
    helltaker_button.pack(pady=20)
    examtaker_button.pack(pady=20)

def create_window():
    global window, helltaker_button, examtaker_button, additional_buttons, or_labels
    window = tk.Tk()
    window.title("HellBot")
    window.geometry("240x150")
    window.configure(bg="#AB333E")
    window.iconbitmap('./assets/icon.ico')

    additional_buttons = []
    or_labels = []

    helltaker_button = tk.Button(window, text="HellTaker", command=lambda: show_buttons("HellTaker"), bg="#3B3A4F", fg="white")
    helltaker_button.pack(pady=20)

    examtaker_button = tk.Button(window, text="ExamTaker", command=lambda: show_buttons("ExamTaker"), bg="#3B3A4F", fg="white")
    examtaker_button.pack(pady=20)

    window.mainloop()

if __name__ == "__main__":
    create_window()
