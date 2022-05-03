import argparse


class APPParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog="Uniform Invoice app",
            description="Manage Uniform Invoice app Log",
        )

        self.subparser = self.parser.add_subparsers(
            dest="subcmd", help="description", metavar="Actions", required=True
        )

        self.add_start_parser()

    def add_start_parser(self):
        start = self.subparser.add_parser("start", help="Start app service")
        start.add_argument(dest="start", action="store_true", help="Start app service")

    def parse_args(self):
        return self.parser.parse_args()


if __name__ == "__main__":
    app_parser = APPParser()
    res = app_parser.parse_args()
    print(res)
