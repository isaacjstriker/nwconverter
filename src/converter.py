import pandas as pd

def read_csv(file_path):
    """Reads the CSV file from the given file path"""
    return pd.read_csv(file_path)

def process_data(df):
    """Process the data to match the format required by the proprietary program."""
    # Example processing: rename columns, change data types, etc.
    df.columns = [col.strip().lower() for col in df.columns]
    # Add more processing steps as needed
    return df

def write_csv(df, output_path):
    """Write the processed data to a new CSV file."""
    df.to_csv(output_path, index=False)

def convert_csv(input_path, output_path):
    """Convert the input CSV file to the required format and save it to the output path."""
    df = read_csv(input_path)
    processed_df = process_data(df)
    write_csv(processed_df, output_path)

if __name__ == "__main__":
    input_path = "src/csv/input.csv"
    output_path = "/csv/output.csv"
    convert_csv(input_path, output_path)