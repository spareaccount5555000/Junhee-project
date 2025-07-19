Studetails = ("junhee", 21)

address = ("Singapore", "PasirRis", "Link", "Seastrandcondominium", "518188")

for i in address:
    print(i, end=" ")

# unpacking
country, town, street, estate, postalcode = address

print()
print("CNTRY", country)
print("TOWN", town)
print(street)
print(estate)
print(postalcode)

hi = 3, 4.6, "dog"
print(hi)

n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

print(n_tuple[0][3])
print(n_tuple[1][1])

my_tuple = ("p", "r", "o", "g", "r", "a", "m", "i", "z")

print(my_tuple[1:4])
print(my_tuple[0:2])
print(my_tuple[7:])
print(my_tuple)

my_tuple1 =(4,2,3,[4,5])
my_tuple1[3][0] = 9
print(mytuple1)

my_tuple1 = ("p", "r", "o", "g", "r", "a", "m", "i", "z")
print(mytuple1)

