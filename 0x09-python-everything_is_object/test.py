high = 0
i = 8

while i >= high:
    space = " " * high 
    stars = "*" * (2 * (i - high) - 1)
    print(space + stars)
    high += 1