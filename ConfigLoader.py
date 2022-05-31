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
            # TODO set what to do if configruation.json is not found
            pass

        
        try:
            with open(self.lanuageFile) as lang:
                self.stringsFile = json.load(lang)
        except FileNotFoundError as e:
            # TODO set what to do if strings.json is not found
            pass
        
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
            # TODO Implement error than config was found but no strings file was found
            pass


    def configReturn(self):
        self.openFile()
        return self.config, self.strings, self.colors, self.dimens
            
    
    def loadDatabaseConfiguration(self):
        # TODO add database configuration
        pass
            
        
        
if __name__ == "__main__":
    configLoader = ConfigurationLoader()
    configRead = configLoader.configReturn()
    


    
