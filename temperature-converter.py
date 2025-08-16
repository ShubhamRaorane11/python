unit = input("Is this temperature in Celsius or farenheit (C/F): ")
temp = float(input("Enter the temperature here: "))

if unit == "C":
    temp = round((9 * temp / 5 + 32,1))
    print(f"The temperature in farenheit is: {temp}°F")
elif unit == "F":
    temp = round((temp -32) * 5 / 9,1)
    print(f"The temperature in Celsius is: {temp}°C")
else:
    print(f"{unit} is an invalid unit of tempearture")
