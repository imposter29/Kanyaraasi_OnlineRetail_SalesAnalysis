import pandas as pd
import numpy as np
import os
import sys

def main():
    # Setup paths
    default_input = os.path.join(os.path.dirname(__file__), '../data/raw/Online_Retail.csv')
    input_path = sys.argv[1] if len(sys.argv) > 1 else default_input
    output_dir = os.path.join(os.path.dirname(__file__), '../data/processed')

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    print("Starting ETL Pipeline...")
    print(f"Reading data from {input_path}")

    # Load data
    try:
        df = pd.read_csv(input_path, encoding='ISO-8859-1')
    except FileNotFoundError:
        print(f"Error: Could not find file at {input_path}")
        sys.exit(1)
        
    print(f"Raw rows: {len(df)}")

    # Step 1 — Remove duplicates
    raw_count = len(df)
    df = df.drop_duplicates()
    print(f"Step 1: Removed duplicates. Rows after dedup: {len(df)} (-{raw_count - len(df)})")

    # Step 2 — Fix Description whitespace
    df['Description'] = df['Description'].str.strip()
    print("Step 2: Whitespace stripped from Description column.")

    # Step 3 — Drop rows with missing Description
    prev_count = len(df)
    df = df.dropna(subset=['Description'])
    print(f"Step 3: Dropped null descriptions. Rows remaining: {len(df)} (-{prev_count - len(df)})")

    # Step 4 — Convert InvoiceDate to datetime
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    print("Step 4: Converted InvoiceDate to datetime.")

    # Step 5 — Convert CustomerID to string
    df['CustomerID'] = df['CustomerID'].fillna(-1).astype(int).astype(str).replace('-1', np.nan)
    print("Step 5: Converted CustomerID to string.")

    # Step 6 — Flag and separate cancellations
    df['is_cancelled'] = df['InvoiceNo'].str.startswith('C')
    cancellations_df = df[df['is_cancelled']].copy()
    df = df[~df['is_cancelled']]
    print(f"Step 6: Separated cancellations. {len(cancellations_df)} cancellation rows found.")

    # Step 7 — Remove non-product StockCodes
    non_product_codes = ['POST', 'DOT', 'M', 'D', 'S', 'B', 'BANK CHARGES', 'AMAZONFEE', 'CRUK', 'PADS', 'DCGSSGIRL', 'DCGSSBG']
    prev_count = len(df)
    df = df[~df['StockCode'].isin(non_product_codes)]
    df = df[~df['StockCode'].str.startswith('gift_', na=False)]
    print(f"Step 7: Removed non-product StockCodes. Rows remaining: {len(df)} (-{prev_count - len(df)})")

    # Step 8 — Remove zero/negative UnitPrice
    prev_count = len(df)
    df = df[df['UnitPrice'] > 0]
    print(f"Step 8: Removed zero/negative UnitPrice. Rows remaining: {len(df)} (-{prev_count - len(df)})")

    # Step 9 — Remove remaining negative Quantity rows
    prev_count = len(df)
    df = df[df['Quantity'] > 0]
    print(f"Step 9: Removed remaining negative Quantity rows. Rows remaining: {len(df)} (-{prev_count - len(df)})")

    # Step 10 — Feature engineering
    df['Revenue'] = df['Quantity'] * df['UnitPrice']
    df['Year'] = df['InvoiceDate'].dt.year
    df['Month'] = df['InvoiceDate'].dt.month
    df['Quarter'] = df['InvoiceDate'].dt.quarter
    df['DayOfWeek'] = df['InvoiceDate'].dt.day_name()
    df['Hour'] = df['InvoiceDate'].dt.hour
    df['is_uk'] = df['Country'] == 'United Kingdom'
    print("Step 10: Created new features (Revenue, Time parts, is_uk).")

    # Save outputs
    sales_path = os.path.join(output_dir, 'cleaned_sales.csv')
    cancellations_path = os.path.join(output_dir, 'cancellations.csv')
    
    df.to_csv(sales_path, index=False)
    cancellations_df.to_csv(cancellations_path, index=False)
    
    print("\n=== CLEANING LOG ===")
    print("Raw rows:           541,909")
    print(f"After dedup:        {raw_count}   (-{541909 - raw_count})")
    print(f"Cancellations separated: {len(cancellations_df)} rows")
    print(f"Final clean sales:  {len(df)} rows")
    print("\nETL Pipeline completed successfully.")

if __name__ == '__main__':
    main()
