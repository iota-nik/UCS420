"""
Q3) Write a Python script to select your roll number as seed for NumPy and then
generate a dataset of 50 values using np.random.randn().
    Create a 2x2 subplot layout displaying:
        - Line plot showing cumulative sum.
        - Scatter plot with random noise.
    Customize with titles, axis labels, and grids.
"""

import numpy as np
import matplotlib.pyplot as plt

roll_number = 1024170030
np.random.seed(roll_number % (2**32))

data = np.random.randn(50)
cumulative_sum = np.cumsum(data)
noise = np.random.randn(50)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].plot(cumulative_sum, color="blue")
axs[0, 0].set_title("Cumulative Sum - Line Plot")
axs[0, 0].set_xlabel("Index")
axs[0, 0].set_ylabel("Cumulative Sum")
axs[0, 0].grid(True)

axs[0, 1].scatter(range(50), data, c=noise, cmap="viridis")
axs[0, 1].set_title("Random Data with Noise - Scatter Plot")
axs[0, 1].set_xlabel("Index")
axs[0, 1].set_ylabel("Value")
axs[0, 1].grid(True)

axs[1, 0].plot(data, color="green")
axs[1, 0].set_title("Random Data - Line Plot")
axs[1, 0].set_xlabel("Index")
axs[1, 0].set_ylabel("Value")
axs[1, 0].grid(True)

axs[1, 1].scatter(range(50), cumulative_sum, color="red")
axs[1, 1].set_title("Cumulative Sum - Scatter Plot")
axs[1, 1].set_xlabel("Index")
axs[1, 1].set_ylabel("Cumulative Sum")
axs[1, 1].grid(True)

plt.tight_layout()
plt.savefig("Q3_output.png")
plt.show()
