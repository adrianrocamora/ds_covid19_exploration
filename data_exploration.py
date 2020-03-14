# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + [markdown]
# # Data Exploration

# + [markdown]
# ## Data Sources:
# 2019 Coronavirus dataset (January - February 2020)
# Tracking the spread of 2019-nCoV
# https://www.kaggle.com/brendaso/2019-coronavirus-dataset-01212020-01262020
# 
# Novel Corona Virus 2019 Dataset
# Day level information on covid-19 affected cases
# https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset/kernels


# + [markdown]
# ## Imports 
# + 
import os
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np
from scipy.signal import periodogram
sns.set(style="white")
sns.set()

# + [markdown]
# ## Data Wrangling
# + 
data_dir = 'data/novel-corona-virus-2019-dataset/'

file_confimed = 'time_series_covid_19_confirmed.csv'
file_deaths = 'time_series_covid_19_deaths.csv'
file_recovered = 'time_series_covid_19_recovered.csv'

df_confirmed = pd.read_csv(os.path.join(data_dir, file_confimed))
df_deaths = pd.read_csv(os.path.join(data_dir, file_deaths))
df_recovered = pd.read_csv(os.path.join(data_dir, file_recovered))

# + 
df_confirmed

# + [markdown]
# ## Analyzing a famous cruise ship's data with this dataset
# The Diamond Princess cruise ship is one of the most famous (and experimentally controlled) sources of informations for 
# + 
province_state = 'Diamond Princess cruise ship'
dp_deaths = df_deaths['3/10/20'][df_deaths['Province/State'] == province_state]
dp_confirmed = df_confirmed['3/10/20'][df_confirmed['Province/State'] == province_state]

# + 
dp_deaths


