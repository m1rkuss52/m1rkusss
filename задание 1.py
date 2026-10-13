# Перевод расстояния из километров в мили
def km_to_miles():
    miles_per_km = 0.621371
    kilometers = float(input("Введите расстояние в километрах: "))
    miles = kilometers * miles_per_km

    print(miles)
    return miles


# Пересчёт массы из килограммов в фунты
def kg_to_pounds():
    pounds_per_kg = 2.20462
    kilograms = float(input("Введите массу в килограммах: "))
    pounds = kilograms * pounds_per_kg

    print(pounds)
    return pounds
