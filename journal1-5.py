import math

def main_program():
    x_values = []
    sine_values = []
    for i in range(1000):
        x = i * 0.002
        sine_value = math.sin(x)
        x_values.append(x)
        sine_values.append(sine_value)
    print("X\tSine(X)")
    for x, sin_x in zip(x_values, sine_values):
        print(f"{x:.{14}f}{sine_value}")

if __name__ == "__main__":
    main_program()