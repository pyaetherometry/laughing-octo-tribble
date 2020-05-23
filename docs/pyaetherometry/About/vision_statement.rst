.. _pyaetherometry-vision-statement:

PyAetherometry's Vision Statement
=================================

About PyAetherometry
--------------------

PyAetherometry is a free and open source Python package that 
provides common functionality required for applying the tools 
of `Aetherometry <http://www.aetherometry.com/>`_ in a single, 
reliable codebase.

Motivation
----------

`Aetheometry, 
<http://www.encyclopedianomadica.org/English/aetherometry.php>`_ 
as a scientific discipline, makes novel contributions to the 
language and study of physics - beginning with its object of 
study - massfree energy. 

In approaching Aetherometry, the student of Aetherometry is 
presented with a systematic body of work - `experimentally 
<http://www.encyclopedianomadica.org/English/experimental_aetherometry.php>`_ 
and `theoretically <http://www.encyclopedianomadica.org/English/atos.php>`_. 
elaborated - that establishes and formalizes these contributions 
in the `mathematical language of aetherometric functions
<http://www.encyclopedianomadica.org/English/aetherometric_mathematics.php>`_.

Fundamental characteristics of this language - for example, its 
mass-to-length transformation - lead to the elaboration of a 
system of units based solely in meters and seconds, to exact 
functions for the conversion and expression of all fundamental 
physical constants and SI base units in this aetherometric system
of units. 

The fundamental nature of the scientific contributions made by 
aetherometric theory, lie at the encounter of definitions at the 
foundations of currently accepted physical theory - for example, 
questioning (i.e. making redundant) the need for defining the 
Ampere as a base unit, expressing the fundamental electric charge, 
e, instead, as a linear momentum at 13.97017 m^2 / sec. 
* TODO: mass-to-length example
* TODO: connection/implications on all scientific disciplines

The simple examples above highlights the need for a software package 
able to provide the core functionality and common framework for handling 
these exclusively aetherometric unit conversions required for the analysis
and representation of data. 

It is our intention for this software package to serve as an 
educational tool for the benefit of future students of Aetheometry, 
and to be cooperatively developed by researchers in many scientific
disciplines interested in employing the tools of Aetheometry in their
work. In this document, we lay out our vision for PyAetherometry: 
a community-developed and community-driven open source core Python 
software package for aetherometric physics.

Organizational Structure
------------------------

The Coordinating Committee (CC) will oversee the PyAetherometry project 
and code development. The CC will ensure that roles are being filled,
facilitate community-wide communication, coordinate and delegate tasks,
manage the project repository, oversee the code review process, regulate
intercompatibility between different subpackages, seek funding
mechanisms, facilitate compromises and cooperation, enforce the code of
conduct, and foster a culture of appreciation.

Development Procedure
---------------------

The initial developers of PyAetherometry will create a flexible development
roadmap that outlines and prioritizes subpackages to be developed. The
developers will survey existing open source Python packages in plasma
physics. Priority will be given to determining how data will be stored
and structured. Developers will break up into small groups to work on
different subpackages. These small groups will communicate regularly and
work towards interoperability and common coding practices.

New code and edits should be submitted as a pull request to the
development branch of the PyAetherometry repository on GitHub. The pull
request will undergo a code review by the subpackage maintainers, who 
will provide suggestions on how the contributor may update the pull 
request. A friendly guide on how users may contribute new code to 
PyAetherometry will be developed.

New code should conform to the `PEP 8 style guide for Python
code <https://www.python.org/dev/peps/pep-0008/>`_ and the established
coding style within PyAetherometry. New code should be submitted with
documentation and tests. Documentation should be written primarily in
docstrings and follow the `numpydoc documentation style
guide <https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt>`_.
Every new module, class and function should have an appropriate
docstring. The documentation should describe the interface and the
purpose for the method, but generally not the implementation. The code
itself should be readable enough to be able to explain how it works.
Documentation should be updated when the code is edited. The tests
should cover new functionality (especially methods with complex logic),
but the tests should also be readable and easy to maintain. Existing
tests should be updated when necessary [e.g., during the initial
development of a new feature when the application program interface
(API) is not yet stable], but with caution since this may imply loss of
backwards compatibility.

