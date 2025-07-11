==============
Prerequisites
==============

**NRGSuite** works with most **PyMOL** versions. However, to generate figures without watermarks we recommend installing **PyMOL open-source**. For making single mutations,
**MODELLER** is also required, though it is not necessary for using **NRGSuite**.
You’ll find detailed installation instructions below.

To avoid operating system specific installation issues, we recommend to install **PyMOL open-source** with `Anaconda`_ or `Miniconda`_.
Bellow we provide instructions on how to install Miniconda.

.. _Anaconda: https://docs.anaconda.com/anaconda/
.. _Miniconda: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html


.. tabs::

    .. tab:: Miniconda

        .. tabs::

            .. group-tab:: Windows

                #. Download the latest version of miniconda at the following link (Platform: Windows): https://docs.anaconda.com/miniconda/#miniconda-latest-installer-links
                #. Double-click the downloaded **.exe** file.
                #. Follow the instructions on the screen. If you are unsure about any setting, accept the defaults. You can change them later.
                #. When the installation finishes, use the **Windows** key and search for Anaconda Prompt.
                #. Click on it.

            .. group-tab:: MacOS

                .. note::
                    In your **System Settings**, within the **Privacy and Security** section, verify that **Allow applications from**
                    is marked as **App store and identified developers**.

                    .. image:: /_static/images/installation/security.png
                        :alt: Privacy and security
                        :width: 65%
                        :align: center

                I) Open 'Terminal':
                    #. Open **Spotlight Search** by pressing :kbd:`⌘` + :kbd:`Space`

                    #. Type **Terminal**

                    #. Click on the first result

                II) Paste the following command and press :kbd:`Enter`:

                    .. code-block:: console

                            mkdir -p ~/miniconda3
                            curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o ~/miniconda3/miniconda.sh
                            bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
                            rm ~/miniconda3/miniconda.sh
                            ~/miniconda3/bin/conda init bash
                            ~/miniconda3/bin/conda init zsh

                III) Close **Terminal** and open it again.

            .. group-tab:: Linux

                I) In a Terminal window paste the following command and press :kbd:`Enter`:

                    .. code-block:: console

                            mkdir -p ~/miniconda3
                            curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o ~/miniconda3/miniconda.sh
                            bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
                            rm ~/miniconda3/miniconda.sh
                            ~/miniconda3/bin/conda init bash
                            ~/miniconda3/bin/conda init zsh

                II) Close **Terminal** and open it again.


    .. tab:: PyMOL (open-source)

        Paste following commands in **Terminal** (MacOS) or **Anaconda Prompt** (Windows) and press :kbd:`Enter`

        1. Creating a new environment to avoid a conflict with dependency versions:

            .. code-block:: console

                conda create -n "pymol-env" python=3.12

        2. Loading the new environment (you will need to use this command to open PyMol):

            .. code-block:: console

                conda activate pymol-env

        3. Installing PyMol:

            .. code-block:: console

                conda install conda-forge::pymol-open-source

        4. Opening PyMol :

            .. code-block:: console

                pymol

    .. tab:: MODELLER (optional; requires license key)

        MODELLER is available free for academic non-profit institutions. You can obtain a key `here <https://salilab.org/modeller/registration.html>`_.
        Paste the following command in **Terminal** (MacOS) or **Anaconda Prompt** (Windows) and press :kbd:`Enter`:

            .. code-block:: console

                conda config --add channels salilab
                conda install modeller

        You will be prompted after installation to edit a file to add your MODELLER license key to a config.py file.


