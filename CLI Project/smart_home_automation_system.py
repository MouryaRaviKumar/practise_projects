# Smart Home Automation System


class Device:
    def __init__(self, name):
        self.name = name
        self.status = "OFF"


class Light(Device):
    def __init__(self, name):
        super().__init__(name)
        self.brightness = 100

    def turn_on(self):
        self.status = "ON"

    def turn_off(self):
        self.status = "OFF"

    def set_brightness(self, brightness):
        self.brightness = brightness


class Thermostat(Device):
    def __init__(self, name):
        super().__init__(name)
        self.temperature = 24
        self.mode = "Cooling"

    def set_temperature(self, temperature):
        self.temperature = temperature

    def set_mode(self, mode):
        self.mode = mode


# Creating devices

living_light = Light("Living Room Light")
bedroom_light = Light("Bedroom Light")
guest_light = Light("Guest Room Light")

living_thermostat = Thermostat("Living Room Thermostat")
guest_thermostat = Thermostat("Guest Room Thermostat")


# Function to display devices

def show_devices():
    print("\n--- Devices ---")
    print("1. Living Room Light")
    print("2. Living Room Thermostat")
    print("3. Bedroom Light")
    print("4. Guest Room Light")
    print("5. Guest Room Thermostat")


# Function to control lights

def control_light(light):

    print(f"\n{light.name}")
    print("1. Turn ON")
    print("2. Turn OFF")
    print("3. Set Brightness")

    choice = input("Enter your choice: ")

    if choice == "1":
        light.turn_on()
        print("Light turned ON")

    elif choice == "2":
        light.turn_off()
        print("Light turned OFF")

    elif choice == "3":
        brightness = int(input("Enter brightness (0-100): "))

        if brightness >= 0 and brightness <= 100:
            light.set_brightness(brightness)
            print("Brightness set to", brightness, "%")
        else:
            print("Brightness should be between 0 and 100")


# Function to control thermostat

def control_thermostat(thermostat):

    print(f"\n{thermostat.name}")
    print("1. Set Temperature")
    print("2. Change Mode")

    choice = input("Enter your choice: ")

    if choice == "1":

        temperature = int(input("Enter temperature: "))
        thermostat.set_temperature(temperature)

        print("Temperature set to", temperature, "°C")

    elif choice == "2":

        mode = input("Enter mode (Heating/Cooling): ")

        if mode.lower() == "heating" or mode.lower() == "cooling":
            thermostat.set_mode(mode.capitalize())
            print("Mode changed to", thermostat.mode)

        else:
            print("Invalid mode")


# Owner menu

def owner_menu():

    while True:

        print("\n===== OWNER MENU =====")
        print("1. View Devices")
        print("2. Control Living Room Light")
        print("3. Control Living Room Thermostat")
        print("4. Control Bedroom Light")
        print("5. Control Guest Room Light")
        print("6. Control Guest Room Thermostat")
        print("7. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_devices()

        elif choice == "2":
            control_light(living_light)

        elif choice == "3":
            control_thermostat(living_thermostat)

        elif choice == "4":
            control_light(bedroom_light)

        elif choice == "5":
            control_light(guest_light)

        elif choice == "6":
            control_thermostat(guest_thermostat)

        elif choice == "7":
            print("Logged out.")
            break

        else:
            print("Invalid choice")


# Guest menu

def guest_menu():

    while True:

        print("\n===== GUEST ROOM =====")
        print("1. Control Light")
        print("2. Control Thermostat")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            control_light(guest_light)

        elif choice == "2":
            control_thermostat(guest_thermostat)

        elif choice == "3":
            break

        else:
            print("Invalid choice")


# Owner password

OWNER_PASSWORD = "1234"


# Main program

while True:

    print("\n============================")
    print("    SMART HOME AUTOMATION")
    print("============================")

    print("1. Owner")
    print("2. Guest")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        password = input("Enter owner password: ")

        if password == OWNER_PASSWORD:
            print("Login successful")
            owner_menu()

        else:
            print("Wrong password")

    elif choice == "2":

        print("\nWelcome Guest!")
        print("You can only control the Guest Room.")

        guest_menu()

    elif choice == "3":

        print("Thank you for using Smart Home Automation")
        break

    else:
        print("Invalid choice")