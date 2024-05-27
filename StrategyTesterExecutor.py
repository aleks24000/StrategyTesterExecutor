import configparser
import os
import csv
from itertools import combinations,permutations
from itertools import product


class StrategyTesterExecutor:

    def __init__(self, argfile, argexepath):
        self.argfile = argfile
        self.symbols = 'EURUSD'
        self.otherkeys = 'keys'
        self.othervalues = 'values'
        self.othervaluesmap = []

        self.mt4path = argexepath

    def f(self):
        return 'hello world'

    def read_ini_file(self):
        config = configparser.ConfigParser()
        config.optionxform = str
        config.sections()
        config.read(self.argfile)
        self.symbols = config['symbols']['symbol'].split()
        self.otherkeys = list(config['others'].keys())
        self.othervalues = list(config['others'].values())
        #transform to map
        for e in (self.othervalues):
            self.othervaluesmap.append(e.split())

        print(self.otherkeys)
        print(self.othervalues)
        print(self.othervaluesmap)
        print(self.symbols)

    def exec_all(self):
        # init csv report file
        with open(self.mt4path + '/fullreport.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=';',
                                    quotechar=',', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['Total Trades', 'Profit', 'Profit brut', 'Perte brute', 'Chute', 'Keys', 'Values', 'Symbol'])

        for sym in self.symbols:
            self.parse_all_ini_and_exec(sym)

    def parse_all_ini_and_exec(self, symbol):

        #parse symbols
        # create empty list to store the
        # combinations
        unique_combinations = []
        elementlist=[]
        for element in product(*self.othervaluesmap):
            elementlist.append(element)
            print(symbol)
            print(element)

        #idx=0
        #for e in product(self.othervalues[0].split(), repeat=len(self.otherkeys)):
            idx=0
            #for sube in e:
            #    print(self.otherkeys[idx])
            #    print(sube)
            #    idx=idx+1
            # create ini file
            #self.create_mt4_ini_file(e)
            # create preset
            self.create_preset(element)
            self.create_mt4_ini_file(symbol)
            self.executeTester()
            self.read_report(symbol, element)

    def create_preset(self, valuestab):
        config = configparser.RawConfigParser()
        config.optionxform = str
        config.read('./presets/FTD_v1.set')
        #config['dummy']['TestSymbol'] = 'EURUSD'

        #f = open(self.mt4path + '/MQL4/tester/FTD_v1.set', "w")
        #for each_section in config.sections():
        #    for (each_key, each_val) in config.items(each_section):
        #        f.write(each_key+"="+each_val+"\n")
        #f.close()
        idx = 0
        for val in valuestab:
            config['dummy'][self.otherkeys[idx]] = val
            idx=idx+1

        with open(self.mt4path + '/tester/FTD_v1.set', 'w') as configfile:
            config.write(configfile, space_around_delimiters=False)


    def create_mt4_ini_file(self, symbol):
        config = configparser.ConfigParser()
        config.optionxform = str
        config.read('./ini/styt.ini')
        config['dummy']['TestSymbol'] = symbol

        with open(self.mt4path+'/curmt4.ini', 'w') as configfile:
            config.write(configfile, space_around_delimiters=False)

    def executeTester(self):
        os.system('cd '+self.mt4path+' ; rm curreport* ; wine terminal.exe curmt4.ini')

    def read_report(self, symbol, valuestab):
        with open(self.mt4path+'/curreport.html', encoding='latin-1') as htmlreport:
            #lines = [line for line in htmlreport]
            profit='';
            profitbrut=''
            pertebrute=''
            chute=''
            totaltrades=''
            for line in htmlreport:
                if(line.__contains__('Profit total net')):
                    id1=line.index('Profit total net')+37
                    id2=line.index('td',id1)-2
                    profit=line[id1:id2]
                    id3=line.index('Profit brut')+32
                    id4=line.index('td',id3)-2
                    profitbrut=line[id3:id4]
                    id5 = line.index('Perte brute') + 32
                    id6 = line.index('td', id5) - 2
                    pertebrute = line[id5:id6]
                    #print(line[id1,id2])
                if (line.__contains__('Chute maximale')):
                    id7 = line.index('Chute maximale') + 35
                    id8 = line.index('td', id7) - 2
                    chute = line[id7:id8]
                if (line.__contains__('Total des Trades')):
                    id9 = line.index('Total des Trades') + 37
                    id10 = line.index('td', id9) - 2
                    totaltrades = line[id9:id10]
                    break

        with open(self.mt4path+'/fullreport.csv', 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=';',
                                    quotechar=',', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([totaltrades, profit, profitbrut, pertebrute, chute, self.otherkeys, valuestab, symbol])