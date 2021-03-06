import requests
import os
import urllib.request
import xkcd
import tweepy
import swapi
from secrets import *
from random import randint

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
api = tweepy.API(auth)

opc = randint(1,6)

if(opc == 1):
	#films
	try:
		film = swapi.get_film(randint(1,7))
	except:
		film = swapi.get_film(1)
	tweet = "#StarWars\nFilm\nTitle: "+film.title+"\nDirector: "+film.director+"\nRelease Date: "+film.release_date+"\nOpening Crawl:"
	if(len(tweet) < 276):
		ocL = len(film.opening_crawl)
		tL = len(tweet)
		tot = ( ocL if ocL+tL <= 276 else 276-tL)
		tweet += film.opening_crawl[:tot] + "..."
elif(opc == 2):
	#people
	try:
		person = swapi.get_person(randint(1,87))
	except:
		person = swapi.get_person(1)
	home = person.get_homeworld()
	tweet = "#StarWars\nPerson\nName: "+person.name+"\nHeight: "+person.height+"\nMass: "+person.mass+"\nHair Color: "+person.hair_color+"\nSkin Color: "+person.skin_color+"\nEye Color: "+person.eye_color+"\nBirth Year: "+person.birth_year+"\nGender: "+person.gender+"\nHomeworld: "+home.name
elif(opc == 3):
	#planets
	try:
		planet = swapi.get_planet(randint(1, 61))
	except:
		planet = swapi.get_planet(1)
	tweet = "#StarWars\nPlanet\nName: " + planet.name+"\nRotation Period: "+planet.rotation_period+"\nOrbital Period: "+planet.orbital_period+"\nDiameter: "+planet.diameter+"\nClimate:"+planet.climate+"\nGravity: "+planet.gravity+"\nTerrain: "+planet.terrain+"\nSurface_water:" +planet.surface_water+"\nPopulation:" +planet.population
elif(opc == 4):
	#starships
	try:
		starship = swapi.get_starship(randint(1,37))
	except:
		starship = swapi.get_starship(10)
	tweet = "#StarWars\nStarship\nName: "+starship.name+"\nModel: "+starship.model+"\nManufacturer: "+starship.manufacturer+"\nMax Atmosphering Speed: "+starship.max_atmosphering_speed+"\nStarship Class: "+starship.starship_class+"\nCargo Capacity: "+starship.cargo_capacity
elif(opc == 5):
	#vehicles
	try:
		vehicle = swapi.get_vehicle(randint(1,39))
	except:
		vehicle = swapi.get_vehicle(14)
	tweet = "#StarWars\nVehicle\nName: "+vehicle.name+"\nModel :"+vehicle.model+"\nManufacturer :"+vehicle.manufacturer+"\nMax Atmosphering Speed: "+vehicle.max_atmosphering_speed+"\nVehicle Class: "+vehicle.vehicle_class+"\nCargo Capacity: "+vehicle.cargo_capacity

try:
	if(opc == 6):
		comic = xkcd.getRandomComic()
		url = comic.getImageLink() 
		tweet = "New Comic guys"
#		tweet_image(url, tweet)
		filename = 'temp.jpg'
		request = requests.get(url, stream=True)
		if request.status_code == 200:
			with open(filename, 'wb') as image:
				for chunk in request:
					image.write(chunk)
			api.update_with_media(filename, tweet)
			os.remove(filename)
		else:
			print("Unable to download image")
	else:
		api.update_status(tweet)
except:
	print("error")
	traceback.print_exc()
