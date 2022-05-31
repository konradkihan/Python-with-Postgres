import tkinter as tk
import json

# custom
from ConfigLoader import ConfigurationLoader



class MainMenu:
    """
    Main menu of an app
    """
    def __init__(self):
        self.master = tk.Tk()
        
        # loading configuration from a file using configuration module
        # file returns respectivley config, strings, colors, dimens
        ConfLoad = ConfigurationLoader().configReturn()
        self.config = ConfLoad[0]
        self.strings = ConfLoad[1]
        self.colors = ConfLoad[2]
        self.dimens = ConfLoad[3]
        del ConfLoad    # delete whole configruation while it is loaded

        # option value for widet buttons
        self.optionValue = 0

        # initatie window configuration and widgets
        self.configuration()
        self.widgets()
        

    def configuration(self):
        """ Apply configuration to a window """
        # conf window geometry
        w = self.config['window_X']
        h = self.config['window_Y']
        # get screen width and height   
        ws = self.master.winfo_screenwidth() # width of the screen
        hs = self.master.winfo_screenheight() # height of the screen
        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        # set window geometry
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.master.resizable(bool(self.config["resizable_X"]), bool(self.config["resizable_Y"]))
        
        self.master.title(self.strings["app_title"])

        self.master.configure(background=self.colors["primary"])

        self.paddingY = self.dimens["pad_m"]
        self.button_width = self.dimens["width_l"]

        
        
    def widgets(self):
        """
        Generate widgets and mainloop the window
        """
        

        # add new client
        newClientBtn: Button = tk.Button(
            text=self.strings["cli_new"], 
            command=self.clientNew, 
            pady=self.paddingY, width=self.button_width)
        newClientBtn.pack(pady=self.paddingY)
        # show existing client's data
        showClientBtn: Button = tk.Button(
            text=self.strings["cli_data"], 
            command=self.clientShow,
            pady=self.paddingY, width=self.button_width)
        showClientBtn.pack(pady=self.paddingY)
        # remove existing client from database
        remClientBtn: Button = tk.Button(
            text=self.strings["cli_rem"], 
            command=self.clientRemove,
            pady=self.paddingY, width=self.button_width)
        remClientBtn.pack(pady=self.paddingY)

        # generate report
        genPltBtn: Button = tk.Button(
            text=self.strings["gen_plt"], 
            command=self.genPlt,
            pady=self.paddingY, width=self.button_width)
        genPltBtn.pack(pady=self.paddingY*4)

        # quit app
        quitAppBtn: Button = tk.Button(text=self.strings["quit_app"], command=self.quitApp)
        quitAppBtn.pack(pady=self.paddingY*3)

        # mainloop window
        self.master.mainloop()


    """
    Commands attached to button widgets
    """
    def clientNew(self):
        self.master.destroy()
        self.optionValue = 100
    
    def clientShow(self):
        self.master.destroy()
        self.optionValue = 200

    def clientRemove(self):
        self.master.destroy()
        self.optionValue = 300

    def genPlt(self):
        self.master.destroy()
        self.optionValue = 400


    def quitApp(self):
        self.master.destroy()
        exit()



if __name__ == "__main__":
    while True:
        mm = MainMenu()
        
        # quit app via clicking X
        if mm.optionValue == 0:
            exit()

        print(mm.optionValue)
