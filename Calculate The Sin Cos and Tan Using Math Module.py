import math

def calculate_trig_functions(angle_degrees):
    # Convert degrees to radians
    angle_radians = math.radians(angle_degrees)

    # Calculate sine, cosine, and tangent
    sine_value = math.sin(angle_radians)
    cosine_value = math.cos(angle_radians)
    tangent_value = math.tan(angle_radians)

    return sine_value, cosine_value, tangent_value

def main():
    # Get user input
    angle_degrees = float(input("Enter an angle in degrees: "))

    # Calculate the trigonometric values
    sine, cosine, tangent = calculate_trig_functions(angle_degrees)

    # Display the results
    print(f"Sine({angle_degrees}) = {sine}")
    print(f"Cosine({angle_degrees}) = {cosine}")
    print(f"Tangent({angle_degrees}) = {tangent}")

if __name__ == "__main__":
    main()