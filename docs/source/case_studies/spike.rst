========================================
Spike Variant (Protein-Protein analysis)
========================================

.. _Spike variant (Protein-Protein analysis):

In this tutorial, we will reproduce a few results regarding the evolution of the SARS-CoV-2 Spike protein. We will employ tools available at NRGSuite_Qt to study its conformatioal dynamics, binding affiity to ACE2 and antibody recognition.

Preparing the protein
====================

We will firstly evaluate conformational dynamics. For that purpose, we will use 2 Spike structures, one in the 3-down conformation and one in the 1-up conformation.

Open PyMOL and run the command:

    .. code-block:: console

            fetch 6vxx
            fetch 6vyb
            remove hetatm


Creating mutations and evaluating dynamical effects
====================

The D614G substituion became common during the summer of 2020 and was the first widely selected Spike substitution during the COVID-19 pandemic. Let's evaluate its effects on the Spike dynamics.

    .. code-block:: console

            sele resi 614

Run Modeller
Run NRGTEN

We can see the pattern of increased flexibilty of the closed state and decreased flexibility of the open conformation, particularly around the open Receptor-Binding Domain. These results reproduce the observations from Teruel et al. (2021) for the D614G mutation favoring the open state occupancy, also confirmed by more costly computational methods and experimental observations (Mansbach et al. 2021, Gobeil et al. 2021).

Teruel et al. proceeds to look for the same pattern of effect on flexibility for over 17,000 mutants. Here, we will reproduce two of the main results, for positions 417 and 501.

