import csv
from amazon.api import AmazonAPI

keys = []
with open('../rootkey.csv', 'rb') as keysfile:
	spamreader = csv.reader(keysfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		keys.extend(row)

AMAZON_ACCESS_KEY = keys[0]
AMAZON_SECRET_KEY = keys[1]
AMAZON_ASSOC_TAG = keys[2]

amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)
book = amazon.lookup(ItemId='1602820120', IdType='ISBN', SearchIndex='Books')
print book