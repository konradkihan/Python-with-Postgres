from MainMenu import MainMenu
from NewUser import NewUser
from UserInfo import ClientInfo
from RemoveUser import RemoveUser


if __name__ == "__main__":
    while True:
            mainMenu = MainMenu()
            # quit app via clicking X
            if mainMenu.optionValue == 0:
                exit()
            # add new user
            elif mainMenu.optionValue == 100:
                newUser = NewUser()
            # see through user list
            elif mainMenu.optionValue == 200:
                clientInfo = ClientInfo()
            elif mainMenu == 300:
                removeUser == RemoveUser()
