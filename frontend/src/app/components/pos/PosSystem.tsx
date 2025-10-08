'use client'

import { useState } from 'react'
import ProductInput from './ProductInput'
import ProductDisplay from './ProductDisplay'
import PurchaseList from './PurchaseList'
import { Product, PurchaseItem } from '@/lib/types'
import { searchProduct, createPurchase, ApiProduct, PurchaseItemRequest } from '@/lib/api'

export default function PosSystem() {
  const [productCode, setProductCode] = useState('')
  const [currentProduct, setCurrentProduct] = useState<Product | null>(null)
  const [purchaseList, setPurchaseList] = useState<PurchaseItem[]>([])

  // 商品検索
  const handleProductSearch = async () => {
    if (!productCode.trim()) {
      alert('商品コードを入力してください')
      return
    }

    try {
      const response = await searchProduct(productCode)
      if (response.success && response.product) {
        setCurrentProduct({
          id: response.product.PRD_ID,
          code: response.product.CODE,
          name: response.product.NAME,
          price: response.product.PRICE
        })
      } else {
        setCurrentProduct(null)
        alert(response.message || '商品が見つかりません')
      }
    } catch (error) {
      console.error('商品検索エラー:', error)
      alert('商品検索でエラーが発生しました')
      setCurrentProduct(null)
    }
  }

  // 購入リストに追加
  const handleAddToList = () => {
    if (currentProduct) {
      const existingItem = purchaseList.find(item => item.code === currentProduct.code)
      
      if (existingItem) {
        setPurchaseList(purchaseList.map(item =>
          item.code === currentProduct.code
            ? { ...item, quantity: item.quantity + 1, total: (item.quantity + 1) * item.price }
            : item
        ))
      } else {
        setPurchaseList([...purchaseList, {
          ...currentProduct,
          quantity: 1,
          total: currentProduct.price
        }])
      }
      
      setProductCode('')
      setCurrentProduct(null)
    }
  }

  // 商品削除
  const handleRemoveFromList = (codeToRemove: string) => {
    setPurchaseList(purchaseList.filter(item => item.code !== codeToRemove))
  }

  // 購入処理
  const handlePurchase = async () => {
    if (purchaseList.length === 0) {
      alert('商品を追加してください')
      return
    }

    try {
      // バックエンドAPI用のデータ形式に変換（数量を考慮）
      const purchaseItems: PurchaseItemRequest[] = []

      purchaseList.forEach(item => {
        for (let i = 0; i < item.quantity; i++) {
          purchaseItems.push({
            PRD_ID: item.id || 0,
            PRD_CODE: item.code,
            PRD_NAME: item.name,
            PRD_PRICE: item.price
          })
        }
      })

      const purchaseData = {
        EMP_CD: '9999999999',
        STORE_CD: '30',
        POS_NO: '90',
        items: purchaseItems
      }

      const response = await createPurchase(purchaseData)

      if (response.success) {
        alert(`購入完了！\n取引ID: ${response.transaction_id}\n合計金額: ${response.total_amount}円`)
        setPurchaseList([])
        setCurrentProduct(null)
        setProductCode('')
      } else {
        alert(`購入処理エラー: ${response.message}`)
      }
    } catch (error) {
      console.error('購入処理エラー:', error)
      alert('購入処理でエラーが発生しました')
    }
  }

  // 全クリア
  const handleClearAll = () => {
    setPurchaseList([])
    setCurrentProduct(null)
    setProductCode('')
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-cyan-50 via-blue-50 to-white p-4">
      <div className="max-w-7xl mx-auto">
        {/* ヘッダー */}
        <div className="text-center mb-8">
          <div className="bg-white rounded-2xl shadow-lg border border-cyan-100 p-8 mb-6">
            <div className="bg-gradient-to-r from-cyan-500 to-blue-600 bg-clip-text text-transparent">
              <h1 className="text-4xl font-bold mb-2">🏪 POSレジシステム</h1>
              <p className="text-lg text-cyan-600">コクヨ文房具店</p>
            </div>
            <div className="w-32 h-1 bg-gradient-to-r from-cyan-400 to-blue-400 mx-auto mt-4 rounded-full"></div>
          </div>
        </div>

        <div className="flex flex-col md:flex-row gap-8">
          {/* 左側：商品入力・表示エリア（左余白付き） */}
          <div className="md:w-1/3 md:ml-16 space-y-6">
            <ProductInput
              productCode={productCode}
              setProductCode={setProductCode}
              onSearch={handleProductSearch}
            />

            {currentProduct && (
              <>
                <ProductDisplay product={currentProduct} />
                <button
                  onClick={handleAddToList}
                  className="w-full bg-gradient-to-r from-green-500 to-emerald-500 hover:from-green-600 hover:to-emerald-600 text-white font-bold py-4 px-6 rounded-xl text-lg transition-all duration-300 shadow-lg hover:shadow-xl transform hover:scale-105"
                >
                  <span className="flex items-center justify-center space-x-2">
                    <span>➕</span>
                    <span>カートに追加</span>
                  </span>
                </button>
              </>
            )}
          </div>

          {/* 右側：購入リストとお会計（2列表示） */}
          <div className="md:w-2/3">
            <PurchaseList
              purchaseList={purchaseList}
              onRemoveItem={handleRemoveFromList}
              onClearAll={handleClearAll}
              onPurchase={handlePurchase}
            />
          </div>
        </div>
      </div>
    </div>
  )
}