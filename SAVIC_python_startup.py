import sys
import os
import time
import json
import h5py
import numpy as np
import scipy.special as ss
import scipy.integrate as si
import scipy.signal as ssi
import warnings
warnings.filterwarnings("ignore")
import pylab
pylab.rc('font', family='serif', size=13)
import pandas as pd
from scipy import io
from itertools import product
import scipy.stats as stats
import scipy.optimize as so

# constants -------------------------------------------------------------------
k_b = 1.38e-23
m_p = 1.67e-27
m_e = 9.1e-31
e_c = 1.6e-19
mu_0 = 4 * np.pi * 1e-7
au_km = 149597870.7
eps_0 = 8.85e-12
c_const = 299792458.

def rename(col, name):
    if col.startswith(name):
        return name
    else:
        return col
		
