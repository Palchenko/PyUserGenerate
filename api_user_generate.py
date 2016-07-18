import json
import urllib
import requests

url_1 = "https://randomuser.me/api/"
url_2 = 'http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false'

class RandomUserData(object):
    data = {}

    def __init__(self):
        self.url_1 = URL_1
        self.url_2 = URL_2
        self.data = json.loads(urllib2.urlopen(URL_1))

    def get_name(self):
		first_name = self.data['results'][0]['name']['first']
		last_name = self.data['results'][0]['name']['last']
        return '{0} {1}'.format(first_name, last_name)

    def get_authorization(self):
    	login = self.data['results'][0]['login']['username']
    	password = self.data['results'][0]['login']['password']
        return '{0} {1}'.format(login, password)

    def get_gender(self):
        return self.data['results'][0]['gender']

    def get_email(self):
        return self.data['results'][0]['email']

    def get_postcode(self):
        return self.data['results'][0]['location']['postcode']

    def get_phone(self):
        return self.data['results'][0]['phone']        

    def get_location(self):
        street = self.data['results'][0]['location']['street']
        city = self.data['results'][0]['location']['city']
        state = self.data['results'][0]['location']['state']
        return '{0} ,{1}, {2}'.format(street, city, state)

        params = {'city': city, 'street': street, 'state': state}
		results = self.requests.get(URL_2, params=params).json()['results']
		location_lat = results[0]['geometry']['location']['lat']
		location_lng = results[0]['geometry']['location']['lng']
        return '{0} {1}'.format(location_lat, location_lng)
 
