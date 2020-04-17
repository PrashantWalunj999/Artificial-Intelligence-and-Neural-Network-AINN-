print('ELECTRICITY BILL CALCULATOR')

unit=input('Enter Unit')
print('your unit is ',unit)

if unit<50:
    bill=(float(unit*(0.50)))
    print(bill+(17/100))
elif unit>50 and unit<150:
    bill=(50*0.50+(unit-50)*0.75)
    print(bill+(17/100))
elif unit>50 and unit>150 and unit<250:
    bill=(50*0.50+(100*0.75)+((unit-150)*1.25))
    print(bill+(17/100))
else:
    if unit>250:
        bill=unit*1.50
        print(bill+(17/100))
