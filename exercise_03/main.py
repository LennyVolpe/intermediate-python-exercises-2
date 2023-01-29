import numpy

a = numpy.random.uniform(low = 0, high = 1, size = 10)

print(a)
print("mean = " + str(numpy.mean(a)))
print ("median = " + str(numpy.median(a)))
print("Standard Deviation = " + str(numpy.std(a)))

