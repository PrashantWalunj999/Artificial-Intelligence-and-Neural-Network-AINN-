print('Enter marks')
phy=input('Enter marks of physics ')
chem=input('Enter marks of chem ')
math=input('Enter marks of math ')
bio=input('Enter marks of bio ')
mar=input('Enter marks of mar')

total=phy+chem+math+bio+mar

percent=total*(100/500)

if percent>80:
    print('grade A')
elif percent>60:
    print('grade B')
elif percent>40:
    print('grade C')
else:
    print('grade D')
