basic=input('Enter basic Salary')

da=basic*(75/100)
hra=basic*(20/100)

if basic<10000:
    gross=da+basic
    print(gross)
elif basic >=10000 and basic<20000:
    gross=da+basic+(hra*(50/100))
    print(gross)
elif basic>=20000:
    gross=basic+da+hra
    print(gross)
