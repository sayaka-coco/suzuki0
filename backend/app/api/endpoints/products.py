from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ... import crud, schemas
from ...database import get_db

router = APIRouter()

@router.get("/products/{code}", response_model=schemas.ProductSearchResponse)
async def search_product(code: str, db: Session = Depends(get_db)):
    """
    商品マスタ検索API
    - パラメータ：商品コード
    - リターン：商品情報またはNULL
    """
    try:
        # 商品検索
        product = crud.get_product_by_code(db, code=code)
        
        if product:
            return schemas.ProductSearchResponse(
                success=True,
                product=schemas.Product.model_validate(product),
                message="商品が見つかりました"
            )
        else:
            # 1-e1: 対象が見つからなかった場合はNULL情報を返す
            return schemas.ProductSearchResponse(
                success=False,
                product=None,
                message="商品が見つかりません"
            )
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"商品検索エラー: {str(e)}")