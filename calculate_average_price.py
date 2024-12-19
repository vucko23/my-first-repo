def calculate_average():
    prices = []
    print("Unesite cene (unesite 'kraj' da završite unos):")

    while True:
        user_input = input("Cena: ")
        if user_input.lower() == 'kraj':
            break
        try:
            price = float(user_input)
            prices.append(price)
        except ValueError:
            print("Molimo unesite važeći broj ili 'kraj' da završite.")

    if prices:
        average_price = sum(prices) / len(prices)
        print(f"Prosek unetih cena je: {average_price:.2f}")
    else:
        print("Niste uneli nijednu cenu.")

# Pozivanje funkcije
calculate_average()
