from sqlalchemy import Column, Integer, String, DateTime
from pydantic import BaseModel
from .db import Base
from .db import DATABASE_ENGINE
from datetime import datetime, timedelta

# モデルとスキーマの定義
# articlesテーブル
class ArticleTable(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    detail = Column(String, nullable=False)
    type = Column(String, nullable=False)
    img_url = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False,
                           default=datetime.now, onupdate=datetime.now)

# モデル定義 
class Article(BaseModel):
    id: int
    title: str
    detail: str
    type: str
    img_url: str
    created_at: datetime
    updated_at: datetime

# commentsテーブル
class CommentTable(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, primary_key=False)
    article_id = Column(Integer, primary_key=False)
    detail = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False,
                           default=datetime.now, onupdate=datetime.now)

class Comment(BaseModel):
    name: str
    article_id: int
    detail: str
    created_at: datetime
    updated_at: datetime

# コメントをPOSTするときの形
class CommentPostBody(BaseModel):
    name: str
    article_id: int
    detail: str

# usersテーブル
class UserTable(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    e_mail = Column(String, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False,
                           default=datetime.now, onupdate=datetime.now)

class User(BaseModel):
    id: int
    e_mail: str
    password: str
    created_at: datetime
    updated_at: datetime

def main():
    # テーブル構築
    Base.metadata.create_all(bind=DATABASE_ENGINE)

if __name__ == "__main__":
    main()