'use client'

import { PurchaseItem } from '@/lib/types'

interface PurchaseListProps {
  purchaseList: PurchaseItem[]
  onRemoveItem: (code: string) => void
  onClearAll: () => void
  onPurchase: () => void
}

export default function PurchaseList({ 
  purchaseList, 
  onRemoveItem, 
  onClearAll, 
  onPurchase 
}: PurchaseListProps) {
  const totalAmount = purchaseList.reduce((sum, item) => sum + item.total, 0)

  return (
    <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 h-fit">
      {/* 左列：購入リスト */}
      <div className="bg-white rounded-xl shadow-lg border border-cyan-100">
        <div className="bg-gradient-to-r from-cyan-500 to-cyan-600 text-white p-4 rounded-t-xl">
          <div className="flex justify-between items-center">
            <h2 className="text-xl font-bold">🛒 購入リスト</h2>
            {purchaseList.length > 0 && (
              <button
                onClick={onClearAll}
                className="text-sm bg-white/20 hover:bg-white/30 text-white px-3 py-1 rounded-lg transition-all duration-200 backdrop-blur-sm"
              >
                全てクリア
              </button>
            )}
          </div>
        </div>

        <div className="p-6">
          {purchaseList.length === 0 ? (
            <div className="text-center py-12">
              <div className="text-6xl mb-4">🛍️</div>
              <p className="text-cyan-600 text-lg font-medium">商品を追加してください</p>
            </div>
          ) : (
            <div className="space-y-3 max-h-80 overflow-y-auto pr-2">
              {purchaseList.map((item, index) => (
                <div key={index} className="bg-gradient-to-r from-cyan-50 to-white p-4 rounded-lg border border-cyan-100 hover:shadow-md transition-all duration-200">
                  <div className="flex justify-between items-center">
                    <div className="flex-1">
                      <p className="font-semibold text-gray-800 mb-1">{item.name}</p>
                      <p className="text-sm text-cyan-600 bg-cyan-100 px-2 py-1 rounded-full inline-block">
                        {item.price}円 × {item.quantity}
                      </p>
                    </div>
                    <div className="flex items-center space-x-3">
                      <p className="font-bold text-xl text-cyan-700">{item.total}円</p>
                      <button
                        onClick={() => onRemoveItem(item.code)}
                        className="text-red-500 hover:text-white hover:bg-red-500 text-sm bg-red-50 hover:shadow-md px-3 py-2 rounded-lg transition-all duration-200"
                      >
                        ✕
                      </button>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>

      {/* 右列：購入手続き */}
      <div className="bg-white rounded-xl shadow-lg border border-cyan-100">
        <div className="bg-gradient-to-r from-cyan-600 to-blue-600 text-white p-4 rounded-t-xl">
          <h2 className="text-xl font-bold">💳 お会計</h2>
        </div>

        <div className="p-6">
          {purchaseList.length > 0 ? (
            <div className="space-y-6">
              {/* 合計金額表示 */}
              <div className="bg-gradient-to-br from-cyan-50 via-white to-blue-50 p-6 rounded-xl border border-cyan-200">
                <div className="text-center">
                  <p className="text-lg text-cyan-600 font-medium mb-2">合計金額</p>
                  <p className="text-4xl font-bold text-cyan-700 mb-4">{totalAmount.toLocaleString()}円</p>
                  <div className="w-16 h-1 bg-gradient-to-r from-cyan-400 to-blue-400 mx-auto rounded-full"></div>
                </div>
              </div>

              {/* 商品点数表示 */}
              <div className="flex justify-center">
                <div className="bg-white border border-cyan-200 px-4 py-2 rounded-lg">
                  <span className="text-cyan-600">商品点数: </span>
                  <span className="font-bold text-cyan-700">{purchaseList.reduce((sum, item) => sum + item.quantity, 0)}点</span>
                </div>
              </div>

              {/* 購入ボタン */}
              <button
                onClick={onPurchase}
                className="w-full bg-gradient-to-r from-cyan-500 to-blue-500 hover:from-cyan-600 hover:to-blue-600 text-white font-bold py-6 px-6 rounded-xl text-xl transition-all duration-300 shadow-lg hover:shadow-xl transform hover:scale-105"
              >
                <span className="flex items-center justify-center space-x-2">
                  <span>💰</span>
                  <span>購入する</span>
                </span>
              </button>
            </div>
          ) : (
            <div className="text-center py-12">
              <div className="text-6xl mb-4">💸</div>
              <p className="text-cyan-600 text-lg font-medium">商品が追加されると</p>
              <p className="text-cyan-600 text-lg font-medium">お会計ができます</p>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}