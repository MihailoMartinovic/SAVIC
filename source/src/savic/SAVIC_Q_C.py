import numpy as np
import pandas as pd
import xgboost as xgb
import os
import savic

path_Q_C = os.path.dirname(savic.__file__) + '/Output/ML/models/xgbr_c.json'
xgbr_c1_c = xgb.XGBRegressor()
xgbr_c1_c.load_model(path_Q_C)

def SAVIC_Q_C(df_c_):
    
    df_c_uns_ = df_c_[df_c_['unstable']].drop(columns = ['unstable'])
    
    df_c_uns_pre_SQ_ = df_c_uns_.copy()
    df_c_uns_pre_SQ_ = np.log10(df_c_uns_pre_SQ_)
    df_c_uns_pre_SQ_.columns = [['log_beta_par_core', 'log_alph_c']]
    
    df_c_uns_pre_SQ_[['log_Pow_core', 'log_kB_angle']] = xgbr_c1_c.predict(df_c_uns_pre_SQ_.values)
    
    df_c_uns_post_SQ_ = pow(10., df_c_uns_pre_SQ_)
    df_c_uns_post_SQ_.columns = ['beta_par_core', 'alph_c', 'Pow_core', 'kB_angle']
    
    df_c_post_SQ_ = df_c_.copy()
    df_c_post_SQ_[['Pow_core', 'kB_angle']] = np.nan
    df_c_post_SQ_.loc[df_c_uns_post_SQ_.index, ['Pow_core', 'kB_angle']] = df_c_uns_post_SQ_[['Pow_core', 'kB_angle']]
    
    return df_c_post_SQ_