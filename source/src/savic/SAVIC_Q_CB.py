import numpy as np
import pandas as pd
import xgboost as xgb
import pandas as pd
import os
import savic

path_Q_CB = os.path.dirname(savic.__file__) + '/'

xgbc_kcb = xgb.XGBClassifier()
xgbc_kcb.load_model(path_Q_CB + 'Output/ML/models/xgbc_kcb.json')

xgbr_c1_b1 = xgb.XGBRegressor()
xgbr_c1_b1.load_model(path_Q_CB + 'Output/ML/models/xgbr_cb_c1_b1.json')

xgbr_c1_b0 = xgb.XGBRegressor()
xgbr_c1_b0.load_model(path_Q_CB + 'Output/ML/models/xgbr_cb_c1_b0.json')

xgbr_c0_b1_k0 = xgb.XGBRegressor()
xgbr_c0_b1_k0.load_model(path_Q_CB + 'Output/ML/models/xgbr_cb_c0_b1_k0.json')

xgbr_c0_b1_k1 = xgb.XGBRegressor()
xgbr_c0_b1_k1.load_model(path_Q_CB + 'Output/ML/models/xgbr_cb_c0_b1_k1.json')

def SAVIC_Q_CB(df_cb_):
    
    df_cb_uns_ = df_cb_[df_cb_['unstable']].drop(columns = ['unstable'])
    df_cb_uns_pre_SQ_ = df_cb_uns_.copy()
    df_cb_uns_pre_SQ_[['beta_par_core', 'alph_c', 'alph_b']] = \
    np.log10(df_cb_uns_pre_SQ_[['beta_par_core', 'alph_c', 'alph_b']])
    df_cb_uns_pre_SQ_.columns = [['log_beta_par_core', 'log_alph_c', 'tau_b', 'log_alph_b', 'D_b', 'vv_b']]
    
    df_cb_uns_postC_SQ_ = df_cb_uns_pre_SQ_.copy()
    df_cb_uns_postC_SQ_['group'] = xgbc_kcb.predict(df_cb_uns_pre_SQ_.values)
    
    df_cb_uns_preQ_SQ_ = df_cb_uns_postC_SQ_.copy()
    df_cb_uns_preQ_SQ_[['log_beta_par_core', 'log_alph_c', 'log_alph_b']] = \
    pow(10., df_cb_uns_preQ_SQ_[['log_beta_par_core', 'log_alph_c', 'log_alph_b']]) 
    df_cb_uns_preQ_SQ_.columns = ['beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'group']
    
    # regressors
    df_cb_uns_preQ_SQ_0_ = df_cb_uns_preQ_SQ_[df_cb_uns_preQ_SQ_['group'] == 0].drop(columns = ['group'])
    df_cb_uns_preQ_SQ_1_ = df_cb_uns_preQ_SQ_[df_cb_uns_preQ_SQ_['group'] == 1].drop(columns = ['group'])
    df_cb_uns_preQ_SQ_2_ = df_cb_uns_preQ_SQ_[df_cb_uns_preQ_SQ_['group'] == 2].drop(columns = ['group'])
    df_cb_uns_preQ_SQ_3_ = df_cb_uns_preQ_SQ_[df_cb_uns_preQ_SQ_['group'] == 3].drop(columns = ['group'])
    df_cb_uns_preQ_SQ_4_ = df_cb_uns_preQ_SQ_[df_cb_uns_preQ_SQ_['group'] == 4].drop(columns = ['group'])
    df_cb_uns_preQ_SQ_5_ = df_cb_uns_preQ_SQ_[df_cb_uns_preQ_SQ_['group'] == 5].drop(columns = ['group'])
    
    
    if df_cb_uns_preQ_SQ_0_.size > 0:
        df_cb_uns_preQ_SQ_0_log_ = df_cb_uns_preQ_SQ_0_.copy()

        df_cb_uns_preQ_SQ_0_log_[['beta_par_core', 'alph_c','alph_b']] = \
        np.log10(df_cb_uns_preQ_SQ_0_log_[['beta_par_core', 'alph_c','alph_b']])
        
        df_cb_uns_preQ_SQ_0_log_[['Pow_core', 'Pow_beam', 'kB_angle']] = \
        xgbr_c1_b1.predict(df_cb_uns_preQ_SQ_0_log_).astype(float)

        df_cb_uns_preQ_SQ_0_log_[['beta_par_core', 'alph_c','alph_b', 'Pow_core', 'Pow_beam', 'kB_angle']] = \
        10**df_cb_uns_preQ_SQ_0_log_[['beta_par_core', 'alph_c','alph_b', 'Pow_core', 'Pow_beam', 'kB_angle']]

        df_cb_uns_postQ_SQ_0_ = df_cb_uns_preQ_SQ_0_log_.copy()
        df_cb_uns_postQ_SQ_0_ = df_cb_uns_postQ_SQ_0_[['beta_par_core', 'alph_c', 'tau_b', 'D_b', 'alph_b', 'vv_b', 'Pow_core', 'Pow_beam', 'kB_angle']]
    else:
        df_cb_uns_postQ_SQ_0_ = pd.DataFrame(columns = ['beta_par_core', 'alph_c', 'tau_b', 'D_b', 'alph_b', 'vv_b', 'Pow_core', 'Pow_beam', 'kB_angle'])

    if df_cb_uns_preQ_SQ_1_.size > 0:
        df_cb_uns_preQ_SQ_1_log_ = df_cb_uns_preQ_SQ_1_.copy()


        df_cb_uns_preQ_SQ_1_log_[['beta_par_core', 'alph_c','alph_b']] = \
        np.log10(df_cb_uns_preQ_SQ_1_log_[['beta_par_core', 'alph_c','alph_b']])
        
        df_cb_uns_preQ_SQ_1_log_[['Pow_core', 'Pow_beam', 'kB_angle']] = \
        xgbr_c1_b1.predict(df_cb_uns_preQ_SQ_1_log_).astype(float)

        df_cb_uns_preQ_SQ_1_log_[['beta_par_core', 'alph_c','alph_b', 'Pow_core', 'Pow_beam', 'kB_angle']] = \
        10**df_cb_uns_preQ_SQ_1_log_[['beta_par_core', 'alph_c','alph_b', 'Pow_core', 'Pow_beam', 'kB_angle']]

        df_cb_uns_postQ_SQ_1_ = df_cb_uns_preQ_SQ_1_log_.copy()
        df_cb_uns_postQ_SQ_1_ = df_cb_uns_postQ_SQ_1_[['beta_par_core', 'alph_c', 'tau_b', 'D_b', 'alph_b', 'vv_b', 'Pow_core', 'Pow_beam', 'kB_angle']]
    else:
        df_cb_uns_postQ_SQ_1_ = pd.DataFrame(columns = ['beta_par_core', 'alph_c', 'tau_b', 'D_b', 'alph_b', 'vv_b', 'Pow_core', 'Pow_beam', 'kB_angle'])

    if df_cb_uns_preQ_SQ_2_.size > 0:
        df_cb_uns_preQ_SQ_2_log_ = df_cb_uns_preQ_SQ_2_.copy()


        df_cb_uns_preQ_SQ_2_log_[['beta_par_core', 'alph_c','alph_b']] = \
        np.log10(df_cb_uns_preQ_SQ_2_log_[['beta_par_core', 'alph_c','alph_b']])
        
        df_cb_uns_preQ_SQ_2_log_[['Pow_core', 'kB_angle']] = \
        xgbr_c1_b0.predict(df_cb_uns_preQ_SQ_2_log_).astype(float)

        df_cb_uns_preQ_SQ_2_log_[['beta_par_core', 'alph_c','alph_b', 'Pow_core', 'kB_angle']] = \
        10**df_cb_uns_preQ_SQ_2_log_[['beta_par_core', 'alph_c','alph_b', 'Pow_core', 'kB_angle']]

        df_cb_uns_postQ_SQ_2_ = df_cb_uns_preQ_SQ_2_log_.copy()
        df_cb_uns_postQ_SQ_2_['Pow_beam'] = 0
        df_cb_uns_postQ_SQ_2_ = df_cb_uns_postQ_SQ_2_[['beta_par_core', 'alph_c', 'tau_b', 'D_b', 'alph_b', 'vv_b', 'Pow_core', 'Pow_beam', 'kB_angle']]
    else:
        df_cb_uns_postQ_SQ_2_ = pd.DataFrame(columns = ['beta_par_core', 'alph_c', 'tau_b', 'D_b', 'alph_b', 'vv_b', 'Pow_core', 'Pow_beam', 'kB_angle'])

    if df_cb_uns_preQ_SQ_3_.size > 0:
        df_cb_uns_preQ_SQ_3_log_ = df_cb_uns_preQ_SQ_3_.copy()


        df_cb_uns_preQ_SQ_3_log_[['beta_par_core', 'alph_c','alph_b']] = \
        np.log10(df_cb_uns_preQ_SQ_3_log_[['beta_par_core', 'alph_c','alph_b']])
        
        df_cb_uns_preQ_SQ_3_log_[['Pow_core', 'kB_angle']] = \
        xgbr_c1_b0.predict(df_cb_uns_preQ_SQ_3_log_).astype(float)

        df_cb_uns_preQ_SQ_3_log_[['beta_par_core', 'alph_c','alph_b', 'Pow_core', 'kB_angle']] = \
        10**df_cb_uns_preQ_SQ_3_log_[['beta_par_core', 'alph_c','alph_b', 'Pow_core', 'kB_angle']]

        df_cb_uns_postQ_SQ_3_ = df_cb_uns_preQ_SQ_3_log_.copy()
        df_cb_uns_postQ_SQ_3_['Pow_beam'] = 0
        df_cb_uns_postQ_SQ_3_ = df_cb_uns_postQ_SQ_3_[['beta_par_core', 'alph_c', 'tau_b', 'D_b', 'alph_b', 'vv_b', 'Pow_core', 'Pow_beam', 'kB_angle']]
    else:
        df_cb_uns_postQ_SQ_3_ = pd.DataFrame(columns = ['beta_par_core', 'alph_c', 'tau_b', 'D_b', 'alph_b', 'vv_b', 'Pow_core', 'Pow_beam', 'kB_angle'])

    if df_cb_uns_preQ_SQ_4_.size > 0:
        df_cb_uns_preQ_SQ_4_log_ = df_cb_uns_preQ_SQ_4_.copy()


        df_cb_uns_preQ_SQ_4_log_[['beta_par_core', 'alph_c','alph_b']] = \
        np.log10(df_cb_uns_preQ_SQ_4_log_[['beta_par_core', 'alph_c','alph_b']])
        
        df_cb_uns_preQ_SQ_4_log_[['Pow_beam', 'kB_angle']] = \
        xgbr_c0_b1_k1.predict(df_cb_uns_preQ_SQ_4_log_).astype(float)

        df_cb_uns_preQ_SQ_4_log_[['beta_par_core', 'alph_c','alph_b', 'Pow_beam', 'kB_angle']] = \
        10**df_cb_uns_preQ_SQ_4_log_[['beta_par_core', 'alph_c','alph_b', 'Pow_beam', 'kB_angle']]

        df_cb_uns_postQ_SQ_4_ = df_cb_uns_preQ_SQ_4_log_.copy()
        df_cb_uns_postQ_SQ_4_['Pow_core'] = 0
        df_cb_uns_postQ_SQ_4_ = df_cb_uns_postQ_SQ_4_[['beta_par_core', 'alph_c', 'tau_b', 'D_b', 'alph_b', 'vv_b', 'Pow_core', 'Pow_beam', 'kB_angle']]
    else:
        df_cb_uns_postQ_SQ_4_ = pd.DataFrame(columns = ['beta_par_core', 'alph_c', 'tau_b', 'D_b', 'alph_b', 'vv_b', 'Pow_core', 'Pow_beam', 'kB_angle'])

    if df_cb_uns_preQ_SQ_5_.size > 0:
        df_cb_uns_preQ_SQ_5_log_ = df_cb_uns_preQ_SQ_5_.copy()


        df_cb_uns_preQ_SQ_5_log_[['beta_par_core', 'alph_c','alph_b']] = \
        np.log10(df_cb_uns_preQ_SQ_5_log_[['beta_par_core', 'alph_c','alph_b']])
        
        df_cb_uns_preQ_SQ_5_log_[['Pow_beam', 'kB_angle']] = \
        xgbr_c0_b1_k0.predict(df_cb_uns_preQ_SQ_5_log_).astype(float)

        df_cb_uns_preQ_SQ_5_log_[['beta_par_core', 'alph_c','alph_b', 'Pow_beam', 'kB_angle']] = \
        10**df_cb_uns_preQ_SQ_5_log_[['beta_par_core', 'alph_c','alph_b', 'Pow_beam', 'kB_angle']]

        df_cb_uns_postQ_SQ_5_ = df_cb_uns_preQ_SQ_5_log_.copy()
        df_cb_uns_postQ_SQ_5_['Pow_core'] = 0
        df_cb_uns_postQ_SQ_5_ = df_cb_uns_postQ_SQ_5_[['beta_par_core', 'alph_c', 'tau_b', 'D_b', 'alph_b', 'vv_b', 'Pow_core', 'Pow_beam', 'kB_angle']]
    else:
        df_cb_uns_postQ_SQ_5_ = pd.DataFrame(columns = ['beta_par_core', 'alph_c', 'tau_b', 'D_b', 'alph_b', 'vv_b', 'Pow_core', 'Pow_beam', 'kB_angle'])

    df_cb_uns_postQ_SQ_ = pd.concat([df_cb_uns_postQ_SQ_0_, df_cb_uns_postQ_SQ_1_, df_cb_uns_postQ_SQ_2_, \
                                 df_cb_uns_postQ_SQ_3_, df_cb_uns_postQ_SQ_4_, df_cb_uns_postQ_SQ_5_]).sort_index()
    
    df_cb_postQ_SQ_ = df_cb_.copy()

    df_cb_postQ_SQ_['group'] = np.nan
    df_cb_postQ_SQ_.loc[df_cb_uns_preQ_SQ_.index, 'group' ] = \
    df_cb_uns_preQ_SQ_['group']
    df_cb_postQ_SQ_['group'] = df_cb_postQ_SQ_['group']#.astype('Int64')

    df_cb_postQ_SQ_[['Pow_core', 'Pow_beam', 'kB_angle']] = np.nan
    df_cb_postQ_SQ_.loc[df_cb_uns_postQ_SQ_.index, ['Pow_core', 'Pow_beam', 'kB_angle'] ] = \
    df_cb_uns_postQ_SQ_[['Pow_core', 'Pow_beam', 'kB_angle'] ]
    
    return df_cb_postQ_SQ_