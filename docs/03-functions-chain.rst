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

output:     output data frame

**All the following input structures, or their a combinations (merged data frames) are accepted.**

input structure:   'beta_par_core', 'alph_c'

input structure:   'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b'

input structure:   'beta_par_core', 'alph_c', 'tau_a', 'alph_a', 'D_a', 'vv_a'

input structure:   'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'tau_a', 'alph_a', 'D_a', 'vv_a'

output structure:  'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'tau_a', 'alph_a', 'D_a', 'vv_a', 'unstable', 'group', 'Pow_core', 'Pow_beam', 'Pow_alpha', 'kB_angle', 'ins_type'


SAVIC_Core.py
------------

*functions: SAVIC_Core.SAVIC_Core*

called as:  *SAVIC_Core.SAVIC_Core* 

called by:  *SAVIC* 

input:      input data frame

output:     output data frame

calls:      'SAVIC_P_C.SAVIC_P_C', 'SAVIC_Q_C.SAVIC_Q_C', 'SAVIC_C_C.SAVIC_C_C'

input structure:   'beta_par_core', 'alph_c'

output structure:  'beta_par_core', 'alph_c', 'unstable', 'Pow_core', 'kB_angle', 'ins_type'

SAVIC_CoreBeam.py
------------

*functions: SAVIC_CoreBeam.SAVIC_CoreBeam*

called as:  *SAVIC_CoreBeam.SAVIC_CoreBeam* 

called by:  *SAVIC* 

input:      input data frame

output:     output data frame

calls:      'SAVIC_P_CB.SAVIC_P_CB', 'SAVIC_Q_CB.SAVIC_Q_CB', 'SAVIC_C_CB.SAVIC_C_CB'

input structure:   'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b'

output structure:  'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'unstable', 'Pow_core', 'Pow_beam', 'kB_angle', 'ins_type'


SAVIC_CoreAlpha.py
------------

*functions: SAVIC_CoreAlpha.SAVIC_CoreAlpha*

called as:  *SAVIC_CoreAlpha.SAVIC_CoreAlpha* 

called by:  *SAVIC* 

input:      input data frame

output:     output data frame

calls:      'SAVIC_P_CA.SAVIC_P_CA', 'SAVIC_Q_CA.SAVIC_Q_CA', 'SAVIC_C_CA.SAVIC_C_CA'

input structure:   'beta_par_core', 'alph_c', 'tau_a', 'alph_a', 'D_a', 'vv_a'

output structure:  'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'unstable', 'group', 'Pow_core', 'Pow_beam', 'kB_angle', 'ins_type'


SAVIC_CoreBeamAlpha.py
------------

*functions: SAVIC_CoreBeamAlpha.SAVIC_CoreBeamAlpha*

called as:  *SAVIC_CoreBeamAlpha.SAVIC_CoreBeamAlpha* 

called by:  *SAVIC* 

input:      input data frame

output:     output data frame

calls:      'SAVIC_P_CBA.SAVIC_P_CBA', 'SAVIC_Q_CBA.SAVIC_Q_CBA', 'SAVIC_C_CBA.SAVIC_C_CBA'

input structure:   'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'tau_a', 'alph_a', 'D_a', 'vv_a'

output structure:  'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'tau_a', 'alph_a', 'D_a', 'vv_a', 'unstable', 'group', 'Pow_core', 'Pow_beam', 'Pow_alpha', 'kB_angle', 'ins_type'

