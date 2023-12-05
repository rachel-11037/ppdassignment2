from distance import Distance
from temperature import Temperature
from volume import Volume
from mass import Mass
from area import Area


# menu function
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

    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("+ Temperature Conversion            +")
    print("+ 1. Fahrenheit to Celsius          +")
    print("+ 2. Celsius to Fahrenheit          +")
    print("+ Back to main menu                 +")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

    user_choice = int(input("Type the number corresponding to your choice and press enter:"))
    while user_choice != 3:
        if user_choice == 1:
            convert_far2cel()
    main()

def main():
    menu()
    user_choice = int(input("Type the number corresponding to your choice and press enter:"))
    while user_choice != 6:
        if user_choice == 1:
            distance()
        elif user_choice == 2:
            temperature()
    print("Goodbye!")
    quit()

main()
