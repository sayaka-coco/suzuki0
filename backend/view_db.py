#!/usr/bin/env python3
"""
データベース内容確認用スクリプト
使用方法: python view_db.py
"""

import sys
import os
from sqlalchemy.orm import sessionmaker

# 親ディレクトリのappモジュールをインポート可能にする
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import SessionLocal
from app.models import Product, Transaction, TransactionItem

def view_products():
    """商品マスタを表示"""
    session = SessionLocal()
    products = session.query(Product).order_by(Product.PRD_ID).all()

    print("=" * 80)
    print("商品マスタ (products)")
    print("=" * 80)
    print(f"{'ID':>3} | {'商品コード':>13} | {'商品名':<20} | {'価格':>6}")
    print("-" * 80)

    for p in products:
        print(f"{p.PRD_ID:>3} | {p.CODE:>13} | {p.NAME:<20} | {p.PRICE:>4}円")

    print(f"\n合計: {len(products)}件")
    session.close()

def view_transactions():
    """取引履歴を表示"""
    session = SessionLocal()
    transactions = session.query(Transaction).order_by(Transaction.TRD_ID.desc()).limit(10).all()

    print("\n" + "=" * 80)
    print("取引履歴 (transactions) - 最新10件")
    print("=" * 80)
    print(f"{'取引ID':>6} | {'日時':<19} | {'従業員':>10} | {'合計金額':>8}")
    print("-" * 80)

    for t in transactions:
        print(f"{t.TRD_ID:>6} | {t.DATETIME.strftime('%Y-%m-%d %H:%M:%S')} | {t.EMP_CD:>10} | {t.TOTAL_AMT:>6}円")

    session.close()

def view_transaction_items(transaction_id=None):
    """取引明細を表示"""
    session = SessionLocal()

    if transaction_id:
        items = session.query(TransactionItem).filter(TransactionItem.TRD_ID == transaction_id).all()
        print(f"\n取引ID {transaction_id} の明細:")
    else:
        items = session.query(TransactionItem).order_by(TransactionItem.TRD_ID.desc()).limit(20).all()
        print(f"\n取引明細 (transaction_items) - 最新20件:")

    print("=" * 90)
    print(f"{'取引ID':>6} | {'明細ID':>6} | {'商品コード':>13} | {'商品名':<15} | {'価格':>6}")
    print("-" * 90)

    for item in items:
        print(f"{item.TRD_ID:>6} | {item.DTL_ID:>6} | {item.PRD_CODE:>13} | {item.PRD_NAME:<15} | {item.PRD_PRICE:>4}円")

    session.close()

def search_product(code):
    """商品コードで検索"""
    session = SessionLocal()
    product = session.query(Product).filter(Product.CODE == code).first()

    if product:
        print(f"\n商品コード '{code}' の検索結果:")
        print("=" * 50)
        print(f"ID: {product.PRD_ID}")
        print(f"コード: {product.CODE}")
        print(f"商品名: {product.NAME}")
        print(f"価格: {product.PRICE}円")
        print(f"作成日時: {product.created_at}")
        print(f"更新日時: {product.updated_at}")
    else:
        print(f"商品コード '{code}' は見つかりませんでした。")

    session.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "search" and len(sys.argv) > 2:
            search_product(sys.argv[2])
        elif sys.argv[1] == "transaction" and len(sys.argv) > 2:
            view_transaction_items(int(sys.argv[2]))
        else:
            print("使用方法:")
            print("  python view_db.py                    # 全データ表示")
            print("  python view_db.py search CODE        # 商品検索")
            print("  python view_db.py transaction ID     # 特定取引の明細")
    else:
        view_products()
        view_transactions()
        view_transaction_items()