Members of the PyAetherometry community may submit `PyAetherometry 
Enhancement Proposals (PAEPs) <https://github.com/PyAetherometry/PyAetherometry-PAEPs>`_ 
to suggest changes such as major reorganization of a subpackage, creation
of a new subpackage, non-backwards compatible changes to a stable
package, or significant changes to policies and procedures related to
the organization of this project. The issues list on GitHub will
generally be more appropriate for changes that do not require community
discussion. The PyAetherometry Developers shall maintain a GitHub repository 
of PAEPs. PAEPs will be made openly available for community discussion and 
transparency for a period of at least four weeks, during which time the 
proposal may be updated and revised by the proposers. The CC shall approve 
or decline these proposals after seeking community input. The rationale 
behind the decision and a summary of the community discussion shall be 
recorded along with the PAEP.

Programming Guidelines
----------------------

Choice of Languages
~~~~~~~~~~~~~~~~~~~

PyAetherometry shall be written using Python 3. PyAetherometry shall 
initially guarantee compatibility with Python 3.6 and above. Python 3 is
continually growing, so we will proceed on the general principle that
future updates to PyAetherometry remain compatible with releases of Python
that are up to two years old. Python 2.7 and below will not be supported
as these versions will no longer be updated past 2020. The core package
will initially be written solely in Python.

Code readability is more important than optimization, except when
performance is critical. Code should be optimized only after getting it
to work, and primarily for where there is a performance bottleneck.
Performance-critical parts of the core package will preferably be
written using Numba to achieve compiled speeds while maintaining 
the significant advantages of using a high level language.

Versioning
~~~~~~~~~~

PyAetherometry will use `Semantic Versioning <http://semver.org/>`_. 
Releases will be given version numbers of the form *MAJOR*.\ *MINOR*.\ 
*PATCH*, where *MAJOR*, *MINOR*, and *PATCH* are nonnegative integers. 
Starting with version 1.0, *MAJOR* will be incremented when backwards
incompatible changes are made, *MINOR* will be incremented when new
backwards-compatible functionality is added, and *PATCH* will be
incremented when backwards-compatible bug fixes are made.

Development releases will have *MAJOR* equal to zero and start at
version 0.1. The API should not be considered stable during the
development phase. PyAetherometry will release version 1.0 once it has 
a stable public API that users are depending on for production code.

All releases will be provided with release notes and change log entries,
and a table will be provided that describes the stability of the public
API for each PyAetherometry subpackage.

Dependencies
~~~~~~~~~~~~

Dependencies have the advantage of providing capabilities that will
enhance PyAetherometry and speed up its development, but the disadvantage 
that they can make manual installation more difficult and potentially
frustrating. Package managers such as Anaconda and Homebrew greatly
simplify installation of Python packages, but there will be situations
where manual installation is necessary (e.g., on some supercomputers
without package managers). The core package should be able to be
imported using a minimal number of packages (e.g., NumPy, SciPy, and
matplotlib) without getting an import error. Additional packages may be
included as dependencies of the core package if there is a strong need
for it, and if these packages are easily installed with currently
available package managers. Subpackages may use additional dependencies
when appropriate.

Affiliated Packages
~~~~~~~~~~~~~~~~~~~

We will follow the practice of Astropy by having a core package and
affiliated packages. The core package will contain common tools and base
functionality that most aetherometric physicists will need. The affiliated
packages contained in separate repositories will include more specialized 
functionality that may be needed for application of aetherometric physics 
in specific scientific discipline or domains. This approach will reduce the 
likelihood of scope creep for the core package while maintaining avenues for 
broader development.

Fundamental Constants
~~~~~~~~~~~~~~~~~~~~~

The values of the fundamental physical constants to used in this package 
will be the set of self-consistent values of the basic constants and 
conversion factors of physics and chemistry recommended by the Committee 
on Data for Science and Technology (CODATA) for international use.

* TODO: Define precisely which fundamental constants will be considered
as such by Aetherometry, and differences introduced by aetherometric theory.
Link to _pyaetherometry.constants for further discussion/elaboration.

Units
~~~~~

Code will be written assuming the aetherometric meter-second system 
of units. However, due to the necessity of working with fundamental 
physical constants and data most commonly reported in SI base units,
we will use an existing Python module (e.g., astropy.units or pint) 
to assign units to variables and allow straightforward conversion 
between different systems of units.

* TODO: consider better addressing decision vs. SI units