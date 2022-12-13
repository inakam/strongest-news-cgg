from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import os

# データベース設定
DATABASE_URL = 'mysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
    'user': os.environ.get('DATABASE_USER'),
    'password': os.environ.get('DATABASE_PASSWORD'),
    'host': os.environ.get('DATABASE_HOST'),
    'db_name': os.environ.get('DATABASE_DB_NAME')
})
DATABASE_ENGINE = create_engine(
    DATABASE_URL,
    encoding="utf-8",
    echo=True
)
database_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=DATABASE_ENGINE
    )
)
Base = declarative_base()
Base.query = database_session.query_property()
