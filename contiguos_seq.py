
#there are [n*(n+1)]/2 arrays are there
#[1,2,7] -> [1],[2],[7],[1,2],[1,2,7],[2,7]

def solve(arr):
  cont_sub = []
  for i in range(len(arr)):
    for j in range(i,len(arr)):
      lis = []
      for k in range(i,j+1):
        lis.append(arr[k])
      cont_sub.append(lis)    
  print(cont_sub)    

solve([1,2,7])

