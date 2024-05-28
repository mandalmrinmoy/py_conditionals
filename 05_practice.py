# Weather activity suggestion
weather_location=input("Enter your location's weather: ")
weather=weather_location.lower()
if weather == "sunny":
    print("Go for a walk")
elif weather == "rainy":
    print("Read a book")
elif weather == "snowy":
    print("Build a snowman")