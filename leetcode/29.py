dividend = 40
divisor = 3

shift = 0

while True:
    value = divisor << shift
    print(value)

    if value > dividend:
        break

    shift += 1