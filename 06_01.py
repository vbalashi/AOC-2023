import sys

#test example
a = [
    (7,9),
    (15,40),
    (30,200)
]

#part 1
a = [
    (51,377),
    (69,1171),
    (98, 1224),
    (78,1505)
]

#part 2
# a = [
#     (51699878, 377117112241505)
# ]

# Time:        51     69     98     78
# Distance:   377   1171   1224   1505

s = 1
for i in a:
    c = list(range(0,i[0]+1))
    # print(c)
    # print(c[::-1])
    d = [x * y for x, y in zip(c, c[::-1])]
    # print(d)
    for y in range(len(d)):
        if d[y] > i[1]:
            d[y] = 1
        else:
            d[y] = 0
    # print(d)
    # print(sum(d))
    s *= sum(d)

print(s)