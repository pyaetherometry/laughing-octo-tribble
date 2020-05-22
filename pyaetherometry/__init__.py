__all__ = []

from .example_mod import *   

__all__ += ['do_primes']   
# or you can keep everything from the subpackage with the following instead
# __all__ += example_mod.__all__
