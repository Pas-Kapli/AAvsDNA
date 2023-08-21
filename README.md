Supplementary data for the manuscript:
Kapli P., Kotari I., Telford M., Goldman N., Yang Z. DNA Sequences Are as Useful as Protein Sequences for Inferring Deep Phylogenies.

Brief explanations of the files:

* The script "convert.py" takes as input a codon alignment and outputs the equivalent amino acid and the DNA alignment of the 1st and 2nd codon positions.

* In the HOMO folder, the "HOMO-control.txt" is the control file for simulating sequences under the homogeneous model with [indelible](http://abacus.gene.ucl.ac.uk/software/indelible/). All guide trees and model parameters (M0 and M3) are provided in the file.

* In the SH1 folder, the "SH1-control.txt" is the control file for simulating sequences under the site-heterogeneous (SH1) model. SH1 assumes site-heterogeneous codon frequencies generated from observed frequencies in coding genes from mammal species. All guide trees and model parameters (M0 and M3) are provided in the file.

* The folder "SH2" contains two Python scripts: "generate_control_M0.py" and "generate_control_M3.py" that create control files for indelible with the SH2 model. In particular, it converts the amino acid frequencies from the mixture models C10-C60 into equivalent codon frequencies, i.e. the frequency of each codon is calculated by the frequency of the amino acid divided by the number of synonymous codons for the amino acid and multiplied by the nucleotide frequency for the nucleotide at the 3rd codon position. It then formats the indelible control file accordingly. All guide trees are available in each of the scripts.

Syntax for running the script:
./generate_control_M[0 or 3].py [AA mixture model: C10-C60] [frequency C] [frequency T] [frequency A] [ALIGNMENT LENGTH]

An example output of the generate_control_M0.py is provided in the folder.

* The "BSH" folder contains the equivalent scripts as in SH2 but for the branch-site model.

Syntax for running the script:
./generate_control_M[0 or 3].py [AA mixture model: C10-C60] [frequency C 1] [frequency T 1] [frequency A 1] [frequency C 2] [frequency T 2] [frequency A 2] [ALIGNMENT LENGTH]

The two sets of frequencies are assigned to different parts of the tree.

* The "metazoa" folder contains: 1) the DNA alignment for the 22 animal species used in the study, 2) two scripts: "generate_control_M3_BSH.py" and "generate_control_M3_SH2.py"  that generate indelible control files under the BSH and the SH2 models correspondingly and with guide trees matching the metazoa phylogenies A and C of Figure 3 in the manuscript, and, 3) the iqtree and phylobayes tree shown in figure 3 of the manuscript (for phylobayes the corresponding alignment subsets are also provided).

For further information regarding these files or the analyses presented in the manuscript, contact me at p.kapli@ucl.ac.uk or k.pashalia@gmail.com.
