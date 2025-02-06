import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import pearsonr
from sklearn.metrics import mean_absolute_error

# Data
skill_levels = [
    "Green Beginner", "Yellow Beginner", "Red Beginner", "Green Intermediate", "Yellow Intermediate", "Red Intermediate", 
    "Green Advanced", "Yellow Advanced", "Red Advanced", "Green Expert", "Yellow Expert", "Red Expert", 
    "Green Grandmaster", "Yellow Grandmaster", "Red Grandmaster", "Grandmaster"
]

actual_values = np.array([70, 52, 30, 15, 12, 9, 8, 7, 6, 4, 3.5, 2.25, 1.5, 1, 0.5, 0.25])
perceived_values = np.array([48.13, 29, 23, 26.3, 24, 17.54, 13, 18, 12.39, 11, 11, 10, 6.32, 7, 2.71, 3.18])

# Convert skill levels to indices
x_data = np.arange(len(skill_levels))
y_actual = actual_values
y_perceived = perceived_values

# Define fitting functions
def exp_func(x, a, b, c):
    return a * np.exp(b * x) + c  # Exponential decay

def log_func(x, a, b):
    return a * np.log(x + .02) + b  # Logarithmic growth

def poly2_func(x, a, b, c):
    return a*x**2 + b*x + c  # Quadratic

# Fit models
params_actual_log, _ = curve_fit(log_func, x_data, y_actual, maxfev=5000)
params_perceived_poly, _ = curve_fit(poly2_func, x_data, y_perceived)

# Generate smooth data
x_smooth = np.linspace(0, len(skill_levels) - 1, 200)
y_smooth_actual_log = log_func(x_smooth, *params_actual_log)
y_smooth_perceived_poly = poly2_func(x_smooth, *params_perceived_poly)

# Make correlation metrics
corr, _ = pearsonr(y_actual, y_perceived)
r_squared = np.corrcoef(y_actual, y_perceived)[0, 1] ** 2
mae = mean_absolute_error(y_actual, y_perceived)

# Plotting
plt.figure(figsize=(12, 6))
plt.scatter(x_data, y_actual, label="Actual Percentile", color="blue", marker="o")
plt.scatter(x_data, y_perceived, label="Perceived Percentile", color="red", marker="o")

# Plot curves
plt.plot(x_smooth, y_smooth_actual_log, label="Best Fit (Actual - Exp)", color="blue", linestyle="--")
plt.plot(x_smooth, y_smooth_perceived_poly, label="Best Fit (Perceived - Poly)", color="red", linestyle="--")

# Labels
plt.xlabel("Real Skill Level")
plt.ylabel("Percentile (Lower is Better)")
plt.title(f"Actual vs Perceived Skill Percentiles\nCorrelation: {corr:.3f}, R²: {r_squared:.3f}, MAE: {mae:.2f}")
plt.xticks(x_data, skill_levels, rotation=45, ha="right")
plt.yticks(range(0, 101, 10))
plt.ylim(0, 100)
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
