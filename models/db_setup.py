from .db_connection import get_db
from sqlalchemy import text

sess = next(get_db())

def create_table_questions_stable():
    sess.execute(
        text("""
        CREATE TABLE IF NOT EXISTS public.questions_stable (
            id SERIAL PRIMARY KEY,
            question_text TEXT NOT NULL
        )
        """)
    )
    sess.commit()
