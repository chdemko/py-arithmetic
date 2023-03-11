# distutils: sources = arithmetic/c-arithmetic/src/numeric/arithmetic.c arithmetic/c-arithmetic/src/numeric/gcd.c
# distutils: include_dirs = arithmetic/c-arithmetic/src/numeric
# distutils: extra_compile_args = -O3
# cython: embedsignature=True

cimport arithmetic.c_arithmetic

def gcd(a: int, b: int) -> int:
    """
    Compute the greatest common divisor of two numbers.
    
    Parameters
    ----------
    a : int
        The first number
    b : int
        The second number

    Returns
    -------
    int
        The greatest common divisor.         
    """
    return arithmetic.c_arithmetic.arithmetic_gcd(a, b)
    
def lcm(a: int, b: int) -> int:
    """
    Compute the least common multiple of two numbers.
    
    Parameters
    ----------
    a : int
        The first number
    b : int
        The second number

    Returns
    -------
    int
        The least common multiple.         
    """
    return arithmetic.c_arithmetic.arithmetic_lcm(a, b)
    
