import psycopg2
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
# importing google_images_download module 
from google_images_download import google_images_download 
## pip install git+https://github.com/Joeclinton1/google-images-download.git
## use this instead as google's isn't working correctly
# creating object 
response = google_images_download.googleimagesdownload() 
url = 'https://greekgodsandgoddesses.net/'
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
names = soup.find_all("h3")
text = soup.find_all("p")
# print(soup.get_text())
for name in range(len(names)):
	print(names[name].string)


#print(text[4].string)
parents = re.search(r'\b(the son of)\b', text[4].string)
parentsText = parents.group()
if (parents):
	print('yes')
	print(parentsText)
else: 
	print('no')
# for paragraphs in range(len(text)):
# 	if len(text[paragraphs]) < 5:
# 		print(text[3].string)

# print(html)
# pattern = "<h3.*? *?>. *?</h3.*?>"
# results = re.search(pattern, html, re.IGNORECASE)
# names = results.group()
# names = re.sub("<.*?>", "", names) # removes tags
# print(names)
# start_index = html.find('<h3>') + len('<title>')
# end_index = html.find('</h3>')
# names = html[start_index:end_index]
# print(names)
search_queries = [  ## name + origin + Mythology
  'Prometheus',
  'Apollo',
	'Ares',
	'Dionysus',
	'Hades',
	'Hephaestus',
	'Hermes',
	'Poseidon',
	'Zeus',
	'Aphrodite',
	'Artemis',
	'Hera',
	'Hestia',
	'Tyche', 
] 

# connection = psycopg2.connect(
# 	host="localhost",
# 	database="mythAPI"
# 	user="postgres",
# 	password='1199',
# )

# connection.autocommit = True

def downloadimages(query): 
	# keywords is the search query 
	# format is the image file format 
	# limit is the number of images to be downloaded 
	# print urs is to print the image file url 
	# size is the image size which can 
	# be specified manually ("large, medium, icon") 
	# aspect ratio denotes the height width ratio 
	# of images to download. ("tall, square, wide, panoramic") 
	arguments = {"keywords": query, 
				"format": "jpg", 
				"limit":3, 
				"print_urls":True, 
				"exact_size": "640, 480",
        } 
				# "aspect_ratio":"panoramic"} 
	try: 
		response.download(arguments) 
	
	# Handling File NotFound Error	 
	except FileNotFoundError: 
		arguments = {"keywords": query, 
					"format": "jpg", 
					"limit":2, 
					"print_urls":True, 
					"size": "medium"} 
					
		# Providing arguments for the searched query 
		try: 
			# Downloading the photos based 
			# on the given arguments 
			response.download(arguments) 
		except: 
			pass

# Driver Code 
for query in search_queries: 
	downloadimages(query + " Greek Mythology Statue") 
	print() 
