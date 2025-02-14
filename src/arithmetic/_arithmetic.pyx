# distutils: sources = src/arithmetic/c-arithmetic/src/numeric/arithmetic.c
# distutils: include_dirs = src/arithmetic/c-arithmetic/src/numeric
# distutils: extra_compile_args = -O3

cimport arithmetic.c_arithmetic

def gcd(a: int, b: int) -> int:
    """
    Compute the greatest common divisor of two numbers.
    
    Parameters
    ----------
    a
        The first number
    b
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
    a
        The first number
    b
        The second number

    Returns
    -------
    int
        The least common multiple.         
    """
    return arithmetic.c_arithmetic.arithmetic_lcm(a, b)
    
