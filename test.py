import numpy as np
from imbalancedegree import ImbalanceDegree
from imbalanceratio import ImbalanceRatio

#Variables
complementMeasures = ['MANHATTAN_DISTANCE','EUCLIDEAN_DISTANCE','CHEBYSHEV_DISTANCE','KULLBACKLEIBLER_DIVERGENCE','HELLIGER_DISTANCE','TOTALVARIATION_DISTANCE','CHISQUARE_DIVERGENCE']


#Random generation of a class distribution by sampling a Dirichlet
classDistribution = np.random.dirichlet(np.random.randint(50,size= np.random.randint(2,10,size=1)), 1)
#Flatten the output list
classDistribution = [item for sublist in classDistribution for item in sublist]

print '============================='
print 'SAMPLED CLASS DISTRIBUTION'
print '============================='
stats = ImbalanceDegree(classDistribution)
print 'Number of classes: ' + str(stats.numClasses)
print 'Number of minority classes: ' + str(stats.numMinorityClasses)
print 'Class Distribution: ' + str([ '%.2f' % elem for elem in stats.classDistribution])
print 'Balanced distribution: ' + str([ '%.2f' % elem for elem in stats.balancedClassDistribution])
print 'Distribution with the lowest entropy: ' + str([ '%.2f' % elem for elem in stats.lowestEntropyClassDistribution])

print '============================='
print 'MEASURES'
print '============================='
#IMBALANCE RATIO
IR = ImbalanceRatio(classDistribution)
print 'IMBALANCE_RATIO: ' + str("{0:.2f}".format(IR.value))
print '-'
#IMBALANCE DEGREE
for complementMeasure in complementMeasures:
	ID = ImbalanceDegree(classDistribution,complementMeasure)
	print 'IMBALANCE_DEGREE_'+str(complementMeasure) + ': ' + str("{0:.2f}".format(ID.value))
