n=int(input("Enter number of elements "))
arr=[]
print("Enter elements :")
for i in range(0,n):
    z=int(input())
    arr.append(z)

if(n==1):
    print("Not possible")
    exit()

k=int(input("Enter the value of k:"))
dict={}

for i in range(0,n):
        if arr[i] not in dict:
                dict[arr[i]]=1
        else:
            dict[arr[i]]=dict[arr[i]]+1


count=0
temp=0
temp1=0
for i in range(0,n):
    if((k-arr[i]) in dict and ((k-arr[i])==arr[i])):
        dict[arr[i]]=dict[arr[i]]-1
        temp1=temp1+dict[arr[i]]
    elif ((k-arr[i]) in dict and ((k-arr[i])!=arr[i])):
        temp=temp+dict[k-arr[i]]

temp1=temp1+temp//2
count=temp1
print(count)

