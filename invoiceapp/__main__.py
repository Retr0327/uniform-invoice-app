import sys
from pathlib import Path
from src import APPParser, UniformInvoiceApp


path = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(path))


app_parser = APPParser()

parser = vars(app_parser.parse_args())

if parser.get("subcmd") == "start":
    print("Starting ...")
    UniformInvoiceApp().mainloop()
