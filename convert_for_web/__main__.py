from parser import args_parser
from converter import Converter


def main():
    args = args_parser()
    if args:
        converter = Converter(args.path, args.extensions)
        converter.start()
    else:
        print('No args exit')


if __name__ == '__main__':
    main()
