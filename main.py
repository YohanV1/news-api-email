import requests
from send_email import send_email

api_key = "7cdcc677bfb94f5ebd98ef68029fb083"
topic = "mrbeast"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-01-05&sort" \
      "By=publishedAt&apiKey=7cdcc677bfb94f5ebd98ef68029fb083&language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

raw_message = ""

# Access the article titles and descriptions
for article in content["articles"][:10]:
      raw_message = raw_message + f"{article['title']}: " \
                                  f"\n{article['description']}" \
                                  f"\n{article['url']}\n\n\n"

message = f"""\
Subject: Today's News!

{raw_message}
"""

send_email(message.encode('utf-8'))

