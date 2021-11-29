from sqlalchemy import create_engine
from sqlalchemy import text
import config as Config

# postgresql://<username>:<password>@<host>/<database>
# Getting url strings secretly.
db_string = Config.DB_URL
db_string1 = Config.DB_URL1

engine = create_engine(db_string)
engine1 = create_engine(db_string1, echo=True)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM studies LIMIT 1"))
    print(result.all())

with engine1.connect() as conn:
    conn.execute(text("CREATE TABLE IF NOT EXISTS students(id INT PRIMARY KEY, name VARCHAR(50) NOT NULL, city VARCHAR(50) NOT NULL)"))
    conn.execute(text("INSERT INTO students VALUES (:id, :name, :city)"), [{"id": 5, "name": "Daman", "city": "Ludhiana"}, 
    {"id": 6, "name": "Mukul", "city": "Ludhiana"}])
    