import json

class ConfigurationLoader:
    def __init__(self, configFile: "path" = None):
        if configFile == None:
            self.configFile = "./configs/configuration.json"
        else:
            self.configFile = configFile
            
        self.lanuageFile = "./configs/strings.json"
        
        
    def openFile(self):
        """
        Load configuration file, if config file not found - load default configuration
        Load languages from 
        """
        try:
            with open(self.configFile, "r") as cfg:
                self.configFile = json.load(cfg)
                self.config = self.configFile["window"][0]
        except FileNotFoundError as e:
            exit(f"An error occured: {e}")

        
        try:
            with open(self.lanuageFile) as lang:
                self.stringsFile = json.load(lang)
        except FileNotFoundError as e:
            exit(f"An error occured: {e}")
        
        try:
            # load languages
            if self.config["language"] == "ENG":
                self.strings = self.stringsFile["ENG"][0]
            elif self.config["language"] == "POL":
                self.strings = self.stringsFile["POL"][0]

            # load dimens and colors
            self.colors = self.configFile["colors"][0]
            self.dimens = self.configFile["dimens"][0]
        except UnboundLocalError as e:
            exit(f"An error occured: {e}. There is config file but no strings.json file.")


    def configReturn(self):
        self.openFile()
        return self.config, self.strings, self.colors, self.dimens
        
        
if __name__ == "__main__":
    configLoader = ConfigurationLoader()
    configRead = configLoader.configReturn()
    


    
