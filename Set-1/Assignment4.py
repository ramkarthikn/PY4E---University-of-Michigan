hrs = int(input("Enter Hours:"))
rate= float(input("Enter the rate:"))
if hrs>40:
    total= 40*rate
    rest=hrs-40
    rate1= rate*1.5
    sum1= rest*rate1
print(sum1+total)
