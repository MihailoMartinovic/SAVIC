import numpy as np
import pandas as pd
import xgboost as xgb
import os
import savic

path_P_CA = os.path.dirname(savic.__file__) + '/Output/ML/models/xgbc_sus_ca.json'
xgbc_sus_ca = xgb.XGBClassifier()
xgbc_sus_ca.load_model(path_P_CA)

def SAVIC_P_CA(df_ca_):
    df_ca_pre_SP_ = df_ca_.copy()
    df_ca_pre_SP_[['beta_par_core', 'alph_c', 'tau_a', 'alph_a']] = \
    np.log10(df_ca_pre_SP_[['beta_par_core', 'alph_c', 'tau_a', 'alph_a']])
    df_ca_pre_SP_['unstable'] = xgbc_sus_ca.predict(df_ca_pre_SP_.values).astype('bool')
    
    df_ca_post_SP_ = df_ca_pre_SP_.copy()
    df_ca_post_SP_[['beta_par_core', 'alph_c', 'tau_a', 'alph_a']] = \
    pow(10., df_ca_post_SP_[['beta_par_core', 'alph_c', 'tau_a', 'alph_a']])
    
    return df_ca_post_SP_