
import requests
from bs4 import BeautifulSoup

def request1():
	url = 'https://angel.co/companies'

	r = requests.get(url)	
	t = r.text
	#h = r.headers
	c = r.cookies['_angellist']

	soup = BeautifulSoup(t)
	for content in soup.find_all('meta'):
		if content.get('name') == "csrf-token":
			csrf = content.get('content')
	return c,csrf


