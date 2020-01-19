import requests

# make an API call and store the response.

url = 'https://api.github.com/search/repositories?q=language:pyhton&sort=stars'
headers = {'accpet': 'application/n=vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'statuscode: {r.status_code}')