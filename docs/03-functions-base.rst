.. role:: math(raw)
    :format: latex html

#######
Base Functions
#######


SAVIC_Input_Sort
------------

Internal Function that separates C, C B, C :math:`&#945;` , and C B :math:`&#945;` subsets in the input file. 

*functions: SAVIC_Input_Sort.SAVIC_Input_Sort*

called as:  *SAVIC_Input_Sort.SAVIC_Input_Sort* 

input:      input data frame

output:     list of 4 input data frames (some of which might be empty), of adequate formats to input into SAVIC_P_C, SAVIC_P_CB, SAVIC_P_CA, and SAVIC_P_CBA, respectively. 


SAVIC_P_C
------------

Predicts stability of a VDF with only core (C) component. 

called as:         *SAVIC_P_C.SAVIC_P_C*

called by:         *SAVIC_Core*

input:             data frame 

input structure:   'beta_par_core', 'alph_c'

output:            data frame 

output structure:  'beta_par_core', 'alph_c', 'unstable'


SAVIC_P_CB
------------

Predicts stability of a VDF with core and beam (CB) components. 

called as:         *SAVIC_P_CB.SAVIC_P_CB*

called by:         *SAVIC_CoreBeam*

input:             data frame 

input structure:   'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b'

output:            data frame 

output structure:  'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'unstable'


SAVIC_P_CA
------------

Predicts stability of a VDF with core and alpha (CA) components. 

called as:         *SAVIC_P_CA.SAVIC_P_CA*

called by:         *SAVIC_CoreAlpha*

input:             data frame 

input structure:   'beta_par_core', 'alph_c', 'tau_a', 'alph_a', 'D_a', 'vv_a'

output:            data frame 

output structure:  'beta_par_core', 'alph_c', 'tau_a', 'alph_a', 'D_a', 'vv_a', 'unstable' 


SAVIC_P_CBA
------------

Predicts stability of a VDF with core, beam, and alpha (CBA) components. 

called as:         *SAVIC_P_CBA.SAVIC_P_CBA*

called by:         *SAVIC_CoreBeamAlpha*

input:             data frame 

input structure:   'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'tau_a', 'alph_a', 'D_a', 'vv_a'

output:            data frame 

output structure:  'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'tau_a', 'alph_a', 'D_a', 'vv_a', 'unstable'


SAVIC_Q_C
------------

Quantifies the emitted power and propagation direction (:math:`k,B` angle) for unstable VDF with only core (C) component. 

called as:         *SAVIC_Q_C.SAVIC_Q_C*

called by:         *SAVIC_Core*

input:             data frame 

input structure:   'beta_par_core', 'alph_c', 'unstable'

output:            data frame 

output structure:  'beta_par_core', 'alph_c', 'unstable', 'Pow_core', 'kB_angle'


SAVIC_Q_CB
------------

Quantifies the emitted power and propagation direction (:math:`k,B` angle) for unstable VDF with core and beam (CB) components. 

called as:         *SAVIC_Q_CB.SAVIC_Q_CB*

called by:         *SAVIC_CoreBeam*

input:             data frame 

input structure:   'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b'

output:            data frame 

output structure:  'beta_par_core', 'alph_c', 'unstable', 'Pow_core', 'kB_angle'

Note: 'group' variable shows the result of the internal classifier: 

0 - C+B+k\ :sub:`⊥`\
 
1 - C+B+k\ :sub:`∥`\
 
2 - C+B-k\ :sub:`⊥`\
 
3 - C+B-k\ :sub:`∥`\
 
4 - C-B+k\ :sub:`⊥`\

5 - C-B+k\ :sub:`∥`\

SAVIC_Q_CA
------------

Quantifies the emitted power and propagation direction (:math:`k,B` angle) for unstable VDF with core and alpha (CA) components. 

called as:         *SAVIC_Q_CA.SAVIC_Q_CA*

called by:         *SAVIC_CoreAlpha*

input:             data frame 

input structure:   'beta_par_core', 'alph_c', 'tau_a', 'alph_a', 'D_a', 'vv_a'

output:            data frame 

output structure:  'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'unstable', 'group', 'Pow_core', 'Pow_beam', 'kB_angle'

Note: 'group' variable shows the result of the internal classifier: 

0 - C+𝛼+k\ :sub:`⊥`\

1 - C+𝛼+k\ :sub:`∥`\

2 - C+𝛼-k\ :sub:`⊥`\

3 - C+𝛼-k\ :sub:`∥`\

4 - C-𝛼+k\ :sub:`⊥`\

5 - C-𝛼+k\ :sub:`∥`\


SAVIC_Q_CBA
------------

Quantifies the emitted power and propagation direction (:math:`k,B` angle) for unstable VDF with core, beam, and alpha (CBA) components. 

called as:         *SAVIC_Q_CBA.SAVIC_Q_CBA*

called by:         *SAVIC_CoreBeamAlpha*

input:             data frame 

input structure:   'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'tau_a', 'alph_a', 'D_a', 'vv_a'

output:            data frame 

output structure:  'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'tau_a', 'alph_a', 'D_a', 'vv_a', 'unstable'
