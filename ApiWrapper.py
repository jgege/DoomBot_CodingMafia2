from ApiPlayer import ApiPlayer
from ApiPlayers import ApiPlayers
from ApiWorld import ApiWorld

class ApiWrapper(object):
    def __init__(self, host):
        self.player = ApiPlayer(host)
        self.players = ApiPlayers(host)
        self.world = ApiWorld(host)
    