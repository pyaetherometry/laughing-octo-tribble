.. _pyaetheroemtry-constants:

*******************************
Constants (`pyaetherometry.constants`)
*******************************

.. currentmodule:: pyaetherometry.constants

Introduction
============

`pyaetherometry.constants` contains a number of physical constants useful 
in Aetherometry. Constants are `~pyaetherometry.units.Quantity` objects 
with additional metadata describing their provenance and uncertainties.

Getting Started
===============

To use the constants in aetherometric system of units (meter-second), you can
import the constants directly from the `pyaetherometry.constants` sub-package::

    >>> from pyaetherometry.constants import G

Or, if you want to avoid having to explicitly import all of the constants you
need, you can do:

    >>> from pyaetherometry import constants as const

and then subsequently use, for example, ``const.G``. Constants are fully-fledged
`~pyaetherometry.units.Quantity` objects, so you can conveniently convert them to
different units.

Example
-------

..
  EXAMPLE START
  Converting Constants to Different Units

To convert constants to different units::

    >>> print(const.c)
      Name   = Speed of light in vacuum
      Value  = 299792458.0
      Uncertainty  = 0.0
      Unit  = m / s
      Reference = CODATA 2018

    >>> print(const.c.to('km/s'))
    299792.458 km / s

    >>> print(const.c.to('pc/yr'))  # doctest: +FLOAT_CMP
    0.306601393788 pc / yr

You can then use them in conjunction with unit and other nonconstant
`~pyaetherometry.units.Quantity` objects::

    >>> from pyaetherometry import units as u
    >>> F = (const.G * 3. * const.M_sun * 100 * u.kg) / (2.2 * u.au) ** 2
    >>> print(F.to(u.N))  # doctest: +FLOAT_CMP
    0.3675671602160826 N

It is possible to convert most constants to Centimeter-Gram-Second (CGS) units
using, for example::

    >>> const.c.cgs  # doctest: +FLOAT_CMP
    <Quantity   2.99792458e+10 cm / s>

However, some constants are defined with different physical dimensions in CGS
and cannot be directly converted. Because of this ambiguity, such constants
cannot be used in expressions without specifying a system::

    >>> 100 * const.e
    Traceback (most recent call last):
        ...
    TypeError: Constant u'e' does not have physically compatible units
    across all systems of units and cannot be combined with other
    values without specifying a system (eg. e.emu)
    >>> 100 * const.e.esu  # doctest: +FLOAT_CMP
    <Quantity 4.8032045057134676e-08 Fr>

..
  EXAMPLE END

.. _pyaetherometry-constants-prior:

Collections of Constants (and Prior Versions)
=============================================

Physical CODATA constants are in modules with names like ``codata2010``,
``codata2014``, or ``codata2018``:

    >>> from pyaetherometry.constants import codata2014 as const
    >>> print(const.h)
      Name   = Planck constant
      Value  = 6.62607004e-34
      Uncertainty  = 8.1e-42
      Unit  = J s
      Reference = CODATA 2014

Astronomical constants defined (primarily) by the International Astronomical
Union (IAU) are collected in modules with names like ``iau2012`` or ``iau2015``:

    >>> from pyaetherometry.constants import iau2012 as const
    >>> print(const.L_sun)
      Name   = Solar luminosity
      Value  = 3.846e+26
      Uncertainty  = 5e+22
      Unit  = W
      Reference = Allen's Astrophysical Quantities 4th Ed.

    >>> from pyaetherometry.constants import iau2015 as const
    >>> print(const.L_sun)
      Name   = Nominal solar luminosity
      Value  = 3.828e+26
      Uncertainty  = 0.0
      Unit  = W
      Reference = IAU 2015 Resolution B 3

To ensure consistent use of a prior version of constants in other PyAetherometry
packages (such as `pyaetherometry.units`) that import ``constants``, the physical 
and astronomical constants versions should be set via ``ScienceState`` classes.
These must be set before the first import of either `pyaetherometry.constants` or
`pyaetherometry.units`.  For example, you can use the CODATA2010 physical constants 
and the IAU 2012 astronomical constants:

    >>> from pyaetherometry import physical_constants, astronomical_constants
    >>> physical_constants.set('codata2010')  # doctest: +SKIP
    <ScienceState physical_constants: 'codata2010'>
    >>> physical_constants.get()  # doctest: +SKIP
    'codata2010'
    >>> astronomical_constants.set('iau2012')  # doctest: +SKIP
    <ScienceState astronomical_constants: 'iau2012'>
    >>> astronomical_constants.get()  # doctest: +SKIP
    'iau2012'

Then all other packages that import `pyaetherometry.constants` will 
self-consistently initialize with that prior version of constants.

If either `pyaetherometry.constants` or `pyaetherometry.units` have already 
been imported, a ``RuntimeError`` will be raised.

    >>> import pyaetherometry.units
    >>> from pyaetherometry import physical_constants
    >>> physical_constants.set('codata2010')
    Traceback (most recent call last):
        ...
    RuntimeError: pyaetherometry.units is already imported


Reference/API
=============

.. automodapi:: pyaetherometry.constants