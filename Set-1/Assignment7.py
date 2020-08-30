largest = None
smallest = None
while True:
    
    num = input("Enter a number: ")
    
    if num == "done" : 
        break
    try:
        num=int(num)
    except:
        print("Invalid input")
        continue
    if smallest is None:
        smallest = int(num)
    elif int(num)< smallest:
        smallest= int(num)
    if largest is None:
        largest=int(num)
    elif int(num)>largest:
        largest=int(num)
print("Maximum is", largest)
print("Minimum is", smallest)
