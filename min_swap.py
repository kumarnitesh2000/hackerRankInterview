#make min swaps to make seq similar code chef ----> CHFNSWPS





#min_swaps will tell 
# a = x1, x2
# b = y1 , y2
#after swapping x1 and y2 both a and b becomes equal
#tell the min swaps 
#assuming a and not fulfil normal cases :
def min_swaps(a,b):
  sumi = 0
  for i in range(len(a)-1):
    
    if a[i]!=b[i]:
      b[i] , a[i+1] = a[i+1],b[i]
      if a==b:
        sumi+=min(b[i],a[i+1])
  if sumi==0:      
    return -1  
  else:
    return sumi    



def find_cost(a,b):
  n = len(a)
  if n==1 and a[0]!=b[0]:
    return -1
  elif n==1 and a[0]==b[0]:
    return 0
  else:
    a.sort()
    b.sort()
    for i in range(n):
      c=0
      if a[i]==b[i]:
        c=c+1
      if c==n-1:  
        return 0
      else:
        return min_swaps(a,b)
  
t = int(input())
n = [0 for i in range(t)]
a = [[] for i in range(t)]
b = [[] for i in range(t)]

for i in range(t):
  n[i] = int(input())
  a[i] = list(map(int,input().split()))
  b[i] = list(map(int,input().split()))
  
res = [0 for i in range(t)]
for i in range(t):
  res[i] = find_cost(a[i],b[i])
  print(res[i])

