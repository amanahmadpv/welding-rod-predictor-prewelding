# 🔩 Welding Rod Consumption Predictor - Model B (Pre-Welding Estimation)

This Streamlit application predicts **welding rod consumption (kg/ton)** using real-time data available **just before welding**. It helps production engineers estimate required welding material with higher context accuracy.

---

## 🧠 Project Context

This project is part of an internship-based industrial machine learning initiative developed at **Peekay Steel Castings** during the MBA (Data Analytics) program at **Pondicherry University**.  
It aims to support **real-time welding material forecasting** right before welding operations begin.

---

## 🎯 Objective

> Predict welding rod usage based on pre-welding inputs like casting weight, grade, temperature readings, nozzle type, gouging quantity, etc. This provides a **practical aid** to the production floor for managing welding rod supply.

---

## ⚙️ Model Overview

| Attribute        | Value |
|------------------|-------|
| 💡 **Model Used**       | XGBoost Regressor |
| 🧪 **Target Variable**   | `TOT (Kgs/T)` (log-transformed) |
| 📈 **Accuracy (R²)**     | **66.88%** on test set |
| 📦 **Data Size Used**    | ~7,000 cleaned production records |
| 📉 **Test Performance**  | MAE ≈ 5.13 kg/ton, RMSE ≈ 8.72 kg/ton |

---

## 🧾 Features Used

The following **12 top features** were selected using feature importance and performance-based pruning:

- `Grade_encoded`  
- `GougRodQty`  
- `Smp_encoded`  
- `RT Req`  
- `Family_encoded`  
- `TotDespCastWt(Ton)`  
- `PouringTemp`  
- `FP_encoded`  
- `Nozzle`  
- `Desc_encoded`  
- `Heat_encoded`  
- `TappingTemp`

These include numeric, label-encoded, and encoded categorical features representing real-time production variables.

---

## 🌐 Try the Live App

You can try this model live without installing anything using the Streamlit Cloud deployment below:

🔗 **[Open Model B App](https://welding-rod-predictor-prewelding-pxneyrmfsf6qwpnqokux5p.streamlit.app/)**

---

## 🧪 Why Log Transformation?

The target `TOT (Kgs/T)` was **right-skewed with outliers**. To ensure better performance:
- Applied `np.log1p()` before training
- Reversed during prediction using `np.expm1()`
- Improved model stability and generalization

---

## 🛠️ Files in This Repository

| File             | Description |
|------------------|-------------|
| `app2.py`        | Streamlit UI for Model B |
| `model_b.pkl`    | Trained XGBoost model |
| `features_b.pkl` | Feature list used in model |
| `requirements.txt` | Python dependencies |
| `README.md`      | You're reading this 🎯 |

---

## 💻 How to Run Locally

pip install -r requirements.txt
streamlit run app2.py

---

## 📊 Business Impact
✅ Accurate estimation of welding rods before production
✅ Reduces waste, stockouts, and overordering
✅ Allows tighter cost control and inventory planning
✅ Built and tested on real industrial data

---

## ✍️ Developed by
- Aman Ahmad P V
- MBA (Data Analytics) — Pondicherry University
- Data Analytics Intern @ Peekay Steel Castings
- Email: pvaman7@gmail.com
- GitHub: @amanahmadpv
