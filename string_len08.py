def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    if len(s)%2 != 0:
        a = len(s)//2
        return s[a]
    else:
        a = len(s)//2
        b = a+1
        return s[a] + s[b]

print(main('abcdfe'))