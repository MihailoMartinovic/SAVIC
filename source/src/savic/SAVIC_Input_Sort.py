import numpy as np
import pandas as pd
import xgboost as xgb
import os
import savic

def SAVIC_Input_Sort(df_load_):
    
    cols_c_ = ['beta_par_core', 'alph_c']
    cols_cb_ = ['beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b']
    cols_ca_ = ['beta_par_core', 'alph_c', 'tau_a', 'alph_a', 'D_a', 'vv_a']
    cols_cba_ = ['beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'tau_a', 'alph_a', 'D_a', 'vv_a']
    
    df_c_empty = pd.DataFrame(columns = cols_c_)
    df_cb_empty = pd.DataFrame(columns = cols_cb_)
    df_ca_empty = pd.DataFrame(columns = cols_ca_)
    df_cba_empty = pd.DataFrame(columns = cols_cba_)
    
    if set(df_load_.columns) == set(cols_cba_):
        df_c_ = df_load_[~(df_load_['D_b'] > 0) & ~(df_load_['D_a'] > 0)][cols_c_]
        df_cb_ = df_load_[(df_load_['D_b'] > 0) & ~(df_load_['D_a'] > 0)][cols_cb_]
        df_ca_ = df_load_[~(df_load_['D_b'] > 0) & (df_load_['D_a'] > 0)][cols_ca_]
        df_cba_ = df_load_[(df_load_['D_b'] > 0) & (df_load_['D_a'] > 0)]
        if df_c_.size == 0:
            df_c_ = df_c_empty
        if df_cb_.size == 0:
            df_cb_ = df_cb_empty
        if df_ca_.size == 0:
            df_ca_ = df_ca_empty
        if df_cba_.size == 0:
            df_cba_ = df_cba_empty
        return df_c_, df_cb_, df_ca_, df_cba_
    elif set(df_load_.columns) == set(cols_ca_):
        df_c_ = df_load_[~(df_load_['D_a'] > 0)][cols_c_]
        df_ca_ = df_load_[df_load_['D_a'] > 0]
        if df_c_.size == 0:
            df_c_ = df_c_empty
        if df_ca_.size == 0:
            df_ca_ = df_ca_empty
        df_cb_ = df_cb_empty
        df_cba_ = df_cba_empty
        return df_c_, df_cb_, df_ca_, df_cba_
    elif set(df_load_.columns) == set(cols_cb_):
        df_c_ = df_load_[~(df_load_['D_b'] > 0)][cols_c_]
        df_cb_ = df_load_[df_load_['D_b'] > 0]
        if df_c_.size == 0:
            df_c_ = df_c_empty
        if df_cb_.size == 0:
            df_cb_ = df_cb_empty
        df_ca_ = df_ca_empty
        df_cba_ = df_cba_empty
        return df_c_, df_cb_, df_ca_, df_cba_
    elif set(df_load_.columns) == set(cols_c_):
        df_c_ = df_load_
        if df_c_.size == 0:
            df_c_ = df_c_empty
        df_cb_ = df_cb_empty
        df_ca_ = df_ca_empty
        df_cba_ = df_cba_empty
        return df_c_, df_cb_, df_ca_, df_cba_
    else:
        raise ValueError('Column set not recognized')
        
        