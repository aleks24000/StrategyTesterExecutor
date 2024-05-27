import argparse
from StrategyTesterExecutor import StrategyTesterExecutor


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help='Strategy executor file argument')
    parser.add_argument('--exepath', help='MT4 path')
    args = parser.parse_args()
    #print(f'Hello, {args.exepath}!')
    ste = StrategyTesterExecutor(args.file, args.exepath)
    #print(ste.f())
    ste.read_ini_file()
    ste.exec_all()
    #ste.parse_all_ini_and_exec()
    #ste.create_preset(None)
    #ste.create_mt4_ini_file()
    #ste.executeTester()
    #ste.read_report()

if __name__ == "__main__":
    main()
