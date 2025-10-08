from sqlalchemy.orm import Session
from . import models, schemas

def get_product_by_code(db: Session, code: str):
    """商品コードで商品を検索"""
    return db.query(models.Product).filter(models.Product.CODE == code).first()

def create_transaction(db: Session, emp_cd: str = '9999999999', store_cd: str = '30', pos_no: str = '90'):
    """取引レコード作成"""
    db_transaction = models.Transaction(
        EMP_CD=emp_cd if emp_cd else '9999999999',
        STORE_CD=store_cd if store_cd else '30',
        POS_NO=pos_no if pos_no else '90',
        TOTAL_AMT=0
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def create_transaction_item(db: Session, transaction_id: int, detail_id: int, item: schemas.PurchaseItemRequest):
    """取引明細作成"""
    db_item = models.TransactionItem(
        TRD_ID=transaction_id,
        DTL_ID=detail_id,
        PRD_ID=item.PRD_ID,
        PRD_CODE=item.PRD_CODE,
        PRD_NAME=item.PRD_NAME,
        PRD_PRICE=item.PRD_PRICE
    )
    db.add(db_item)
    return db_item

def update_transaction_total(db: Session, transaction_id: int, total_amount: int):
    """取引テーブルの合計金額更新"""
    db_transaction = db.query(models.Transaction).filter(models.Transaction.TRD_ID == transaction_id).first()
    if db_transaction:
        db_transaction.TOTAL_AMT = total_amount
        db.commit()
        db.refresh(db_transaction)
    return db_transaction