from distance import Distance
from temperature import Temperature
from volume import Volume
from mass import Mass
from area import Area


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
        miles = int(input("Enter, in miles, your measurement:"))
        miles = Distance(miles)
        result = miles.convert_miles2km()
        print(f"{miles.distance} miles = {result}km.")

    def convert_km():
        km = int(input("Enter, in kilometres, your measurement:"))
        km = Distance(km)
        result = km.convert_km2miles()
        print(f"{km.distance}km = {result} miles.")

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
    menu()

def temperature():
    def convert_far
def main():
    menu()


main()
