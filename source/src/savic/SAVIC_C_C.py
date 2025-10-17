import numpy as np
import pandas as pd
import xgboost as xgb
import os
from sklearn.mixture import GaussianMixture
import savic

gmm_c_name = os.path.dirname(savic.__file__) + '/Output/ML/models/GMM_C/GMM_C'

# reload
means = np.load(gmm_c_name + '_means.npy')
covar = np.load(gmm_c_name + '_covariances.npy')
gmm_c = GaussianMixture(n_components = len(means), covariance_type='full')
gmm_c.precisions_cholesky_ = np.linalg.cholesky(np.linalg.inv(covar))
gmm_c.weights_ = np.load(gmm_c_name + '_weights.npy')
gmm_c.means_ = means
gmm_c.covariances_ = covar

def SAVIC_C_C(df_c_):
    
    df_c_uns_ = df_c_[df_c_['unstable']].drop(columns = ['unstable'])
    df_c_uns_.drop(columns = ['Pow_core'], inplace = True)
    
    df_c_uns_pre_SC_ = df_c_uns_.copy()
    df_c_uns_pre_SC_['uns_IC'] = (1. + 0.367 / ( df_c_uns_pre_SC_['beta_par_core'] - 0.011 )**0.364) < df_c_uns_pre_SC_['alph_c']
    df_c_uns_pre_SC_['uns_Mirror'] = (1. + 0.702 / ( df_c_uns_pre_SC_['beta_par_core'] + 0.009 )**0.674) < df_c_uns_pre_SC_['alph_c']
    df_c_uns_pre_SC_['uns_FM'] = (1. - 0.408 / ( df_c_uns_pre_SC_['beta_par_core'] - 0.410 )**0.529) > df_c_uns_pre_SC_['alph_c']
    df_c_uns_pre_SC_['uns_OFH'] = (1. - 1.454 / ( df_c_uns_pre_SC_['beta_par_core'] + 0.178 )**1.023) > df_c_uns_pre_SC_['alph_c']
    df_c_uns_pre_SC_['uns_core'] = df_c_uns_pre_SC_['uns_OFH'] | df_c_uns_pre_SC_['uns_FM'] | df_c_uns_pre_SC_['uns_Mirror'] | df_c_uns_pre_SC_['uns_IC']
    df_c_uns_pre_SC_.drop(columns = ['uns_Mirror'], inplace = True)
    
    df_c_uns_pre_SC_[['beta_par_core', 'alph_c']] = np.log10(df_c_uns_pre_SC_[['beta_par_core', 'alph_c']])
    df_c_uns_pre_SC_.rename(columns={"beta_par_core": "log_beta_par_core", "alph_c": "log_alph_c"}, inplace = True)
    
    df_c_uns_post_SC_ = df_c_uns_pre_SC_.copy()
    df_c_uns_post_SC_['cluster'] = gmm_c.predict(df_c_uns_pre_SC_[['log_beta_par_core', 'log_alph_c', 'kB_angle', \
                                                                   'uns_IC', 'uns_FM', 'uns_OFH', 'uns_core']].values)
    
    df_c_uns_post_SC_[['log_beta_par_core', 'log_alph_c']] = \
    pow(10., df_c_uns_post_SC_[['log_beta_par_core', 'log_alph_c']])
    df_c_uns_post_SC_.rename(columns={"log_beta_par_core": "beta_par_core", "log_alph_c": "alph_c"}, inplace = True)
    
    df_c_uns_post_SC_['ins_type'] = np.nan
    ins_types = ['Ion Cyclotron', 'Parallel Firehose', 'Mirror', 'Oblique Firehose']
    for cluster, ins_type in zip(np.arange(4), ins_types):
        df_c_uns_post_SC_['ins_type'][df_c_uns_post_SC_['cluster'] == cluster] = ins_type
    
    df_c_post_SC_ = df_c_.copy()
    df_c_post_SC_['ins_type'] = np.nan
    df_c_post_SC_.loc[df_c_uns_post_SC_.index, ['ins_type']] = df_c_uns_post_SC_['ins_type']
    
    return df_c_post_SC_