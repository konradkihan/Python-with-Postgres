import json

class ConfigurationLoader:
    def __init__(self, configFile: "path" = None):
        if configFile == None:
            self.configFile = "./configs/configuration.conf.json"
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
                self.config = json.load(cfg)["window"][0]
                print(self.config)
        except FileNotFoundError as e:
            pass
        except IOError as e:
            pass
        
        try:
            with open(self.lanuageFile) as lang:
                self.strings = json.load(lang)
                print(self.strings)
        except FileNotFoundError as e:
            pass
        except IOError as e:
            pass
        
        try:
            if self.config["language"] == "EN":
                self.strings = self.strings["ENG"][0]
            elif self.config["language"] == "POL":
                self.strings = self.strings["POL"][0]
        except UnboundLocalError as e:
            # TODO Implement error than config was found but no strings file was found
            pass


    def LoadWindowConfiguration(self):
        pass
            
    
    def LoadDatabaseConfiguration(self):
        pass
            
        
        
if __name__ == "__main__":
    configLoader = ConfigurationLoader()
    configRead = configLoader.openFile()

    
