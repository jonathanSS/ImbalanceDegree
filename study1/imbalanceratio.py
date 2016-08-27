#==============================================
# Object to calculate the imbalance Degree
#==============================================
class ImbalanceRatio(object):

	def __init__(self, classDistribution):

		#Normalise the class distribution in the event of introducing the occurrences of the classes instead of the class distribution
		def normalisedDistribution(classDistribution):
			if sum(classDistribution) != 1.0:
				classDistribution = [i/ sum(classDistribution) for i in classDistribution]
			return classDistribution

		def balancedClassDistribution(k):
			return [1./k for i in range(k)]

		def imbalanceDegreeCalculator(classDistribution):
			if min(classDistribution) == 0.0:
				return float("inf")
			else:
				return 1.0*max(classDistribution)/min(classDistribution)

		self.numClasses = len(classDistribution)
		self.numMinorityClasses = sum(i < (1.0/self.numClasses) for i in normalisedDistribution(classDistribution))
		self.classDistribution = normalisedDistribution(classDistribution)
		self.balancedClassDistribution = [1.0/self.numClasses for i in range(self.numClasses)]
		self.value = imbalanceDegreeCalculator(classDistribution)
	
	def numClasses(self):
		return self.numClasses
	
	def numMinorityClasses(self):
		return self.numMinorityClasses


	def classDistribution(self):
		return self.classDistribution

	def balancedClassDistribution(self):
		return self.balancedClassDistribution


	def value(self):
		return self.value