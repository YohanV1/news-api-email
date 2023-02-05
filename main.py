import requests

api_key = "7cdcc677bfb94f5ebd98ef68029fb083"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-01-05&sort" \
      "By=publishedAt&apiKey=7cdcc677bfb94f5ebd98ef68029fb083"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and descriptions
for article in content["articles"]:
      print(article["title"])
      print(article["description"])
