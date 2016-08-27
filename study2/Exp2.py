import numpy
import scipy.stats
import math
import sys
from imbalancedegree import ImbalanceDegree
from imbalanceratio import ImbalanceRatio

def namestr(obj, namespace):
	return [name for name in namespace if namespace[name] is obj]

print '\n========================================================'
print 'TABLE 1: Performance results for the datasets'
print '========================================================\n'


scores = []
f = open('performanceresults.txt', 'r')
for line in f:
	if not line.startswith('#'):
		elements = line.split('\t')
		datasetname = elements[0]
		numclasses = int(elements[1])
		j48 = [float(x) for x in elements[2].split(',')]
		if len(j48) != numclasses:
			print('error j48')
		part = [float(x) for x in elements[3].split(',')]
		if len(part) != numclasses:
			print('error part')
		jrip = [float(x) for x in elements[4].split(',')]
		if len(jrip) != numclasses:
			print('error jrip')
		multilayerperceptron = [float(x) for x in elements[5].split(',')]
		if len(multilayerperceptron) != numclasses:
			print('error multilayerperceptron')
		naivebayes = [float(x) for x in elements[6].split(',')]
		if len(naivebayes) != numclasses:
			print('error naivebayes')
		smo = [float(x) for x in elements[7].split(',')]
		if len(smo) != numclasses:
			print('error smo')
		string = datasetname + '	'
		Means = []
		for recalls in (j48,jrip,multilayerperceptron,naivebayes,smo):
		#for recalls in (j48,part,jrip,multilayerperceptron,naivebayes,smo):
			Amean = numpy.mean(recalls)
			Gmean = numpy.prod(recalls)** (1. / float(numclasses))
			Minmean = min(recalls)
			Means.append(Amean)
			Means.append(Gmean)
			Means.append(Minmean)
			string+="%.2f \t %.2f \t %.2f \t "%(Amean,Gmean,Minmean)
		scores.append(Means)
		print(string + "\n")

print '\n========================================================'
print 'TABLE 2: Measures and stats for the datasets'
print '========================================================\n'

IRS = []
MANHATTAN_DISTANCES = []
EUCLIDEAN_DISTANCES = []
CHEBYSHEV_DISTANCES = []
HELLIGER_DISTANCES = []
TOTALVARIATION_DISTANCES = []
KULLBACKLEIBLER_DIVERGENCES = []
CHISQUARE_DIVERGENCES = []

f = open('datasetsstats.txt', 'r')
for line in f:
	if not line.startswith('#'):
		elements = line.split('\t')
		datasetname = elements[0]
		numclasses = int(elements[1])
		occurrences = [int(x) for x in elements[2].split(',')]
		IR = ImbalanceRatio(occurrences)
		IRS.append(IR.value)
		ImbalanceDegree_Manhattan = ImbalanceDegree(occurrences,'MANHATTAN_DISTANCE')
		ImbalanceDegree_Euclidean = ImbalanceDegree(occurrences,'EUCLIDEAN_DISTANCE')
		ImbalanceDegree_Chebyshev = ImbalanceDegree(occurrences,'CHEBYSHEV_DISTANCE')
		ImbalanceDegree_KullbackLeibler = ImbalanceDegree(occurrences,'KULLBACKLEIBLER_DIVERGENCE')
		ImbalanceDegree_Helliger = ImbalanceDegree(occurrences,'HELLIGER_DISTANCE')
		ImbalanceDegree_TotalVariation = ImbalanceDegree(occurrences,'TOTALVARIATION_DISTANCE')
		ImbalanceDegree_ChiSquare = ImbalanceDegree(occurrences,'CHISQUARE_DIVERGENCE')
		MANHATTAN_DISTANCES.append(ImbalanceDegree_Manhattan.value - ImbalanceDegree_Manhattan.numMinorityClasses)
		EUCLIDEAN_DISTANCES.append(ImbalanceDegree_Euclidean.value - ImbalanceDegree_Euclidean.numMinorityClasses)
		CHEBYSHEV_DISTANCES.append(ImbalanceDegree_Chebyshev.value - ImbalanceDegree_Chebyshev.numMinorityClasses)
		KULLBACKLEIBLER_DIVERGENCES.append(ImbalanceDegree_KullbackLeibler.value - ImbalanceDegree_KullbackLeibler.numMinorityClasses)
		HELLIGER_DISTANCES.append(ImbalanceDegree_Helliger.value - ImbalanceDegree_Helliger.numMinorityClasses)
		TOTALVARIATION_DISTANCES.append(ImbalanceDegree_TotalVariation.value - ImbalanceDegree_TotalVariation.numMinorityClasses)
		CHISQUARE_DIVERGENCES.append(ImbalanceDegree_ChiSquare.value - ImbalanceDegree_ChiSquare.numMinorityClasses)
		numattributes = int(elements[3])
		print("%s \t %i \t %i \t %s \t %s \t %s \t %.2f \t %.2f \t %.2f \t %.2f \t %.2f \t %.2f \t %.2f\n"%(
			datasetname,
			numattributes,
			numclasses,
			'/'.join("%.2f"%(e) for e in ImbalanceDegree_Manhattan.classDistribution),
			'/'.join(str(e) for e in occurrences),
			IR.value,
			ImbalanceDegree_Manhattan.value,
			ImbalanceDegree_Euclidean.value,
			ImbalanceDegree_Chebyshev.value,
			ImbalanceDegree_KullbackLeibler.value,
			ImbalanceDegree_Helliger.value,
			ImbalanceDegree_TotalVariation.value,
			ImbalanceDegree_ChiSquare.value))
		
print '\n========================================================'
print 'TABLE 3: Correlation between measures and performance'
print '========================================================\n'

#Dealing with problematic infinities
IRS[5] = 8.4
IRS[11] = 853.0


for summary in (IRS,MANHATTAN_DISTANCES,EUCLIDEAN_DISTANCES,CHEBYSHEV_DISTANCES,KULLBACKLEIBLER_DIVERGENCES,HELLIGER_DISTANCES,TOTALVARIATION_DISTANCES,CHISQUARE_DIVERGENCES):
	scoreLists = map(list, zip(*scores))
	string = namestr(summary, globals())[0] +'\t'
	for score in scoreLists:
		pearson = scipy.stats.pearsonr(summary,score)[0]*100
		string+="%.0f\t"%(pearson)
	print(string+'\n')



