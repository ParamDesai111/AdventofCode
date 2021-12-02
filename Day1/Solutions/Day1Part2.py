arr1= []
arr1 += (int(input()) for x in range(2000))
         
arr1.append(1)
arr1.append(1)
arr1.append(1)
answer =0
for x in range(len(arr1)+6) :
    if arr1[x]==arr1[len(arr1)-3]:
        break
    if arr1[x]+arr1[x+1]+arr1[x+2]<arr1[x+1]+arr1[x+2]+arr1[x+3]:
        answer = answer+1
    print(arr1[x])
    

print(answer)
