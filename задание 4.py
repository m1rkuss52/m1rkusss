import tkinter as tk


def greet_user():
    user_name = name_entry.get().strip()

    if user_name:
        message_label.config(text=f"Привет, {user_name}!")
    else:
        message_label.config(text="Вы ничего не ввели!")


# Настраиваем окно приложения
window = tk.Tk()
window.title("Приветствие")
window.geometry("350x200")

name_entry = tk.Entry(window, font=("Arial", 14))
name_entry.pack(pady=20)

greet_button = tk.Button(
    window,
    text="Поздороваться",
    command=greet_user,
    font=("Arial", 12),
)
greet_button.pack()

message_label = tk.Label(
    window,
    text="Введите ваше имя",
    font=("Arial", 14),
)
message_label.pack(pady=20)

window.mainloop()
