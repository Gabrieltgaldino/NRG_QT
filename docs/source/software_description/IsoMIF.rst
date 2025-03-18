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


The similarity between two cavities can be measured by identifying the largest set of vertices that share corresponding interaction types and are in geometrically equivalent positions. To achieve this, IsoMIF employs the **Bron–Kerbosch (BK) algorithm** to find the **maximum common subgraph isomorphisms**.

Tanimoto Score Calculation
++++++++++++++++++++++++++++

The visual output of each Molecular Interaction Field (MIF) and the visual output of IsoMIF matching both binding sites are shown in the Pymol interface in a group called "IsoMIF". Each sphere around the binding site indicates one of the six probes (cyan (hydrophobic), orange (aromatic), blue (donor), red (acceptor), green (positive charge), and magenta (negative charge)). In the IsoMIF visual output, the larger the sphere, the higher the similarity at that point.

The similarity between two cavities can be measured by finding the largest ensemble of vertices between two cavities that have corresponding interaction types and that are in geometrically equivalent positions. To do this IsoMIF uses the `Bron and Kerbosch (BK) algorithm <https://dl.acm.org/doi/10.1145/362342.362367>`_ to find the maximum common subgraph isomorphisms. In the visual output of IsoMIF, the largest is the sphere in the cavity the more both cavities have common probes in that position, when no sphere is shown that position has no probes in common.


The **Tanimoto score** quantifies this similarity by comparing the number of common probes between the two cavities to the total number of distinct probes. It is calculated as:

.. math::

   MSS = \frac{N_c}{N_a + N_b - N_c}

where:

- :math:`N_c` is the number of common probes in geometrically equivalent positions,
- :math:`N_a` and :math:`N_b` are the total number of probes in each cavity with **significant interaction energies**.

A **significant interaction energy** refers to an energy value below a predefined threshold, indicating a strong and relevant molecular interaction at that position. Only probes with such meaningful energetic contributions are considered in the similarity calculation.

A higher **MSS** value indicates greater similarity between the two cavities.

The Tanimoto coefficient of the IsoMIF against all DUD-E targets of different families is plotted in an HTML file. The z-scores and p-values are only significant when the user has indicated a ligand selection for both targets before running IsoMIF.

.. image:: /_static/images/IsoMIF/IsoMIF_results.png
       :alt: An example image
       :width: 100%
       :align: center


