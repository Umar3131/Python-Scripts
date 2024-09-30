#_____________--Data Cleaning--_______________#

import pandas as pd

def clean_csv(file_path):
    df = pd.read_csv(file_path)

    df.drop_duplicates(inplace=True)

    for col in df.columns:
        if df[col].dtype == 'object':  
            df[col].fillna(df[col].mode()[0], inplace=True)
        else:  
            df[col].fillna(df[col].mean(), inplace=True)

    df = df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)

    cleaned_file_path = file_path.replace('.csv', '_cleaned.csv')
    df.to_csv(cleaned_file_path, index=False)
    print(f"Cleaned data saved to {cleaned_file_path}")

file_path = 'C:\\Users\\HP\\Desktop\\Code Alpha Projects\\Python Scripts\\Sample_data_for_cleaning.csv'
clean_csv(file_path)
