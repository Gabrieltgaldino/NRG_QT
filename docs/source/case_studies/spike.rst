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

We will also evaluate the interaction with the receptor ACE2:

    .. code-block:: console
            
            fetch 6m17
            remove 6m17 and (chain A or chain C or chain D or chain F)
            remove hetatm

As well as immune recognition, here represented by interactions with antibody C105:

    .. code-block:: console

            fetch 6xcn
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

First, we need to create the mutations:

    .. code-block:: console

        sele resi 417 and 6vxx

Run Modeller

    .. code-block:: console

        sele resi 417 and 6vyb

Run Modeller

Now that the mutations are done for both conformational states, we can evaluate their effects on dynamics.

Run NRGTEN
Run NRGTEN

We see that K417N has similar effects to D614G, making the closed conformation more flexible around the Receptor-Binding Domain, and the open Receptor-Binding Domain becomes more rigid.

We can make the same evaluation for mutation N501Y, starting by creating the mutations:

    .. code-block:: console
        
        sele resi 501 and 6vxx

Run Modeller

    .. code-block:: console
        
        sele resi 501 and 6vyb

Run Modeller

Now that the mutations are done for both conformational states, we can evaluate their effects on dynamics.

Run NRGTEN
Run NRGTEN

The mutation N501Y also makes the closed conformation more flexible and the open Receptor-Binding Domain more rigid. This reproduces the predictive results from Teruel et al. (2021). The dynamical effects of these mutations have also been shown experimentally (Gobeil et al. 2021).

Creating mutations and evaluating ACE2 interactions
====================

The mutation N501Y is known for increasing interaction with the receptor ACE2 (starr2020deep, sergeeva2023free, tian2021n501y, laffeber2021experimental, geng2022structural, moulana2022compensatory). Let's see if we can reproduce these results!

We first model the mutation in the complex structure with ACE2:

    .. code-block:: console
    
        sele 6m17 and chain E and resi 501

Run Modeller

Chain E represents the Receptor-Binding Domain of the Spike protein, and chain C is the ACE2 protein. We can now evaluate their per-residue interactions.

Run Surfaces

If we look at the difference in total CF, we see an increase in binding affinity of 0.31 kcal/mol due to the modeled mutation.

Creating mutations and evaluating immune recognition
====================

The K417N substition is in a very important epitope of antibody recognition. Deep mutational scanning (DMS) results show that it affects the recognition of many antibodies, among which the C105 antibody (greaney2022antibody, cao2023imprinted). We can try to reproduce these results evaluating the complex structure.

We start by modeling the mutation:

    .. code-block:: console
    
        sele 6XCN and chain C and resi 417

Run Modeller

And we can evaluate the interactions of the wild-type and mutant Spike structures with C105 using Surfaces - the chain representing Spike is chain C and the antibody is built by the light chain L and the heavy chain H.

Run Surfaces

We see that the mutation K417N lowers the binding affinity, as seen in escape evaluations.

Conformational ensembles
====================
