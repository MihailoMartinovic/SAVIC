import numpy as np
import pandas as pd
import xgboost as xgb
import os
from sklearn.mixture import GaussianMixture
import savic


from savic import SAVIC_Input_Sort
from savic import SAVIC_Core
from savic import SAVIC_CoreBeam
from savic import SAVIC_CoreAlpha
from savic import SAVIC_CoreBeamAlpha

def SAVIC(df_load_):
    
    df_s_ = []
    
    df_c_, df_cb_, df_ca_, df_cba_ = SAVIC_Input_Sort.SAVIC_Input_Sort(df_load_)
    
    if df_c_.size > 0:
        SAVIC_df_c_ = SAVIC_Core.SAVIC_Core(df_c_)
        df_s_.append(SAVIC_df_c_)
    if df_cb_.size > 0:
        SAVIC_df_cb_ = SAVIC_CoreBeam.SAVIC_CoreBeam(df_cb_)
        df_s_.append(SAVIC_df_cb_)
    if df_ca_.size > 0:
        SAVIC_df_ca_ = SAVIC_CoreAlpha.SAVIC_CoreAlpha(df_ca_)
        df_s_.append(SAVIC_df_ca_)
    if df_cba_.size > 0:
        SAVIC_df_cba_ = SAVIC_CoreBeamAlpha.SAVIC_CoreBeamAlpha(df_cba_)
        df_s_.append(SAVIC_df_cba_)
    SAVIC_df_ = pd.concat(df_s_)
    
    col_CBA_ = ['beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'tau_a', \
       'alph_a', 'D_a', 'vv_a', 'unstable', 'group', 'Pow_core', 'Pow_beam', \
       'Pow_alpha', 'kB_angle', 'ins_type']
    
    if df_cba_.size > 0:
        columns_ = col_CBA_
    elif (df_cb_.size > 0) & (df_ca_.size > 0):
        columns_ = col_CBA_
    elif df_cb_.size > 0:
        columns_ = SAVIC_df_cb_.columns
    elif df_ca_.size > 0:
        columns_ = SAVIC_df_ca_.columns
    else:
        columns_ = SAVIC_df_c_.columns
    
    SAVIC_df_ = SAVIC_df_[columns_]
    
    SAVIC_df_ = SAVIC_df_.reindex(df_load_.index)
    
    return SAVIC_df_
    
    