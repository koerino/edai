# Question 5: Learning With Restarts

from Testing import average, stDeviation, testPenData, testCarData

# Run 5 iterations of testPenData 
print "Tesing Pen Data:"
penDataTestAccuracy = []
for i in xrange(5):
    iterationResult = testPenData()[1]
    penDataTestAccuracy.append(iterationResult)
    
print "Max: ", max(penDataTestAccuracy)
print "Average: ", average(penDataTestAccuracy)
print "Standard deviation: ", stDeviation(penDataTestAccuracy)


print "\n"

# Run 5 iterations of testCarData
print "Tesing Car Data:"
carDataTestAccuracy = []
for i in xrange(5):
    iterationResult = testCarData()[1]
    carDataTestAccuracy.append(iterationResult)
    
print "Max: ", max(carDataTestAccuracy)
print "Average: ", average(carDataTestAccuracy)
print "Standard deviation: ", stDeviation(carDataTestAccuracy)