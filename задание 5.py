import tkinter as tk


click_count = 0


def increase_count():
    # Увеличиваем значение на единицу и обновляем надпись
    global click_count
    click_count += 1
    counter_label.config(text=str(click_count))


def clear_count():
    # Возвращаем счётчик к начальному значению
    global click_count
    click_count = 0
    counter_label.config(text=str(click_count))


# Создание и настройка окна
window = tk.Tk()
window.title("Счётчик кликов")
window.geometry("300x250")

counter_label = tk.Label(window, text="0", font=("Arial", 40))
counter_label.pack(pady=50)

tk.Button(
    window,
    text="Клик",
    command=increase_count,
).pack(pady=10)

tk.Button(
    window,
    text="Сброс",
    command=clear_count,
).pack(pady=10)

window.mainloop()
