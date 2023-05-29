# Normal import because python and cyclic imports
import config.gamemodeconfig as gmc
from main import Player, RandomWordProvider
from .game import Game


class SingleplayerGame(Game):
    def __init__(self, config: gmc.GamemodeConfig):
        super().__init__(config)
        self.random = RandomWordProvider(lambda: self.config.get_value(gmc.GamemodeConfig.DICTIONARY_LOCATION))
        
        self.player = Player(self.random.get_word(), self.config.get_value(gmc.GamemodeConfig.NUMBER_LIVES))

    def run(self):
        while self.player.state == Player.State.PLAYING:
            self.player.turn()
            self.config.check_file_changes()
        match self.player.state:
            case Player.State.WON:
                print("YOU WIN!!!")
            case Player.State.DEAD:
                print(f"YOU LOST! The word was '{self.player.word}'")