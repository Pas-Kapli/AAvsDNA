Supplementary data for the manuscript: 
Kapli P., Kotari I., Telford M., Goldman N., Yang Z. DNA Sequences Are as Useful as Protein Sequences for Inferring Deep Phylogenies. 

Brief explanations of the files:

* The script "convert.py" takes as input a codon alignment and outputs the equivalent amino-acid and the 1st+2nd codon positions DNA alignment.

* In the HOMO folder the "HOMO-control.txt" is the control file for simulating sequences under the homogeneous model with [indelible](http://abacus.gene.ucl.ac.uk/software/indelible/). All guide trees and model parameters (M0&M3) are provided in the file.

* In the SH1 model the "SH1-control.txt" is the control file for simulating sequences under the site heterogeneous (SH1) model. SH1 assumes site-heterogeneous codon-frequencies generated from observed frequencies in coding genes from mammal species. All guide trees and model parameters (M0&M3) are provided in the file.

* The folder "SH2" contains two python scripts: "generate_control_M0.py" and "generate_control_M3.py" that create control files for indelible with the SH2 model. In particular it converts the AA frequencies from the mixture models C10-C60 into the equivallent codon frequencies and formates the indelible control file accordingly. All guide trees are available in each of the scripts.

Syntax for running the script:
./generate_control_M[0 or 3].py [AA mixture model: C10-C60] [frequency C] [frequency T] [frequency A] [ALIGNMENT LENGHT]

an example output of the generate_control_M0.py is provided in the folder.  

* The "BSH" folder contains the equivallent scripts as in SH2 but for the branch-site model. 

Syntax for running the script:
./generate_control_M[0 or 3].py [AA mixture model: C10-C60] [frequency C 1] [frequency T 1] [frequency A 1] [frequency C 2] [frequency T 2] [frequency A 2] [ALIGNMENT LENGHT]

The two sets of frequencies are assigned to different parts of the tree.

* The "metazoa-based" folder contains two scripts the "generate_control_M3_BSH.py" and "generate_control_M3_SH2.py" that generate indelible control files under the BSH and the SH2 models correspondingly and with guide trees matching the metazoa phylogenies A & C of Figure 3 in the manuscript.


For further information regarding these files or the analyses presented in the manuscript contact me at p.kapli@ucl.ac.uk or k.pashalia@gmail.com
