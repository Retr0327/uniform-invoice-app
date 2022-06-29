from pathlib import Path

pkg_path = Path(__file__).resolve().parent.parent.parent
DB_PATH = pkg_path / ".db" / "invoice.db"

