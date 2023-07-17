.. role:: math(raw)
    :format: latex html

#######
Chain Functions
#######

SAVIC.py
------------

An overarching function that accepts the input sile of any allowed structure (or merged file with different combinatio of structures) and processed through SAVIC-P,Q,C in their respective C, C B, C :math:`&#945;` , and C B :math:`&#945;` subsets. 

*functions: SAVIC.SAVIC*

input:    input data frame
output:   output data frame

input structure:   'beta_par_core', 'alph_c'

output structure:  'beta_par_core', 'alph_c', 'unstable', 'Pow_core', 'kB_angle', 'ins_type'

input structure:   'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b'

output structure:  'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'unstable', 'Pow_core', 'Pow_beam', 'kB_angle', 'ins_type'

input structure:   'beta_par_core', 'alph_c', 'tau_a', 'alph_a', 'D_a', 'vv_a'

output structure:  'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'unstable', 'group', 'Pow_core', 'Pow_beam', 'kB_angle', 'ins_type'

input structure:   'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'tau_a', 'alph_a', 'D_a', 'vv_a'

output structure:  'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'tau_a', 'alph_a', 'D_a', 'vv_a', 'unstable', 'group', 'Pow_core', 'Pow_beam', 'Pow_alpha', 'kB_angle', 'ins_type'

