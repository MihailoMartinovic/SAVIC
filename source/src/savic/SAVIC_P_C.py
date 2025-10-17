import numpy as np
import pandas as pd
import xgboost as xgb
import os
import savic

path_P_C = os.path.dirname(savic.__file__) + '/Output/ML/models/xgbc_sus_c.json'
xgbc_sus_c = xgb.XGBClassifier()
xgbc_sus_c.load_model(path_P_C)

def SAVIC_P_C(df_c_):
    
    df_c_pre_SP_ = df_c_.copy()
    df_c_pre_SP_ = np.log10(df_c_pre_SP_)
    df_c_pre_SP_['unstable'] = xgbc_sus_c.predict(df_c_pre_SP_.values).astype('bool')
    
    df_c_post_SP_ = df_c_pre_SP_.copy()
    df_c_post_SP_[['beta_par_core', 'alph_c']] = pow(10., df_c_post_SP_[['beta_par_core', 'alph_c']])
    
    return df_c_post_SP_