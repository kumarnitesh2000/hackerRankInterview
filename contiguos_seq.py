
#there are [n*(n+1)]/2 arrays are there
#[1,2,7] -> [1],[2],[7],[1,2],[1,2,7],[2,7]
#Bit wise question 
#point to be noted that -> 0^x = x also 0|x = x
def oR(matrix):
  or_arr = []
  for i in matrix:
    fin = 0
    for j in i:
      fin=fin|j
    or_arr.append(fin)
  return or_arr    

def solve(arr):
  cont_sub = []
  for i in range(len(arr)):
    for j in range(i,len(arr)):
      lis = []
      for k in range(i,j+1):
        lis.append(arr[k])
      cont_sub.append(lis)
  final = oR(cont_sub)
  return final        

def check_pairwise(arr):
  g = arr[:]
  g.sort()
  for i in range(len(g)-1):
    if g[i]==g[i+1]:
      return "NO"
  return "YES"

or_arr = solve([1,2])
res = check_pairwise(or_arr)
print(res)
