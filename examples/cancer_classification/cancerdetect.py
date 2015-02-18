#!/usr/bin/python

import sys
import deeplearn

deeplearn.setErrorThreshold(0, 1.6)
deeplearn.setErrorThreshold(1, 0.6)
deeplearn.setErrorThreshold(2, 0.6)
deeplearn.setErrorThreshold(3, 3.0)

noOfSamples = deeplearn.readCsvFile("wdbc.data", 16, 3, [1])
print str(noOfSamples) + " samples loaded"

deeplearn.setLearningRate(0.2)
deeplearn.setDropoutsPercent(0.001)
deeplearn.setHistoryPlotInterval(50000)
deeplearn.setPlotTitle("Cancer Classification Training")

print "Training started"

timeStep = 0
while (deeplearn.training() != 0):
    timeStep = timeStep + 1

print "Training Completed"
print "Test data set performance is " + str(deeplearn.getPerformance()) + "%";

deeplearn.export("result.c")
print "Exported trained network"