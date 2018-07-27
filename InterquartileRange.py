def median(arr):
    #print arr
    l= len(arr)
    if l%2==1:
        median=arr[l//2]
    else:
        median=sum(arr[l//2-1:l//2+1])/2
    return median
#6
#6 12 8 10 20 16
#5 4 3 2 1 5
leng=int(input())
arr=map(int,raw_input().split(' '))
freq=map(int,raw_input().split(' '))
lis=[]
for i in range(0,leng):
    lis.extend([arr[i]]*freq[i])

leng=len(lis)
lis.sort()
#print lis
q1=median(lis[:leng//2])
if leng%2==0:
    q3=median(lis[leng//2:])
else:
    q3=median(lis[leng//2+1:])
print round(q3-q1,1)
