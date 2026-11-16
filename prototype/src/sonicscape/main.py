import arcade

from src.sonicscape.frontend.ScreenViews import SignInScreen

WIDTH, HEIGHT, TITLE = 960, 600, "SonicScape"

def main():
    window = arcade.Window(WIDTH, HEIGHT, TITLE)
    window.show_view(SignInScreen())
    arcade.run()
    
if __name__ == "__main__":
    main()