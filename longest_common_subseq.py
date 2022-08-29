def longestStringSubsequence(text1,text2):
    result = ''
    while result == '':
        com = list(set(text1)&set(text2))
        for i in text1:
            if i not in com:
                text1 = text1.replace(i,'')
        for i in text2:
            if i not in com:
                text2 = text2.replace(i,'')
        if len(text1) >= len(text2):
            if text2 not in text1:
                text2 = text2[:-1]
            else:
                result += text2
        else:
            if text1 not in text2:
                text1 = text1[:-1]
            else:
                result += text1
    return result
if __name__  == "__main__":
    s1 = "AGGTAB"
    s2 = "GXTXAYB"
    res = longestStringSubsequence(s1,s2)
    print(res)