import tkinter as tk


def open_catalog():
    # Переходим к списку товаров, если поле логина заполнено
    if login_entry.get().strip():
        login_frame.pack_forget()
        catalog_frame.pack(pady=50)


def open_cart():
    # Скрываем каталог и отображаем корзину
    catalog_frame.pack_forget()
    cart_frame.pack(pady=50)


# Основное окно программы
window = tk.Tk()
window.title("RANDOM")
window.geometry("1920x1080")

# Экран входа
login_frame = tk.Frame(window)
login_frame.pack(pady=100)

tk.Label(
    login_frame,
    text="Логин",
    font=("Arial", 20, "bold"),
).pack(pady=20)

login_entry = tk.Entry(login_frame, font=("Arial", 16))
login_entry.pack(pady=20)

tk.Button(
    login_frame,
    text="Войти",
    command=open_catalog,
).pack(pady=10)

# Раздел с товарами
catalog_frame = tk.Frame(window)

tk.Label(
    catalog_frame,
    text="Каталог товаров",
    font=("Arial", 20, "bold"),
).pack(pady=20)

tk.Button(
    catalog_frame,
    text="Корзина",
    command=open_cart,
).pack(pady=10)

# Экран корзины
cart_frame = tk.Frame(window)

tk.Label(
    cart_frame,
    text="Корзина",
    font=("Arial", 20, "bold"),
).pack(pady=20)

window.mainloop()
