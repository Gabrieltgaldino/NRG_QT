.. _NRGTEN:

NRGTEN
=======

NRGTEN (https://academic.oup.com/bioinformatics/article/37/19/3369/6179106?login=false) is a python package for Normal Mode Analysis calculations using the ENCoM potential (
10.1371/journal.pcbi.1003569). NRGTEN can be applied for the calculation of Dynamical Signatures and Conformational ensembles of proteins and protein ligand complexes.

.. image:: /_static/images/NRGTEN/NRGTEN_settings.png
       :alt: An example image
       :width: 65%
       :align: center

An object containing all molecules to be considered for the dynamical signature calculations must be loaded in the pymol interface.

.. note::

    We recommend that the user use the pymol's "Remove solvent" function before using NRGTEN in order to avoid errors. All small molecules, residues and chains are going to be considered for the calculation s of dynamical signatures and conformational ensembles. WE RECOMMEND THE CALCULATIONS USING NRGTEN TO BE DONE USING ONLY ONE CHAIN PER OBJECT AND NO MORE THAN ONE SMALL MOLECULE, since our methods were validated for those cases only. For more information about NRGTEN settings refer to its manual (https://nrgten.readthedocs.io/en/latest/) .

At the "Load object" area press "Refresh" and select the object of interest at the "Object" list.

If the user wants to define a "Ligand" of interest in the object, they must define a selection containing the ligand of interest (this selection can contain more than one molecule and they all ar going to be considered as a single group).

.. note::
    When a second object is defined, the "Ligand" selection doesn't generate a differential in NRGTEN plot.

NRGTEN also allows the comparison between mutants and wild-type, as well as different ligands bound to the same target. For that a multi-state object containing all mutants (1 mutant per state) or all complexes (1 protein/ligand complex per state) must be created before running NRGTEN. Those multi-states objects can be created using the "Single Mutations" functionality (see :doc:`Single_Mutations`) or the "Multi-state object manager" functionality (see :doc:`Settings`). Load this object at the "Object" list at "Load object 2" area.

The NRGTEN functionality only allow the calculations of entropic signatures so a beta value must be defined at the "Dynamical Signature" area. We recommend the user to start their study by the default value and explore the betas as wanted. Press the "Run DynaSig" button to start the calculations.








