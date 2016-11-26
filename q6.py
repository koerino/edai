# Question 6: Varying The Hidden Layer

from Testing import average, stDeviation, testPenData, testCarData

for i in xrange(9):
    print "Tesing Pen Data ({} perceptrons):".format(i * 5)
    penDataTestAccuracy = []
    for i in xrange(5):
        iterationResult = testPenData([i * 5])[1]
        penDataTestAccuracy.append(iterationResult)
    
    print "Max: ", max(penDataTestAccuracy)
    print "Average: ", average(penDataTestAccuracy)
    print "Standard deviation: ", stDeviation(penDataTestAccuracy)
    
for i in xrange(9):
    print "Tesing Car Data ({} perceptrons):".format(i * 5)
    carDataTestAccuracy = []
    for i in xrange(5):
        iterationResult = testCarData([i * 5])[1]
        carDataTestAccuracy.append(iterationResult)
    
    print "Max: ", max(carDataTestAccuracy)
    print "Average: ", average(carDataTestAccuracy)
    print "Standard deviation: ", stDeviation(carDataTestAccuracy)