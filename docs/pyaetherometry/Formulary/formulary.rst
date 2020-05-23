.. _formulary:

********************************
Formulary (`PyAetherometry.formulary`)
********************************

.. currentmodule:: pyaetherometry.formulary

`pyaetherometry.formulary` provides theoretical formulas for calculation of
physical quantities helpful for aetherometric physics.

.. toctree::
   :maxdepth: 1

  

The subpackage makes heavy use of `astropy.units.Quantity` for handling
conversions between different unit systems. 

Most functions expect `astropy.units.Quantity` as input, however some
will use the `~pyaetherometry.utils.decorators.validate_quantities` decorator
to automatically cast arguments to Quantities with appropriate units. If
that happens, you will be notified via an `astropy.units.UnitsWarning`.

Please note that well maintained physical constant data with units and
uncertainties can be found in `astropy.constants`.

For a general overview of how unit-based input works, take a look at the
following example:

.. topic:: Examples:

   * :ref:`sphx_glr_auto_examples_plot_physics.py`

Notes for developers
====================
Values should be returned as an Astropy Quantity in aetherometric units.

The docstrings for aetherometric methods should be consistent with 
explanations and terminology provided in the publications of 
Experimental Aetherometry and Aetherometric Theory of Synchronicity. 