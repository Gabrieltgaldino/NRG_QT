.. _Surfaces:

Surfaces
======

Surfaces (https://academic.oup.com/bioinformatics/article/39/10/btad608/7288175 ) comprises a collection of Python scripts that provide a rapid means to assess protein interactions by analyzing the atomic surface areas in contact and the types of atoms involved in the interaction.
Surfaces is fully implemented in NRGSuite-QT and can be applied to protein-protein and ligand-protein interactions calculations.

.. note::
    In order to run surfaces for protein-protein interactions all chains must be loaded in the same object.

    In order to run surfaces to calculate ligand-protein interactions, the ligand and the target must be loaded in pymol in a single object. A selection with containing the ligand must be created.

    .. image:: /_static/images/Surfaces/surfaces_note.png
       :alt: An example image
       :width: 50%
       :align: center


Press 'Refresh' in the "Surfaces selection" area.


.. image:: /_static/images/Surfaces/surfaces_settings.png
       :alt: An example image
       :width: 65%
       :align: center

Select the object containing the object of interest in the "Object" list.

If running for *** Protein-Ligand *** interactions: Select the selection containing the ligand in the "Ligand (optional)" list. All other fields should be marked as "None". By default if a ligand is specified the chain's information in the "Protein-Protein interactions" section is ignored.

If running for  *** Protein-Protein *** interactions: The "Ligand (optional)" list must be marked as "None". In the "Protein-Protein Interactions" section the user must specify one or a group of chains in the "Chain 1:" and "Chain 2:", those chains must be one letter or all letters representing all chains in the group (i. e. "A" for "chain A" or "ABC" for a group of three chains A, B and C).

.. note::

    If the user specify "ABC" in the "Chain 1:" area and "DE" in the "Chain2" area, that will provide a calculation of the interactions between residues of the first group of chains (A, B and C in the example) and residues of the second group of chains (D and E in the example).

    For more information refer to the surfaces manual: https://surfaces-tutorial.readthedocs.io/en/latest/Protein-protein.html

Press "Run Surfaces"

Results
-----------



The results per interaction residue (target)/atom (ligand) will be shown in the "Results" tab that will open automatically once the calculation is done.

The visual of surfaces will be shown in the pymol window.

To visualize specific interactions click on the residue name and a selection called "sele_surfaces", containing the residue will be crated and the residue will be shown in lines representation.

.. image:: /_static/images/Surfaces/surfaces_results_ligand.png
       :alt: An example image
       :width: 65%
       :align: center





