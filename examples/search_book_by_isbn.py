import csv
import json
from amazon.api import AmazonAPI
from pprint import pprint

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

keys = []
with open('../rootkey.csv', 'r') as keysfile:
    spamreader = csv.reader(keysfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        keys.extend(row)

AMAZON_ACCESS_KEY = keys[0]
AMAZON_SECRET_KEY = keys[1]
AMAZON_ASSOC_TAG = keys[2]

amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)

#to json
data = []
with open('ff-books.json') as data_file:    
    ff_books = json.load(data_file)
    for book in ff_books:
        if(book['isbn']):
            try:
                isbn = book['isbn']
                item = amazon.lookup(ItemId=isbn, IdType='ISBN', SearchIndex='Books')
                item_link = ''
                if(type(item) is list):
                        item_link = item[0].detail_page_url
                else:
                        item_link = item.detail_page_url
                        
                i = {}
                i['title'] = book['title']
                i['author'] = book['author']
                i['link'] = book['link']
                i['amazon'] = item_link
                data.append(i)
            except Exception:
                pass
                
writeToJSONFile('./','amazon',data)
