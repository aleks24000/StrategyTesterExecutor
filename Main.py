import argparse
from StrategyTesterExecutor import StrategyTesterExecutor


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help='Strategy executor file argument')
    args = parser.parse_args()
    #print(f'Hello, {args.file}!')
    ste = StrategyTesterExecutor(args.file)
    #print(ste.f())
    ste.read_ini_file()
    ste.create_mt4_ini_file()
    ste.executeTester()
    ste.read_report()

if __name__ == "__main__":
    main()
