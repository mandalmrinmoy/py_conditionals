# fruit ripeness checker
fruit="banana"
color_fruit=input("Enter the color of fruit: ")
color=color_fruit.lower()
if fruit=="banana":
    if color=="green":
        print("Unripe")
    elif color=="Yollow":
        print("Ripe")
    elif color=="brown":
        print("Overripe")