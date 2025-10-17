import numpy as np
import xgboost as xgb
import os
from sklearn.mixture import GaussianMixture
import savic


from savic import SAVIC_P_C
from savic import SAVIC_Q_C
from savic import SAVIC_C_C

def SAVIC_Core(df_c_):
    
    df_c_post_SP_ = SAVIC_P_C.SAVIC_P_C(df_c_)
    df_c_post_SQ_ = SAVIC_Q_C.SAVIC_Q_C(df_c_post_SP_)
    df_c_post_SC_ = SAVIC_C_C.SAVIC_C_C(df_c_post_SQ_)
    
    return df_c_post_SC_
    