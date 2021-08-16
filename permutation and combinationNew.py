orders=0
books=[0,0,0,1,2,3,4,5,6,7]
a=len(books)
for i in range(0,8):
    for j in range(i+1,8):
        for k in range(j+1,8):
            List=[1,1,1,1,1,1,1,1]
            List[i]=0
            List[j]=0
            List[k]=0
            for l in range(a):
                if l!=k and l!=i and l!=j:
                    for m in range(a):
                        if m!=k and m!=i and m!=j and m!=l:
                            for n in range(a):                                        
                                if n!=k and n!=i and n!=j and n!=l and n!=m:
                                    for o in range(a):
                                        if o!=k and o!=i and o!=j and o!=l and o!=m and o!=n:
                                            for p in range(a):
                                                if p!=k and p!=i and p!=j and p!=l and p!=m and p!=n and p!=o:
                                                    orders+=1
                                                    if orders<101:
                                                        print (books[i],books[j],books[k],books[l],books[m],books[n],books[o],books[p])
print("The total count is : ", orders)
