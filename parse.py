import requests
from bs4 import BeautifulSoup

# Find author in HTML, or return None if not found
def parse_author(html):
	author_tag = html.find('meta', attrs={'name': 'author'})
	if author_tag:
		author = author_tag.get('content')
		return author

# Find title in HTML, or return None if not found
def parse_title(html):
	title_tag = html.find('meta', attrs={'property': 'og:title'})
	if title_tag:
		title = title_tag.get('content')
		return title

def parse_url(url):
	resp = requests.get(url)
	html = BeautifulSoup(resp.text, features='html5lib')

	# Store source information in dictionary
	source = {}
	source['Author'] = parse_author(html)
	source['Title'] = parse_title(html)

	# Iterate and print all source information
	for elem in source:
		if source[elem]:
			print('{}:'.format(elem), source[elem])
		else:
			# Handle missing information
			print('{} not found'.format(elem))

url = input('Enter a URL: ')
parse_url(url)