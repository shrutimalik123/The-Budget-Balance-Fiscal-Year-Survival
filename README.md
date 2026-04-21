# 💰 The Budget Balance - Healthcare CFO Simulator

A financial strategy simulation designed to teach the fundamentals of Healthcare Accounting and Capital Allocation. You play as the CFO of a regional hospital, managing a $1,000,000 quarterly budget. To succeed, you must navigate unpredictable monthly variances in labor and supply costs while deciding when to reinvest in staff and technology or save reserves to protect the hospital’s solvency.

This project focuses on teaching:
* **Variance Analysis:** Identifying and reacting to "Unfavorable" (increased costs) and "Favorable" (increased revenue) budgetary deviations.
* **Capital Expenditure (CapEx):** Understanding the cost of maintaining high-tech medical machinery and the risks of depreciation.
* **Operating Margin Management:** Maintaining a positive cash flow while simultaneously funding quality-of-care initiatives.
* **The HCAHPS Correlation:** Simulating how patient satisfaction scores act as a metric for long-term organizational health.

---

## ✨ Features

* **Monthly Variance Engine:** Randomly generates real-world financial hurdles such as nursing overtime spikes, supply chain inflation, or patient volume surges.
* **Investment Decision Matrix:** Offers strategic choices between Staff Development (Human Capital), Equipment Maintenance (Physical Capital), or Fiscal Conservation.
* **Equipment Decay Logic:** Simulates the "drift" of medical technology; if you don't spend on repairs, your equipment health degrades over time.
* **Fiscal Performance Audit:** Evaluates your success based on your final "Margin" and your ability to keep quality scores above industry targets.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You need **Python 3** installed.

### 2. Setup and Execution
1.  **Save the Code:** Save the script as `health_finance_sim.py`.
2.  **Open Terminal:** Navigate to the folder containing the file.
3.  **Run the Script:**
    ```bash
    python health_finance_sim.py
    ```

### 3. Gameplay Instructions
1.  **Monitor Your Variance:** Every month, check if you lost or gained money due to labor, supplies, or volume.
2.  **Spend Wisely:** * **Staff Training ($100k):** Increases Patient Satisfaction.
    * **Equipment Repair ($150k):** Increases Equipment Health (reduces future downtime).
    * **Save:** Protects your budget but causes a -5% drift in satisfaction and equipment quality.
3.  **Balance the Books:** Try to end the quarter with a high satisfaction score and a budget surplus.



---

## 🧠 Code Structure Highlights

### Variance Logic
This block demonstrates "Unfavorable" vs "Favorable" variances. It uses a conditional branch to either subtract expenses or add revenue, simulating the volatility of a hospital's Profit and Loss (P&L) statement.

```python
# Simulating the volatility of healthcare operations
if variance_type == "Labor":
    cost = 50000 # Unfavorable Variance
elif variance_type == "Volume":
    gain = 40000 # Favorable Variance

