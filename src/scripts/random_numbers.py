import matplotlib.pyplot as plt
import numpy as np
import paths

# Generate some data
random_numbers = np.random.randn(100, 1)

# Plot and save
fig = plt.figure(figsize=(7, 6))
x = np.linspace(0, 2 * np.pi, 100)
plt.plot(x, np.sin(x) + random_numbers)
plt.xlabel("x")
plt.ylabel("y")
fig.savefig(paths.figures / "random_numbers.pdf", bbox_inches="tight", dpi=300)