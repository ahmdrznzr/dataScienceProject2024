from impl import Handler, MetadataUploadHandler, ProcessDataUploadHandler
import pandas as pd

hand = Handler()
print(hand.getDbPathOrUrl())
path = 'data/process.json'
hand.setDbPathOrUrl(path)
file = hand.getDbPathOrUrl()
print(file)

process = ProcessDataUploadHandler()

df = process.pushDataToDb(file)
print(df)

#df.to_csv('test.csv')(
