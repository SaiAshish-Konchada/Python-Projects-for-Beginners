import requests
from bs4 import BeautifulSoup as bs
import urllib.request

username = input("Enter GitHub Username: ")
github_profile = "https://github.com/" + username
req = requests.get(github_profile)
scraper = bs(req.content, "html.parser")
profile_picture = scraper.find("img", {"alt": "Avatar"})["src"]
path="D:\\"+username+".jpg"
urllib.request.urlretrieve(profile_picture,path)
print("The profile pic has been downloaded at: "+path)