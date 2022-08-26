def longestStringSubsequence(s1,s2):
    result = ''
    while result == '':
        com = list(set(s1)&set(s2))
        s1 = ''.join([i for i in s1 if i in com])
        s2 = ''.join([i for i in s2 if i in com])
        if len(s1) >= len(s2):
            if s2 not in s1:
                s2 = s2[:-1]
            else:
                result += s2
        else:
            if s1 not in s2:
                s1 = s1[:-1]
            else:
                result += s1
    return result
if __name__  == "__main__":
    s1 = "AAAA"
    s2 = "AA"
    res = longestStringSubsequence(s1,s2)
    print(res)