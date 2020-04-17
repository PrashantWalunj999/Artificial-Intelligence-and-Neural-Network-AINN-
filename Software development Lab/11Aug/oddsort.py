x=[1,2,3,4,5,6,7,8,9,0]
i=0
while i<len(x):
        if x[i] %2==1:
            x[i]+=1
        i+=1
print x


x=[1,2,3,4,5,6,7,8,9,0]

print 'before',x
odd=[]
for val in x:
        if val%2