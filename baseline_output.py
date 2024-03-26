# %%
import os, json
import pandas as pd
import numpy as np
from tqdm import tqdm


# %%
def read_json_for_cooc(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    df = pd.DataFrame(data)
    df.iloc[:, 1] = df.iloc[:, 1].apply(lambda x: x['score']['novelty'])
    df = df.drop('year', axis=1)
    # print(f"* loaded {len(df)} lines from {file_path}!")
    return df

def read_json_for_embe(file_path, embedding="title"):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    df = pd.DataFrame(data)
    if embedding == "title":
        df.iloc[:, 1] = df.iloc[:, 1].apply(lambda x: x['shibayama_title_embedding']['percentiles']['100%'])
    elif embedding == "abstract":
        df.iloc[:, 1] = df.iloc[:, 1].apply(lambda x: x.get('shibayama_abstract_embedding', {}).get('percentiles', {}).get('100%', np.nan))
    df.rename(columns={'shibayama': 'shibayama_'+embedding}, inplace=True)
    # print(f"* loaded {len(df)} lines from {file_path}!")
    return df

def read_jsons(file_folder, start_year=2000, end_year=2010, indicator="cooc", embedding="title"):
    all_dfs = []
    for year in tqdm(range(start_year, end_year+1)):
        file_name = f"{year}.json"
        file_path = os.path.join(file_folder, file_name)
        if indicator == "cooc":
            df = read_json_for_cooc(file_path)
        elif indicator == "embe":
            df = read_json_for_embe(file_path, embedding)
        all_dfs.append(df)  # Append the DataFrame to the list
    combined_df = pd.concat(all_dfs, ignore_index=True) # Concatenate all DataFrames into one
    print(f"* loaded {len(combined_df)} lines from {file_folder}!")
    return combined_df


# %%
df_foster = read_jsons("./Result/foster/Mesh_year_category", indicator="cooc")
df_lee = read_jsons("./Result/lee/c04_referencelist", indicator="cooc")
df_uzzi = read_jsons("./Result/uzzi/c04_referencelist", indicator="cooc")
df_wang = read_jsons("./Result/wang/c04_referencelist_3_1_restricted50", indicator="cooc")

df_foster2 = read_jsons("./Result/foster/c04_referencelist", indicator="cooc")
df_lee2 = read_jsons("./Result/lee/Mesh_year_category", indicator="cooc")
df_uzzi2 = read_jsons("./Result/uzzi/Mesh_year_category", indicator="cooc")
df_wang2 = read_jsons("./Result/wang/Mesh_year_category_3_1_restricted50", indicator="cooc")

df_shibayama_title = read_jsons("./Result/shibayama", indicator="embe", embedding="title")
df_shibayama_abstract = read_jsons("./Result/shibayama", indicator="embe", embedding="abstract")


# %%
merged_df = df_foster
for df in [df_lee, df_uzzi, df_wang, df_shibayama_title, df_shibayama_abstract, df_foster2, df_lee2, df_uzzi2, df_wang2]:
    merged_df = pd.merge(merged_df, df, on='PMID', how='outer')
merged_df = merged_df.rename(columns={'PMID': 'pmid'})
# merged_df.to_csv('./baseline_results.tsv', sep='\t', index=False)


# %%
