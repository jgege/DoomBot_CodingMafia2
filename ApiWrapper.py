from ApiPlayer import ApiPlayer
from ApiPlayers import ApiPlayers
from ApiWorld import ApiWorld
import httplib

class ApiWrapper(object):
    def __init__(self, host):
        conn = httplib.HTTPConnection(host)
        self.player = ApiPlayer(conn)
        self.players = ApiPlayers(conn)
        self.world = ApiWorld(conn)
    