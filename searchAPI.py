from flask import Flask
from flask_restful import Api, Resource, reqparse
app = Flask(__name__)
api = Api(app)
import requests
from bs4 import BeautifulSoup
class searchAlgo(Resource):
  def get(self,search):
    new_url = "https://www.google.com/search?psb=1&tbm=shop&authuser&q="+search+"&ved=0CAUQr4sDKAFqFwoTCNnkoPfCueoCFaIWCgMd8UULUBAC"
    page2 = requests.get(new_url)
    soup2 = BeautifulSoup(page2.content, 'html.parser')
    large_list = soup2.find_all("div", class_="rgHvZc")
    food_list = []
    for i in range(0, len(large_list)):
      intermediate_list = large_list[i].find_all("a")
      for entry in intermediate_list:
        food_list.append(entry.get_text())
    images = soup2.find_all("div", class_="oR27Gd")
    images_urls = []
    for i in range(0,len(images)):
      intermediate_list = images[i].find_all("img")
      for entry in intermediate_list:
        images_urls.append(entry['src'])
    searchResults = []
    for i in range(0,len(images)):
      try:
        searchResults.append({"product": food_list[i], "image": images_urls[i]})
      except IndexError:
        break
    return((searchResults))

api.add_resource(searchAlgo, "/searching", "/searching/", "/searching/<string:id>")

if __name__ == '__main__':
  app.run(debug=True)
