def convert_length(value,from_unit, to_unit):
    length_units = {
        "meters_to_kilometers": 0.001,
        "meters_to_feet": 3.28084,
        "meters_to_ichhes": 39.3701,
        "kilometers_to_meters": 1000,
        "feet_to_meters": 0.3048,
        "inches_to_meters": 0.0254
    }
    key  = f"{from_unit}_to_{to_unit}"
    if key in length_units:
        return value * length_units[key]
    elif f"{to_unit}_to_{from_unit}" in length_units:
        return value / length_units[f"{to_unit}_to_{from_unit}"]
    else:
        raise ValueError("Invalid unit combination")
    
def convert_weight(value,from_unit, to_unit):
    weight_units = {
        "kilograms_to_pounds": 2.20462,
        "pounds_to_kilograms": 0.453592,
        "kilograms_to_grams": 1000,
        "grams_to_kilograms": 0.001
    }
    key = f"{from_unit}_to_{to_unit}"
    if key in weight_units:
        return value * weight_units[key]
    elif f"{to_unit}_to_{from_unit}" in weight_units:
        return value / weight_units[f"{to_unit}_to_{from_unit}"]
    else:
        raise ValueError("Invalid unit combination")

def convert_temperature(value,from_unit, to_unit):
    if from_unit.lower() == "celsius" and to_unit.lower() == "fahrenheit":
        return value *9/5 +32
    elif from_unit.lower() == "fahrenheit" and to_unit.lower() == "celsius":
        return (value - 32) * 5/9
    elif from_unit.lower() =="celsius" and to_unit.lower() == "kelvin":
        return value + 273.15
    elif from_unit.lower() == "kelvin" and to_unit.lower() == "celsius":
        return value - 273.15
    elif from_unit.lower() == "fahrenheit" and to_unit.lower() == "kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit.lower() == "kelvin" and to_unit.lower() == "fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        raise ValueError("Invalid unit combination")

def display_menu():
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Quit")

# Main function to run the program
def main():
    """Main function to run the program"""
    print("Welcome to the Unit Converter")
    display_menu()
    choice = input("Choose a category (1-4): ")
    if choice == "1":
        value = float(input("Enter the value to convert: "))
        from_unit = input("Convert from (meters, kilometers, feet, inches): ")
        to_unit = input("Convert to (meters, kilometers, feet, inches): ")
        try:
            result = convert_length(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {result} {to_unit}")
        except ValueError as e:
            print(f"Error: {e}")
    elif choice == "2":
        value = float(input("Enter the value to convert: "))
        from_unit = input("Convert from (kilograms, pounds, grams): ")
        to_unit = input("Convert to (kilograms, pounds, grams): ")
        try:
            result = convert_weight(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {result} {to_unit}")
        except ValueError as e:
            print(f"Error: {e}")
    elif choice == "3":
        value = float(input("Enter the value to convert: "))
        from_unit = input("Convert from (celsius, fahrenheit, kelvin): ")
        to_unit = input("Convert to (celsius, fahrenheit, kelvin): ")
        try:
            result = convert_temperature(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {result} {to_unit}")
        except ValueError as e:
            print(f"Error: {e}")
    elif choice == "4":
        print("Goodbye!")
    else:  
        print("Invalid choice")

# Run the main function
if __name__ == "__main__":
    main() 