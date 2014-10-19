import util
from util import *

def extractWordFeatures(x):
    """
    Extract word features for a string x.
    @param string x: 
    @return dict: feature vector representation of x.
    Example: "I am what I am" --> {'I': 2, 'am': 2, 'what': 1}
    """
    dict = {}
    words = x.split()
    for w in words:
        if w not in dict:
            dict[w] = 0
        dict[w] = dict[w]+1
    return dict


# Using stochastic gradient descent
def learnPredictor(trainExamples, testExamples, featureExtractor):
    '''
    Given |trainExamples| and |testExamples| (each one is a list of (x,y)
    pairs), a |featureExtractor| to apply to x, and the number of iterations to
    train |numIters|, return the weight vector (sparse feature vector) learned.

    You should implement stochastic gradient descent.

    Note: call evaluatePredictor() on both trainExamples and testExamples
    to see how you're doing as you learn after each iteration.
    '''

    weights = {}  # feature => weight
    stepSize = 1
    numIters = 15 
    for it in range(0, numIters):
        # iterate through every training example and extract the features of x
        for x, y in trainExamples:
            phi = featureExtractor(x)
            # print phi
            # if y * score < 1 (wrong prediction) then calculate gradient loss then update weight for each feature
            margin = y*util.dotProduct(weights, phi)
            if (1-margin) > 0:
                indicator = 1
            else:
                indicator = 0
            scale = stepSize*indicator*y
            increment(weights, scale, phi)  

        # this uses the defined feature extractor to predict the classification of x
        def predictor(x):
            phi = featureExtractor(x)
            # create thresholds for different scores
            score = dotProduct(phi, weights)
            # return 1 if (dotProduct(phi, weights) > 0) else -1

        # Print out training and test error for every iteration:
        # print 'TRAINING ERROR:', util.evaluatePredictor(trainExamples, predictor)
        # print 'TEST ERROR:', util.evaluatePredictor(testExamples, predictor)
    return weights

# Run
trainReviews = util.readExamples('reviews.train')
testReviews = util.readExamples('reviews.dev')
featureExtractor = extractWordFeatures
weights = learnPredictor(trainReviews, testReviews, featureExtractor)

print 'output weights:', weights