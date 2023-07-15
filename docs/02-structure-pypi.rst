.. role:: math(raw)
    :format: latex html

#######
File Structure
#######


SAVIC.py
------------

An overarching function that accepts the input sile of any allowed structure (or merged file with different combinatio of structures) and processed through SAVIC-P,Q,C in their respective C, C B, C :math:`&#945;` , and C B :math:`&#945;` subsets. 

*functions: SAVIC.SAVIC*

input:    input data frame
output:   output data frame


SAVIC_Input_Sort.py
------------

Internal Function that separates C, C B, C :math:`&#945;` , and C B :math:`&#945;` subsets in the input file. 

*functions: SAVIC_Input_Sort.SAVIC_Input_Sort*

called by : *SAVIC.SAVIC* 
input:      input data frame
output:     list of 4 input data frames (some of which might be empty)


