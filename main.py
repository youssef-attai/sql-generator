import datetime
import random

from names import generate_random_name, NameType
from emails import generate_random_email

N1 = "\n" * 1
N2 = "\n" * 2

S1 = " " * 1
S2 = " " * 2
S3 = " " * 3
S4 = " " * 4
S5 = " " * 5
S6 = " " * 6
S7 = " " * 7

T1 = "\t" * 1
T2 = "\t" * 2


def prepare_for_insert(value):
    if isinstance(value, str):
        return f"'{value}'"
    if isinstance(value, datetime.datetime):
        return f"'{value.isoformat()}'"
    return str(value)


def check_before_insert(table, data):
    assert len(table.columns) == len(
        data), "Number of columns and data must match"
    return True


def insert_into_table(table, data):
    check_before_insert(table, data)
    data = [prepare_for_insert(value) for value in data]

    columns = ', '.join(table.columns)
    values = ', '.join(data)
    sql = f"INSERT INTO {table.name}({columns}){N1}VALUES ({values})"

    return f"{sql};"


def insert_multiple_into_table(table, rows):
    for row in rows:
        check_before_insert(table, row)

    rows = [[prepare_for_insert(value) for value in row] for row in rows]

    columns = ', '.join(table.columns)
    values = f'),{N1}{S7}('.join([', '.join(row) for row in rows])
    sql = f"INSERT INTO {table.name} ({columns}){N1}VALUES ({values})"

    return f"{sql};"


class Table:
    def __init__(self, name, columns):
        self.name = name
        self.columns = columns


if __name__ == "__main__":
    table = Table("users", ["id", "name", "gender", "email"])
    rows = []
    for i in range(1, 100):
        gender = random.choice([NameType.MALE, NameType.FEMALE])
        name = generate_random_name(gender, 2)
        email = generate_random_email(name)
        mf = "M" if gender == NameType.MALE else "F"

        rows.append([i, name, mf, email])

    print(insert_multiple_into_table(table, rows))
