from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

users = {"madilin351":"hello2",}

class LoginPage(App):
    def build(self):
        return QuizManager()

class QuizManager(ScreenManager):
    pass

class LoginScreen(Screen):
    def create_account(self):
        self.manager.current = "create"
    def answer_question(self, text, text2):
        print(users)
        placeholder = False
        for key in users:
            if key == text and users[key] == text2:
                placeholder = True
            else:
                placeholder = False
        if placeholder:
            self.manager.current = "logout"
        else:
            self.ids.test.text = "Wrong Username or password"
            self.ids.test.font_size = 45
            self.ids.test.color = "orange"

class LogoutScreen(Screen):
    def logout(self):
        self.manager.current = "login"


class NewAccount(Screen):
    def runthing(self):
        self.ids.test.text = "Please follow the requirements"
        self.ids.test.font_size = 25
        self.ids.test.color = "orange"
    def password_check(self, username, password, password2):
        capital_letter = False
        lower_letter = False
        special_letter = False
        if password != password2:
            self.runthing()
        elif len(password)<8:
            self.runthing()
        elif " " in password:
            self.runthing()
        for letter in password:
            for letter2 in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                if capital_letter == True: break
                if letter == letter2:
                    capital_letter = True
                else:
                    capital_letter = False
            for letter2 in "abcdefghijklmnopqrstuvwxyz":
                if lower_letter == True: break
                if letter == letter2:
                    lower_letter = True
                else:
                    lower_letter = False
            for letter2 in "~!@#$%^&*()`_+-={}|[]\:<>?,./":
                if special_letter == True: break
                if letter == letter2:
                    special_letter = True
                else:
                    special_letter = False
        if special_letter != True:
            self.runthing()
        elif lower_letter != True:
            self.runthing()
        elif capital_letter != True:
            self.runthing()
        users[username] = password
        self.manager.current = "login"
        





LoginPage().run()