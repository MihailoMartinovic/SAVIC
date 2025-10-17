import numpy as np
import pandas as pd
import xgboost as xgb
import os
from sklearn.mixture import GaussianMixture
import savic

gmm_ca_name = os.path.dirname(savic.__file__) + '/Output/ML/models/GMM_CA/GMM_CA'

# reload
means = np.load(gmm_ca_name + '_means.npy')
covar = np.load(gmm_ca_name + '_covariances.npy')
gmm_ca = GaussianMixture(n_components = len(means), covariance_type='full')
gmm_ca.precisions_cholesky_ = np.linalg.cholesky(np.linalg.inv(covar))
gmm_ca.weights_ = np.load(gmm_ca_name + '_weights.npy')
gmm_ca.means_ = means
gmm_ca.covariances_ = covar


def SAVIC_C_CA(df_ca_):
    
    df_ca_uns_ = df_ca_[df_ca_['unstable']].drop(columns = ['unstable'])
    
    df_ca_uns_pre_SC_ = df_ca_uns_.copy()

    df_ca_uns_pre_SC_['uns_IC'] = (1. + 0.367 / ( df_ca_uns_pre_SC_['beta_par_core'] - 0.011 )**0.364) < df_ca_uns_pre_SC_['alph_c']
    df_ca_uns_pre_SC_['uns_Mirror'] = (1. + 0.702 / ( df_ca_uns_pre_SC_['beta_par_core'] + 0.009 )**0.674) < df_ca_uns_pre_SC_['alph_c']
    df_ca_uns_pre_SC_['uns_FM'] = (1. - 0.408 / ( df_ca_uns_pre_SC_['beta_par_core'] - 0.410 )**0.529) > df_ca_uns_pre_SC_['alph_c']
    df_ca_uns_pre_SC_['uns_OFH'] = (1. - 1.454 / ( df_ca_uns_pre_SC_['beta_par_core'] + 0.178 )**1.023) > df_ca_uns_pre_SC_['alph_c']
    df_ca_uns_pre_SC_['uns_core'] = df_ca_uns_pre_SC_['uns_OFH'] | df_ca_uns_pre_SC_['uns_FM'] | df_ca_uns_pre_SC_['uns_Mirror'] | df_ca_uns_pre_SC_['uns_IC']

    df_ca_uns_pre_SC_['beta_par_alpha'] = df_ca_uns_pre_SC_['beta_par_core'] * df_ca_uns_pre_SC_['D_a'] / df_ca_uns_pre_SC_['tau_a']
    df_ca_uns_pre_SC_['lambda_FH_beta'] = ( (df_ca_uns_pre_SC_['beta_par_core'] + df_ca_uns_pre_SC_['beta_par_alpha']) - \
    (df_ca_uns_pre_SC_['beta_par_core'] * df_ca_uns_pre_SC_['alph_c'] + df_ca_uns_pre_SC_['beta_par_alpha'] * df_ca_uns_pre_SC_['alph_a']) ) / 2.
    df_ca_uns_pre_SC_['lambda_FH_alpha'] = 4 * df_ca_uns_pre_SC_['D_a'] / (1. + df_ca_uns_pre_SC_['D_a'] + 4 * df_ca_uns_pre_SC_['D_a']) * df_ca_uns_pre_SC_['vv_a']**2.
    df_ca_uns_pre_SC_['lambda_FH'] = df_ca_uns_pre_SC_['lambda_FH_beta'] + df_ca_uns_pre_SC_['lambda_FH_alpha']
    df_ca_uns_pre_SC_['lambda_FH'] = df_ca_uns_pre_SC_['lambda_FH'] > 1.

    df_ca_uns_pre_SC_['Pow_core'][df_ca_uns_pre_SC_['Pow_core'] < 0] = 0
    df_ca_uns_pre_SC_['Pow_alpha'][df_ca_uns_pre_SC_['Pow_alpha'] < 0] = 0
    
    column_list_ca_ = ['beta_par_core', 'alph_c', 'kB_angle', \
                       'tau_a', 'D_a', 'alph_a', 'vv_a', 'Pow_core', 'Pow_alpha', \
                       'uns_IC', 'uns_FM', 'uns_OFH', 'uns_core', 'lambda_FH']

    df_ca_uns_pre_SC_cut_ = df_ca_uns_pre_SC_[column_list_ca_]
    
    df_ca_uns_pre_SC_cut_[['beta_par_core', 'alph_c']] = np.log10(df_ca_uns_pre_SC_cut_[['beta_par_core', 'alph_c']])
    df_ca_uns_pre_SC_cut_.rename(columns={"beta_par_core": "log_beta_par_core", "alph_c": "log_alph_c"}, inplace = True)
    
    df_ca_uns_post_SC_ = df_ca_uns_pre_SC_cut_.copy()
    df_ca_uns_post_SC_['cluster'] = gmm_ca.predict(df_ca_uns_pre_SC_cut_.values)
    
    df_ca_uns_post_SC_['ins_type'] = np.nan
    ins_types_ca_ = ['Parallel Firehose', 'IC (A)', 'Oblique Firehose', \
                     'CGL Firehose; Mirror', 'A anis; borderline PFH', 'IC (C)']
    for cluster, ins_type in zip(np.arange(6), ins_types_ca_):
        df_ca_uns_post_SC_['ins_type'][df_ca_uns_post_SC_['cluster'] == cluster] = ins_type
    
    df_ca_post_SC_ = df_ca_.copy()
    df_ca_post_SC_['ins_type'] = np.nan
    df_ca_post_SC_.loc[df_ca_uns_post_SC_.index, ['ins_type']] = df_ca_uns_post_SC_['ins_type']
    
    return df_ca_post_SC_