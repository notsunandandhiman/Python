def is_valid_age(age):
    """Check if the age is a valid non-negative integer."""
    return isinstance(age, int) and age >= 0

def check_age_parity(age):
    """Check if the age is odd or even."""
    if age % 2 == 0:
        return "even"
    else:
        return "odd"

def main():
    try:
        # Get user input
        age_input = input("Enter your age: ")
        
        # Attempt to convert input to an integer
        age = int(age_input)

        # Check if the age is valid
        if is_valid_age(age):
            parity = check_age_parity(age)
            print(f"Your age is {age}, which is {parity}.")
        else:
            print("Error: Age must be a non-negative integer.")

    except ValueError:
        print("Error: Please enter a valid integer for age.")

if __name__ == "__main__":
    main()