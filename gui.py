import tkinter as tk
import json

# custom
from set_configs import ConfigurationLoader



class MainMenu:
    """
    Main menu of an app - 
    """
    def __init__(self):
        self.master = tk.Tk()

        self.conf = ConfigurationLoader()

        self.configuration()
        self.widgets()
        


    def configration():
        # TODO load configs
        self.root.size(windowSize)
        self.master.resizable(isResizable, isResizable)
        self.master.title(title)
        
        
    def widgets(self):
        pass
