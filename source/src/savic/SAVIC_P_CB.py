import numpy as np
import pandas as pd
import xgboost as xgb
import os
import savic

path_P_CB = os.path.dirname(savic.__file__) + '/Output/ML/models/xgbc_sus_cb.json'
xgbc_sus_cb = xgb.XGBClassifier()
xgbc_sus_cb.load_model(path_P_CB)

def SAVIC_P_CB(df_cb_):
    df_cb_pre_SP_ = df_cb_.copy()
    df_cb_pre_SP_[['beta_par_core', 'alph_c', 'tau_b', 'alph_b']] = \
    np.log10(df_cb_pre_SP_[['beta_par_core', 'alph_c', 'tau_b', 'alph_b']])
    df_cb_pre_SP_['unstable'] = xgbc_sus_cb.predict(df_cb_pre_SP_.values).astype('bool')
    
    df_cb_post_SP_ = df_cb_pre_SP_.copy()
    df_cb_post_SP_[['beta_par_core', 'alph_c', 'tau_b', 'alph_b']] = \
    pow(10., df_cb_post_SP_[['beta_par_core', 'alph_c', 'tau_b', 'alph_b']])
    
    return df_cb_post_SP_