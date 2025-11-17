import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load image
image_path = "sample_pad.png"
img = cv2.imread(image_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Use entire image as ROI
roi = img_rgb

# Extract RGB
R = np.mean(roi[:,:,0])
G = np.mean(roi[:,:,1])
B = np.mean(roi[:,:,2])

print(f"R={R:.2f}, G={G:.2f}, B={B:.2f}")

# Compute intensity
I = 255 - R
print("Intensity:", I)

# Calibration data
C_std = np.array([0, 5, 10, 20, 40]).reshape(-1, 1)
I_std = np.array([15, 75, 125, 165, 220])

# Fit model
model = LinearRegression().fit(C_std, I_std)
slope = model.coef_[0]
intercept = model.intercept_

print(f"Calibration: I = {slope:.3f} * C + {intercept:.3f}")

# Predict concentration of unknown sample
C_pred = (I - intercept) / slope
print("Predicted concentration:", C_pred)

# -------------------------------
# PLOT CALIBRATION CURVE
# -------------------------------

plt.figure(figsize=(8,6))

# Plot standard points
plt.scatter(C_std, I_std, color='blue', s=80, label="Standard Samples")

# Plot regression line
C_line = np.linspace(0, 40, 100).reshape(-1, 1)
I_line = model.predict(C_line)
plt.plot(C_line, I_line, color='red', label='Calibration Line')

# Plot unknown sample
plt.scatter([C_pred], [I], color='green', s=120, label="Unknown Sample")

# Labels
plt.xlabel("Concentration (µg/L)", fontsize=12)
plt.ylabel("Intensity (I)", fontsize=12)
plt.title("Calibration Curve for Colorimetric Detection", fontsize=14)
plt.grid(True)
plt.legend()

plt.show()
