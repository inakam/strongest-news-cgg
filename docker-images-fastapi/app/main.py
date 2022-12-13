from typing import Optional
from fastapi import FastAPI
from fastapi import Body, status, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from .db import database_session
from .model import ArticleTable, Article, CommentTable, Comment, UserTable, User, CommentPostBody

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# コメント一覧取得
@app.get("/comments")
async def get_comment_list():
    comments = database_session.query(CommentTable).all()
    return comments

# idでコメント取得
@app.get("/comments/{id}")
async def get_comment(id: int):
    # IDに対応するコメントを取得
    comment = database_session.query(CommentTable).filter(CommentTable.article_id == id).all()
    return comment

# コメントを作成する
@app.post("/comments")
async def post_comment(comment: CommentPostBody):
    commentModel = CommentTable(
        name=comment.name,
        article_id=comment.article_id,
        detail=comment.detail,
    )
    database_session.add(commentModel)
    database_session.commit()
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=jsonable_encoder(commentModel))

# コメントを更新する
@app.put("/comments/{id}")
async def put_comment(id: int, comment: Comment):
    commentModel = database_session.query(CommentTable).filter(CommentTable.id == id).first()
    if not commentModel:
        raise HTTPException(status_code=404, detail="comment not found")
    # 更新
    commentModel.detail = comment.detail
    database_session.commit()
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=commentModel)

# コメントを削除する
@app.delete("/comments/{id}")
async def delete_comment(id: int):
    commentModel = database_session.query(CommentTable).filter(CommentTable.id == id).first()
    if not commentModel:
        raise HTTPException(status_code=404, detail="comment not found")
    # レコードの削除 deleteしてcommit
    database_session.delete(commentModel)
    database_session.commit()
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=None)

# 記事を全件取得する
@app.get("/articles")
async def get_article_list(limit: int = None):
    if limit:
        articles = database_session.query(ArticleTable).order_by(ArticleTable.created_at.desc()).limit(limit).all()
    else:
        articles = database_session.query(ArticleTable).all()
    return articles

# 記事を取得する
@app.get("/articles/{id}")
async def get_article(id: int):
    # IDに対応する記事を取得
    article = database_session.query(ArticleTable).filter(ArticleTable.id == id).first()
    return article

# タイトル一覧を取得する
@app.get("/titles")
async def get_title_list(limit: int = None):
    if limit:
        # limitの数だけ新しい順に取得する
        titles = database_session.query(ArticleTable.id, ArticleTable.title, ArticleTable.img_url, ArticleTable.created_at).order_by(ArticleTable.created_at.desc()).limit(limit).all()
    else:
        titles = database_session.query(ArticleTable.id, ArticleTable.title, ArticleTable.img_url, ArticleTable.created_at).all()
    return titles

# キーワードに関する記事を取得する
@app.get("/keywords")
async def get_keyword_list(keyword: str):
    articles = database_session.query(ArticleTable.id, ArticleTable.title, ArticleTable.img_url, ArticleTable.created_at).filter(ArticleTable.title.like("%" + keyword + "%")).all()
    return articles

# カテゴリに関する記事を取得する
@app.get("/categories")
async def get_category_list(type: str):
    articles = database_session.query(ArticleTable.id, ArticleTable.title, ArticleTable.img_url, ArticleTable.created_at).filter(ArticleTable.type.like("%" + type + "%")).all()
    return articles