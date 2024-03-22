# %% Sample Download
from novelpy.utils.get_sample import download_sample
download_sample()


# %% Co-occurrence Matrices Prepare
import novelpy

ref_cooc = novelpy.utils.cooc_utils.create_cooc(
                 collection_name = "Ref_Journals_sample",
                 year_var="year",
                 var = "c04_referencelist",
                 sub_var = "item",
                 time_window = range(1995,2016),
                 weighted_network = True, self_loop = True)
ref_cooc.main()

ref_cooc = novelpy.utils.cooc_utils.create_cooc(
                 collection_name = "Ref_Journals_sample",
                 year_var="year",
                 var = "c04_referencelist",
                 sub_var = "item",
                 time_window = range(1995,2016),
                 weighted_network = False, self_loop = False)
ref_cooc.main()

ref_cooc = novelpy.utils.cooc_utils.create_cooc(
                 collection_name = "Meshterms_sample",
                 year_var="year",
                 var = "Mesh_year_category",
                 sub_var = "descUI",
                 time_window = range(1995,2016),
                 weighted_network = True, self_loop = True)
ref_cooc.main()

ref_cooc = novelpy.utils.cooc_utils.create_cooc(
                 collection_name = "Meshterms_sample",
                 year_var="year",
                 var = "Mesh_year_category",
                 sub_var = "descUI",
                 time_window = range(1995,2016),
                 weighted_network = False, self_loop = False)
ref_cooc.main()


# %% Text-embedding Prepare
from novelpy.utils.embedding import Embedding

embedding = Embedding(
            year_variable = 'year',
            time_range = range(1995,2016),
            id_variable = 'PMID',
            references_variable = 'refs_pmid_wos',
            pretrain_path = 'en_core_sci_lg-0.5.4/en_core_sci_lg/en_core_sci_lg-0.5.4',
            title_variable = 'ArticleTitle',
            abstract_variable = 'a04_abstract',
            abstract_subvariable = 'AbstractText')

# articles

embedding.get_articles_centroid(
      collection_articles = 'Title_abs_sample',
      collection_embedding = 'embedding')


# %%
