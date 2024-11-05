Welcome to NRGlab's documentation for NRGSuite-QT PyMOL plugin!
===================================

NRGSuite-QT is a PyMOL plug-in for molecular docking and virtual screening using NRGdock, GetCleft, FlexAID and Surfaces. This plug-in was created to facilitate the use the tools developed in Najmanovich's Reseach Group and was inspired in the NRG suite PyMOL plug-in (ref) for FlexAID.

The plug-in counts with a variaty of functionalities: Binding site defition, docking similaiton with FlexAID and NRGdock, high-throughput screening with NRGdock using the Chemical Component Dictionary (CCD) and the dataset of all approved drugs of DrugBank and ligand interaction visualization using surfaces.

Check out the :doc:`installation/installation_index` section for further information, including
how to install the project.


.. note::

   This project is under active development. Please contact rafael.najmanovich@umontreal.ca if you encounter any issues.

Contents
--------

.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: Getting Started

    installation/installation_index
    Removing NRGSuite <installation/Uninstalling>

.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: Case Studies

    Eph4 drug repurposing (Protein-Ligand) </case_studies/eph4>
    Spike Variant (Protein-Protein) </case_studies/spike>

.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: Software Description

    /software_description/GetCleft
    /software_description/NRGDock
    /software_description/FlexAID
    /software_description/Surfaces
    /software_description/NRGTEN
    /software_description/IsoMIF
    Single Mutations </case_studies/Single_Mutations>