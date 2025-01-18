.. _IsoMIF:

IsoMIF
======

**IsoMIF** (https://pmc.ncbi.nlm.nih.gov/articles/PMC4743630/) identifies molecular interaction field similarities between protein binding sites defined with GetCleft (see :doc:`GetCleft`). It detects both geometric and chemical equivalences across cavities using six chemical probes. This tool is used to predict protein function, detect potential off-targets, suggest bioisosteric replacements, and assist in drug repurposing efforts.

.. image:: /_static/images/IsoMIF/IsoMIF_settings.png
       :alt: An example image
       :width: 65%
       :align: center

To use IsoMIF, a binding site must be defined (see :doc:`GetCleft`) in the Pymol interface.

Running IsoMIF requires two targets and two binding sites. If only one target and one binding site are provided, only the molecular interaction field is generated.

It is not necessary for ligands to be present in both cavities, but it is strongly recommended that the user includes them when possible in order to obtain a p-value and a z-score relative to a distribution of similarities from a dataset of targets (`DUD-E <https://dude.docking.org/targets>`_).

Press "Refresh" and select the first "Object" in the "Object 1" section. Select the binding site in the "Cleft" list. Select the selection containing the ligand in the "Ligand" list.

Press "Refresh" and select the first "Object" in the "Object 2" section. Select the binding site in the "Cleft" list. Select the selection containing the ligand in the "Ligand" list.

Press "Run IsoMIF" to start the calculations.

Results
-------

The visual output of each Molecular Interaction Field (MIF) and the visual output of IsoMIF matching both binding sites are shown in the Pymol interface in a group called "IsoMIF". Each sphere around the binding site indicates one of the six probes (hydrophobic, aromatic, H-bond donor/acceptor, and positive/negative charge). In the IsoMIF visual output, the larger the sphere, the higher the similarity at that point.

The Tanimoto coefficient of the IsoMIF against all DUD-E targets of different families is plotted in an HTML file. The z-scores and p-values are only significant when the user has indicated a ligand selection for both targets before running IsoMIF.

.. image:: /_static/images/IsoMIF/IsoMIF_results.png
       :alt: An example image
       :width: 100%
       :align: center


