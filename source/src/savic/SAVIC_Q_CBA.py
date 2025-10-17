import numpy as np
import pandas as pd
import xgboost as xgb
import pandas as pd
import os
import savic

path_Q_CBA = os.path.dirname(savic.__file__) + '/'

xgbc_kcba = xgb.XGBClassifier()
xgbc_kcba.load_model(path_Q_CBA + 'Output/ML/models/xgbc_kcba.json')

xgbr_c1_b1_a1 = xgb.XGBRegressor()
xgbr_c1_b1_a1.load_model(path_Q_CBA + 'Output/ML/models/xgbr_cba_c1_b1_a1.json')

xgbr_c1_b1_a0 = xgb.XGBRegressor()
xgbr_c1_b1_a0.load_model(path_Q_CBA + 'Output/ML/models/xgbr_cba_c1_b1_a0.json')

xgbr_c1_b0_a1 = xgb.XGBRegressor()
xgbr_c1_b0_a1.load_model(path_Q_CBA + 'Output/ML/models/xgbr_cba_c1_b0_a1.json')

xgbr_c1_b0_a0 = xgb.XGBRegressor()
xgbr_c1_b0_a0.load_model(path_Q_CBA + 'Output/ML/models/xgbr_cba_c1_b0_a0.json')

xgbr_c0_b1_a1 = xgb.XGBRegressor()
xgbr_c0_b1_a1.load_model(path_Q_CBA + 'Output/ML/models/xgbr_cba_c0_b1_a1.json')

xgbr_c0_b1_a0_k1 = xgb.XGBRegressor()
xgbr_c0_b1_a0_k1.load_model(path_Q_CBA + 'Output/ML/models/xgbr_cba_c0_b1_a0_k1.json')

xgbr_c0_b1_a0_k0 = xgb.XGBRegressor()
xgbr_c0_b1_a0_k0.load_model(path_Q_CBA + 'Output/ML/models/xgbr_cba_c0_b1_a0_k0.json')

xgbr_c0_b0_a1 = xgb.XGBRegressor()
xgbr_c0_b0_a1.load_model(path_Q_CBA + 'Output/ML/models/xgbr_cba_c0_b0_a1.json')


