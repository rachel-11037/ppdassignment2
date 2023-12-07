from distance import Distance
from temperature import Temperature
from volume import Volume
from mass import Mass
from area import Area


# main menu function, to conserve space and improve performance
def menu():
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("+ Welcome to the conversion tool!   +")
    print("+ 1: Distance                       +")
    print("+ 2: Temperature                    +")
    print("+ 3: Volume                         +")
    print("+ 4: Mass                           +")
    print("+ 5: Area                           +")
    print("+ 6: Quit                           +")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")


def distance():
    def convert_miles():
        convert_again = True
        while convert_again:
            while True:
                try:
                    miles = float(input("Enter, in miles, your measurement:"))
                except ValueError:
                    print("Sorry, you have not entered an integer/float value. Please try again.")
                else:
                    miles = Distance(miles)
                    result = miles.convert_miles2km()
                    print(f"{miles.distance} miles = {result}km.")
                    convert_again = input("Would you like to convert again? y/n:")
                    if convert_again == "y":
                        convert_again = True
                    else:
                        distance()

    def convert_km():
        convert_again = True
        while convert_again:
            while True:
                try:
                    km = float(input("Enter, in kilometres, your measurement:"))
                except ValueError:
                    print("Sorry, you have not entered an integer/float value. Please try again.")
                else:
                    km = Distance(km)
                    result = km.convert_km2miles()
                    print(f"{km.distance}km = {result} miles.")
                    convert_again = input("Would you like to convert again? y/n:")
                    if convert_again == "y":
                        convert_again = True
                    else:
                        distance()

    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("+ Distance Conversion               +")
    print("+ 1. Convert miles to kilometres    +")
    print("+ 2. Convert kilometres to miles    +")
    print("+ 3. Back to main menu              +")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    while True:
        try:
            user_choice = int(input("Enter your choice:"))
            break
        except ValueError:
            print("Sorry, you have not entered an integer value. Please try again.")

    while user_choice != 3:
        if user_choice == 1:
            convert_miles()
        elif user_choice == 2:
            convert_km()
        else:
            print("Invalid. Try again.")
            distance()
    main()


def temperature():
    def convert_far2cel():
        convert_again = True
        while convert_again:
            while True:
                try:
                    far = float(input("Enter, in °F, your temperature:"))
                except ValueError:
                    print("Sorry, you have not entered an integer/float value. Please try again.")
                else:
                    far = Temperature(far)
                    result = far.convert_far2cel()
                    print(f"{far.temp}°F = {result}°C")
                    convert_again = input("Would you like to convert again? y/n:")
                    if convert_again == "y":
                        convert_again = True
                    else:
                        temperature()

    def convert_cel2far():
        convert_again = True
        while convert_again:
            while True:
                try:
                    cel = float(input("Enter, in °C, your temperature:"))
                except ValueError:
                    print("Sorry, you have not entered an integer/float value. Please try again.")
                else:
                    cel = Temperature(cel)
                    result = cel.convert_cel2far()
                    print(f"{cel.temp}°C = {result}°F")
                    convert_again = input("Would you like to convert again? y/n:")
                    if convert_again == "y":
                        convert_again = True
                    else:
                        temperature()

    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("+ Temperature Conversion            +")
    print("+ 1. Fahrenheit to Celsius          +")
    print("+ 2. Celsius to Fahrenheit          +")
    print("+ 3. Back to main menu              +")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    while True:
        try:
            user_choice = int(input("Enter your choice:"))
            break
        except ValueError:
            print("Sorry, you have not entered an integer value. Please try again.")

    while user_choice != 3:
        if user_choice == 1:
            convert_far2cel()
        elif user_choice == 2:
            convert_cel2far()
        else:
            print("Invalid. Try again")
            temperature()
    main()


def volume():
    def convert_pnt2ltr():
        convert_again = True
        while convert_again:
            while True:
                try:
                    pint = float(input("Enter, in pints, your volume:"))
                except ValueError:
                    print("Sorry, you have not entered an integer/float value. Please try again.")
                else:
                    pint = Volume(pint)
                    result = pint.convert_pnt_to_ltr()
                    print(f"{pint.volume} pints = {result}l")
                    convert_again = input("Would you like to convert again? y/n:")
                    if convert_again == "y":
                        convert_again = True
                    else:
                        volume()

    def convert_ltr2pnt():
        convert_again = True
        while convert_again:
            while True:
                try:
                    ltr = float(input("Enter, in litres, your volume:"))
                except ValueError:
                    print("Sorry, you have not entered an integer/float value. Please try again.")
                else:
                    ltr = Volume(ltr)
                    result = ltr.convert_lrt_to_pnt()
                    print(f"{ltr.volume}l = {result} pints")
                    convert_again = input("Would you like to convert again? y/n:")
                    if convert_again == "y":
                        convert_again = True
                    else:
                        volume()

    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("+ Volume Conversion                 +")
    print("+ 1. Convert Pints to Litres        +")
    print("+ 2. Convert Litres to Pints        +")
    print("+ 3. Back to Main Menu              +")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    while True:
        try:
            user_choice = int(input("Enter your choice:"))
            break
        except ValueError:
            print("Sorry, you have not entered an integer value. Please try again.")

    while user_choice != 3:
        if user_choice == 1:
            convert_pnt2ltr()
        elif user_choice == 2:
            convert_ltr2pnt()
        else:
            print("Invalid. Try again")
            volume()
    main()


