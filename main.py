from MainMenu import MainMenu
from NewUser import NewUser
from ClientInfo import GetClientId, ClientInfoShow
from RemoveUser import RemoveUser
from DatabaseManager import DatabaseConnect


if __name__ == "__main__":
    databaseConnect = DatabaseConnect()
    while True:
            mainMenu = MainMenu()
            # quit app via clicking X
            if mainMenu.optionValue == 0:
                exit()
            # add new user
            elif mainMenu.optionValue == 100:
                newUser = NewUser()
                # getting user data from form
                # fomrat: dict(name: str, surname: str, address1: str, address2: str)
                newUserData: dict = newUser.newUserData
                databaseConnect.insert_into_client(newUserData["name"],
                                                   newUserData["surname"],
                                                   newUserData["address1"]+newUserData["address2"])
            # see through user list
            elif mainMenu.optionValue == 200:
                while True:
                    clientId = GetClientId().userId
                    clientInfo = databaseConnect.select_customer(clientId)
                    if not ClientInfoShow(clientInfo).doContinue:
                        break


            elif mainMenu == 300:
                removeUser = RemoveUser()
            else:
                exit(69)
