from bs4 import BeautifulSou
import requests


response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
website = response.text
soup = BeautifulSoup(website, "html.parser")

content = soup.find_all(class_="jsx-4245974604")





