# Capstone Project: Online Retail Sales Analysis
**Team:** Kanyaraasi  
**Sector:** Retail / E-commerce

## Problem Statement
The objective of this project is to analyze transactional e-commerce data to identify which product categories, regions, and time periods drive the most revenue for a UK-based online retailer. Furthermore, the analysis aims to uncover transaction patterns that indicate revenue leakage through cancellations, enabling the business to optimize inventory, focus marketing efforts, and improve overall operational efficiency.

## Dataset Source
**Source:** UCI Machine Learning Repository - Online Retail Dataset  
**Citation:** Chen, Daqing. (2015). Online Retail. UCI Machine Learning Repository. https://doi.org/10.24432/C5CG6D.

## GitHub Repository
[https://github.com/dingdong-vamshi/Kanyaraasi_OnlineRetail_SalesAnalysis](https://github.com/dingdong-vamshi/Kanyaraasi_OnlineRetail_SalesAnalysis)

## Tableau Dashboard
[Dashboard Link To Be Added After Publishing]

## How to Run the Project
To reproduce the findings, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dingdong-vamshi/Kanyaraasi_OnlineRetail_SalesAnalysis.git
   cd Kanyaraasi_OnlineRetail_SalesAnalysis
   ```

2. **Set up the dataset:**
   Ensure the raw dataset (`Online_Retail.csv`) is placed in the `data/raw/` directory.

3. **Install dependencies:**
   Ensure you have Python installed, then install required libraries:
   ```bash
   pip install pandas numpy matplotlib seaborn scipy scikit-learn jupyter
   ```

4. **Run the Jupyter Notebooks sequentially:**
   Open the notebooks in Jupyter or your IDE and run them in order from `01_extraction.ipynb` to `05_final_load_prep.ipynb`.

5. **(Optional) Run the automated ETL Pipeline:**
   If you prefer to bypass the notebooks and just get the cleaned data, you can run the standalone Python script:
   ```bash
   python scripts/etl_pipeline.py
   ```
   This will output the clean datasets into the `data/processed/` directory.

## Repository Structure
```
Kanyaraasi_OnlineRetail_SalesAnalysis/
├── data/
│   ├── raw/                  ← Raw unedited dataset
│   └── processed/            ← Cleaned outputs and aggregates
├── notebooks/                ← Step-by-step Jupyter notebooks for analysis
├── scripts/                  ← Standalone ETL Python script
├── docs/                     ← Data dictionary and documentation
├── tableau/                  ← Dashboard screenshots and links
└── README.md                 ← Project overview
```