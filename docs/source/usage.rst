Usage
=====

.. _installation:

Pymol Installation
------------


MAC OS:

Open-Source PyMOL is available free of charge and may be readily installed via the Homebrew (recommended)

.. code-block:: console

   brew install brewsci/bio/pymol

WINDOWS INSTALL:

for windows install information refer to: https://pymolwiki.org/index.php/Windows_Install

LINUX INSTALL:




Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

