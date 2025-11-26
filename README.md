# 📊 Pupil Absence Data Analysis & Visualisation

This project analyses pupil absence data from the UK Department for Education (DfE) and produces meaningful visualisations to explore national absence trends. It was completed as part of an academic data analysis coursework.

---

## 📁 Project Overview

The goal is to:
- Clean and prepare the raw absence data.
- Explore patterns in overall and persistent absence rates.
- Generate clear, interpretable visualisations using Python.
- Summarise findings in a structured analytical report.

---

## 🔧 Tools & Technologies

- **Python 3**
- **Pandas** — data cleaning & preprocessing  
- **Matplotlib / Seaborn** — data visualisation  
- **Jupyter / VS Code** — development environment  
- **Datasets**:  
  - `data-pupil-absence-in-schools-in-england.csv`  
  - `data-pupil-absence-in-schools-in-england.xlsx`  
  - `data-pupil-absence-in-schools-in-england.ods`

---

## 📈 Visualisations Generated

Two Python scripts produce the visual outputs:

1. **`bar_chart.py`**  
   - Creates a bar chart showing absence levels across categories (e.g., school type, year, or other attributes).

2. **`scatter_plot.py`**
   - Plots relationships between persistent absence and other school indicators.

Generated outputs:
- `bar_chart.png`
- `scatter_plot.png`

---

## 📊 Example Insights

- Analysed **5,000+ school records** across regions and academic years.  
- Identified notable differences between overall absence and persistent absence rates.  
- Observed patterns suggesting correlations between specific demographic or school-level factors and absence levels.

---

## 🚀 How to Run the Project

### 1. Install dependencies
You may create a virtual environment (optional):

```bash
pip install pandas matplotlib seaborn
````

### 2. Run the visualisation scripts

```bash
python bar_chart.py
python scatter_plot.py
```

The figures will be saved automatically as PNG files.

---

## 📄 Coursework Report

The written coursework report is included in `report.pdf`.

It contains:
* Background context
* Data preprocessing steps
* Analytical findings
* Visual interpretation
* Conclusions

---

## 📚 Project Structure

```
├── bar_chart.py
├── scatter_plot.py
├── bar_chart.png
├── scatter_plot.png
├── data-pupil-absence-in-schools-in-england.csv
├── data-pupil-absence-in-schools-in-england.xlsx
├── data-pupil-absence-in-schools-in-england.ods
├── Individual Coursework.pdf
└── Coursework.docx
```

---

## ✅ Status

This project is completed as part of academic coursework and serves as a demonstration of:

* Python data analysis
* Data cleaning & preparation
* Visualisation design
* Interpretation of educational datasets