def SAVIC_Q_CBA(df_cba_):
    
    df_cba_uns_ = df_cba_[df_cba_['unstable']].drop(columns = ['unstable'])
    
    df_cba_uns_pre_SQ_ = df_cba_uns_.copy()
    df_cba_uns_pre_SQ_[['beta_par_core', 'alph_c', 'alph_b', 'alph_a']] = \
    np.log10(df_cba_uns_pre_SQ_[['beta_par_core', 'alph_c', 'alph_b', 'alph_a']])
    df_cba_uns_pre_SQ_.columns = [['log_beta_par_core', 'log_alph_c', \
                                   'tau_b', 'log_alph_b', 'D_b', 'vv_b', \
                                   'tau_a', 'log_alph_a', 'D_a', 'vv_a']]
    
    df_cba_uns_postC_SQ_ = df_cba_uns_pre_SQ_.copy()
    df_cba_uns_postC_SQ_['group'] = xgbc_kcba.predict(df_cba_uns_pre_SQ_.values)
    
    df_cba_uns_preQ_SQ_ = df_cba_uns_postC_SQ_.copy()
    df_cba_uns_preQ_SQ_[['log_beta_par_core', 'log_alph_c', 'log_alph_b', 'log_alph_a']] = \
    pow(10., df_cba_uns_preQ_SQ_[['log_beta_par_core', 'log_alph_c', 'log_alph_b', 'log_alph_a']]) 
    df_cba_uns_preQ_SQ_.columns = ['beta_par_core', 'alph_c', \
                                   'tau_b', 'alph_b', 'D_b', 'vv_b', \
                                   'tau_a', 'alph_a', 'D_a', 'vv_a', 'group']

    
    df_cba_uns_preQ_SQ_0_ = df_cba_uns_preQ_SQ_[df_cba_uns_preQ_SQ_['group'] == 0].drop(columns = ['group'])
    df_cba_uns_preQ_SQ_1_ = df_cba_uns_preQ_SQ_[df_cba_uns_preQ_SQ_['group'] == 1].drop(columns = ['group'])
    df_cba_uns_preQ_SQ_2_ = df_cba_uns_preQ_SQ_[df_cba_uns_preQ_SQ_['group'] == 2].drop(columns = ['group'])
    df_cba_uns_preQ_SQ_3_ = df_cba_uns_preQ_SQ_[df_cba_uns_preQ_SQ_['group'] == 3].drop(columns = ['group'])
    df_cba_uns_preQ_SQ_4_ = df_cba_uns_preQ_SQ_[df_cba_uns_preQ_SQ_['group'] == 4].drop(columns = ['group'])
    df_cba_uns_preQ_SQ_5_ = df_cba_uns_preQ_SQ_[df_cba_uns_preQ_SQ_['group'] == 5].drop(columns = ['group'])
    df_cba_uns_preQ_SQ_6_ = df_cba_uns_preQ_SQ_[df_cba_uns_preQ_SQ_['group'] == 6].drop(columns = ['group'])
    df_cba_uns_preQ_SQ_7_ = df_cba_uns_preQ_SQ_[df_cba_uns_preQ_SQ_['group'] == 7].drop(columns = ['group'])
    
    
    # regressors
    cba_full_col_list_ = ['beta_par_core', 'alph_c', \
                          'tau_b', 'D_b', 'alph_b', 'vv_b', \
                          'tau_a', 'D_a', 'alph_a', 'vv_a', \
                          'Pow_core', 'Pow_beam', 'Pow_alpha', 'kB_angle']

    # group 0 - C1B1A1
    if df_cba_uns_preQ_SQ_0_.size > 0:
        df_cba_uns_preQ_SQ_0_log_ = df_cba_uns_preQ_SQ_0_.copy()

        df_cba_uns_preQ_SQ_0_log_[['beta_par_core', 'alph_c', 'alph_b','alph_a']] = \
        np.log10(df_cba_uns_preQ_SQ_0_log_[['beta_par_core', 'alph_c', 'alph_b','alph_a']])
        df_cba_uns_preQ_SQ_0_log_[['Pow_core', 'Pow_beam', 'Pow_alpha', 'kB_angle']] = \
        xgbr_c1_b1_a1.predict(df_cba_uns_preQ_SQ_0_log_).astype(float)

        df_cba_uns_preQ_SQ_0_log_[['beta_par_core', 'alph_c', 'alph_b','alph_a', 'Pow_core', 'Pow_beam', 'Pow_alpha', 'kB_angle']] = \
        10**df_cba_uns_preQ_SQ_0_log_[['beta_par_core', 'alph_c', 'alph_b','alph_a', 'Pow_core', 'Pow_beam', 'Pow_alpha', 'kB_angle']]

        df_cba_uns_postQ_SQ_0_ = df_cba_uns_preQ_SQ_0_log_.copy()
        df_cba_uns_postQ_SQ_0_ = df_cba_uns_postQ_SQ_0_[cba_full_col_list_]
    else:
        df_cba_uns_postQ_SQ_0_ = pd.DataFrame(columns = cba_full_col_list_)



    # group 1 - C1B1A0
    if df_cba_uns_preQ_SQ_1_.size > 0:
        df_cba_uns_preQ_SQ_1_log_ = df_cba_uns_preQ_SQ_1_.copy()

        df_cba_uns_preQ_SQ_1_log_[['beta_par_core', 'alph_c', 'alph_b','alph_a']] = \
        np.log10(df_cba_uns_preQ_SQ_1_log_[['beta_par_core', 'alph_c', 'alph_b', 'alph_a']])

        df_cba_uns_preQ_SQ_1_log_[['Pow_core', 'Pow_beam', 'kB_angle']] = \
        xgbr_c1_b1_a0.predict(df_cba_uns_preQ_SQ_1_log_).astype(float)

        df_cba_uns_preQ_SQ_1_log_[['beta_par_core', 'alph_c', 'alph_b','alph_a', 'Pow_core', 'Pow_beam', 'kB_angle']] = \
        10**df_cba_uns_preQ_SQ_1_log_[['beta_par_core', 'alph_c', 'alph_b','alph_a', 'Pow_core', 'Pow_beam', 'kB_angle']]

        df_cba_uns_postQ_SQ_1_ = df_cba_uns_preQ_SQ_1_log_.copy()
        df_cba_uns_postQ_SQ_1_['Pow_alpha'] = 0
        df_cba_uns_postQ_SQ_1_ = df_cba_uns_postQ_SQ_1_[cba_full_col_list_]
    else:
        df_cba_uns_postQ_SQ_1_ = pd.DataFrame(columns = cba_full_col_list_)

    # group 2 - C1B0A1
    if df_cba_uns_preQ_SQ_2_.size > 0:
        df_cba_uns_preQ_SQ_2_log_ = df_cba_uns_preQ_SQ_2_.copy()

        df_cba_uns_preQ_SQ_2_log_[['beta_par_core', 'alph_c', 'alph_b','alph_a']] = \
        np.log10(df_cba_uns_preQ_SQ_2_log_[['beta_par_core', 'alph_c', 'alph_b', 'alph_a']])

        df_cba_uns_preQ_SQ_2_log_[['Pow_core', 'Pow_alpha', 'kB_angle']] = \
        xgbr_c1_b0_a1.predict(df_cba_uns_preQ_SQ_2_log_).astype(float)

        df_cba_uns_preQ_SQ_2_log_[['beta_par_core', 'alph_c', 'alph_b','alph_a', 'Pow_core', 'Pow_alpha', 'kB_angle']] = \
        10**df_cba_uns_preQ_SQ_2_log_[['beta_par_core', 'alph_c', 'alph_b','alph_a', 'Pow_core', 'Pow_alpha', 'kB_angle']]

        df_cba_uns_postQ_SQ_2_ = df_cba_uns_preQ_SQ_2_log_.copy()
        df_cba_uns_postQ_SQ_2_['Pow_beam'] = 0
        df_cba_uns_postQ_SQ_2_ = df_cba_uns_postQ_SQ_2_[cba_full_col_list_]
    else:
        df_cba_uns_postQ_SQ_2_ = pd.DataFrame(columns = cba_full_col_list_)

    # group 3 - C1B0A0
    if df_cba_uns_preQ_SQ_3_.size > 0:
        df_cba_uns_preQ_SQ_3_log_ = df_cba_uns_preQ_SQ_3_.copy()

        df_cba_uns_preQ_SQ_3_log_[['beta_par_core', 'alph_c', 'alph_b','alph_a']] = \
        np.log10(df_cba_uns_preQ_SQ_3_log_[['beta_par_core', 'alph_c', 'alph_b', 'alph_a']])

        df_cba_uns_preQ_SQ_3_log_[['Pow_core', 'kB_angle']] = \
        xgbr_c1_b0_a0.predict(df_cba_uns_preQ_SQ_3_log_).astype(float)

        df_cba_uns_preQ_SQ_3_log_[['beta_par_core', 'alph_c', 'alph_b','alph_a', 'Pow_core', 'kB_angle']] = \
        10**df_cba_uns_preQ_SQ_3_log_[['beta_par_core', 'alph_c', 'alph_b','alph_a', 'Pow_core', 'kB_angle']]

        df_cba_uns_postQ_SQ_3_ = df_cba_uns_preQ_SQ_3_log_.copy()
        df_cba_uns_postQ_SQ_3_[['Pow_beam', 'Pow_alpha']] = 0
        df_cba_uns_postQ_SQ_3_ = df_cba_uns_postQ_SQ_3_[cba_full_col_list_]
    else:
        df_cba_uns_postQ_SQ_3_ = pd.DataFrame(columns = cba_full_col_list_)

    # group 4 - C0B1A1
    if df_cba_uns_preQ_SQ_4_.size > 0:
        df_cba_uns_preQ_SQ_4_log_ = df_cba_uns_preQ_SQ_4_.copy()

        df_cba_uns_preQ_SQ_4_log_[['beta_par_core', 'alph_c', 'alph_b','alph_a']] = \
        np.log10(df_cba_uns_preQ_SQ_4_log_[['beta_par_core', 'alph_c', 'alph_b', 'alph_a']])

        df_cba_uns_preQ_SQ_4_log_[['Pow_beam', 'Pow_alpha', 'kB_angle']] = \
        xgbr_c0_b1_a1.predict(df_cba_uns_preQ_SQ_4_log_).astype(float)

        df_cba_uns_preQ_SQ_4_log_[['beta_par_core', 'alph_c', 'alph_b','alph_a', 'Pow_beam', 'Pow_alpha', 'kB_angle']] = \
        10**df_cba_uns_preQ_SQ_4_log_[['beta_par_core', 'alph_c', 'alph_b','alph_a', 'Pow_beam', 'Pow_alpha', 'kB_angle']]

        df_cba_uns_postQ_SQ_4_ = df_cba_uns_preQ_SQ_4_log_.copy()
        df_cba_uns_postQ_SQ_4_[['Pow_core']] = 0
        df_cba_uns_postQ_SQ_4_ = df_cba_uns_postQ_SQ_4_[cba_full_col_list_]
    else:
        df_cba_uns_postQ_SQ_4_ = pd.DataFrame(columns = cba_full_col_list_)


    # group 5 - C0B1A0k1
    if df_cba_uns_preQ_SQ_5_.size > 0:
        df_cba_uns_preQ_SQ_5_log_ = df_cba_uns_preQ_SQ_5_.copy()

        df_cba_uns_preQ_SQ_5_log_[['beta_par_core', 'alph_c', 'alph_b','alph_a']] = \
        np.log10(df_cba_uns_preQ_SQ_5_log_[['beta_par_core', 'alph_c', 'alph_b', 'alph_a']])

        df_cba_uns_preQ_SQ_5_log_[['Pow_beam', 'kB_angle']] = \
        xgbr_c0_b1_a0_k1.predict(df_cba_uns_preQ_SQ_5_log_).astype(float)

        df_cba_uns_preQ_SQ_5_log_[['beta_par_core', 'alph_c', 'alph_b','alph_a', 'Pow_beam', 'kB_angle']] = \
        10**df_cba_uns_preQ_SQ_5_log_[['beta_par_core', 'alph_c', 'alph_b','alph_a', 'Pow_beam', 'kB_angle']]

        df_cba_uns_postQ_SQ_5_ = df_cba_uns_preQ_SQ_5_log_.copy()
        df_cba_uns_postQ_SQ_5_[['Pow_core', 'Pow_alpha']] = 0
        df_cba_uns_postQ_SQ_5_ = df_cba_uns_postQ_SQ_5_[cba_full_col_list_]
    else:
        df_cba_uns_postQ_SQ_5_ = pd.DataFrame(columns = cba_full_col_list_)    

    # group 6 - C0B1A0k0
    if df_cba_uns_preQ_SQ_6_.size > 0:
        df_cba_uns_preQ_SQ_6_log_ = df_cba_uns_preQ_SQ_6_.copy()

        df_cba_uns_preQ_SQ_6_log_[['beta_par_core', 'alph_c', 'alph_b','alph_a']] = \
        np.log10(df_cba_uns_preQ_SQ_6_log_[['beta_par_core', 'alph_c', 'alph_b', 'alph_a']])

        df_cba_uns_preQ_SQ_6_log_[['Pow_beam', 'kB_angle']] = \
        xgbr_c0_b1_a0_k0.predict(df_cba_uns_preQ_SQ_6_log_).astype(float)

        df_cba_uns_preQ_SQ_6_log_[['beta_par_core', 'alph_c', 'alph_b','alph_a', 'Pow_beam', 'kB_angle']] = \
        10**df_cba_uns_preQ_SQ_6_log_[['beta_par_core', 'alph_c', 'alph_b','alph_a', 'Pow_beam', 'kB_angle']]

        df_cba_uns_postQ_SQ_6_ = df_cba_uns_preQ_SQ_6_log_.copy()
        df_cba_uns_postQ_SQ_6_[['Pow_core', 'Pow_alpha']] = 0
        df_cba_uns_postQ_SQ_6_ = df_cba_uns_postQ_SQ_6_[cba_full_col_list_]
    else:
        df_cba_uns_postQ_SQ_6_ = pd.DataFrame(columns = cba_full_col_list_)    


    # group 7 - C0B0A1
    if df_cba_uns_preQ_SQ_7_.size > 0:
        df_cba_uns_preQ_SQ_7_log_ = df_cba_uns_preQ_SQ_7_.copy()

        df_cba_uns_preQ_SQ_7_log_[['beta_par_core', 'alph_c', 'alph_b','alph_a']] = \
        np.log10(df_cba_uns_preQ_SQ_7_log_[['beta_par_core', 'alph_c', 'alph_b', 'alph_a']])

        df_cba_uns_preQ_SQ_7_log_[['Pow_alpha', 'kB_angle']] = \
        xgbr_c0_b0_a1.predict(df_cba_uns_preQ_SQ_7_log_).astype(float)

        df_cba_uns_preQ_SQ_7_log_[['beta_par_core', 'alph_c', 'alph_b','alph_a', 'Pow_alpha', 'kB_angle']] = \
        10**df_cba_uns_preQ_SQ_7_log_[['beta_par_core', 'alph_c', 'alph_b','alph_a', 'Pow_alpha', 'kB_angle']]

        df_cba_uns_postQ_SQ_7_ = df_cba_uns_preQ_SQ_7_log_.copy()
        df_cba_uns_postQ_SQ_7_[['Pow_core', 'Pow_beam']] = 0
        df_cba_uns_postQ_SQ_7_ = df_cba_uns_postQ_SQ_7_[cba_full_col_list_]
    else:
        df_cba_uns_postQ_SQ_7_ = pd.DataFrame(columns = cba_full_col_list_)    


    df_cba_uns_postQ_SQ_ = pd.concat([df_cba_uns_postQ_SQ_0_, df_cba_uns_postQ_SQ_1_, df_cba_uns_postQ_SQ_2_, \
                                      df_cba_uns_postQ_SQ_3_, df_cba_uns_postQ_SQ_4_, df_cba_uns_postQ_SQ_5_, \
                                      df_cba_uns_postQ_SQ_6_,df_cba_uns_postQ_SQ_7_]).sort_index()
    
    df_cba_postQ_SQ_ = df_cba_.copy()

    df_cba_postQ_SQ_['group'] = np.nan
    df_cba_postQ_SQ_.loc[df_cba_uns_preQ_SQ_.index, 'group' ] = \
    df_cba_uns_preQ_SQ_['group']
    df_cba_postQ_SQ_['group'] = df_cba_postQ_SQ_['group']#.astype('Int64')

    df_cba_postQ_SQ_[['Pow_core', 'Pow_beam', 'Pow_alpha', 'kB_angle']] = np.nan
    df_cba_postQ_SQ_.loc[df_cba_uns_postQ_SQ_.index, ['Pow_core', 'Pow_beam', 'Pow_alpha', 'kB_angle'] ] = \
    df_cba_uns_postQ_SQ_[['Pow_core', 'Pow_beam', 'Pow_alpha', 'kB_angle'] ]
    
    return df_cba_postQ_SQ_
    