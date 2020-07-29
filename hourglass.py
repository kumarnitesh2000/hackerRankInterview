def hourglassSum(arr):
    maxi=-10000
    #sumi=0
    for i in range(4):
        
        for j in range(4):
            sumi = 0
            sumi+=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j+1]+arr[i+2][j+2]+arr[i+2][j]
            maxi = max(sumi,maxi)
            print(maxi)
            
    
    return maxi
