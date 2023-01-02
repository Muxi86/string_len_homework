def main(a):
    """
    A string type variable is given. Return True if its length is even. Return False if its length is odd.
    Args:
        a: string
    Returns:
        True or False
    """
    a = len(a)
    ans = ''
    if a%2==0:
        ans = "True"
    else:
        ans = "False"
    return ans

print(main("code"))