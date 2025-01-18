.. _IsoMIF:

IsoMIF
======

IsoMIF (https://pmc.ncbi.nlm.nih.gov/articles/PMC4743630/ ) identifies molecular interaction field similarities between protein binding sites defined with GetCleft (see :doc:`GetCleft`). It detects both geometric and chemical equivalences across cavities using six chemical probes. This tool can be used to predict protein function, detect potential off-targets, suggest bioisosteric replacements, and in drug repurposing efforts.

.. image:: /_static/images/IsoMIF/IsoMIF_settings.png
       :alt: An example image
       :width: 65%
       :align: center

To use IsoMIF a binding site must be defined (see :doc:`GetCleft`) in pymol interface.

For running IsoMIF it is necessary two targets and two biding sites. When only one target and one binding-site is giving only the molecular interaction field is generated.

It is not necessary the presence of ligands in both cavities, but strongly recommend the user to do so when possible in order to obtain a p-value and a z-score in relation to a distribution of similarities of data-set of targets (DUD-E: https://dude.docking.org/targets ).

Press "Refresh" and select the first "Object" in the "Object 1" area. Select the binding site in the "Cleft" list. Select the selection containing the ligand in the "Ligand" list.

Press "Refresh" and select the first "Object" in the "Object 2" area. Select the binding site in the "Cleft" list. Select the selection containing the ligand in the "Ligand" list.

Press "Run IsoMIF" to start the calculations.


Results
--------------








