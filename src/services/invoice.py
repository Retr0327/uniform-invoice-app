from models import query
from typing import Dict, List

invoice_table = "invoice"
prize_table = "prize"
prize_types_table = "prize_types"


def get_invoice(invoice_data) -> List:
    invoice_query = f"""
    SELECT {prize_table}.type_id, 
           {prize_table}.prize
    FROM {invoice_table}
    INNER JOIN {prize_table}
    ON {prize_table}.invoice_id = {invoice_table}.id
    WHERE month=? AND year=?;
    """
    return query(invoice_query, invoice_data)


def get_claiming_date(invoice_data) -> List:
    date_query = f"""
    SELECT {invoice_table}.claiming_date_start,
           {invoice_table}.claiming_date_end
    FROM {invoice_table}
    WHERE month=? AND year=?;
    """
    return query(date_query, invoice_data)


def create_invoice(invoice_data: List[str]) -> List[tuple]:
    invoice_insertion = f"""
    INSERT INTO {invoice_table} (
        month, 
        year, 
        claiming_date_start, 
        claiming_date_end
    )
    VALUES (?, ?, ?, ?)
    RETURNING id;
    """
    return query(invoice_insertion, invoice_data)


def create_prize(prize_data: Dict[str, str]) -> List[tuple]:
    prize_insertion = f"""
    WITH invoice_id AS (
        SELECT {invoice_table}.id 
        FROM {invoice_table} 
        WHERE month=:month 
        AND year=:year
    )

    INSERT INTO {prize_table} (
        invoice_id, 
        type_id, 
        prize
    ) VALUES (
        (SELECT * FROM invoice_id), 
        (SELECT {prize_types_table}.id 
         FROM {prize_types_table} 
         WHERE type=:type
        ), 
        :prize
    );
    """

    return query(prize_insertion, prize_data, mode="many")
