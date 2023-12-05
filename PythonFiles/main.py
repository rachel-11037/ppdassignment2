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
            miles = int(input("Enter, in miles, your measurement:"))
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
            km = int(input("Enter, in kilometres, your measurement:"))
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
    user_choice = int(input("Select your choice:"))
    while user_choice != 3:
        if user_choice == 1:
            convert_miles()
        elif user_choice == 2:
            convert_km()
        else:
            print("Invalid. Try again.")
    main()


def temperature():
    def convert_far2cel():
        convert_again = True
        while convert_again:
            far = int(input("Enter, in °F, your temperature:"))
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
            cel = int(input("Enter, in °C, your temperature:"))
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

    user_choice = int(input("Type the number corresponding to your choice and press enter:"))
    while user_choice != 3:
        if user_choice == 1:
            convert_far2cel()
        elif user_choice == 2:
            convert_cel2far()
        else:
            print("Invalid. Try again")
            user_choice = int(input("Type the number corresponding to your choice and press enter:"))
    main()


def volume():
    def convert_pnt2ltr():
        convert_again = True
        while convert_again:
            pint = int(input("Enter, in pints, your volume:"))
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
            ltr = int(input("Enter, in litres, your volume:"))
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
    user_choice = int(input("Type the number corresponding to your choice and press enter:"))
    while user_choice != 3:
        if user_choice == 1:
            convert_pnt2ltr()
        elif user_choice == 2:
            convert_ltr2pnt()
        else:
            print("Invalid. Try again")
            user_choice = int(input("Type the number corresponding to your choice and press enter:"))
    main()


def mass():
    def convert_kg2stone():
        convert_again = True
        while convert_again:
            kg = int(input("Enter, in kilograms, your mass:"))
            kg = Mass(kg)
            result = kg.convert_kg_to_st()
            print(f"{kg.mass}kg = {result}st")
            convert_again = input("Would you like to convert again? y/n:")
            if convert_again == "y":
                convert_again = True
            else:
                mass()



def area():
    pass


def main():
    menu()
    user_choice = int(input("Type the number corresponding to your choice and press enter:"))
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
