file = open("sample.in", "r")

while True:
    inputstring = file.readline()

    if not inputstring:
        break

    inputdata = inputstring.split()

    num1 = int(inputdata[0])
    num2 = int(inputdata[1])

    numdifference = num1 - num2

    finalproduct = abs(numdifference)

    print(finalproduct)

