import tkinter as tk


# Создаём окно с краткой информацией о студенте
window = tk.Tk()
window.title("Моя визитка")
window.geometry("350x250")

name_label = tk.Label(window, text="Антоний", font=("Arial", 20))
name_label.pack(pady=20)

status_label = tk.Label(window, text="Студент", font=("Arial", 30))
status_label.pack(pady=30)

city_label = tk.Label(window, text="Москва", font=("Arial", 10))
city_label.pack(pady=40)


def on_click():
    city_label.config(text="Вы нажали на кнопку!")


button = tk.Button(window, text="Нажми меня", command=on_click)
button.pack(pady=10)

window.mainloop()
