import sys
from pathlib import Path
import pandas as pd 
from process_feedback import process_feedback

# Get the file name from the command line arguments
file_name = sys.argv[1]

# Concatenate the file name with the csvs directory path
csv_path = Path("csv") / file_name

df = pd.read_csv(csv_path) 
output_path = csv_path.parent / f"{csv_path.stem}_preprocessed.csv"

process_feedback(df, output_path)
