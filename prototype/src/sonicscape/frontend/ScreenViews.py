import arcade
import arcade.gui
from src.sonicscape.frontend.helpers import is_over
from src.sonicscape.database.db import create_user, verify_user

class SignInScreen(arcade.View):
    #Arcade View code for the Sign in screen for SonicScape      
    def __init__(self):
        super().__init__()
        
        #adds the logo.png to arcades sprite list with included positioning
        self.sprites = arcade.SpriteList()
        self.logo = arcade.Sprite("src/sonicscape/frontend/sonicscape_mark.png", scale=0.45)
        self.logo.center_x = self.window.width / 2
        self.logo.center_y = self.window.height / 2 + 80
        self.sprites.append(self.logo)
        
        
        #Creates an object based variable that holds text in the following format
        #String, horizontal position, vertical position, text color, font size, Which part of the string sits at x
        self.title = arcade.Text("Project SonicScape", self.window.width / 2, self.window.height /2 + 220, arcade.color.WHITE, 36, anchor_x="center")
        self.SignIn = arcade.Text("Sign In", self.window.width / 2, self.window.height / 2 - 150, arcade.color.WHITE, 20, anchor_x="center")
        self.CreateNewAccount = arcade.Text("Create New Account", self.window.width / 2, self.window.height / 2 - 200, arcade.color.WHITE, 20, anchor_x="center")
        
    #populates the screen with a background when class is called
    def on_show_view(self):
        self.window.background_color = arcade.color.BLACK

    #function for what happens on a mouse press
    def on_mouse_press(self, x, y, button, modifiers):
        if is_over(self.SignIn, x, y):
            self.window.show_view(LoginScreen())
        elif is_over(self.CreateNewAccount, x, y):
            self.window.show_view(NewAccountScreen())
            
    #function to highlight text the user is hovering over
    def on_mouse_motion(self, x, y, dx, dy):
        for label in (self.SignIn, self.CreateNewAccount):
            label.color = arcade.color.YELLOW if is_over(label, x, y) else arcade.color.WHITE
        
    #"draws" information on the screen constantly
    def on_draw(self):
        #wipes previous screen so new screen is not layered
        self.clear()
        
        #populates the screen with the previously built texts and sprite
        self.title.draw()
        self.CreateNewAccount.draw()
        self.SignIn.draw()
        self.sprites.draw() 
        
        
        
        
        
class LoginScreen(arcade.View):
    def __init__(self, window = None, background_color = None):
        super().__init__(window, background_color)
        self.manager = arcade.gui.UIManager()
        
        #creates screen title and back arrow
        self.title = arcade.Text("Sign In", self.window.width / 3 - 310, self.window.height -60, arcade.color.WHITE, 30, anchor_x="left")
        self.back = arcade.Text("<---", self.window.width / 2 + 420, self.window.height -25, arcade.color.WHITE, 20, anchor_x="left")
        
        #creates textbox that will aceppt user input for UserName and Password
        self.UserName_input = arcade.gui.UIInputText(width = 300, height = 40, font_size = 18, text_color = arcade.color.WHITE).with_border(color=arcade.color.WHITE, width = 2)
        self.Password_input = arcade.gui.UIInputText(width = 300, height = 40, font_size = 18, text_color = arcade.color.WHITE).with_border(color=arcade.color.WHITE, width = 2)
        #create button to allow user to submit both username and password
        self.confirm = arcade.Text("Confirm", self.window.width / 2, self.window.height / 2 - 200, arcade.color.WHITE, 22, anchor_x="center")
         #error message shown under Confirm when sign-in fails (empty until needed)
        self.error = arcade.Text("", self.window.width / 2, self.window.height / 2 - 250, arcade.color.RED, 16, anchor_x="center")
        #creates labels for each of the text fields
        layout = arcade.gui.UIBoxLayout(space_between = 20)
        layout.add(arcade.gui.UILabel(text = "Username", font_size = 18, text_color = arcade.color.WHITE))
        layout.add(self.UserName_input)
        layout.add(arcade.gui.UILabel(text = "Password", font_size = 18, text_color = arcade.color.WHITE))
        layout.add(self.Password_input)
        
        anchor = arcade.gui.UIAnchorLayout()
        anchor.add(layout, anchor_x="center_x", anchor_y="center_y")
        self.manager.add(anchor)
        
    
    #function that will enable keyboard and mouse handling for each box
    def on_show_view(self):
        self.manager.enable()
    #function that will disable keyboard and mouse handling for each box
    def on_hide_view(self):
        self.manager.disable()

    #function to highlight text the user is hovering over
    def on_mouse_motion(self, x, y, dx, dy):
        self.back.color = arcade.color.YELLOW if is_over(self.back, x, y) else arcade.color.WHITE
        self.confirm.color = arcade.color.YELLOW if is_over(self.confirm, x, y) else arcade.color.WHITE
            
    #function for what happens on a mouse press
    def on_mouse_press(self, x, y, button, modifiers):
        if is_over(self.back, x, y):
            self.window.show_view(SignInScreen())
        elif is_over(self.confirm, x, y):
            #saves users username and password when they click confirm
            username = self.UserName_input.text.strip()
            password = self.Password_input.text
            #checks the database; same message for a wrong username or a wrong password
            if verify_user(username, password):
                self.window.show_view(SonicScape_MainScreen())
            else:
                self.error.text = "Sign-in failed. Check your username and password."
                self.Password_input.text = ""
            # if (sql logic to confirm account login):
            #     self.window.show_view(SonicScape_MainScreen())

    #handles what happens when the screen is shown
    def on_draw(self):
        self.clear()
        self.title.draw()
        self.back.draw()
        self.manager.draw()
        self.confirm.draw()
        self.error.draw()
    
    
    

