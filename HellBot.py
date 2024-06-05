import csv
import time
import keyboard
import pyautogui

def leer_secuencia_de_teclas():
    secuencia = []
    with open('keys.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            tecla, tiempo_str = row  # Desempaqueta la fila en tecla y tiempo
            secuencia.append((tecla, tiempo_str))  # Almacena como tupla
    return secuencia


def reproducir_secuencia(secuencia):
    for tecla, tiempo_str in secuencia:
        tiempo = float(tiempo_str) / 1000  # Convertir a segundos
        print(f"'{tecla}' - {tiempo * 1000} milisegundos...")
        keyboard.press(tecla)
        time.sleep(0.1)  # Pequeño tiempo de espera antes de liberar la tecla
        keyboard.release(tecla)
        time.sleep(tiempo)  # Esperar el tiempo especificado antes de la siguiente tecla


if __name__ == "__main__":
    input("Presiona Enter para cambiar al juego Helltaker.")
    pyautogui.getWindowsWithTitle("Helltaker")[0].activate()
    time.sleep(1)  # Esperar 1 segundo antes de empezar a presionar las teclas
    secuencia = leer_secuencia_de_teclas()
    reproducir_secuencia(secuencia)
