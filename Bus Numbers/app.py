file = open("sample-busnumbers.in", "r")

nstops = int(file.readline())

inputstring = file.readline()

inputstring = inputstring.rstrip()

numlist = inputstring.split(" ")

numlist.sort()

finalstring = []

i = 0

while i < nstops:

    if i == nstops - 1:
        finalstring.append(numlist[i])
        break
    else:
        num1 = numlist[i + 1]
        num2 = numlist[i]

    if int(num1) - int(num2) == 1:

        min = num2

        index = i+1

        while True:

            num1 = numlist[index + 1]
            num2 = numlist[index]

            if int(num1) - int(num2) == 1:
                index += 1

            else:
                max = num2
                break

        if int(max) - int(min) > 1:
            finalstring.append(min)
            finalstring.append("-")
            finalstring.append(max)
            finalstring.append(" ")
            i = index + 1

        else:
            finalstring.append(min)
            finalstring.append(" ")
            finalstring.append(max)
            finalstring.append(" ")
            i = index + 1

print("".join(finalstring))