class NewAccountScreen(arcade.View):
    def __init__(self, window = None, background_color = None):
        super().__init__(window, background_color)
        self.manager = arcade.gui.UIManager()

        self.title = arcade.Text("Create An Account", self.window.width / 3 - 310, self.window.height - 60, arcade.color.WHITE, 30, anchor_x="left")
        self.back = arcade.Text("<---", self.window.width / 2 + 420, self.window.height -25, arcade.color.WHITE, 20, anchor_x="left")
        
        #creates textbox that will aceppt user input for UserName and Password
        self.UserName_input = arcade.gui.UIInputText(width = 300, height = 40, font_size = 18, text_color = arcade.color.WHITE).with_border(color=arcade.color.WHITE, width = 2)
        self.Password_input = arcade.gui.UIInputText(width = 300, height = 40, font_size = 18, text_color = arcade.color.WHITE).with_border(color=arcade.color.WHITE, width = 2)
        #create button to allow user to submit both username and password
        self.confirm = arcade.Text("Confirm", self.window.width / 2, self.window.height / 2 - 200, arcade.color.WHITE, 22, anchor_x="center")
         #error message shown under Confirm when sign-in fails (empty until needed)
        self.error = arcade.Text("", self.window.width / 2, self.window.height / 2 - 250, arcade.color.RED, 16, anchor_x="center")
        #creates labels for each of the text fields
        layout = arcade.gui.UIBoxLayout(space_between = 20)
        layout.add(arcade.gui.UILabel(text = "Username", font_size = 18, text_color = arcade.color.WHITE))
        layout.add(self.UserName_input)
        layout.add(arcade.gui.UILabel(text = "Password", font_size = 18, text_color = arcade.color.WHITE))
        layout.add(self.Password_input)
        
        anchor = arcade.gui.UIAnchorLayout()
        anchor.add(layout, anchor_x="center_x", anchor_y="center_y")
        self.manager.add(anchor)
        
    #function that will enable keyboard and mouse handling for each box
    def on_show_view(self):
        self.manager.enable()
    #function that will disable keyboard and mouse handling for each box
    def on_hide_view(self):
        self.manager.disable()

    #function to highlight text the user is hovering over
    def on_mouse_motion(self, x, y, dx, dy):
        self.back.color = arcade.color.YELLOW if is_over(self.back, x, y) else arcade.color.WHITE
        self.confirm.color = arcade.color.YELLOW if is_over(self.confirm, x, y) else arcade.color.WHITE
    
    #function for what happens on a mouse press
    def on_mouse_press(self, x, y, button, modifiers):
        if is_over(self.back, x, y):
            self.window.show_view(SignInScreen())
        elif is_over(self.confirm, x, y):
            #saves users username and password when they click confirm
            username = self.UserName_input.text.strip()
            password = self.Password_input.text
            #clear the text fields once they submit and move them onto the preference screen
            #saves the account; only move on if it was actually created
            if create_user(username, password):
                #clear the text fields once they submit and move them onto the preference screen
                self.UserName_input.text = ""
                self.Password_input.text = ""
                self.window.show_view(PreferenceScreen())
            else:
                self.error.text = "Username is taken or a field is empty."
    
    def on_draw(self):
        self.clear()
        self.title.draw()
        self.back.draw()
        self.manager.draw()
        self.confirm.draw()
         self.error.draw()
        
        
        
        
class PreferenceScreen(arcade.View):
    def __init__(self, window = None, background_color = None):
        super().__init__(window, background_color)
        self.manager = arcade.gui.UIManager()
        
        #creates screen title and screen use description
        self.title = arcade.Text("Preference Page", self.window.width / 3 - 310, self.window.height - 40, arcade.color.WHITE, 30, anchor_x="left")
        #create textbox for user prefernces
        self.Preference_input = arcade.gui.UIInputText(width = 300, height = 40, font_size = 18, text_color = arcade.color.WHITE).with_border(color=arcade.color.WHITE, width = 2)

        #create label for the preference input text field
        layout = arcade.gui.UIBoxLayout(space_between = 20)
        layout.add(arcade.gui.UILabel(text = "Welcome to SonicScape! Please provide some of your music taste prefernces! (Genres, Artists, and or Songs)", font_size = 13, text_color = arcade.color.WHITE))
        layout.add(self.Preference_input)
        
        anchor = arcade.gui.UIAnchorLayout()
        anchor.add(layout, anchor_x="center_x", anchor_y="center_y")
        self.manager.add(anchor)
        
    #function that will enable keyboard and mouse handling for each box
    def on_show_view(self):
        self.manager.enable()
    #function that will disable keyboard and mouse handling for each box
    def on_hide_view(self):
        self.manager.disable()

    #when a user hits enter save what is in the preference text box
    def on_key_press(self, key, modifiers):
        if key in (arcade.key.ENTER, arcade.key.NUM_ENTER):
            preferences = self.Preference_input.text
            self.window.show_view(SonicScape_MainScreen())
            
    #when screen is shown do...
    def on_draw(self):
        self.clear()
        self.title.draw()
        self.manager.draw()
        
        
        
        
class SonicScape_MainScreen(arcade.View):
    def __init__(self, window = None, background_color = None):
        super().__init__(window, background_color)
        
    def on_show_view(self):
        return super().on_show_view()
    
    def on_draw(self):
        self.clear()
