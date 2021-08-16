total=0
books=[0,0,0,1,2,3,4,5,6,7]
count=len(books)
for i in range(0,8):
 for j in range(i+1,8):
 for k in range(j+1,8):
 List=[1,1,1,1,1,1,1,1]
 List[i]=0
 List[j]=0
 List[k]=0
 for l in range(count):
 if l!=k and l!=i and l!=j:
 for a in range(count):
 if a!=k and a!=i and a!=j and a!=l:
 for b in range(count):
 if b!=k and b!=i and b!=j and b!=l and b!=a:
 for c in range(count):
 if c!=k and c!=i and c!=j and c!=l and c!=a
and c!=b:
 for d in range(count):
 if d!=k and d!=i and d!=j and d!=l and
d!=a and d!=b and d!=c:
 total+=1
 if total<=100:
 print
(books[i],books[j],books[k],books[l],books[a],books[b],books[c],books[d])
print("The possibilities of outcomes are : ", total)
