def luckBalance(k, contests):
    sumi = 0
    for i in contests:
        if i[1]==0:
            print('Adding ',i[0])
            sumi+=i[0]
    j=0
    t=0
    contests.sort(reverse=True)
    #print(len(contests))
    
    while j < k and t<len(contests):
        if contests[t][1]==1:
            print("Adding ",contests[t][0])
            sumi+=contests[t][0]
            j+=1      
        t+=1
        
    
    if t < len(contests):
        while  t<len(contests):
            if contests[t][1]==1:
                print("Removing ",contests[t][0])
                sumi-=contests[t][0]
            t+=1

            
    
    
    return sumi
