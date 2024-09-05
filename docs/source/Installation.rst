Installation
=====

.. _installation:

Pymol Installation
------------

Pymol installation will be done using Miniconda (https://docs.anaconda.com/miniconda/#quick-command-line-install )

Once miniconda was installed:

.. code-block:: console

    conda install conda-forge::pymol-open-source


Plug-in installation
----------------

The source code of latest release of NRG_QT version is available at: https://github.com/ThomasDesc/NRG_plugin/releases/

1. Download the "NRGSuite_Qt.zip" in a known directory.

2. Open Pymol interface and click in 'Plugin -> Plugin Manager -> Install New Plugin -> Choose file'.

.. image:: images/pymol_interface.png
       :alt: An example image
       :width: 300px
       :align: center

3. Go to the directory of the source code and select 'NRGSuite_Qt.zip'  and click 'Open'.


4. Choose a directory for the installed plug-in.

.. image:: images/plug-inpath.png
       :alt: An example image
       :width: 300px
       :align: center

5. Close and re-open pymol. The plug-in must be listed as 'NRGSuite_QT' the 'Plugin' menu and should be listed in the 'Installed Plugins' list in the 'Plugin Manager' window.

.. image:: images/pluginlisted.png
    :alt: An example image
    :width: 300px
    :align: center

.. note::
    For macOS users: In your 'System Settings' in the session 'Private and Security' menu the option 'Allow applications from' should marked as 'App store and identified developers'.

    .. image:: images/sucrity_mac.png
        :alt: An example image
        :width: 300px
        :align: center

    For users of older MACs (not M1) the command should be:
    .. code-block:: console

        mkdir -p ~/miniconda3
        curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o ~/miniconda3/miniconda.sh
        bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
        rm ~/miniconda3/miniconda.sh

    and then after the installation:
.. code-block:: console

        ~/miniconda3/bin/conda init bash
        ~/miniconda3/bin/conda init zsh