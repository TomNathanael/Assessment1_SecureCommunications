p = 29
ints = [14, 6, 11]
square_root = []

for i in range(1, p):
    for item in ints:
        if i * i % p == item:
            square_root.append(i)

print(min(square_root))