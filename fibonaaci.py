a,b=0,1

usr_inp = int(input("Enter the limit for fibonacci series: "))

print("fibonaaci series is:")

while(b<usr_inp):
    print(b)
    a,b = b,a+b
