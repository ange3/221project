import json, os


# Reads data from a JSON file into an array of elements each of which can be accessed like a map using the element's attributes
def load_data(filename):
  infile = open(filename, 'r')
  data = json.load(infile)
  infile.close()
  return data

def main(): 
  filenameReview = '../../CS_224W/comma_separated_dataset/yelp_academic_dataset_review_comma.json'
  reviewData = load_data(filenameReview)
  firstReview = reviewData[0]   #access single review element
  print 'SAMPLE: text of first review'
  print firstReview['text']   #access specific attribute of review
  print 'End of sample...'
  print 'Total number of reviews in dataset:', len(reviewData)

if __name__ == '__main__':
  main()
