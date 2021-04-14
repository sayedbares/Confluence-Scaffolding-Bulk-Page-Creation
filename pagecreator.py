import json
import random
import string
import progressbar
import requests
from requests.exceptions import HTTPError
from time import sleep

URL = input ("Enter your Confluence URL eg. (http://localhost:8090): ")
numberOfPages = input ("How many pages you want to create: ")
spaceKey = input ("Enter the Space Key: ")

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
def _url(path):
    return URL + path
def create_page(tp,title,key,body):
    payload = {"type":tp,"title":title,"space":{"key":key},"body":{"storage":{"value":body,"representation":"storage"}}}
    headers={"X-Atlassian-Token":"no-check","Content-Type":"application/json"}
    return requests.post(_url('/rest/api/content'),data=json.dumps(payload),auth=('admin','admin'),headers=headers)
def scaffolding_field_update(page_id,jsonData):
    headers={"Content-Type":"application/json"}
    return requests.put(_url('/rest/scaffolding/1.0/api/form/{:d}'.format(page_id)),data=json.dumps(jsonData),auth=('admin', 'admin'),headers=headers)

if __name__ == "__main__":
	pages=[]
	storageformat=open("ConfluenceStorageFormat.txt", 'r').read()
	print ("Creating Pages in Confluence")
	barPageCreation = progressbar.ProgressBar(maxval=int(numberOfPages), \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
	barPageCreation.start()
	for i in range (int(numberOfPages)):
		try:
		        resCreate = create_page("page","Page "+get_random_string(8),spaceKey,storageformat)
		except HTTPError as http_err:
		        print(f'HTTP error occurred: {http_err}')
		except Exception as err:
		        print(f'Other error occurred: {err}')
		else:
			barPageCreation.update(i+1)
			pages.append(json.loads(resCreate.text)['id'])
	barPageCreation.finish()

	jsonData=json.load(open("ScaffoldingJsonFile.txt", 'r'))
	print ("Updating Scaffolding Metadata")
	barLiveTemplateUpdate = progressbar.ProgressBar(maxval=int(numberOfPages), \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
	barLiveTemplateUpdate.start()

	for page in pages:
		try:
				resUpdateScaffolding =scaffolding_field_update(int(page),jsonData)
		except HTTPError as http_err:
				print(f'HTTP error occurred: {http_err}')
		except Exception as err:
		    	print(f'Other error occurred: {err}')
		else:
			    barLiveTemplateUpdate.update(i+1)
	barLiveTemplateUpdate.finish()