from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ... import crud, schemas
from ...database import get_db

router = APIRouter()

@router.post("/purchase", response_model=schemas.PurchaseResponse)
async def create_purchase(purchase_request: schemas.PurchaseRequest, db: Session = Depends(get_db)):
    """
    購入処理API
    - パラメータ：購入商品リスト、従業員コード、店舗コード、POS番号
    - リターン：購入結果（成功/失敗、合計金額、取引ID）
    """
    try:
        # 取引レコード作成
        transaction = crud.create_transaction(
            db,
            emp_cd=purchase_request.EMP_CD,
            store_cd=purchase_request.STORE_CD,
            pos_no=purchase_request.POS_NO
        )

        total_amount = 0

        # 取引明細作成
        for index, item in enumerate(purchase_request.items, 1):
            crud.create_transaction_item(
                db,
                transaction_id=transaction.TRD_ID,
                detail_id=index,
                item=item
            )
            total_amount += item.PRD_PRICE

        # 取引テーブルの合計金額更新
        crud.update_transaction_total(db, transaction.TRD_ID, total_amount)

        # コミット
        db.commit()

        return schemas.PurchaseResponse(
            success=True,
            total_amount=total_amount,
            transaction_id=transaction.TRD_ID,
            message="購入処理が完了しました"
        )

    except Exception as e:
        # ロールバック
        db.rollback()
        raise HTTPException(status_code=500, detail=f"購入処理エラー: {str(e)}")