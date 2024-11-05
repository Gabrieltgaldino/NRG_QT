Miniconda Installation
---------------------

.. _install-ana_macos:

MacOS (x86_64)
^^^^^^^^^^^^^^
.. note::
    In your 'System Settings', within the 'Private and Security' section, verify that 'Allow applications from'
    is marked as 'App store and identified developers'.

    .. image:: /_static/images/installation/security.png
        :alt: Privacy and security
        :width: 65%
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