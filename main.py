import requests
from send_email import send_email

api_key = "7cdcc677bfb94f5ebd98ef68029fb083"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-01-05&sort" \
      "By=publishedAt&apiKey=7cdcc677bfb94f5ebd98ef68029fb083"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

raw_message = ""

# Access the article titles and descriptions
for article in content["articles"]:
      raw_message = raw_message + f"{article['title']}:\n" \
                          f"{article['description']}\n\n\n"

message = f"""\
Subject: Today's News!

{raw_message}
"""

print(type(message))
send_email(message.encode('utf-8'))
print("Email was sent successfully!")

