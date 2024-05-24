import configparser
config = configparser.RawConfigParser()
config.read("D:\\NopCom\\Configrations\\config.ini")

class ReadConfig():
#for every variable in config.ini we need to create diffrent method

    @staticmethod #to access without creating object
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod  #to access without creating object
    def getUsernamil():
        username = config.get('common info','username')
        return username

    @staticmethod #to access without creating object
    def getPassword():
        password = config.get('common info','password')
        return password
