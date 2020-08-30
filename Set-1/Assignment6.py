def computepay(h,r):
    if h>40:
        total=40*rate
        rem= h-40
        rate1=rate*1.5
        sum1=rate1*rem
        price= total+sum1
    return price
        
hrs = int(input("Enter Hours:"))
rate= float(input("Enter the rate:"))
p = computepay(hrs,rate)
print("Pay",p)
