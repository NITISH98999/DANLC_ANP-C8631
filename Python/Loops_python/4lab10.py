# Q10. Wap to read age of 15 people and find the number of adults, babies and school age students.
baby = 0
schoolage = 0
adult = 0
print("Enter the age of 15 people")
for i in range(1, 16):
    a = int(input(f"Enter the age {i} person :"))
    if a <= 2:
        baby += 1
    elif a <= 17:
        schoolage += 1
    else:
        adult += 1
print(f"baby: {baby}")
print(f"School_age: {schoolage}")
print(f"adult: {adult}")
