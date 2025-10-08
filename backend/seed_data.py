import os
import sys
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# 親ディレクトリのappモジュールをインポート可能にする
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import engine
from app.models import Product

# 環境変数を読み込む
load_dotenv()

# セッション作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def seed_products():
    """商品データをデータベースに投入"""
    session = SessionLocal()

    try:
        # 既存の商品データがあるかチェック
        existing_count = session.query(Product).count()
        if existing_count > 0:
            print(f"既に {existing_count} 件の商品データが存在します。")
            return

        # init.sqlと同じサンプル商品データ
        sample_products = [
            {"code": "1234567890", "name": "おーいお茶", "price": 150},
            {"code": "2345678901", "name": "ソフラン", "price": 300},
            {"code": "3456789012", "name": "福島産うりん菓", "price": 185},
            {"code": "4567890123", "name": "タイガー島ブラン", "price": 200},
            {"code": "5678901234", "name": "西谷サイダー", "price": 160},
        ]

        # 商品データを投入
        for product_data in sample_products:
            product = Product(
                CODE=product_data["code"],
                NAME=product_data["name"],
                PRICE=product_data["price"]
            )
            session.add(product)

        session.commit()
        print(f"{len(sample_products)} 件の商品データを投入しました。")

        # 投入されたデータを確認
        products = session.query(Product).all()
        print("\n投入された商品データ:")
        for product in products:
            print(f"ID: {product.PRD_ID}, CODE: {product.CODE}, NAME: {product.NAME}, PRICE: {product.PRICE}")

    except Exception as e:
        session.rollback()
        print(f"エラーが発生しました: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    print("商品データを投入しています...")
    seed_products()
    print("完了しました。")