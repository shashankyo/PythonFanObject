from abc import abstractmethod
class Player:
    @abstractmethod
    def play(self):
        pass
class CricketPlayer(Player):
    def play(self):
        print("Cricket player play cricket")
class FootBallPlayer(Player):
    def play(self):
        print("Football player play football")
class TennisPlay(Player):
    def play(self):
        print("Tennis player play tennis")
def main():
    c = CricketPlayer()
    c.play()
    f = FootBallPlayer()
    f.play()
    t = TennisPlay()
    t.play()
main()