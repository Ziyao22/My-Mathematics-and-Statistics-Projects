Total=0
i=0
for i in range(0,8):
  for j in range(i+1,8):
  for k in range(j+1,8):
    Total+=1
    List=[1,1,1,1,1,1,1,1]
    List[i]=0
    List[j]=0
    List[k]=0
    for letter in List:
      print(letter,end=" ")
    print()
print("The total outcomes are", Total)
