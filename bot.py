from Player import Player
from ApiWrapper import ApiWrapper

api = ApiWrapper("http://localhost:6001")
bot = Player(api)
bot.goToTheClosestDoor()