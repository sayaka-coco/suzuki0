import pymysql
import os
from dotenv import load_dotenv

# 環境変数を読み込む
load_dotenv()

# データベース設定
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", "3306"))
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "pos_db")

def create_database():
    try:
        # MySQLサーバーに接続（データベースを指定せずに）
        connection = pymysql.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            charset='utf8mb4'
        )

        cursor = connection.cursor()

        # データベースが存在しない場合は作成
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {MYSQL_DATABASE}")
        print(f"Database '{MYSQL_DATABASE}' created or already exists")

        # ユーザーを作成（すでに存在する場合はスキップ）
        try:
            cursor.execute(f"CREATE USER 'pos_user'@'localhost' IDENTIFIED BY 'pos_password'")
            print("User 'pos_user' created")
        except pymysql.err.OperationalError as e:
            if "already exists" in str(e):
                print("User 'pos_user' already exists")
            else:
                print(f"Error creating user: {e}")

        # 権限を付与
        cursor.execute(f"GRANT ALL PRIVILEGES ON {MYSQL_DATABASE}.* TO 'pos_user'@'localhost'")
        cursor.execute("FLUSH PRIVILEGES")
        print("Privileges granted to 'pos_user'")

        cursor.close()
        connection.close()

        return True

    except Exception as e:
        print(f"Error: {e}")
        return False

def test_connection():
    try:
        connection = pymysql.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE,
            charset='utf8mb4'
        )

        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        print("MySQL connection successful!")
        return True

    except Exception as e:
        print(f"Connection failed: {e}")
        return False

if __name__ == "__main__":
    print("Setting up MySQL database...")
    if create_database():
        print("Database setup completed successfully!")
        test_connection()
    else:
        print("Database setup failed!")