def makeAnagram(a, b):
    tot = len(a)+len(b)
    b_S = []
    for i in b:
        b_S.append(i)
    stack = []
    for s in a:
        stack.append(s)
        for s2 in b_S:
            if s2==stack[-1]:
                tot=tot-2
                b_S.remove(s2)
                break

    
    return tot            
