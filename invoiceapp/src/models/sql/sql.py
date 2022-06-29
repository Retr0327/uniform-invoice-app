INVOICE = (
    "CREATE TABLE invoice ("
    "id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
    "month TEXT NOT NULL,"
    "year TEXT NOT NULL"
    ");"
)

PRIZE = (
    "CREATE TABLE prize ("
    "id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
    "invoice_id INTEGER NOT NULL,"
    "type_id INTEGER NOT NULL,"
    "prize TEXT NOT NULL,"
    "CONSTRAINT fkey_invoice_id FOREIGN KEY (invoice_id) REFERENCES invoice(id) ON DELETE RESTRICT ON UPDATE CASCADE,"
    "CONSTRAINT prize_types_id_fkey FOREIGN KEY (type_id) REFERENCES prize_types(id) ON DELETE RESTRICT ON UPDATE CASCADE"
    ");"
)


PRIZE_TYPES = (
    "CREATE TABLE prize_types ("
    "id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
    "type TEXT NOT NULL"
    ");"
)


PRIZE_TYPES_VALUES = (
    "INSERT INTO prize_types(type)"
    "VALUES ('special'),"
    "('grand'),"
    "('first'),"
    "('second'),"
    "('third'),"
    "('fourth'),"
    "('fifth'),"
    "('sixth'),"
    "('additional');"
)

PRIZE_TYPES_INDEX = "CREATE UNIQUE INDEX prize_types_type_key ON prize_types(type);"
