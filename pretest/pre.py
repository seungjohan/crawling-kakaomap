import simplejson, requests
import sys

url = "https://dapi.kakao.com/v2/local/search/keyword.json?"
apikey = "5ab7c9f672a440cbe1fbb73e32668807"
query = "올리브영"

r = requests.get(url, params={'query': query}, headers={'Authorization': 'KakaoAK ' + apikey})
js = simplejson.JSONEncoder().encode(r.json())
r.json()