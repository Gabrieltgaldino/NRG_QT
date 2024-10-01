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
---------------------

.. _install-ana_macos:

MacOS (x86_64)
~~~~~~~~~~~~~~~~~~
.. note::
    In your 'System Settings', within the 'Private and Security' section, verify that 'Allow applications from'
    is marked as 'App store and identified developers'.

    .. image:: images/sucrity_mac.png
        :alt: An example image
        :width: 300px
        :align: center

Open 'Terminal':
    Open **Spotlight Search** by pressing:

    |command-key| + **Space**

    Type in “Terminal.”

    Click on the first result

Paste the following command:

.. code-block:: console

        mkdir -p ~/miniconda3
        curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o ~/miniconda3/miniconda.sh
        bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
        rm ~/miniconda3/miniconda.sh
        ~/miniconda3/bin/conda init bash
        ~/miniconda3/bin/conda init zsh

Close terminal and open it again.

Windows (from the anaconda website)
~~~~~~~~~~~~~~~~~~~

#. Download the latest version of miniconda at the following link (Platform: Windows):
    https://docs.anaconda.com/miniconda/#miniconda-latest-installer-links
#. Double-click the downloaded .exe file.
#. Follow the instructions on the screen. If you are unsure about any setting, accept the defaults. You can change them later.
#. When the installation finishes, use the windows key and search for Anaconda Prompt.
#. Click on it.

Modeller (optional; requires license key)
---------------------

In the open terminal window paste the following code and press enter:

.. code-block:: console
    conda config --add channels salilab
    conda install modeller

You will be prompted after installation to edit a file to add your Modeller license key.

Plugin
======

To save your work, press :kbd:`⌘` + :kbd:`Space`.

.. _Anaconda: https://docs.anaconda.com/anaconda/
.. _Miniconda: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html
.. |command-key| image:: images/Installation/img.png
    :width: 50px
   :height: 50px
.. |s-key| image:: path/to/s-key.png