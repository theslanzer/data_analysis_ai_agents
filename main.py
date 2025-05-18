import pandas as pd
from crew.analysis_crew import csv_analysis_crew

df = pd.read_csv('data/ifood_df.csv')
df = df.iloc[:500]
cleaned_dataset_path = 'data/first_1000_rows.csv'
df.to_csv(cleaned_dataset_path, index=False)

if __name__ == "__main__":
    result = csv_analysis_crew.kickoff()
    print("\nFinal Report:\n", result)