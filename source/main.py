

from . import tool
from . import constants as c
from .state import mainmenu, screen, level, title_screen

def main():
    game = tool.Control()
    state_dict = {c.TITLE: title_screen.TitleScreen(), 
                  c.MAIN_MENU: mainmenu.Menu(),
                  c.GAME_VICTORY: screen.GameVictoryScreen(),
                  c.GAME_LOSE: screen.GameLoseScreen(),
                  c.LEVEL: level.Level()}
    game.setup_states(state_dict, c.TITLE)
    game.main()
    """
    control.setup_states({
    c.TITLE_SCREEN: TitleScreen(),
    c.MAIN_MENU: MainMenu(),
    c.LEVEL: Level()
}, c.TITLE_SCREEN)  # or c.MAIN_MENU or whatever your starting screen is

    """