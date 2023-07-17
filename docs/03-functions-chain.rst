.. role:: math(raw)
    :format: latex html

#######
Chain Functions
#######

SAVIC.py
------------

An overarching function that accepts the input sile of any allowed structure (or merged file with different combinatio of structures) and processed through SAVIC-P,Q,C in their respective C, C B, C :math:`&#945;` , and C B :math:`&#945;` subsets. 

*functions: SAVIC.SAVIC*

called as:  *SAVIC.SAVIC* 

input:      input data frame

output:     list of 4 input data frames (some of which

**All the following input structures, or their a combinations (merged data frames) are accepted.**

input structure:   'beta_par_core', 'alph_c'

input structure:   'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b'

input structure:   'beta_par_core', 'alph_c', 'tau_a', 'alph_a', 'D_a', 'vv_a'

input structure:   'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'tau_a', 'alph_a', 'D_a', 'vv_a'

output structure:  'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'tau_a', 'alph_a', 'D_a', 'vv_a', 'unstable', 'group', 'Pow_core', 'Pow_beam', 'Pow_alpha', 'kB_angle', 'ins_type'


SAVIC_Core.py
------------

*functions: SAVIC.SAVIC*

called as:  *SAVIC_Core.SAVIC_Core* 

called as:  *SAVIC* 
