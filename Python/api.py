import requests
import json

# ENDPOINT to reach top headlines based on counrty
# Fill in country code and Api key
# Sample URL - 'https://newsapi.org/v2/top-headlines?country=us&apiKey=df26ff21b2ff4781b55ecf507e3d6c6a'
# Check out https://newsapi.org/docs/endpoints/top-headlines for more details - same as discussed in class

api_key='59e155c501ab4b63aed74766e3bc9720'

country_code=input('enter the country code:')
c=input('select the category\n1.Business\n2.Entertainment\n3.General\n4.Health\n5.Sports\n6.Tech')

category={'1':'business','2':'entertainment','3':'general','4':'health','5':'sports','6':'technology'}

url = 'https://newsapi.org/v2/top-headlines?country='+country_code+'&category='+category[c]+'&apiKey='+api_key


res = requests.get(url)

if res.status_code == 200:     #Checking if api call is successful
    # Getting data out of response
    data = res.text
    
    #Convert json data to python dict
    data_py = json.loads(data)

    # Parsing source, author, Title and content of each article and formatting with multiline f-strings 
    for article in data_py['articles']:
        news = (f'Source - {article["source"]["name"]}\n'
                f'Author - {article["author"]}\n'
                f'Title:\n{article["title"]}\n'
                f'Content:\n{article["content"]}')
        print(news+'\n\n')
        
