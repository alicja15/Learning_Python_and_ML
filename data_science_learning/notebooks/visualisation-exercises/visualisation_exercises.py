"""
Standalone Python script version of the visualisation exercises.
Run: python visualisation_exercises.py
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.size'] = 10
np.random.seed(42)

# Exercise 1 — Effect of bins on a bimodal age distribution
age = np.concatenate([np.random.normal(28, 5, 600), np.random.normal(52, 8, 400)])

fig, axes = plt.subplots(1, 3, figsize=(15, 4), sharey=True)
for ax, b in zip(axes, [8, 25, 60]):
    ax.hist(age, bins=b, color='#3498db', edgecolor='black', alpha=0.7)
    ax.set_title(f'Number of bins = {b}')
    ax.set_xlabel('Age')
    ax.grid(axis='y', linestyle='--', alpha=0.5)
axes[0].set_ylabel('Count')
plt.suptitle('Exercise 1: Effect of the bins parameter on distribution estimation', y=1.05)
plt.tight_layout()
plt.show()
