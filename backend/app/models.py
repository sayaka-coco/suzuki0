from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .database import Base

class Product(Base):
    __tablename__ = "products"
    
    PRD_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    CODE = Column(String(13), unique=True, index=True, nullable=False)
    NAME = Column(String(50), nullable=False)
    PRICE = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

class Transaction(Base):
    __tablename__ = "transactions"
    
    TRD_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    DATETIME = Column(TIMESTAMP, server_default=func.now())
    EMP_CD = Column(String(10), default='9999999999')
    STORE_CD = Column(String(5), default='30')
    POS_NO = Column(String(3), default='90')
    TOTAL_AMT = Column(Integer, default=0)
    
    # リレーション
    items = relationship("TransactionItem", back_populates="transaction")

class TransactionItem(Base):
    __tablename__ = "transaction_items"
    
    TRD_ID = Column(Integer, ForeignKey("transactions.TRD_ID"), primary_key=True)
    DTL_ID = Column(Integer, primary_key=True)
    PRD_ID = Column(Integer, ForeignKey("products.PRD_ID"))
    PRD_CODE = Column(String(13))
    PRD_NAME = Column(String(50))
    PRD_PRICE = Column(Integer)
    
    # リレーション
    transaction = relationship("Transaction", back_populates="items")
    product = relationship("Product")