"""
Q1) Ask the user to enter a value (e.g., M) for a mathematical function.
    Generate x values from -10 to 10 using np.linspace().
    Compute y values for:
        y = M * x^2
        y = M * sin(x)
    Plot both functions in a single figure:
        - Use different colors and line styles.
        - Add legend, grid, and title.
"""

import numpy as np
import matplotlib.pyplot as plt

M = float(input("Enter a value for M: "))

x = np.linspace(-10, 10, 200)
y1 = M * x ** 2
y2 = M * np.sin(x)

plt.plot(x, y1, color="blue", linestyle="-", label="y = M * x^2")
plt.plot(x, y2, color="red", linestyle="--", label="y = M * sin(x)")
plt.title(f"Plots of y = M*x^2 and y = M*sin(x) for M = {M}")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.savefig("Q1_output.png")
plt.show()
