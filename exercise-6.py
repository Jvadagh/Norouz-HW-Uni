values = []
for i in range(20):
    a = float(input("enter {0} value : ".format(i+1)))
    values.append(a)

print("sum: ", sum(values))
print("average: ", sum(values)/len(values))
print("min: ", min(values))
print("max: ", max(values))