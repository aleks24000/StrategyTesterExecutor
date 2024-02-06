import configparser
import os
import csv


class StrategyTesterExecutor:

    def __init__(self, argfile):
        self.argfile = argfile
        self.symbols = 'EURUSD'
        self.mt4path = "/home/alex/work/FXCMMetaTrader4"

    def f(self):
        return 'hello world'

    def read_ini_file(self):
        config = configparser.ConfigParser()
        config.sections()
        config.read(self.argfile)
        self.symbols = config['symbols']['symbol'].split()
        print(self.symbols)

    def create_mt4_ini_file(self):
        config = configparser.ConfigParser()
        config.optionxform = str
        config.read('./ini/styt.ini')
        config['dummy']['TestSymbol'] = 'EURUSD'
        with open(self.mt4path+'/curmt4.ini', 'w') as configfile:
            config.write(configfile, space_around_delimiters=False)

    def executeTester(self):
        os.system('cd '+self.mt4path+'  && rm curreport* && wine terminal.exe curmt4.ini')

    def read_report(self):
        with open(self.mt4path+'/curreport.html', encoding='latin-1') as htmlreport:
            lines = [line for line in htmlreport]
        print(lines)

        with open('fullreport.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar=',', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])