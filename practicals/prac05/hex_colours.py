COLOR_NAME_TO_COLOR_CODE = {
    "aliceblue": "#f0f8ff",
    "amber": "#ffbf00",
    "black olive": "#3b3c36"
}

color_name = input("Enter a color name (hit enter to quit): ").lower()
while color_name != "":
    if color_name in COLOR_NAME_TO_COLOR_CODE:
        print(f"{color_name} has a code of {COLOR_NAME_TO_COLOR_CODE[color_name]}")
    else:
        print("Not found")
    color_name = input("Enter a color name (hit enter to quit): ").lower()
