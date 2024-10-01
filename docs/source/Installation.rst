============
Installation (New)
============

.. _installation:

Pre-requisites
==============

To avoid operating system specific installation issues, we recommend to install pymol with `Anaconda`_ or `Miniconda`_.
Bellow we provide instructions on how to install Miniconda.

.. _install-macos:

Anaconda Installation
-----

.. _install-ana_macos:

MacOS (x86_64)
~~~~~~~~~~~~~~~~~~
.. note::
    In your 'System Settings' in the session 'Private and Security' menu the option 'Allow applications from' should marked as 'App store and identified developers'.

    .. image:: images/sucrity_mac.png
        :alt: An example image
        :width: 300px
        :align: center

Open 'Terminal':
    Open **Spotlight Search** by pressing:

        **command** + **Space**

Paste the following command:

.. code-block:: console

        mkdir -p ~/miniconda3
        curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o ~/miniconda3/miniconda.sh
        bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
        rm ~/miniconda3/miniconda.sh
        ~/miniconda3/bin/conda init bash
        ~/miniconda3/bin/conda init zsh

close terminal and open it again.

Windows
~~~~~~~~~~~~~~~~~~~





.. _Anaconda: https://docs.anaconda.com/anaconda/
.. _Miniconda: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html