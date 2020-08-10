def BruteforceIndex(text,s):
    for i in range(0,len(text)-len(s)+1):
        j=0
        while j<len(s):
            if text[i] != s[j]:
                break
            j+=1
            i+=1
        if j == len(s):
            print(i-3)

BruteforceIndex("patch not appliedap","app")

