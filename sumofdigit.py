n=int(input("Enter a number:"))
total=0
while(n>0):
    dig=n%10
    total=tot+dig
    n=n//10
print("The total sum of digits is:",total)
