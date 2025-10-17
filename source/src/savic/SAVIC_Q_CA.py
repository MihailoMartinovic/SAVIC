import numpy as np
import pandas as pd
import xgboost as xgb
import pandas as pd
import os
import savic

path_Q_CA = os.path.dirname(savic.__file__) + '/'

xgbc_kca = xgb.XGBClassifier()
xgbc_kca.load_model(path_Q_CA + 'Output/ML/models/xgbc_kca.json')

xgbr_c1_a1_k1 = xgb.XGBRegressor()
xgbr_c1_a1_k1.load_model(path_Q_CA + 'Output/ML/models/xgbr_ca_c1_a1_k1.json')

xgbr_c1_a1_k0 = xgb.XGBRegressor()
xgbr_c1_a1_k0.load_model(path_Q_CA + 'Output/ML/models/xgbr_ca_c1_a1_k0.json')

xgbr_c1_a0 = xgb.XGBRegressor()
xgbr_c1_a0.load_model(path_Q_CA + 'Output/ML/models/xgbr_ca_c1_a0_k0.json')

xgbr_c0_a1 = xgb.XGBRegressor()
xgbr_c0_a1.load_model(path_Q_CA + 'Output/ML/models/xgbr_ca_c0_a1_k0.json')

def SAVIC_Q_CA(df_ca_):
    
    df_ca_uns_ = df_ca_[df_ca_['unstable']].drop(columns = ['unstable'])
    
    df_ca_uns_pre_SQ_ = df_ca_uns_.copy()
    df_ca_uns_pre_SQ_[['beta_par_core', 'alph_c', 'alph_a']] = \
    np.log10(df_ca_uns_pre_SQ_[['beta_par_core', 'alph_c', 'alph_a']])
    df_ca_uns_pre_SQ_.columns = [['log_beta_par_core', 'log_alph_c', 'tau_a', 'log_alph_a', 'D_a', 'vv_a']]
    
    df_ca_uns_postC_SQ_ = df_ca_uns_pre_SQ_.copy()
    df_ca_uns_postC_SQ_['group'] = xgbc_kca.predict(df_ca_uns_pre_SQ_.values)
    
    df_ca_uns_preQ_SQ_ = df_ca_uns_postC_SQ_.copy()
    df_ca_uns_preQ_SQ_[['log_beta_par_core', 'log_alph_c', 'log_alph_a']] = \
    pow(10., df_ca_uns_preQ_SQ_[['log_beta_par_core', 'log_alph_c', 'log_alph_a']]) 
    df_ca_uns_preQ_SQ_.columns = ['beta_par_core', 'alph_c', 'tau_a', 'alph_a', 'D_a', 'vv_a', 'group']
    
    df_ca_uns_preQ_SQ_0_ = df_ca_uns_preQ_SQ_[df_ca_uns_preQ_SQ_['group'] == 0].drop(columns = ['group'])
    df_ca_uns_preQ_SQ_1_ = df_ca_uns_preQ_SQ_[df_ca_uns_preQ_SQ_['group'] == 1].drop(columns = ['group'])
    df_ca_uns_preQ_SQ_2_ = df_ca_uns_preQ_SQ_[df_ca_uns_preQ_SQ_['group'] == 2].drop(columns = ['group'])
    df_ca_uns_preQ_SQ_3_ = df_ca_uns_preQ_SQ_[df_ca_uns_preQ_SQ_['group'] == 3].drop(columns = ['group'])
    df_ca_uns_preQ_SQ_4_ = df_ca_uns_preQ_SQ_[df_ca_uns_preQ_SQ_['group'] == 4].drop(columns = ['group'])
    df_ca_uns_preQ_SQ_5_ = df_ca_uns_preQ_SQ_[df_ca_uns_preQ_SQ_['group'] == 5].drop(columns = ['group'])
    
    # regressors
    if df_ca_uns_preQ_SQ_0_.size > 0:
        df_ca_uns_preQ_SQ_0_log_ = df_ca_uns_preQ_SQ_0_.copy()


        df_ca_uns_preQ_SQ_0_log_[['beta_par_core', 'alph_c','alph_a']] = np.log10(df_ca_uns_preQ_SQ_0_log_[['beta_par_core', 'alph_c','alph_a']])
        df_ca_uns_preQ_SQ_0_log_[['Pow_core', 'Pow_alpha', 'kB_angle']] = xgbr_c1_a1_k1.predict(df_ca_uns_preQ_SQ_0_log_).astype(float)

        df_ca_uns_preQ_SQ_0_log_[['beta_par_core', 'alph_c','alph_a', 'Pow_core', 'Pow_alpha', 'kB_angle']] = \
        10**df_ca_uns_preQ_SQ_0_log_[['beta_par_core', 'alph_c','alph_a', 'Pow_core', 'Pow_alpha', 'kB_angle']]

        df_ca_uns_postQ_SQ_0_ = df_ca_uns_preQ_SQ_0_log_.copy()
        df_ca_uns_postQ_SQ_0_ = df_ca_uns_postQ_SQ_0_[['beta_par_core', 'alph_c', 'tau_a', 'D_a', 'alph_a', 'vv_a', 'Pow_core', 'Pow_alpha', 'kB_angle']]
    else:
        df_ca_uns_postQ_SQ_0_ = pd.DataFrame(columns = ['beta_par_core', 'alph_c', 'tau_a', 'D_a', 'alph_a', 'vv_a', 'Pow_core', 'Pow_alpha', 'kB_angle'])

    if df_ca_uns_preQ_SQ_1_.size > 0:
        df_ca_uns_preQ_SQ_1_log_ = df_ca_uns_preQ_SQ_1_.copy()


        df_ca_uns_preQ_SQ_1_log_[['beta_par_core', 'alph_c','alph_a']] = np.log10(df_ca_uns_preQ_SQ_1_log_[['beta_par_core', 'alph_c','alph_a']])
        df_ca_uns_preQ_SQ_1_log_[['Pow_core', 'Pow_alpha', 'kB_angle']] = xgbr_c1_a1_k0.predict(df_ca_uns_preQ_SQ_1_log_).astype(float)

        df_ca_uns_preQ_SQ_1_log_[['beta_par_core', 'alph_c','alph_a', 'Pow_core', 'Pow_alpha', 'kB_angle']] = \
        10**df_ca_uns_preQ_SQ_1_log_[['beta_par_core', 'alph_c','alph_a', 'Pow_core', 'Pow_alpha', 'kB_angle']]

        df_ca_uns_postQ_SQ_1_ = df_ca_uns_preQ_SQ_1_log_.copy()
        df_ca_uns_postQ_SQ_1_ = df_ca_uns_postQ_SQ_1_[['beta_par_core', 'alph_c', 'tau_a', 'D_a', 'alph_a', 'vv_a', 'Pow_core', 'Pow_alpha', 'kB_angle']]
    else:
        df_ca_uns_postQ_SQ_1_ = pd.DataFrame(columns = ['beta_par_core', 'alph_c', 'tau_a', 'D_a', 'alph_a', 'vv_a', 'Pow_core', 'Pow_alpha', 'kB_angle'])

    if df_ca_uns_preQ_SQ_2_.size > 0:
        df_ca_uns_preQ_SQ_2_log_ = df_ca_uns_preQ_SQ_2_.copy()

        df_ca_uns_preQ_SQ_2_log_[['beta_par_core', 'alph_c','alph_a']] = np.log10(df_ca_uns_preQ_SQ_2_log_[['beta_par_core', 'alph_c','alph_a']])
        df_ca_uns_preQ_SQ_2_log_[['Pow_core', 'kB_angle']] = xgbr_c1_a0.predict(df_ca_uns_preQ_SQ_2_log_).astype(float)

        df_ca_uns_preQ_SQ_2_log_[['beta_par_core', 'alph_c','alph_a', 'Pow_core', 'kB_angle']] = \
        10**df_ca_uns_preQ_SQ_2_log_[['beta_par_core', 'alph_c','alph_a', 'Pow_core', 'kB_angle']]

        df_ca_uns_postQ_SQ_2_ = df_ca_uns_preQ_SQ_2_log_.copy()
        df_ca_uns_postQ_SQ_2_['Pow_alpha'] = 0
        df_ca_uns_postQ_SQ_2_ = df_ca_uns_postQ_SQ_2_[['beta_par_core', 'alph_c', 'tau_a', 'D_a', 'alph_a', 'vv_a', 'Pow_core', 'Pow_alpha', 'kB_angle']]
    else:
        df_ca_uns_postQ_SQ_2_ = pd.DataFrame(columns = ['beta_par_core', 'alph_c', 'tau_a', 'D_a', 'alph_a', 'vv_a', 'Pow_core', 'Pow_alpha', 'kB_angle'])

    if df_ca_uns_preQ_SQ_3_.size > 0:
        df_ca_uns_preQ_SQ_3_log_ = df_ca_uns_preQ_SQ_3_.copy()


        df_ca_uns_preQ_SQ_3_log_[['beta_par_core', 'alph_c','alph_a']] = np.log10(df_ca_uns_preQ_SQ_3_log_[['beta_par_core', 'alph_c','alph_a']])
        df_ca_uns_preQ_SQ_3_log_[['Pow_core', 'kB_angle']] = xgbr_c1_a0.predict(df_ca_uns_preQ_SQ_3_log_).astype(float)

        df_ca_uns_preQ_SQ_3_log_[['beta_par_core', 'alph_c','alph_a', 'Pow_core', 'kB_angle']] = \
        10**df_ca_uns_preQ_SQ_3_log_[['beta_par_core', 'alph_c','alph_a', 'Pow_core', 'kB_angle']]

        df_ca_uns_postQ_SQ_3_ = df_ca_uns_preQ_SQ_3_log_.copy()
        df_ca_uns_postQ_SQ_3_['Pow_alpha'] = 0
        df_ca_uns_postQ_SQ_3_ = df_ca_uns_postQ_SQ_3_[['beta_par_core', 'alph_c', 'tau_a', 'D_a', 'alph_a', 'vv_a', 'Pow_core', 'Pow_alpha', 'kB_angle']]
    else:
        df_ca_uns_postQ_SQ_3_ = pd.DataFrame(columns = ['beta_par_core', 'alph_c', 'tau_a', 'D_a', 'alph_a', 'vv_a', 'Pow_core', 'Pow_alpha', 'kB_angle'])

    if df_ca_uns_preQ_SQ_4_.size > 0:
        df_ca_uns_preQ_SQ_4_log_ = df_ca_uns_preQ_SQ_4_.copy()


        df_ca_uns_preQ_SQ_4_log_[['beta_par_core', 'alph_c','alph_a']] = np.log10(df_ca_uns_preQ_SQ_4_log_[['beta_par_core', 'alph_c','alph_a']])
        df_ca_uns_preQ_SQ_4_log_[['Pow_alpha', 'kB_angle']] = xgbr_c0_a1.predict(df_ca_uns_preQ_SQ_4_log_).astype(float)

        df_ca_uns_preQ_SQ_4_log_[['beta_par_core', 'alph_c','alph_a', 'Pow_alpha', 'kB_angle']] = \
        10**df_ca_uns_preQ_SQ_4_log_[['beta_par_core', 'alph_c','alph_a', 'Pow_alpha', 'kB_angle']]

        df_ca_uns_postQ_SQ_4_ = df_ca_uns_preQ_SQ_4_log_.copy()
        df_ca_uns_postQ_SQ_4_['Pow_core'] = 0
        df_ca_uns_postQ_SQ_4_ = df_ca_uns_postQ_SQ_4_[['beta_par_core', 'alph_c', 'tau_a', 'D_a', 'alph_a', 'vv_a', 'Pow_core', 'Pow_alpha', 'kB_angle']]
    else:
        df_ca_uns_postQ_SQ_4_ = pd.DataFrame(columns = ['beta_par_core', 'alph_c', 'tau_a', 'D_a', 'alph_a', 'vv_a', 'Pow_core', 'Pow_alpha', 'kB_angle'])

    if df_ca_uns_preQ_SQ_5_.size > 0:
        df_ca_uns_preQ_SQ_5_log_ = df_ca_uns_preQ_SQ_5_.copy()


        df_ca_uns_preQ_SQ_5_log_[['beta_par_core', 'alph_c','alph_a']] = np.log10(df_ca_uns_preQ_SQ_5_log_[['beta_par_core', 'alph_c','alph_a']])
        df_ca_uns_preQ_SQ_5_log_[['Pow_alpha', 'kB_angle']] = xgbr_c0_a1.predict(df_ca_uns_preQ_SQ_5_log_).astype(float)

        df_ca_uns_preQ_SQ_5_log_[['beta_par_core', 'alph_c','alph_a', 'Pow_alpha', 'kB_angle']] = \
        10**df_ca_uns_preQ_SQ_5_log_[['beta_par_core', 'alph_c','alph_a', 'Pow_alpha', 'kB_angle']]

        df_ca_uns_postQ_SQ_5_ = df_ca_uns_preQ_SQ_5_log_.copy()
        df_ca_uns_postQ_SQ_5_['Pow_core'] = 0
        df_ca_uns_postQ_SQ_5_ = df_ca_uns_postQ_SQ_5_[['beta_par_core', 'alph_c', 'tau_a', 'D_a', 'alph_a', 'vv_a', 'Pow_core', 'Pow_alpha', 'kB_angle']]
    else:
        df_ca_uns_postQ_SQ_5_ = pd.DataFrame(columns = ['beta_par_core', 'alph_c', 'tau_a', 'D_a', 'alph_a', 'vv_a', 'Pow_core', 'Pow_alpha', 'kB_angle'])

    df_ca_uns_postQ_SQ_ = pd.concat([df_ca_uns_postQ_SQ_0_, df_ca_uns_postQ_SQ_1_, df_ca_uns_postQ_SQ_2_, \
                                 df_ca_uns_postQ_SQ_3_, df_ca_uns_postQ_SQ_4_, df_ca_uns_postQ_SQ_5_]).sort_index()
    
    df_ca_postQ_SQ_ = df_ca_.copy()

    df_ca_postQ_SQ_['group'] = np.nan
    df_ca_postQ_SQ_.loc[df_ca_uns_preQ_SQ_.index, 'group' ] = \
    df_ca_uns_preQ_SQ_['group']
    df_ca_postQ_SQ_['group'] = df_ca_postQ_SQ_['group']#.astype('Int64')

    df_ca_postQ_SQ_[['Pow_core', 'Pow_alpha', 'kB_angle']] = np.nan
    df_ca_postQ_SQ_.loc[df_ca_uns_postQ_SQ_.index, ['Pow_core', 'Pow_alpha', 'kB_angle'] ] = \
    df_ca_uns_postQ_SQ_[['Pow_core', 'Pow_alpha', 'kB_angle'] ]
    
    return df_ca_postQ_SQ_