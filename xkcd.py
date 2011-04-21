import urllib
from BeautifulSoup import BeautifulSoup
import random, math

base_url = 'http://xkcd.com/'

def get_comic():


	data = urllib.urlopen(base_url)
	bs = BeautifulSoup(data)


	comic_scoop =  bs.findAll('img')[1]['title']
	comic_link = bs.findAll('img')[1]['src']
	
	return {'title':comic_scoop,'src':comic_link}


# Getting a Random Comic

def get_random_comic():

	comic = int(random.random()*1000)
	if comic > 888:
		# Currently xkcd features 888 Comics.
		comic -= 888
		random_url = base_url + str(comic) + '/'
	else:
		random_url = base_url + str(comic) + '/'

	random_data = urllib.urlopen(random_url)
	random_bs = BeautifulSoup(random_data)


	random_scoop =  random_bs.findAll('img')[1]['title']

	random_link = random_bs.findAll('img')[1]['src']
	
	return {'title':random_scoop,'src':random_link}



   
