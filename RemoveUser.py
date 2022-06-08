import tkinter as tk
from ConfigLoader import ConfigurationLoader


class RemoveUser:
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
        userIdLabel = tk.Label(
            text=self.strings["cli_id"] + ": ", 
            pady=self.dimens["pad_l"], padx=self.dimens["pad_m"],
            background=self.colors["primary"])
        userIdLabel.grid(row=rowCount, column=0)

        self.userIdEntry = tk.Entry(borderwidth=self.dimens["pad_m"], relief=tk.FLAT)
        self.userIdEntry.grid(row=rowCount, column=1)

        rowCount +=1
        
        submitBtn = tk.Button(text=self.strings["confirm"], command=self.onSubmit, padx=self.dimens["pad_m"])
        submitBtn.grid(row=rowCount, column=0, sticky="nesw")

        rowCount +=1

        # SPACER
        tk.Label(text="", background=self.colors["primary"]).grid(row=rowCount, column=0)
        rowCount += 1

        # display confirm
        self.displayUserDataLabel = tk.Label(
            text="", 
            pady=self.dimens["pad_l"], padx=self.dimens["pad_m"],
            background=self.colors["primary"])
        self.displayUserDataLabel.grid(row=rowCount, column=1)

        rowCount += 1

        cancelBtn = tk.Button(text=self.strings["cancel"], command=self.onCancel)
        cancelBtn.grid(row=rowCount, column=0, sticky="nesw")

        self.master.mainloop()

    def onSubmit(self):
        self.userId = self.userIdEntry.get()
        self.displayUserDataLabel.configure(text="Deleted successfully")
        self.master.destroy()

    def onCancel(self):
        self.master.destroy()
        return -1



if __name__ == "__main__":
    RemoveUser()