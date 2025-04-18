The NRGSuite-Qt PyMOL plugin
============================

.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: Getting Started

    /installation/prerequisites
    Installing NRGSuite </installation/nrgsuite>
    Removing NRGSuite </installation/Uninstalling>

.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: Case Studies

    Epha4 Drug Repurposing (Protein-Ligand) </case_studies/epha4>
    Spike Variant (Protein-Protein) </case_studies/spike>

.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: Software Description

    /software_description/GetCleft
    /software_description/NRGRank
    /software_description/FlexAID
    /software_description/Surfaces
    /software_description/NRGTEN
    /software_description/IsoMIF
    Single Mutations </software_description/Single_Mutations>
    /software_description/Settings

NRGSuite-Qt is a PyMOL plug-in for molecular docking and virtual screening using NRGRank, GetCleft, FlexAID and Surfaces. This plug-in was created to facilitate the use the tools developed in Najmanovich's Reseach Group and was inspired in the NRG suite PyMOL plug-in (ref) for FlexAID.

The plug-in counts with a variaty of functionalities: Binding site defition, docking similaiton with FlexAID and NRGRank, high-throughput screening with NRGRank using the Chemical Component Dictionary (CCD) and the dataset of all approved drugs of DrugBank and ligand interaction visualization using surfaces.

.. note::

   This project is under active development. Please contact rafael.najmanovich@umontreal.ca if you encounter any issues.

.. warning::

    The functionalities related to MODELLER currently only work on the **open-source** version of PyMOL. If you would like to use these, please follow the **Install from scratch** instructions below.

Install from scratch:
---------------------

:doc:`/installation/prerequisites`
    This will guide you on how to install PyMOL and NRGSuite

Only install the plugin:
------------------------

:doc:`/installation/nrgsuite`
    Instructions to install NRGSuite if you already have PyMOL

Looking for examples or inspiration?
------------------------------------

:doc:`/case_studies/epha4`
    Useful if studying protein-ligand interactions

:doc:`/case_studies/spike`
    Useful if studying protein-protein interactions
