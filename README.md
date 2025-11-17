# 📘 Colorimetric Detection – Calibration Curve & Concentration Prediction

This project performs **colorimetric analysis** using an image of a test pad.  
The script extracts RGB values, computes intensity, fits a calibration curve using linear regression, and predicts the concentration of an unknown water sample.

---

## 📂 Features
- Load and process a colorimetric test image  
- Extract average RGB values  
- Compute intensity from red channel  
- Fit a linear calibration curve  
- Predict unknown sample concentration  
- Plot calibration curve with standard points and regression line  

---

## ⚙️ Requirements

Install dependencies:

```bash
pip install opencv-python numpy matplotlib scikit-learn
