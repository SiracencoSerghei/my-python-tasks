import random

random.seed()
print(random.random())

print(random.randint(1, 10))
# for _ in range(10):
    # print(random.randint(1, 10), end=" ") # 2 4 5 5 4 6 8 3 4 10
    # print(random.randrange(1, 10), end=" ")

l = list(range(1, 10))
print(l)
random.shuffle(l)
print(l)

print(random.choice(l))
print((random.sample(l, 5)))
# ======================================
d = {
    1:"OREL",
    2:"RESHKA"
}
count_O = 0
count_R = 0
seq = []
while True:
    trial = random.randint(1, 2)
    if trial == 1:
        count_O +=1
        count_R = 0
    else:
        count_R += 1
        count_O = 0
    seq.append(d[trial])
    if count_O == 3 or count_R == 3:
        break
print(f"sequence: {seq}")
print(f"sequence: {len(seq)}")
if count_O == 3:
    print('O')
if count_R == 3:
    print("r")

