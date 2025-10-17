import numpy as np
import pandas as pd
import xgboost as xgb
import os
from sklearn.mixture import GaussianMixture
import savic

gmm_cba_name = os.path.dirname(savic.__file__) + '/Output/ML/models/GMM_CBA/GMM_CBA'

# reload
means = np.load(gmm_cba_name + '_means.npy')
covar = np.load(gmm_cba_name + '_covariances.npy')
gmm_cba = GaussianMixture(n_components = len(means), covariance_type='full')
gmm_cba.precisions_cholesky_ = np.linalg.cholesky(np.linalg.inv(covar))
gmm_cba.weights_ = np.load(gmm_cba_name + '_weights.npy')
gmm_cba.means_ = means
gmm_cba.covariances_ = covar


def SAVIC_C_CBA(df_cba_):
    df_cba_uns_ = df_cba_[df_cba_['unstable']].drop(columns = ['unstable'])
    
    df_cba_uns_pre_SC_ = df_cba_uns_.copy()

    df_cba_uns_pre_SC_['uns_IC'] = (1. + 0.367 / ( df_cba_uns_pre_SC_['beta_par_core'] - 0.011 )**0.364) < df_cba_uns_pre_SC_['alph_c']
    df_cba_uns_pre_SC_['uns_Mirror'] = (1. + 0.702 / ( df_cba_uns_pre_SC_['beta_par_core'] + 0.009 )**0.674) < df_cba_uns_pre_SC_['alph_c']
    df_cba_uns_pre_SC_['uns_FM'] = (1. - 0.408 / ( df_cba_uns_pre_SC_['beta_par_core'] - 0.410 )**0.529) > df_cba_uns_pre_SC_['alph_c']
    df_cba_uns_pre_SC_['uns_OFH'] = (1. - 1.454 / ( df_cba_uns_pre_SC_['beta_par_core'] + 0.178 )**1.023) > df_cba_uns_pre_SC_['alph_c']
    df_cba_uns_pre_SC_['uns_core'] = df_cba_uns_pre_SC_['uns_OFH'] | df_cba_uns_pre_SC_['uns_FM'] | df_cba_uns_pre_SC_['uns_Mirror'] | df_cba_uns_pre_SC_['uns_IC']


    df_cba_uns_pre_SC_['beta_par_beam'] = df_cba_uns_pre_SC_['beta_par_core'] * df_cba_uns_pre_SC_['D_b'] / df_cba_uns_pre_SC_['tau_b']
    df_cba_uns_pre_SC_['beta_par_alpha'] = df_cba_uns_pre_SC_['beta_par_core'] * df_cba_uns_pre_SC_['D_a'] / df_cba_uns_pre_SC_['tau_a']

    df_cba_uns_pre_SC_['lambda_FH_beta'] = ( (df_cba_uns_pre_SC_['beta_par_core'] + df_cba_uns_pre_SC_['beta_par_beam'] + df_cba_uns_pre_SC_['beta_par_alpha']) - \
    (df_cba_uns_pre_SC_['beta_par_core'] * df_cba_uns_pre_SC_['alph_c'] + df_cba_uns_pre_SC_['beta_par_beam'] * df_cba_uns_pre_SC_['alph_b'] + \
    df_cba_uns_pre_SC_['beta_par_alpha'] * df_cba_uns_pre_SC_['alph_a']) ) / 2.

    df_cba_uns_pre_SC_['lambda_FH_alpha'] = 4 * df_cba_uns_pre_SC_['D_a'] / (1. + df_cba_uns_pre_SC_['D_b'] + 4 * df_cba_uns_pre_SC_['D_a']) * df_cba_uns_pre_SC_['vv_a']**2.
    df_cba_uns_pre_SC_['lambda_FH_beam'] = df_cba_uns_pre_SC_['D_b'] / (1. + df_cba_uns_pre_SC_['D_b'] + 4 * df_cba_uns_pre_SC_['D_a']) * df_cba_uns_pre_SC_['vv_b']**2.
    df_cba_uns_pre_SC_['lambda_FH'] = df_cba_uns_pre_SC_['lambda_FH_beta'] + df_cba_uns_pre_SC_['lambda_FH_alpha'] + df_cba_uns_pre_SC_['lambda_FH_beam']
    df_cba_uns_pre_SC_['lambda_FH'] = df_cba_uns_pre_SC_['lambda_FH'] > 1.

    df_cba_uns_pre_SC_['Pow_core'][df_cba_uns_pre_SC_['Pow_core'] < 0] = 0
    df_cba_uns_pre_SC_['Pow_beam'][df_cba_uns_pre_SC_['Pow_beam'] < 0] = 0
    df_cba_uns_pre_SC_['Pow_alpha'][df_cba_uns_pre_SC_['Pow_alpha'] < 0] = 0

    column_list_cba_ = ['beta_par_core', 'alph_c', 'kB_angle', \
                        'tau_b', 'alph_b', 'D_b', 'vv_b', \
                        'tau_a', 'D_a', 'alph_a', 'vv_a', 'Pow_core', 'Pow_beam', 'Pow_alpha', \
                        'uns_IC', 'uns_FM', 'uns_OFH', 'uns_core', 'lambda_FH']

    df_cba_uns_pre_SC_cut_ = df_cba_uns_pre_SC_[column_list_cba_]
    
    df_cba_uns_pre_SC_cut_[['beta_par_core', 'alph_c']] = np.log10(df_cba_uns_pre_SC_cut_[['beta_par_core', 'alph_c']])
    df_cba_uns_pre_SC_cut_.rename(columns={"beta_par_core": "log_beta_par_core", "alph_c": "log_alph_c"}, inplace = True)
    
    df_cba_uns_post_SC_ = df_cba_uns_pre_SC_cut_.copy()
    df_cba_uns_post_SC_['cluster'] = gmm_cba.predict(df_cba_uns_pre_SC_cut_.values)
    
    df_cba_uns_post_SC_[['log_beta_par_core', 'log_alph_c']] = \
    pow(10., df_cba_uns_post_SC_[['log_beta_par_core', 'log_alph_c']])
    df_cba_uns_post_SC_.rename(columns={"log_beta_par_core": "beta_par_core", "log_alph_c": "alph_c"}, inplace = True)
    
    df_cba_uns_post_SC_['r_cluster'] = np.nan
    df_cba_uns_post_SC_['r_cluster'][df_cba_uns_post_SC_['cluster'] == 0] = 9
    df_cba_uns_post_SC_['r_cluster'][df_cba_uns_post_SC_['cluster'] == 1] = 2
    df_cba_uns_post_SC_['r_cluster'][df_cba_uns_post_SC_['cluster'] == 2] = 1
    df_cba_uns_post_SC_['r_cluster'][df_cba_uns_post_SC_['cluster'] == 3] = 4
    df_cba_uns_post_SC_['r_cluster'][df_cba_uns_post_SC_['cluster'] == 4] = 7
    df_cba_uns_post_SC_['r_cluster'][df_cba_uns_post_SC_['cluster'] == 5] = 5
    df_cba_uns_post_SC_['r_cluster'][df_cba_uns_post_SC_['cluster'] == 6] = 12
    df_cba_uns_post_SC_['r_cluster'][df_cba_uns_post_SC_['cluster'] == 7] = 1
    df_cba_uns_post_SC_['r_cluster'][df_cba_uns_post_SC_['cluster'] == 8] = 11
    df_cba_uns_post_SC_['r_cluster'][df_cba_uns_post_SC_['cluster'] == 9] = 10
    df_cba_uns_post_SC_['r_cluster'][df_cba_uns_post_SC_['cluster'] == 10] = 7
    df_cba_uns_post_SC_['r_cluster'][df_cba_uns_post_SC_['cluster'] == 11] = 6
    df_cba_uns_post_SC_['r_cluster'][df_cba_uns_post_SC_['cluster'] == 12] = 8
    df_cba_uns_post_SC_['r_cluster'][df_cba_uns_post_SC_['cluster'] == 13] = 3

    df_cba_uns_post_SC_['r_cluster'] = df_cba_uns_post_SC_['r_cluster'].astype(int)
    
    df_cba_uns_post_SC_['ins_type'] = np.nan
    ins_types_cba_ = ['IC (C)', 'IC (C); A unstable', \
                      'IC (B), C unstable', 'IC (B); A unstable', 'IC (B); high B anis', 'IC (B); borderline PFH', \
                      'IC (A)', 'IC (A); C absorbing', \
                      'Oblique Firehose', 'Parallel Firehose', \
                      'FM (B), oblique', 'FM (B), oblique; mirror']
    for cluster, ins_type in zip(np.arange(12), ins_types_cba_):
        df_cba_uns_post_SC_['ins_type'][df_cba_uns_post_SC_['cluster'] == cluster] = ins_type
    
    df_cba_post_SC_ = df_cba_.copy()
    df_cba_post_SC_['ins_type'] = np.nan
    df_cba_post_SC_.loc[df_cba_uns_post_SC_.index, ['ins_type']] = df_cba_uns_post_SC_['ins_type']
    
    return df_cba_post_SC_
    