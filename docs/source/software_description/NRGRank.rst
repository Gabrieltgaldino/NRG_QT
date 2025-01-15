.. _NRGRank:

NRGRank
=====
**NRGRank** is a software developed for ultra-massive-high-trough-put screening using a scoring function derivated from FlexAID.

.. note::
    To use NRGRank the target object and target cleft (see how to generate clefts in :doc:`GetCleft`) should be loaded in PyMOL interface.

    .. image:: /_static/images/NRGRank/recep-cleft-nrgdock.png
       :alt: An example image
       :width: 65%
       :align: center


General settings
------------

Click on the 'NRGRank' button on the left menu of the plugin.

In the 'Settings' tab:

Within the 'General settings' section select the number of 'Ligand rotations per axis' (default and recommend: 9).

Select the number of top n poses to be shown in pymol interface at the end of the simulation in the box: "Save poses for top n results:".

To start screening from a certain ligand in the ligand set instead of screening the whole data set, chose the starting ligand in the box: "Start screening at ligand:"

Select the desired CPU usage for the screening at "CPU usage target" list.

Ligands sets
------------

By default, three common data sets of are provided: 'DrugBank FDA' containing of all FDA approved drugs available in Drugbank(https://go.drugbank.com/ ), 'PDB small ligands' containing all small molecules available in the Chemical Component Dictionary (https://www.wwpdb.org/data/ccd ) and "Tetrapeptides" that include all 16000 tetrapeptides provided by Prasasty et al. ( https://pmc.ncbi.nlm.nih.gov/articles/PMC6806445/ ).

The list of all other ligands to be tested should be provided in a file in smiles format ('.smi') and added in the session 'Ligand set manager'.
This file contain one ligand per line in the format:

"SMILES ID"

Add the smiles file path to the box 'Smile file' or click in browse to load it via file manager. Press Add to this set to your list of ligand sets.

    .. image:: /_static/images/NRGRank/NRGRank_menu.png
           :alt: An example image
           :width: 65%
           :align: center


This set can be removed when no longer needed in the tab 'Delete' in the same session, by pressing the button refresh and selecting the Ligand set to be deleted in the 'Available ligand sets' box.

.. image:: /_static/images/NRGRank/delete_sets.png
       :alt: An example image
       :width: 65%
       :align: center

Running NRGRank
------------
To run 'NRGRank' click on the tab 'Run' in 'NRGRank' interface.
Press the button 'Refresh' in the 'Target' list and select the target object previously loaded in PyMOL.
Press the button 'Refresh' in the 'Ligand set' list and select the ligand set to be tested (previously added at :ref:`Ligand sets`).
Press the button 'Refresh' in the 'Binding site' list and select the cleft object previously loaded in PyMOL (see: :doc:`GetCleft`).
To start the simulation press the button 'Start'.
The progress of the simulation can be monitored using the 'Progress' bar and the 'Ligand' counter showing 'ligands tested / total ligands in the ligand set'.

.. image:: /_static/images/NRGRank/run_tab_nrgdock.png
       :alt: An example image
       :width: 65%
       :align: center