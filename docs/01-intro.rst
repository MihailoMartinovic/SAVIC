.. role:: raw-math(raw)
    :format: latex html

.. role:: raw-latex(raw)
    :format: latex

#######
Background & Motivation
#######


The understanding of the solar wind plasma kinetics is based on examining the Velocity Distribution Function (VDF) of particles. :raw-latex:`$\pi r^2$`
If the state of VDF is sufficiently different from Local Thermodynamic Equilibrium (LTE), then the particle energy can be emitted through fields---waves are excited and particles lose energy, thereby getting ``pushed'' toward LTE. 
Here, we label the energy that is contained in particles that can be emitted through unstable wave modes ``free energy''. 
VDF characteristics, such as temperature anisotropy, particle drifts, or excess pressure in a given direction can act as sources of free energy. 

Traditionally, prediction of unstable modes is performed by dispersion solvers, who aim to map the dispersion relation of the VDF dispersion relation---

:raw-math:`$$ \underline{\mathbf{D}} \big( \omega, \mathbf{k} \big) $$`

where 

:raw-math:`$$ \omega=\omega_{\textrm{r}} + i \gamma $$`

is complex frequency and $\mathbf{k}$ is wavevector---over the *omega* and **k** phase space. 

If at any point in this space we find $\gamma > 0$, the mode is unstable. 
The calculations of traditional solvers can be done up to an arbitrary level of precision, but generally require a large volume of CPU hours, making them less convenient for analysis of larger data sets. 
Also, such codes are not user friendly, and require a notable time investment before a user becomes familiar. 
A practical consequence of these facts is that usage of the dispersion solvers---even though they are mostly publicly available---is limited almost exclusively to authors of these codes and their respective research groups. 


* use Machine Learning (ML) algorithms to decrease the requirements for the computational power required by traditional solvers by several orders of magnitude, providing the instability properties for a given VDF practically instantaneously
* provide the user friendly environment that would make access to plasma stability analysis tools easy for the entire community
* make additional step in the analysis of the numerical results provided by dispersion solvers by classifying the type of the predicted unstable mode

:raw-math:`$$ \frac{s}{\sqrt{N}} $$`
