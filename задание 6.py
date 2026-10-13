import tkinter as tk


def show_text():
    # Получаем текст из поля ввода и выводим его в окне
    entered_text = text_entry.get().strip()

    if entered_text:
        result_label.config(text=entered_text)
    else:
        result_label.config(text="Вы ничего не ввели")


# Настраиваем главное окно
window = tk.Tk()
window.title("Ввод текста")
window.geometry("300x250")

text_entry = tk.Entry(window, font=("Arial", 14))
text_entry.pack(pady=20)

show_button = tk.Button(
    window,
    text="Показать",
    command=show_text,
)
show_button.pack(pady=10)

result_label = tk.Label(
    window,
    text="Введите текст",
    font=("Arial", 14),
)
result_label.pack(pady=20)

window.mainloop()
