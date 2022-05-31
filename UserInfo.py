import tkinter as tk
from ConfigLoader import ConfigurationLoader


class ClientInfo:
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
        
        self.master.title(self.strings["app_title"] + " - " + self.strings["cli_data"])

        self.master.configure(background=self.colors["primary"])


    def widgets(self):
        # easier grid segmentation, intrement after finishing every row
        rowCount = 0 
        
        # input user ID to search in database
        userIdLabel: Label = tk.Label(
            text=self.strings["cli_id"] + ": ", 
            pady=self.dimens["pad_l"], padx=self.dimens["pad_m"],
            background=self.colors["primary"])
        userIdLabel.grid(row=rowCount, column=0)

        self.userIdEntry: Entry = tk.Entry(borderwidth=self.dimens["pad_m"], relief=tk.FLAT)
        self.userIdEntry.grid(row=rowCount, column=1)

        rowCount +=1
        
        submitBtn: Button = tk.Button(text=self.strings["search"], command=self.onSubmit, padx=self.dimens["pad_m"])
        submitBtn.grid(row=rowCount, column=0, sticky="nesw")

        rowCount +=1
        

        # SPACER
        spacer = tk.Label(text="", background=self.colors["primary"]).grid(row=rowCount, column=0)
        rowCount += 1

        # user info display
        self.displayUserDataLabel: Label = tk.Label(
            text="", 
            pady=self.dimens["pad_l"], padx=self.dimens["pad_m"],
            background=self.colors["primary"])
        self.displayUserDataLabel.grid(row=rowCount, column=0)

        rowCount += 1

        cancelBtn: Button = tk.Button(text=self.strings["cancel"], command=self.onCancel)
        cancelBtn.grid(row=rowCount, column=0, sticky="nesw")

        self.master.mainloop()

    def onSubmit(self):
        self.userIdEntry.get()
        print(self.userIdEntry.get())

    def onCancel(self):
        self.master.destroy()
        return -1

if __name__ == "__main__":
    ClientInfo()