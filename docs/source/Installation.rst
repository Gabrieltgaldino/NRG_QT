==================
Installation
==================

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
^^^^^^^^^^^^^^
.. note::
    In your 'System Settings', within the 'Private and Security' section, verify that 'Allow applications from'
    is marked as 'App store and identified developers'.

    .. image:: images/installation/security.png
        :alt: Privacy and security
        :width: 500px
        :align: center

Open 'Terminal':
    Open **Spotlight Search** by pressing:

        :kbd:`⌘` + :kbd:`Space`

.. apple website has keys

    Type “Terminal”

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Download the latest version of miniconda at the following link (Platform: Windows):
    https://docs.anaconda.com/miniconda/#miniconda-latest-installer-links
#. Double-click the downloaded .exe file.
#. Follow the instructions on the screen. If you are unsure about any setting, accept the defaults. You can change them later.
#. When the installation finishes, use the windows key and search for Anaconda Prompt.
#. Click on it.

Modeller (optional; requires license key)
-----------------------------------------

In the open terminal window paste the following code and press enter:

.. code-block:: console

    conda config --add channels salilab
    conda install modeller

You will be prompted after installation to edit a file to add your Modeller license key.

NRGSuite_Qt
===========

.. _install-general-plugin:

Download NRGSuite_Qt
--------------------

The source code of latest release of NRG_QT version is available at: https://github.com/ThomasDesc/NRG_plugin/releases/

.. _download-plugin:

MacOS
^^^^^

Download ***NRGSuite_Qt_mac.zip*** by clicking on it under assets

Windows
^^^^^^^

Download ***Source code (zip)*** by clicking on it under assets

Installation instructions
-------------------------

#. Open Pymol interface and click in **Plugin** -> **Plugin Manager** -> **Install New Plugin** -> **Choose file**

    .. image:: images/installation/plugin_install.png
           :alt: An example image
           :width: 1000px
           :align: center

#. Go to the directory of the source code and select the downloaded ***.zip*** file and click 'Open'.

    .. note::
        If the file was downloaded via Safari and the zip was extracted and doesn't exist in the directory. Go to the extracted directory and click on the file '__ini__.py'.

        .. image:: images/installation/plugin_install_init.png
           :alt: An example image
           :width: 300px
           :align: center

#. A prompt will appear to choose a directory for the installed plug-in. We recommend the suggested path


#. Close and open PyMol. If installed using anaconda you will need to write pymol in a terminal window and press enter.
If the plugin has been installed correctly it will appear in the "Plugin" tab.

    .. image:: images/installation/installation_end.png
        :alt: An example image
        :width: 500px
        :align: center

.. _Anaconda: https://docs.anaconda.com/anaconda/
.. _Miniconda: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html
