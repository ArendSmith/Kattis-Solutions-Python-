filename = input("Enter file name: ")

file = open(filename, "r")

ndays = int(file.readline())

nresults = file.readline()

results = nresults.split()

ndaysbelowzero = 0

for i in range(0, ndays):
    if int(results[i]) < 0:
        ndaysbelowzero += 1

print(ndaysbelowzero)
