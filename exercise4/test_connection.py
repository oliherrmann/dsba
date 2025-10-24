import pypsql
from pathlib import Path

conn = pypsql.DatabaseConnector(
    db_credential_file='.env'
)

sql_script = """
SELECT *
FROM customers
"""

df = conn.get_data(sql_script)

:q


print(df)
print(age)

