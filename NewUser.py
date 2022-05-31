import tkinter as tk
import json

# custom
from ConfigLoader import ConfigurationLoader


class NewUser:
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
        
        self.master.title(self.strings["app_title"] + " - " + self.strings["cli_new"])

        self.master.configure(background=self.colors["primary"])


    def widgets(self):
        # easier grid segmentation, intrement after finishing every row
        rowCount = 0
        # new user name label+entry
        userNameLabel: Label = tk.Label(
            text=self.strings["cli_name"] + ": ", 
            pady=self.dimens["pad_l"], padx=self.dimens["pad_m"],
            background=self.colors["primary"])
        userNameLabel.grid(row=rowCount, column=0)

        self.newNameEntry: Entry = tk.Entry(borderwidth=self.dimens["pad_m"], relief=tk.FLAT)
        self.newNameEntry.grid(row=rowCount, column=1)

        rowCount += 1

        # new user surname label+entry
        newSurnameLabel: Label = tk.Label(
            text=self.strings["cli_surname"] + ": ", 
            pady=self.dimens["pad_l"], padx=self.dimens["pad_m"],
            background=self.colors["primary"])
        newSurnameLabel.grid(row=rowCount, column=0)

        self.newSurnameEntry: Entry = tk.Entry(borderwidth=self.dimens["pad_m"], relief=tk.FLAT)
        self.newSurnameEntry.grid(row=rowCount, column=1)

        rowCount += 1

        # SPACER
        spacer = tk.Label(text="", background=self.colors["primary"]).grid(row=rowCount, column=0)
        rowCount += 1

        # new user address label+entry
        newAddressLabel: Label = tk.Label(
            text=self.strings["cli_addr"] + " 1/2" + ": ", 
            pady=self.dimens["pad_l"], padx=self.dimens["pad_m"],
            background=self.colors["primary"])
        newAddressLabel.grid(row=rowCount, column=0)

        self.newAddressEntry: Entry = tk.Entry(borderwidth=self.dimens["pad_m"], relief=tk.FLAT, width=30)
        self.newAddressEntry.grid(row=rowCount, column=1)

        rowCount += 1

        newAddressLabel2: Label = tk.Label(
            text=self.strings["cli_addr"] + " 2/2" + ": ", 
            pady=self.dimens["pad_l"], padx=self.dimens["pad_m"],
            background=self.colors["primary"])
        newAddressLabel2.grid(row=rowCount, column=0)

        self.newAddressEntry2: Entry = tk.Entry(borderwidth=self.dimens["pad_m"], relief=tk.FLAT, width=30)
        self.newAddressEntry2.grid(row=rowCount, column=1)

        rowCount += 1

        # SPACER
        spacer = tk.Label(text="", background=self.colors["primary"]).grid(row=rowCount, column=0, columnspan=2)
        rowCount += 1

        # buttons section
        cancelBtn: Button = tk.Button(text=self.strings["cancel"], command=self.onCancel)
        cancelBtn.grid(row=rowCount, column=0, sticky="nesw")
        submitBtn: Button = tk.Button(text=self.strings["submit"], command=self.onSubmit)
        submitBtn.grid(row=rowCount, column=1, sticky="nesw")


        self.master.mainloop()


    def onSubmit(self):
        self.newUserData: tuple = (
            self.newNameEntry.get(),
            self.newSurnameEntry.get(),
            self.newAddressEntry.get(),
            self.newAddressEntry2.get()
        )
        self.master.destroy()
        
    def onCancel(self):
        self.master.destroy()
        return -1

if __name__ == "__main__":
    mm = NewUser()

    