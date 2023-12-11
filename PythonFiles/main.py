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
        try:
            miles = float(input("Enter, in miles, your measurement:"))
        except ValueError:
            print("Sorry, you have not entered an integer/float value. Please try again.")
        else:
            miles = Distance(miles)
            result = miles.convert_miles2km()
            print(f"{miles.distance} miles = {result}km.")

            while True:
                convert_input = input("Would you like to convert again? y/n:")
                if convert_input == "y":
                    break
                elif convert_input == "n":
                    distance()
                else:
                    print("Sorry, only the values 'y' (yes) and 'n' (no) are accepted. Please try again.")
                    continue

    def convert_km():
        try:
            km = float(input("Enter, in kilometres, your measurement:"))
        except ValueError:
            print("Sorry, you have not entered an integer/float value. Please try again.")
        else:
            km = Distance(km)
            result = km.convert_km2miles()
            print(f"{km.distance}km = {result} miles.")

            while True:
                convert_input = input("Would you like to convert again? y/n:")
                if convert_input == "y":
                    break
                elif convert_input == "n":
                    distance()
                else:
                    print("Sorry, only the values 'y' (yes) and 'n' (no) are accepted. Please try again.")
                    continue

    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("+ Distance Conversion               +")
    print("+ 1. Convert Miles to Kilometres    +")
    print("+ 2. Convert Kilometres to Miles    +")
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
            convert_miles()
        elif user_choice == 2:
            convert_km()
        else:
            print("Invalid. Try again.")
            distance()
    main()


def temperature():
    def convert_far2cel():
        try:
            far = float(input("Enter, in °F, your temperature:"))
        except ValueError:
            print("Sorry, you have not entered an integer/float value. Please try again.")
        else:
            far = Temperature(far)
            result = far.convert_far2cel()
            print(f"{far.temp}°F = {result}°C")

            while True:
                convert_input = input("Would you like to convert again? y/n:")
                if convert_input == "y":
                    break
                elif convert_input == "n":
                    temperature()
                else:
                    print("Sorry, only the values 'y' (yes) and 'n' (no) are accepted. Please try again.")
                    continue

    def convert_cel2far():
        try:
            cel = float(input("Enter, in °C, your temperature:"))
        except ValueError:
            print("Sorry, you have not entered an integer/float value. Please try again.")
        else:
            cel = Temperature(cel)
            result = cel.convert_cel2far()
            print(f"{cel.temp}°C = {result}°F")

            while True:
                convert_input = input("Would you like to convert again? y/n:")
                if convert_input == "y":
                    break
                elif convert_input == "n":
                    temperature()
                else:
                    print("Sorry, only the values 'y' (yes) and 'n' (no) are accepted. Please try again.")
                    continue

    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("+ Temperature Conversion            +")
    print("+ 1. Convert Fahrenheit to Celsius  +")
    print("+ 2. Convert Celsius to Fahrenheit  +")
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
            convert_far2cel()
        elif user_choice == 2:
            convert_cel2far()
        else:
            print("Invalid. Try again")
            temperature()
    main()


def volume():
    def convert_pnt2ltr():
        try:
            pint = float(input("Enter, in pints, your volume:"))
        except ValueError:
            print("Sorry, you have not entered an integer/float value. Please try again.")
        else:
            pint = Volume(pint)
            result = pint.convert_pnt_to_ltr()
            print(f"{pint.volume} pints = {result}l")

            while True:
                convert_input = input("Would you like to convert again? y/n:")
                if convert_input == "y":
                    break
                elif convert_input == "n":
                    volume()
                else:
                    print("Sorry, only the values 'y' (yes) and 'n' (no) are accepted. Please try again.")
                    continue

    def convert_ltr2pnt():
        try:
            ltr = float(input("Enter, in litres, your volume:"))
        except ValueError:
            print("Sorry, you have not entered an integer/float value. Please try again.")
        else:
            ltr = Volume(ltr)
            result = ltr.convert_lrt_to_pnt()
            print(f"{ltr.volume}l = {result} pints")

            while True:
                convert_input = input("Would you like to convert again? y/n:")
                if convert_input == "y":
                    break
                elif convert_input == "n":
                    volume()
                else:
                    print("Sorry, only the values 'y' (yes) and 'n' (no) are accepted. Please try again.")
                    continue

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
        try:
            kg = float(input("Enter, in kilograms, your mass:"))
        except ValueError:
            print("Sorry, you have not entered an integer/float value. Please try again.")
        else:
            kg = Mass(kg)
            result = kg.convert_kg_to_st()
            print(f"{kg.mass}kg = {result}st")

            while True:
                convert_input = input("Would you like to convert again? y/n:")
                if convert_input == "y":
                    break
                elif convert_input == "n":
                    mass()
                else:
                    print("Sorry, only the values 'y' (yes) and 'n' (no) are accepted. Please try again.")
                    continue

    def convert_st2kg():
        try:
            st = float(input("Enter, in stone, your mass:"))
        except ValueError:
            print("Sorry, you have not entered an integer/float value. Please try again.")
        else:
            st = Mass(st)
            result = st.convert_kg_to_st()
            print(f"{st.mass}st = {result}kg")

            while True:
                convert_input = input("Would you like to convert again? y/n:")
                if convert_input == "y":
                    break
                elif convert_input == "n":
                    mass()
                else:
                    print("Sorry, only the values 'y' (yes) and 'n' (no) are accepted. Please try again.")
                    continue

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
        try:
            acres = float(input("Enter, in acres, your area:"))
        except ValueError:
            print("Sorry, you have not entered an integer/float value. Please try again.")
        else:
            acres = Area(acres)
            result = acres.convert_acr_to_hect()
            print(f"{acres.area} acres = {result} hectares")

            while True:
                convert_input = input("Would you like to convert again? y/n:")
                if convert_input == "y":
                    break
                elif convert_input == "n":
                    area()
                else:
                    print("Sorry, only the values 'y' (yes) and 'n' (no) are accepted. Please try again.")
                    continue

    def convert_hect2acres():
        try:
            hect = float(input("Enter, in hectares, your area:"))
        except ValueError:
            print("Sorry, you have not entered an integer/float value. Please try again.")
        else:
            hect = Area(hect)
            result = hect.convert_hect_to_acr()
            print(f"{hect.area} hectares = {result} acres")

            while True:
                convert_input = input("Would you like to convert again? y/n:")
                if convert_input == "y":
                    break
                elif convert_input == "n":
                    area()
                else:
                    print("Sorry, only the values 'y' (yes) and 'n' (no) are accepted. Please try again.")
                    continue

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
