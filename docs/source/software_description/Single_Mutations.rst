.. _Single Mutations:

Single Mutations
================

The "Single Mutations" functionality (SMF) is used to create single mutants using Modeller, implemented using their template for the Mutate model (for more information, see: https://salilab.org/modeller/wiki/Mutate_model).

.. note::

    If Modeller is not properly installed, the "Single Mutations" button in the main menu will be grayed out. See :doc:`../installation/prerequisites` to learn how to properly install PyMOL and Modeller via Anaconda.

To use SMF, a selection containing the residue(s) to mutate must be previously defined in PyMOL. Press "Refresh" in the "Load" area and select the object containing the protein of interest in the "Object to Mutate" list. Choose the selection containing the residues to mutate in the "Selected Residue(s)" list. Select the residues to which to mutate in the "Single Mutations" area (pressing the "All" button will select/unselect all residues). Press "Mutate".

.. note::

    Even though more than one residue can be included in the "Selected Residue(s)" selection, it is important to note that **only single mutants** will be generated per run of the SMF. To perform multiple mutations on the same structure, it is necessary to rerun the single mutations functionality more than once.

.. image:: /_static/images/Single_Mutations/Single_mutations.png
    :alt: An example image
    :width: 100%
    :align: center

The result of SMF is a multi-state object containing all the mutants selected (one mutant per state) in a group called "Single Mutants" in the PyMOL interface.
