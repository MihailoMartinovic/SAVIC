import numpy as np
import xgboost as xgb
import os
from sklearn.mixture import GaussianMixture
import savic


from savic import SAVIC_P_CBA
from savic import SAVIC_Q_CBA
from savic import SAVIC_C_CBA

def SAVIC_CoreBeamAlpha(df_cba_):
    
    df_cba_post_SP_ = SAVIC_P_CBA.SAVIC_P_CBA(df_cba_)
    df_cba_post_SQ_ = SAVIC_Q_CBA.SAVIC_Q_CBA(df_cba_post_SP_)
    df_cba_post_SC_ = SAVIC_C_CBA.SAVIC_C_CBA(df_cba_post_SQ_)
    
    return df_cba_post_SC_
    