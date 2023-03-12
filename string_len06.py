def main(s1,s2):
    """
    Given two strings, s1 and s2. Return the shortest length between them.
    Args:
        s1: string
        s2: string
    Returns:
        shortest string
    """
    ans = 0
    if len(s1) > len(s2):
        ans = len(s2)
    if len(s1) < len(s2):
        ans = len(s1)
    return s1

print(main('code','python'))