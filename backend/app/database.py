from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# 環境変数を読み込む
load_dotenv()

# データベース設定
USE_SQLITE = os.getenv("USE_SQLITE", "false").lower() == "true"

if USE_SQLITE:
    # SQLite設定（開発用）
    DATABASE_URL = "sqlite:///./pos_system.db"
    engine = create_engine(
        DATABASE_URL,
        echo=True,
        connect_args={"check_same_thread": False}
    )
else:
    # MySQL設定
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "pos_system")

    # MySQL接続URL（パスワードが空の場合の処理）
    if MYSQL_PASSWORD:
        DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
    else:
        DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

    # SQLAlchemyエンジン作成
    engine = create_engine(
        DATABASE_URL,
        echo=True,  # SQL文をログ出力（本番環境では False にする）
        pool_pre_ping=True,  # 接続確認
        pool_recycle=3600,   # 1時間で接続をリサイクル
    )

# セッションファクトリー作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Baseクラス作成
Base = declarative_base()

# 依存性注入用のDB セッション取得関数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()