import urllib
import requests
import json
from requests.auth import HTTPBasicAuth

API_KEY = "BingSearchAPIWebResult"

def bing_search(query, source_type = "Web", top = 5, format = 'json'):
	query = '%27' + urllib.parse.quote(query) + '%27'
	base_url = 'https://api.datamarket.azure.com/Bing/SearchWeb/v1/' + source_type
	url = base_url + '?Query=' + query + '&$top=' + str(top) + '&$format=' + format

	user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"
	auth = HTTPBasicAuth(API_KEY, API_KEY)
	headers = {'User-Agent': user_agent}

	response_data = requests.get(url, headers = headers, auth = auth)
	json_result = response_data.json()

	return json_result