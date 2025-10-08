import requests
import json

# APIベースURL
API_BASE_URL = "http://localhost:8000"

def test_purchase():
    """購入処理のテスト"""

    # テスト用の購入データ
    purchase_data = {
        "EMP_CD": "9999999999",
        "STORE_CD": "30",
        "POS_NO": "90",
        "items": [
            {
                "PRD_ID": 1,
                "PRD_CODE": "4901085039045",
                "PRD_NAME": "ペプシコーラ 500ml",
                "PRD_PRICE": 150
            },
            {
                "PRD_ID": 2,
                "PRD_CODE": "4902103082129",
                "PRD_NAME": "キットカット ミニ",
                "PRD_PRICE": 250
            }
        ]
    }

    print("購入処理テストを開始します...")
    print(f"購入データ: {json.dumps(purchase_data, indent=2, ensure_ascii=False)}")

    try:
        # 購入処理API呼び出し
        response = requests.post(
            f"{API_BASE_URL}/api/purchase",
            json=purchase_data,
            headers={"Content-Type": "application/json"}
        )

        print(f"\nHTTPステータス: {response.status_code}")

        if response.status_code == 200:
            result = response.json()
            print("購入処理成功！")
            print(f"レスポンス: {json.dumps(result, indent=2, ensure_ascii=False)}")

            # 取引ID取得
            transaction_id = result.get("transaction_id")
            if transaction_id:
                print(f"\n作成された取引ID: {transaction_id}")
                return transaction_id
        else:
            print("購入処理失敗")
            print(f"エラー: {response.text}")
            return None

    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return None

def check_database_data(transaction_id):
    """データベースに保存されたデータを確認"""
    if not transaction_id:
        print("取引IDが無効です")
        return

    print(f"\n取引ID {transaction_id} のデータベースを確認します...")

    # データベース確認用のPythonコード実行
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

    from app.database import SessionLocal
    from app.models import Transaction, TransactionItem

    session = SessionLocal()
    try:
        # 取引データ確認
        transaction = session.query(Transaction).filter(Transaction.TRD_ID == transaction_id).first()
        if transaction:
            print(f"取引データ: ID={transaction.TRD_ID}, 合計={transaction.TOTAL_AMT}円, 従業員={transaction.EMP_CD}")

            # 取引明細確認
            items = session.query(TransactionItem).filter(TransactionItem.TRD_ID == transaction_id).all()
            print(f"取引明細数: {len(items)}")
            for item in items:
                print(f"  明細ID={item.DTL_ID}, 商品={item.PRD_NAME}, 価格={item.PRD_PRICE}円")
        else:
            print("取引データが見つかりません")

    except Exception as e:
        print(f"データベース確認エラー: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    print("=== 購入処理テスト ===")
    transaction_id = test_purchase()
    check_database_data(transaction_id)
    print("=== テスト完了 ===")