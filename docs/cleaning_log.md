# Data Cleaning Log
Project: Kanyaraasi Online Retail Sales Analysis
Dataset: UCI Online Retail, Online_Retail.csv
Raw row count at start: 541,909

This file documents every cleaning step applied to the raw dataset, how many rows were affected, and why each decision was made.

---

## Step 1 - Duplicate Rows Removed
Rows removed: 5,268
Why: Exact duplicate rows were caused by double data exports from the retailer system. Keeping them would double-count revenue and inflate order counts.

## Step 2 - Description Whitespace Stripped
Rows affected: around 114,906 cleaned, not dropped
Why: Product names had invisible leading and trailing spaces, making the same item appear as multiple distinct products when grouping by description.

## Step 3 - Null Description Rows Dropped
Rows removed: 1,454
Why: A row with no product description cannot be linked to any product category. These represent less than 0.3 percent of the data.

## Step 4 - InvoiceDate Converted to Datetime
Rows affected: all rows, type change only
Why: Date was stored as plain text. Converting it allows us to extract Year, Month, Quarter, and Hour for trend analysis.

## Step 5 - CustomerID Converted to String
Rows affected: all rows, type change only
Why: CustomerID is an identifier not a number. Keeping it as a number risks accidental math being done on it.

## Step 6 - Cancellations Separated
Rows separated: around 9,251
Why: Invoices starting with C are cancellations, not completed sales. Mixing them into sales data would undercount revenue. Saved separately in cancellations.csv.

## Step 7 - Non-Product StockCodes Removed
Rows removed: around 2,224
Codes removed: POST, DOT, M, D, S, B, BANK CHARGES, AMAZONFEE, CRUK, PADS, DCGSSGIRL, DCGSSBG, and any starting with gift_
Why: These are internal system codes for postage, discounts, and adjustments, not real product sales.

## Step 8 - Zero or Negative UnitPrice Removed
Rows removed: around 1,046
Why: A product priced at zero or below is a data error or test entry. Some prices were as low as negative 11,062 pounds.

## Step 9 - Remaining Negative Quantity Rows Removed
Rows removed: 0 after Step 6
Why: After separating cancellations, no orphaned negative-quantity rows remained.

---

## Final Counts
Raw: 541,909
After dedup: 536,641
After drop null description: 535,187
After removing non-product codes: around 532,963
After removing bad UnitPrice: around 531,917
Final clean sales: around 522,666
Cancellations saved separately: around 9,251
