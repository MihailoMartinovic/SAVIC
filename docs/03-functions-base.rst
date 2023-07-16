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

output structure:  'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'unstable', 'Pow_core', 'Pow_beam', 'kB_angle'

**Note: 'group' variable shows the result of the internal classifier:**

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

output structure:  'beta_par_core', 'alph_c', 'tau_a', 'alph_a', 'D_a', 'vv_a', 'unstable', 'group', 'Pow_core', 'Pow_alpha', 'kB_angle'

**Note: 'group' variable shows the result of the internal classifier:**

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

input structure:   'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'tau_a', 'alph_a', 'D_a', 'vv_a', 'unstable'

output:            data frame 

output structure:  'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'tau_a', 'alph_a', 'D_a', 'vv_a', 'unstable', 'group', 'Pow_core', 'Pow_beam', 'Pow_alpha', 'kB_angle'

**Note: 'group' variable shows the result of the internal classifier:**

0 - C+B+𝛼+

1 - C+B+𝛼-

2 - C+B-𝛼+

3 - C+B-𝛼-

4 - C-B+𝛼+

5 - C-B+𝛼-k\ :sub:`⊥`\

6 - C-B+𝛼-k\ :sub:`∥`\

7 - C-B-𝛼+


SAVIC_C_C
------------

Quantifies the emitted power and propagation direction (:math:`k,B` angle) for unstable VDF with only core (C) component. 

called as:         *SAVIC_C_C.SAVIC_C_C*

called by:         *SAVIC_Core*

input:             data frame 

input structure:   'beta_par_core', 'alph_c', 'unstable', 'Pow_core', 'kB_angle'

output:            data frame 

output structure:  'beta_par_core', 'alph_c', 'unstable', 'Pow_core', 'kB_angle', 'ins_type'


**Note: 'ins_type' variable has possible values of (explanations in Section 3.3 of the** `ApJ article <https://iopscience.iop.org/article/10.3847/1538-4357/acdb79>`_):

'Ion Cyclotron'

'Parallel Firehose'

'Mirror'

'Oblique Firehose'


SAVIC_C_CB
------------

Quantifies the emitted power and propagation direction (:math:`k,B` angle) for unstable VDF with core and beam (CB) components. 

called as:         *SAVIC_C_CB.SAVIC_C_CB*

called by:         *SAVIC_CoreBeam*

input:             data frame 

input structure:   'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'unstable', 'Pow_core', 'Pow_beam', 'kB_angle'

output:            data frame 

output structure:  'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'unstable', 'Pow_core', 'Pow_beam', 'kB_angle', 'ins_type'

**Note: 'group' variable shows the result of the internal classifier:**

0 - C+B+k\ :sub:`⊥`\
 
1 - C+B+k\ :sub:`∥`\
 
2 - C+B-k\ :sub:`⊥`\
 
3 - C+B-k\ :sub:`∥`\
 
4 - C-B+k\ :sub:`⊥`\

5 - C-B+k\ :sub:`∥`\


**Note: 'ins_type' variable has possible values of (explanations in Section 3.3 of the** `ApJ article <https://iopscience.iop.org/article/10.3847/1538-4357/acdb79>`_):

'IC (C)' - core induced parallel mode

'IC (B), unstable core' - beam induced parallel mode with unstable core

'IC (B); T\ :sub:`⊥`\/T\ :sub:`∥`\ > 1' - beam induced parallel mode with perpendular beam anisotropy

'IC (B); T\ :sub:`⊥`\/T\ :sub:`∥`\ < 1' - beam induced parallel mode with parallel beam anisotropy 

'Parallel Firehose' 

'Oblique Firehose' 

'Oblique FM (B)' - beam drift induced oblique mode

'Oblique FM (B); resonant with Core' - beam drift induced oblique mode with core absorbing emitted power



SAVIC_C_CA
------------

Quantifies the emitted power and propagation direction (:math:`k,B` angle) for unstable VDF with core and alpha (CA) components. 

called as:         *SAVIC_C_CA.SAVIC_C_CA*

called by:         *SAVIC_CoreAlpha*

input:             data frame 

input structure:   'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'unstable', 'group', 'Pow_core', 'Pow_beam', 'kB_angle'

output:            data frame 

output structure:  'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'unstable', 'group', 'Pow_core', 'Pow_beam', 'kB_angle', 'ins_type'

**Note: 'group' variable shows the result of the internal classifier:**

0 - C+𝛼+k\ :sub:`⊥`\

1 - C+𝛼+k\ :sub:`∥`\

2 - C+𝛼-k\ :sub:`⊥`\

3 - C+𝛼-k\ :sub:`∥`\

4 - C-𝛼+k\ :sub:`⊥`\

5 - C-𝛼+k\ :sub:`∥`\


**Note: 'ins_type' variable has possible values of (explanations in Section 3.3 of the** `ApJ article <https://iopscience.iop.org/article/10.3847/1538-4357/acdb79>`_):

'IC (C)' - core induced parallel mode

'IC (A)' - alpha induced parallel mode 

'A anis; borderline PFH' - mix of two modes due to limited classification accuracy 

'Parallel Firehose' 

'Oblique Firehose'

'CGL Firehose; Mirror' - high beta fluid-like instability



SAVIC_C_CBA
------------

Quantifies the emitted power and propagation direction (:math:`k,B` angle) for unstable VDF with core, beam, and alpha (CBA) components. 

called as:         *SAVIC_C_CBA.SAVIC_C_CBA*

called by:         *SAVIC_CoreBeamAlpha*

input:             data frame 

input structure:   'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'tau_a', 'alph_a', 'D_a', 'vv_a', 'unstable', 'group', 'Pow_core', 'Pow_beam', 'Pow_alpha', 'kB_angle'

output:            data frame 

output structure:  'beta_par_core', 'alph_c', 'tau_b', 'alph_b', 'D_b', 'vv_b', 'tau_a', 'alph_a', 'D_a', 'vv_a', 'unstable', 'group', 'Pow_core', 'Pow_beam', 'Pow_alpha', 'kB_angle', 'ins_type'

**Note: 'group' variable shows the result of the internal classifier:**

0 - C+B+𝛼+

1 - C+B+𝛼-

2 - C+B-𝛼+

3 - C+B-𝛼-

4 - C-B+𝛼+

5 - C-B+𝛼-k\ :sub:`⊥`\

6 - C-B+𝛼-k\ :sub:`∥`\

7 - C-B-𝛼+


**Note: 'ins_type' variable has possible values of (explanations in Section 3.3 of the** `ApJ article <https://iopscience.iop.org/article/10.3847/1538-4357/acdb79>`_):

'IC (C)' - core induced parallel mode

'IC (C); A unstable' - core induced parallel mode with unstable alpha

'IC (B), C unstable' - beam induced parallel mode with unstable core

'IC (B); A unstable' - beam induced parallel mode with unstable alpha

'IC (B); high B anis' - beam induced parallel mode with parallel / perpendular beam anisotropy

'IC (B); borderline PFH' - mix of two modes due to limited classification accuracy 

'IC (A)' - alpha induced parallel mode 

'IC (A); C absorbing' - alpha induced parallel mode with core absorbing emitted power

'Oblique Firehose'

'Parallel Firehose'

'FM (B), oblique' - beam drift induced oblique mode

'FM (B), oblique; mirror' - mix of two modes due to limited classification accuracy 


