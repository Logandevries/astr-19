import numpy as np

x_values = np.linspace(0, 2, 1000)
sine_values = np.sin(x_values)

combined_values = np.column_stack((x_values, sine_values))

print(combined_values)
