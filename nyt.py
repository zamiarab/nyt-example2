import requests
import secrets

#gets stories from a particular section of NY Times
def get_stories(section):
    baseurl = 'https://api.nytimes.com/svc/topstories/vs/'
    extendedurl = baseurl + section + '.json'
    params={'api-key': secrets.nyt_key}
    return requests.get(extendedurl,params).json()

section = 'science'
stories = get_stories(section)
print(stories)
