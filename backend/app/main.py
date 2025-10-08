from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.endpoints import products, purchase
from .database import engine
from . import models

# データベーステーブル作成（データベース接続がある場合のみ）
try:
    models.Base.metadata.create_all(bind=engine)
    print("Database tables created successfully")
except Exception as e:
    print(f"Database connection failed: {e}")
    print("Starting without database connection. Please check your MySQL configuration.")

app = FastAPI(
    title="POS System API",
    description="POSシステムのバックエンドAPI",
    version="1.0.0"
)

# CORS設定（Next.jsからのアクセスを許可）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],  # Next.jsのURL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ルーター登録
app.include_router(products.router, prefix="/api", tags=["products"])
app.include_router(purchase.router, prefix="/api", tags=["purchase"])

@app.get("/")
async def root():
    return {"message": "POS System API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)