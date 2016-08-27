import math


#==============================================
# Measures complementing the Imbalance Degree
#==============================================
#Manhattan (or taxi-cab) distance 
def MANHATTAN_DISTANCE(multinomialDistribution):
	value = 0.0
	for parameter in multinomialDistribution:
		value += math.fabs(parameter - 1.0/len(multinomialDistribution))
	return value

#Euclidean distance
def EUCLIDEAN_DISTANCE(multinomialDistribution):
	value = 0.0
	for parameter in multinomialDistribution:
		value += (parameter - 1.0/len(multinomialDistribution))**2
	return math.sqrt(value)

#Chebyshev distance
def CHEBYSHEV_DISTANCE(multinomialDistribution):
	values = []
	for parameter in multinomialDistribution:
		values.append(math.fabs(parameter - 1.0/len(multinomialDistribution)))
	return max(values)

#Kullback-Leibler divergence
def KULLBACKLEIBLER_DIVERGENCE(multinomialDistribution):
	value = 0.0
	for parameter in multinomialDistribution:
		if parameter == 0.0:
			value += 0.0
		else:
			value += parameter*math.log(len(multinomialDistribution)*parameter,2)
	return value

#Helliger or Bhattacharyya distance
def HELLIGER_DISTANCE(multinomialDistribution):
	value = 0.0
	for parameter in multinomialDistribution:
		value += (math.sqrt(parameter) - math.sqrt(1.0/len(multinomialDistribution)))**2
	return 1./math.sqrt(2)*math.sqrt(value)

#Total Variation distance
def TOTALVARIATION_DISTANCE(multinomialDistribution):
	value = 0.0
	for parameter in multinomialDistribution:
		value += math.fabs(parameter - 1.0/len(multinomialDistribution))
	return 0.5*value

#Chi-square divergence
def CHISQUARE_DIVERGENCE(multinomialDistribution):
	value = 0.0
	for parameter in multinomialDistribution:
		value += (parameter - 1.0/len(multinomialDistribution))**2
	return len(multinomialDistribution)*value

#==============================================
# Object to calculate the imbalance Degree
#==============================================
class ImbalanceDegree(object):

	def __init__(self, classDistribution, complementMeasure = 'EUCLIDEAN_DISTANCE'):

		#Normalise the class distribution in the event of introducing the occurrences of the classes instead of the class distribution
		def normalisedDistribution(classDistribution):
			if sum(classDistribution) != 1.0:
				classDistribution = [1.0*i/ sum(classDistribution) for i in classDistribution]
			return classDistribution

		def balancedClassDistribution(k):
			return [1./k for i in range(k)]

		def distributionlowestEntropy(m,k):
			if m == 0:
				return balancedClassDistribution(k)
			else:
				distribution = [1.0 - (k - m - 1)*1./k]
				distribution.extend([0.0 for i in range(m)])
				distribution.extend([1./k for i in range(k - m - 1)])
				return distribution

		def applyComplementMeasure(complementMeasure,args):
			return eval(complementMeasure)(args[:])

		def imbalanceDegreeCalculator(numClasses,numMinorityClasses,complementMeasure,classDistribution,balancedClassDistribution,lowestEntropyClassDistribution):
			if set(lowestEntropyClassDistribution) == set(balancedClassDistribution):
				return 0.0
			else:
				return (numMinorityClasses - 1 + applyComplementMeasure(complementMeasure,classDistribution)/applyComplementMeasure(complementMeasure,lowestEntropyClassDistribution))

		self.numClasses = len(classDistribution)
		self.numMinorityClasses = sum(i < (1.0/self.numClasses) for i in normalisedDistribution(classDistribution))
		self.complementMeasure = complementMeasure
		self.classDistribution = normalisedDistribution(classDistribution)
		self.balancedClassDistribution = [1.0/self.numClasses for i in range(self.numClasses)]
		self.lowestEntropyClassDistribution = distributionlowestEntropy(self.numMinorityClasses,self.numClasses)
		self.value = imbalanceDegreeCalculator(self.numClasses,self.numMinorityClasses,complementMeasure,self.classDistribution,self.balancedClassDistribution,self.lowestEntropyClassDistribution)
	
	def numClasses(self):
		return self.numClasses
	
	def numMinorityClasses(self):
		return self.numMinorityClasses

	def complementMeasure(self):
		return str(complementMeasure)

	def classDistribution(self):
		return self.classDistribution

	def balancedClassDistribution(self):
		return self.balancedClassDistribution

	def lowestEntropyClassDistribution(self):
		return self.lowestEntropyClassDistribution

	def value(self):
		return self.value



