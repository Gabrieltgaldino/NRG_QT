.. _Surfaces:

Surfaces
======

Surfaces (https://academic.oup.com/bioinformatics/article/39/10/btad608/7288175 ) comprises a collection of Python scripts that provide a rapid means to assess protein interactions by analyzing the atomic surface areas in contact and the types of atoms involved in the interaction.
Surfaces is fully implemented in NRGSuite-QT and can be applied to protein-protein and ligand-protein interactions calculations.

Surfaces to protein-ligand interactions
-------

.. note::
    In order to run surfaces to calculate ligand-protein interactions, the ligand and the target must be loaded in pymol in a single object. A selection with containing the ligand must be created.
    .. image:: _static/images/Surfaces/surfaces_note.png
       :alt: An example image
       :width: 65%
       :align: center

Select surfaces in the main menu on the left corner of the plug-in. Press 'Refresh' and select the FlexAID result in 'Result to run surfaces on' list. Press the button 'Run Surfaces'.

.. image:: _static/images/Surfaces/surfaces_settings.png
       :alt: An example image
       :width: 65%
       :align: center

The visual of surfaces will be shown in the pymol window.

.. image:: _static/images/surf-plot.png
       :alt: An example image
       :width: 65%
       :align: center





