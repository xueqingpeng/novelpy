# %%
import os, json
import pandas as pd
from tqdm import tqdm

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    df = pd.DataFrame(data)
    df.iloc[:, 1] = df.iloc[:, 1].apply(lambda x: x['score']['novelty'])
    df = df.drop('year', axis=1)
    # print(f"* loaded {len(df)} lines from {file_path}!")
    return df

def read_jsons(file_folder, start_year=2000, end_year=2010):
    all_dfs = []
    for year in tqdm(range(start_year, end_year+1)):
        file_name = f"{year}.json"
        file_path = os.path.join(file_folder, file_name)
        df = read_json(file_path)    
        all_dfs.append(df)  # Append the DataFrame to the list
    combined_df = pd.concat(all_dfs, ignore_index=True) # Concatenate all DataFrames into one
    print(f"* loaded {len(combined_df)} lines from {file_folder}!")
    return combined_df

df_foster = read_jsons("./Result/foster/Mesh_year_category")
df_lee = read_jsons("./Result/lee/c04_referencelist")
df_uzzi = read_jsons("./Result/uzzi/c04_referencelist")
df_wang = read_jsons("./Result/wang/c04_referencelist_3_1_restricted50")


# %%
merged_df = df_foster
for df in [df_lee, df_uzzi, df_wang]:
    merged_df = pd.merge(merged_df, df, on='PMID', how='outer')
merged_df = merged_df.rename(columns={'PMID': 'pmid'})
merged_df.to_csv('./baseline_result.tsv', sep='\t', index=False)


# %%
