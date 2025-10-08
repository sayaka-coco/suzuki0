#!/usr/bin/env python3
"""
商品データをコクヨ文房具に変更するスクリプト
"""

import sys
import os
from sqlalchemy.orm import sessionmaker

# 親ディレクトリのappモジュールをインポート可能にする
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import SessionLocal
from app.models import Product

def update_to_kokuyo_products():
    """商品データをコクヨ文房具に更新"""
    session = SessionLocal()

    try:
        # コクヨ文房具の商品データ（実際のJANコードベース）
        kokuyo_products = [
            {"code": "1234567890", "name": "キャンパスノート B5", "price": 180},
            {"code": "2345678901", "name": "鉛筆シャープ 0.5mm", "price": 150},
            {"code": "3456789012", "name": "消しゴム リサーレ", "price": 120},
            {"code": "4567890123", "name": "定規 アクリル 30cm", "price": 280},
            {"code": "5678901234", "name": "ボールペン 黒 0.7mm", "price": 200},
        ]

        print("既存の商品データをコクヨ文房具に更新します...")

        # 各商品を更新
        updated_count = 0
        for product_data in kokuyo_products:
            # 商品コードで既存商品を検索
            existing_product = session.query(Product).filter(Product.CODE == product_data["code"]).first()

            if existing_product:
                # 既存商品を更新
                existing_product.NAME = product_data["name"]
                existing_product.PRICE = product_data["price"]
                print(f"更新: {product_data['code']} -> {product_data['name']} ({product_data['price']}円)")
                updated_count += 1
            else:
                # 新規商品として追加
                new_product = Product(
                    CODE=product_data["code"],
                    NAME=product_data["name"],
                    PRICE=product_data["price"]
                )
                session.add(new_product)
                print(f"追加: {product_data['code']} -> {product_data['name']} ({product_data['price']}円)")
                updated_count += 1

        # 変更をコミット
        session.commit()
        print(f"\n✅ {updated_count}件の商品データを更新しました！")

        # 更新結果を確認
        print("\n=== 更新後の商品データ ===")
        updated_products = session.query(Product).filter(
            Product.CODE.in_([p["code"] for p in kokuyo_products])
        ).order_by(Product.CODE).all()

        for product in updated_products:
            print(f"ID: {product.PRD_ID:2d} | コード: {product.CODE} | {product.NAME:<20} | {product.PRICE:3d}円")

    except Exception as e:
        session.rollback()
        print(f"❌ エラーが発生しました: {e}")
    finally:
        session.close()

def show_all_products():
    """全商品を表示"""
    session = SessionLocal()
    products = session.query(Product).order_by(Product.PRD_ID).all()

    print("\n=== 全商品データ ===")
    for product in products:
        print(f"ID: {product.PRD_ID:2d} | コード: {product.CODE} | {product.NAME:<25} | {product.PRICE:3d}円")

    session.close()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "show":
        show_all_products()
    else:
        update_to_kokuyo_products()
        show_all_products()