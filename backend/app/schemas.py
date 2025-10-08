from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# 商品スキーマ
class ProductBase(BaseModel):
    CODE: str
    NAME: str
    PRICE: int

class Product(ProductBase):
    PRD_ID: int
    
    class Config:
        from_attributes = True

# 購入リクエストスキーマ
class PurchaseItemRequest(BaseModel):
    PRD_ID: int
    PRD_CODE: str
    PRD_NAME: str
    PRD_PRICE: int

class PurchaseRequest(BaseModel):
    EMP_CD: Optional[str] = '9999999999'
    STORE_CD: Optional[str] = '30'
    POS_NO: Optional[str] = '90'
    items: List[PurchaseItemRequest]

# 購入レスポンススキーマ
class PurchaseResponse(BaseModel):
    success: bool
    total_amount: int
    transaction_id: int
    message: str

# 商品検索レスポンス
class ProductSearchResponse(BaseModel):
    success: bool
    product: Optional[Product] = None
    message: str