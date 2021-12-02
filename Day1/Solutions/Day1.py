
arr1= []
arr1 += (int(input()) for x in range(2000))
         

answer =0
for x in range(len(arr1)+1) :
    if arr1[x]==arr1[len(arr1)-1]:
        break
    if arr1[x+1]>=arr1[x]:
        answer = answer+1
    

print(answer)
