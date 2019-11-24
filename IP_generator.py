from random import randrange

print("Random IPv4 address generator")
domain = 255
no_of_ip = int(input("Enter the number of IPv4 address to generate:"))
for i in range(no_of_ip):
    print("{}.{}.{}.{}".format(randrange(2, domain), randrange(2, domain), randrange(2, domain), randrange(2, domain)))
