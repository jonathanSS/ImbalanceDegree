
from imbalancedegree import ImbalanceDegree
from imbalanceratio import ImbalanceRatio


def toyProblemDistribution(i):
	return [100,i,5] 

IRS = []
MANHATTAN_DISTANCES = []
EUCLIDEAN_DISTANCES = []
CHEBYSHEV_DISTANCES = []
KULLBACKLEIBLER_DIVERGENCES = []
HELLIGER_DISTANCES = []
TOTALVARIATION_DISTANCES = []
CHISQUARE_DIVERGENCES = []

for i in range(5,100):
	occurrences = toyProblemDistribution(i)
	IR = ImbalanceRatio(occurrences)
	ImbalanceDegree_Manhattan = ImbalanceDegree(occurrences,'MANHATTAN_DISTANCE')
	ImbalanceDegree_Euclidean = ImbalanceDegree(occurrences,'EUCLIDEAN_DISTANCE')
	ImbalanceDegree_Chebyshev = ImbalanceDegree(occurrences,'CHEBYSHEV_DISTANCE')
	ImbalanceDegree_KullbackLeibler = ImbalanceDegree(occurrences,'KULLBACKLEIBLER_DIVERGENCE')
	ImbalanceDegree_Helliger = ImbalanceDegree(occurrences,'HELLIGER_DISTANCE')
	ImbalanceDegree_TotalVariation = ImbalanceDegree(occurrences,'TOTALVARIATION_DISTANCE')
	ImbalanceDegree_ChiSquare = ImbalanceDegree(occurrences,'CHISQUARE_DIVERGENCE')
	IRS.append(IR.value)
	MANHATTAN_DISTANCES.append(ImbalanceDegree_Manhattan.value)
	EUCLIDEAN_DISTANCES.append(ImbalanceDegree_Euclidean.value)
	CHEBYSHEV_DISTANCES.append(ImbalanceDegree_Chebyshev.value)
	KULLBACKLEIBLER_DIVERGENCES.append(ImbalanceDegree_KullbackLeibler.value)
	HELLIGER_DISTANCES.append(ImbalanceDegree_Helliger.value)
	TOTALVARIATION_DISTANCES.append(ImbalanceDegree_TotalVariation.value)
	CHISQUARE_DIVERGENCES.append(ImbalanceDegree_ChiSquare.value)

print '============================='
print 'MEASURES for l_2 in [5,100]'
print '============================='
print 'IMBALANCE_RATIOS = ' + str(IRS).replace("[", "(").replace("]", ")") + '\n'
print 'MANHATTANDISTANCES = ' + str(MANHATTAN_DISTANCES).replace("[", "(").replace("]", ")") + '\n'
print 'EUCLIDEANDISTANCES = ' + str(EUCLIDEAN_DISTANCES).replace("[", "(").replace("]", ")") + '\n'
print 'CHEBYSHEVDISTANCES = ' + str(CHEBYSHEV_DISTANCES).replace("[", "(").replace("]", ")") + '\n'
print 'KULLBACKLEIBLERDIVERGENCES = ' + str(KULLBACKLEIBLER_DIVERGENCES).replace("[", "(").replace("]", ")") + '\n'
print 'HELLIGERDISTANCES = ' + str(HELLIGER_DISTANCES).replace("[", "(").replace("]", ")") + '\n'
print 'TOTALVARIATIONDISTANCES = ' + str(TOTALVARIATION_DISTANCES).replace("[", "(").replace("]", ")") + '\n'
print 'CHISQUAREDIVERGENCES = ' + str(CHISQUARE_DIVERGENCES).replace("[", "(").replace("]", ")") + '\n'
