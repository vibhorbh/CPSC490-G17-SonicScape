import arcade

from src.sonicscape.frontend.ScreenViews import SignInScreen
from src.sonicscape.database.db import init_db

WIDTH, HEIGHT, TITLE = 960, 600, "SonicScape"

def main():
    window = arcade.Window(WIDTH, HEIGHT, TITLE)
    init_db()   #creates user table if it doesnt exist.
    window.show_view(SignInScreen())
    arcade.run()
    
if __name__ == "__main__":
    main()
