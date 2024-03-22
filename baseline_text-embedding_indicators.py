# Text-embedding Indicators
import novelpy
import tqdm

for focal_year in tqdm.tqdm(range(2000,2011), desc = "Computing indicator for window of time"):
    shibayama = novelpy.indicators.Shibayama2021(collection_name = 'Citation_net_sample',
                                                 collection_embedding_name = 'embedding',
                                                 id_variable = 'PMID',
                                                 year_variable = 'year',
                                                 ref_variable = 'refs_pmid_wos',
                                                 entity = ['title_embedding','abstract_embedding'],
                                                 focal_year = focal_year,
                                                 density = True)
    shibayama.get_indicator()