def mass():
    def convert_kg2st():
        convert_again = True
        while convert_again:
            while True:
                try:
                    kg = float(input("Enter, in kilograms, your mass:"))
                except ValueError:
                    print("Sorry, you have not entered an integer/float value. Please try again.")
                else:
                    kg = Mass(kg)
                    result = kg.convert_kg_to_st()
                    print(f"{kg.mass}kg = {result}st")
                    convert_again = input("Would you like to convert again? y/n:")
                    if convert_again == "y":
                        convert_again = True
                    else:
                        mass()

    def convert_st2kg():
        convert_again = True
        while convert_again:
            while True:
                try:
                    st = float(input("Enter, in stone, your mass:"))
                except ValueError:
                    print("Sorry, you have not entered an integer/float value. Please try again.")
                else:
                    st = Mass(st)
                    result = st.convert_kg_to_st()
                    print(f"{st.mass}st = {result}kg")
                    convert_again = input("Would you like to convert again? y/n:")
                    if convert_again == "y":
                        convert_again = True
                    else:
                        mass()

    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("+ Mass (Weight) Conversion          +")
    print("+ 1. Convert Kilograms to Stone     +")
    print("+ 2. Convert Stone to Kilograms     +")
    print("+ 3. Back to Main Menu              +")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    while True:
        try:
            user_choice = int(input("Enter your choice:"))
            break
        except ValueError:
            print("Sorry, you have not entered an integer value. Please try again.")

    while user_choice != 3:
        if user_choice == 1:
            convert_kg2st()
        elif user_choice == 2:
            convert_st2kg()
        else:
            print("Invalid. Try again")
            mass()
    main()


def area():
    def convert_acres2hect():
        convert_again = True
        while convert_again:
            while True:
                try:
                    acres = float(input("Enter, in acres, your area:"))
                except ValueError:
                    print("Sorry, you have not entered an integer/float value. Please try again.")
                else:
                    acres = Area(acres)
                    result = acres.convert_acr_to_hect()
                    print(f"{acres.area} acres = {result} hectares")
                    convert_again = input("Would you like to convert again? y/n")
                    if convert_again == "y":
                        convert_again = True
                    else:
                        area()

    def convert_hect2acres():
        convert_again = True
        while convert_again:
            while True:
                try:
                    hect = float(input("Enter, in hectares, your area:"))
                except ValueError:
                    print("Sorry, you have not entered an integer/float value. Please try again.")
                else:
                    hect = Area(hect)
                    result = hect.convert_hect_to_acr()
                    print(f"{hect.area} hectares = {result} acres")
                    convert_again = input("Would you like to convert again? y/n")
                    if convert_again == "y":
                        convert_again = True
                    else:
                        area()
                area()

    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("+ Area Conversion                   +")
    print("+ 1. Convert Acres to Hectares      +")
    print("+ 2. Convert Hectares to Acres      +")
    print("+ 3. Back to Main Menu              +")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    while True:
        try:
            user_choice = int(input("Enter your choice:"))
            break
        except ValueError:
            print("Sorry, you have not entered an integer value. Please try again.")

    while user_choice != 3:
        if user_choice == 1:
            convert_acres2hect()
        elif user_choice == 2:
            convert_hect2acres()
        else:
            print("Invalid. Try again")
            area()
    main()


# TODO I'm gonna try and make lines 211 to 224 a bit cleaner. The while loop helps but I feel like it can be a bit
#  better
def main():
    menu()
    while True:
        try:
            user_choice = int(input("Enter your choice:"))
            break
        except ValueError:
            print("Sorry, you have not entered an integer value. Please try again.")

    while user_choice != 6:
        if user_choice == 1:
            distance()
        elif user_choice == 2:
            temperature()
        elif user_choice == 3:
            volume()
        elif user_choice == 4:
            mass()
        elif user_choice == 5:
            area()
        else:
            print("Invalid. Try again")
            main()
    print("Goodbye!")
    quit()


if __name__ == "__main__":
    main()
