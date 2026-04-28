# Kanyaraasi — Online Retail Sales Analysis

**Institute:** Newton School of Technology
**Program:** Data Visualization & Analytics — Capstone 2
**Sector:** Retail / E-commerce
**Team:** Kanyaraasi

---

## problem statement

which product categories, regions, and time periods drive the most revenue for this online retailer, and what patterns in the data indicate revenue loss through cancellations?

---

## business context

the retailer is a uk-based online gift and homeware company selling wholesale to businesses across europe. most of their customers are small retail shops buying in bulk. the key challenge is that revenue is heavily concentrated in a few months and a few product lines, and cancellations are eating into margins. this project tries to figure out where money is coming from and where it's leaking out.

**core business question:** which products, countries, and time periods drive the most revenue — and are cancellations seasonal or product-specific?

**decision supported:** inventory planning for Q4, identifying which international markets are worth investing in, and flagging product lines with high return rates.

---

## dataset

- source: UCI Machine Learning Repository
- link: https://archive.ics.uci.edu/dataset/352/online+retail
- rows: 541,909
- columns: 8
- time period: december 2010 to december 2011
- description: transactional data from a uk-based online gift retailer
- encoding: ISO-8859-1

---

## team members

| name | role |
|------|------|
| Vamshi | ETL pipeline, notebook 01 and 02 |
| Sravnath | EDA, notebook 03 |
| Prem | statistical analysis, notebook 04 |
| Rithwik | KPI computation, notebook 05 |
| Kantrol | data dictionary, documentation |

---

## kpi framework

| kpi | formula |
|-----|---------|
| Total Revenue | sum of Quantity × UnitPrice |
| Total Orders | count of unique InvoiceNo |
| Average Order Value | Total Revenue / Total Orders |
| Cancellation Rate | cancelled rows / (all rows) × 100 |
| Customer LTV | sum of revenue per CustomerID |

full definitions are in docs/data_dictionary.md

---

## key insights

1. november 2011 is the peak revenue month — holiday season demand drives a sharp spike
2. uk accounts for about 84% of total revenue — heavy home market concentration
3. thursday and tuesday are the highest revenue days — confirms b2b buying pattern
4. orders are placed mostly between 10am and 3pm — standard business hours
5. cancellation rate spikes in high-volume months — fulfilment likely under strain during peak
6. top 20 products follow the pareto rule — a small set drives most of the revenue
7. netherlands and eire are the strongest international markets after the uk
8. most transactions are low value but a few bulk orders are responsible for outsized revenue

---

## recommendations

1. stock up key products by october — the november spike is predictable and inventory must be ready
2. look into why cancellations go up in peak months — likely a fulfilment or stock availability issue
3. run targeted campaigns in netherlands and eire — they have solid revenue with room to grow
4. identify and protect the top 20 revenue products — these should never go out of stock
5. offer volume deals to bulk buyers to increase average order value across the year

---

## how to run

1. clone the repo
2. install dependencies: `pip install -r requirements.txt`
3. place the raw dataset at `data/raw/Online_Retail.csv`
4. open notebooks in order — 01 through 05
5. each notebook reads from `data/raw/` or `data/processed/`
6. outputs are saved to `data/processed/`

if working locally:

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

---

## tableau dashboard

link: [add after publishing on tableau public]

---

## github repo

link: https://github.com/dingdong-vamshi/Kanyaraasi_OnlineRetail_SalesAnalysis

---

## repository structure

```
Kanyaraasi_OnlineRetail_SalesAnalysis/
├── README.md
├── .gitignore
├── requirements.txt
├── data/
│   ├── raw/                  ← original dataset, never edited
│   └── processed/            ← cleaned output from ETL pipeline
├── notebooks/
│   ├── 01_extraction.ipynb
│   ├── 02_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_statistical_analysis.ipynb
│   └── 05_final_load_prep.ipynb
├── scripts/
│   └── etl_pipeline.py
├── tableau/
│   ├── screenshots/
│   └── dashboard_links.md
├── reports/
│   ├── project_report.pdf
│   └── presentation.pdf
└── docs/
    └── data_dictionary.md
```

---

## analytical pipeline

1. define — sector selected, problem scoped, dataset confirmed
2. extract — raw data loaded and profiled in notebook 01
3. clean and transform — all cleaning steps done in notebook 02, standalone script in scripts/
4. analyze — EDA in notebook 03, statistical tests in notebook 04
5. visualize — tableau dashboard built and published on tableau public
6. recommend — 3-5 business recommendations based on findings
7. report — final report and presentation exported to pdf in reports/

---

## tech stack

python, pandas, numpy, matplotlib, seaborn, scipy, scikit-learn, tableau public, jupyter

---

## contribution matrix

| name | notebooks | files | commits |
|------|-----------|-------|---------|
| Vamshi | 01, 02 | etl_pipeline.py, README | - |
| Sravnath | 03 | docs/cleaning_log.md | - |
| Prem | 04 | requirements.txt | - |
| Rithwik | 04, 05 | docs/kpi_definitions.md | - |
| Kantrol | 05 | .gitignore | - |

declaration: we confirm that the above contribution details are accurate and verifiable through github insights and commit history.
