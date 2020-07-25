import pyreadstat
import pandas as pd

""" Program for the International Assessment of Adult Competencies 2012/2014 """
""" U.S National Supplement Public Use Data Files - Household """
""" [Data Source] (https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2016667REV) """
""" File Name: 2016667REV_spss.zip"""

# Load spss file with pyreadstat to correctly seperate the values and metadata
# https://github.com/Roche/pyreadstat#reading-files
raw, meta = pyreadstat.read_sav('prgushp1_puf.sav')

# Evaluate the dataset as a whole
raw.info()
raw.head()

# Select variables and create a subset of data
# Country Information : CNTRYID (For US only data, this is not included)
# Participant ID : SEQID
# Demographic Information: Gender (GENDER_R), Highest Qualification - Education Levels - ISCED (B_Q01A)
# ISCED Levels can be found: http://uis.unesco.org/en/topic/international-standard-classification-education-isced
# Employment Status (C_D05) Employed, Unemployed, Out of Labor Force
# Index of Using Reading or Writing Skills at Home or at Work
#   At home: READHOME, WRITHOME
#   At work: READWORK, WRITWORK
# Index of Using Numeracy Skills at Home or at Work
#   At home: NUMHOME
#   At work: NUMWORK
# ICT Skills
#   At home: ICTHOME
#   At work: ICTWORK
# Literacy - plausible values: PVLIT1 to PVLIT10
# Numeracy - plausible valuesL PVNUM1 to PVNUM10

""" Research Focus: What are the subgroups of U.S. adults in characteristics of their ICT, numeracy, and literacy skills? """

# Create three dataframes: background variables (bkg), literacy scores (lit), and numeracy scores (num).

bkg = raw[["SEQID", "GENDER_R", "B_Q01A", "C_D05", "WRITHOME", "WRITWORK", "READHOME", "READWORK",
           "ICTHOME", "ICTWORK"]]
lit = raw[
    ['SEQID', 'PVLIT1', 'PVLIT2', 'PVLIT3', 'PVLIT4', 'PVLIT5', 'PVLIT6', 'PVLIT7', 'PVLIT8', 'PVLIT9', 'PVLIT10']]
num = raw[
    ['SEQID', 'PVNUM1', 'PVNUM2', 'PVNUM3', 'PVNUM4', 'PVNUM5', 'PVNUM6', 'PVNUM7', 'PVNUM8', 'PVNUM9', 'PVNUM10']]

# Check Data types and count of any missing values
bkg.info()
lit.info()
num.info()
# Missing data in background variables
bkg.isnull().sum()
# WRITWORK, READWORK, ICTHOME and LEARNATWORK all have over a thousands of missing values
# After reviewing the codebook, most of the missing values are skip responses due to the logic of the survey
# For example: WRITWORK has 2286 valid skip response and 177 not stated response

# Then, listwise deletion is used to remove participants who skip these variables.
# Reset index after removing null values
bkg_cleaned = bkg.dropna(how='any', inplace=False).reset_index(drop=True)
bkg_cleaned.isnull().sum()

""" Prepare Datasets """
""" Combine subsets of data: bkg, lit, and num in their raw forms before removing NULLs"""
# First, merge all background variables with all 10 literacy scores
bkg_lit = pd.merge(bkg, lit, on='SEQID')
# Second, merge all background variables, literacy scores, with all 10 numeracy scores
bkg_lit_num_raw = pd.merge(bkg_lit, num, on='SEQID')
bkg_lit_num_raw.info()

# Create a dataframe with descriptive statistics
descriptive_table1 = bkg_lit_num_raw.describe()
# Export the dataframe to CSV file
descriptive_table1.to_csv('Table1_Raw_Data.csv')

"""bkg_lit_num is the cleaned background dataset with all PVLIT and PVNUM values"""
# Drop any missing values in the bkg_lit_num dataset
bkg_lit_num_cleaned = bkg_lit_num_raw.dropna(how='any', inplace=False).reset_index(drop=True)
bkg_lit_num_cleaned.info()
descriptive_table2 = bkg_lit_num_cleaned.describe()
descriptive_table2.to_csv('Table2_Cleaned_Data.csv')

# Create a subset of background variables with literacy scores PVlIT1 and PVNUM1
subset1 = bkg_lit_num_cleaned.loc[:, ["GENDER_R", "B_Q01A", "C_D05", "WRITHOME", "WRITWORK", "READHOME", "READWORK",
                                      "ICTHOME", "ICTWORK", "PVLIT1", "PVNUM1"]]

# TODO  Create a loop to assign each subset
""" CRISP - Data Mining Methodology """
""" Cluster Analysis """
""" K-means clustering analysis"""

# Import scikit-learn resources: https://scikit-learn.org/stable/
from sklearn.cluster import KMeans

# Conduct clustering and add a cluster column to the data table
cluster_kmeans = KMeans(n_clusters=6, n_init=25, max_iter=300, random_state=0)
subset1['cluster'] = cluster_kmeans.fit_predict(subset1)
# Cluster is recorded as integer (which won't run in PCA)
subset1['cluster'] = subset1['cluster'].astype(float)
subset1.info()
# Create a dataframe with all rows for cluster number 0
cluster_0 = subset1[subset1['cluster'] == 0]
cluster_0.describe()  # Descriptive Summary of Cluster 0
cluster_0['GENDER_R'].value_counts()

# TODO create a loop to separate each cluster

# Select features
# Drop the SEQID column since it is not needed
features = list(bkg_lit_num_cleaned.columns)[1:]
data = bkg_lit_num_cleaned[features]

kmeans10 = KMeans(n_clusters=10, n_init=25, max_iter=300, random_state=0)
data['cluster'] = kmeans10.fit_predict(data)
# Cluster is recorded as integer (which won't run in PCA)
data['cluster'] = data['cluster'].astype(float)
data.info()

# Create a dataframe with all rows for cluster number 0
cluster_0 = data[data['cluster'] == 0]
cluster_0.describe()  # Descriptive Summary of Cluster 0
cluster_0['GENDER_R'].value_counts()
