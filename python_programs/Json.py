import requests
import json

response= requests.get("http://newsapi.org/v2/everything?q=bitcoin&from=2020-08-08&sortBy=publishedAt&apiKey=7f151344fc4d420b9570773b11af7cd1").text
json_response = json.loads(response)

# print(json.dumps(json_response,indent=2))
for item in json_response['articles']:
    author=item['author']
    title=item['title']
    publishedAt=item['publishedAt']
    print(author,title,publishedAt )