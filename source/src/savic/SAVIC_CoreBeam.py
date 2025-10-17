import numpy as np
import xgboost as xgb
import os
from sklearn.mixture import GaussianMixture
import savic


from savic import SAVIC_P_CB
from savic import SAVIC_Q_CB
from savic import SAVIC_C_CB

def SAVIC_CoreBeam(df_cb_):
    
    df_cb_post_SP_ = SAVIC_P_CB.SAVIC_P_CB(df_cb_)
    df_cb_post_SQ_ = SAVIC_Q_CB.SAVIC_Q_CB(df_cb_post_SP_)
    df_cb_post_SC_ = SAVIC_C_CB.SAVIC_C_CB(df_cb_post_SQ_)
    
    return df_cb_post_SC_
    