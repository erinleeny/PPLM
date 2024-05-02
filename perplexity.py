import sys
import numpy as np
import torch
# import torch.nn.functional as F
import pandas as pd


ALPHA_03_MAP = {
   'legal': './output_files/alpha_03/pplm_legal.csv',
   'politics': '',
   'religion': './output_files/alpha_03/pplm_religion.csv',
   'science': '',
   'technology': ''
}

NORMAL_MAP = {
   'legal': '',
   'politics': '',
   'religion': '',
   'science': '',
   'technology': ''
}

def main():
    # Check if file path argument is provided
    if len(sys.argv) != 2:
        print("Usage: python perplexity.py <csv_file_path>")
        return

    csv_file_path = sys.argv[1]

    # Read Excel file into DataFrame
    try:
        df = pd.read_csv(csv_file_path)
        losses=[]
        for _, row in df.iterrows():
            loss=row.iloc[2]
            losses.append(loss)

        losses=torch.tensor(losses)
        perp=torch.exp(torch.mean(losses))
        print(perp.item())

        # print(perp)
        # Explore data or perform further operations here
    except FileNotFoundError:
        print("File not found:", csv_file_path)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()