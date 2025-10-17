import numpy as np
import xgboost as xgb
import os
from sklearn.mixture import GaussianMixture
import savic


from savic import SAVIC_P_CA
from savic import SAVIC_Q_CA
from savic import SAVIC_C_CA

def SAVIC_CoreAlpha(df_ca_):
    
    df_ca_post_SP_ = SAVIC_P_CA.SAVIC_P_CA(df_ca_)
    df_ca_post_SQ_ = SAVIC_Q_CA.SAVIC_Q_CA(df_ca_post_SP_)
    df_ca_post_SC_ = SAVIC_C_CA.SAVIC_C_CA(df_ca_post_SQ_)
    
    return df_ca_post_SC_
    