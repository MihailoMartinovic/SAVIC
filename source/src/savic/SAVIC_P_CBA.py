import numpy as np
import pandas as pd
import xgboost as xgb
import os
import savic

path_P_CBA = os.path.dirname(savic.__file__) + '/Output/ML/models/xgbc_sus_cba.json'
xgbc_sus_cba = xgb.XGBClassifier()
xgbc_sus_cba.load_model(path_P_CBA)

def SAVIC_P_CBA(df_cba_):
    df_cba_pre_SP_ = df_cba_.copy()
    df_cba_pre_SP_['unstable'] = xgbc_sus_cba.predict(df_cba_pre_SP_.values).astype('bool')
    df_cba_post_SP_ = df_cba_pre_SP_.copy()
    
    return df_cba_post_SP_
    