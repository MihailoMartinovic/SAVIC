import numpy as np
import pandas as pd
import xgboost as xgb
import os
from sklearn.mixture import GaussianMixture
import savic

gmm_cb_name = os.path.dirname(savic.__file__) + '/Output/ML/models/GMM_CB/GMM_CB'

# reload
means = np.load(gmm_cb_name + '_means.npy')
covar = np.load(gmm_cb_name + '_covariances.npy')
gmm_cb = GaussianMixture(n_components = len(means), covariance_type='full')
gmm_cb.precisions_cholesky_ = np.linalg.cholesky(np.linalg.inv(covar))
gmm_cb.weights_ = np.load(gmm_cb_name + '_weights.npy')
gmm_cb.means_ = means
gmm_cb.covariances_ = covar


def SAVIC_C_CB(df_cb_):
    
    df_cb_uns_ = df_cb_[df_cb_['unstable']].drop(columns = ['unstable'])
    df_cb_uns_pre_SC_ = df_cb_uns_.copy()

    df_cb_uns_pre_SC_['uns_IC'] = (1. + 0.367 / ( df_cb_uns_pre_SC_['beta_par_core'] - 0.011 )**0.364) < df_cb_uns_pre_SC_['alph_c']
    df_cb_uns_pre_SC_['uns_Mirror'] = (1. + 0.702 / ( df_cb_uns_pre_SC_['beta_par_core'] + 0.009 )**0.674) < df_cb_uns_pre_SC_['alph_c']
    df_cb_uns_pre_SC_['uns_FM'] = (1. - 0.408 / ( df_cb_uns_pre_SC_['beta_par_core'] - 0.410 )**0.529) > df_cb_uns_pre_SC_['alph_c']
    df_cb_uns_pre_SC_['uns_OFH'] = (1. - 1.454 / ( df_cb_uns_pre_SC_['beta_par_core'] + 0.178 )**1.023) > df_cb_uns_pre_SC_['alph_c']
    df_cb_uns_pre_SC_['uns_core'] = df_cb_uns_pre_SC_['uns_OFH'] | df_cb_uns_pre_SC_['uns_FM'] | df_cb_uns_pre_SC_['uns_Mirror'] | df_cb_uns_pre_SC_['uns_IC']

    df_cb_uns_pre_SC_['beta_par_beam'] = df_cb_uns_pre_SC_['beta_par_core'] * df_cb_uns_pre_SC_['D_b'] / df_cb_uns_pre_SC_['tau_b']
    df_cb_uns_pre_SC_['lambda_FH_beta'] = ( (df_cb_uns_pre_SC_['beta_par_core'] + df_cb_uns_pre_SC_['beta_par_beam']) - \
    (df_cb_uns_pre_SC_['beta_par_core'] * df_cb_uns_pre_SC_['alph_c'] + df_cb_uns_pre_SC_['beta_par_beam'] * df_cb_uns_pre_SC_['alph_b']) ) / 2.
    df_cb_uns_pre_SC_['lambda_FH_beam'] = df_cb_uns_pre_SC_['D_b'] * df_cb_uns_pre_SC_['vv_b']**2.
    df_cb_uns_pre_SC_['lambda_FH'] = df_cb_uns_pre_SC_['lambda_FH_beta'] + df_cb_uns_pre_SC_['lambda_FH_beam']# + df_cb_uns_pre_SC_['lambda_FH_alpha']
    df_cb_uns_pre_SC_['lambda_FH'] = df_cb_uns_pre_SC_['lambda_FH'] > 1.

    df_cb_uns_pre_SC_['Pow_core'][df_cb_uns_pre_SC_['Pow_core'] < 0] = 0
    df_cb_uns_pre_SC_['Pow_beam'][df_cb_uns_pre_SC_['Pow_beam'] < 0] = 0

    
    column_list_cb_ = ['beta_par_core', 'alph_c', 'kB_angle', \
                       'tau_b', 'D_b', 'alph_b', 'vv_b', 'Pow_core', 'Pow_beam', \
                       'uns_IC', 'uns_FM', 'uns_OFH', 'uns_core', 'lambda_FH']

    df_cb_uns_pre_SC_cut_ = df_cb_uns_pre_SC_[column_list_cb_]
    
    df_cb_uns_pre_SC_cut_[['beta_par_core', 'alph_c']] = np.log10(df_cb_uns_pre_SC_cut_[['beta_par_core', 'alph_c']])
    df_cb_uns_pre_SC_cut_.rename(columns={"beta_par_core": "log_beta_par_core", "alph_c": "log_alph_c"}, inplace = True)
    
    df_cb_uns_post_SC_ = df_cb_uns_pre_SC_cut_.copy()
    df_cb_uns_post_SC_['cluster'] = gmm_cb.predict(df_cb_uns_pre_SC_cut_.values)
    
    df_cb_uns_post_SC_[['log_beta_par_core', 'log_alph_c']] = \
    pow(10., df_cb_uns_post_SC_[['log_beta_par_core', 'log_alph_c']])
    df_cb_uns_post_SC_.rename(columns={"log_beta_par_core": "beta_par_core", "log_alph_c": "alph_c"}, inplace = True)
    
    df_cb_uns_post_SC_['ins_type'] = np.nan
    ins_types_cb_ = ['Oblique FM (B); resonant with Core', 'IC (B); $T_\perp/T_{||} < 1$', 'Oblique FM (B)', \
                    'Oblique Firehose', 'IC (B); $T_\perp/T_{||} > 1$', 'Parallel Firehose', 'IC (B), unstable core', 'IC (C)']
    for cluster, ins_type in zip(np.arange(8), ins_types_cb_):
        df_cb_uns_post_SC_['ins_type'][df_cb_uns_post_SC_['cluster'] == cluster] = ins_type
    
    df_cb_post_SC_ = df_cb_.copy()
    df_cb_post_SC_['ins_type'] = np.nan
    df_cb_post_SC_.loc[df_cb_uns_post_SC_.index, ['ins_type']] = df_cb_uns_post_SC_['ins_type']
    
    return df_cb_post_SC_