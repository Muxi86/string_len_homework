def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    s = len(s1) + len(s2) + len(s3)
    if s%2 != 0:
        return [s3]
    else:
        return [s1,s2]

print(main('codeschool.uz','example','python'))