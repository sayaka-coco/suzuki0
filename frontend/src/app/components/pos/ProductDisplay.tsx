'use client'

import { Product } from '@/lib/types'

interface ProductDisplayProps {
  product: Product
}

export default function ProductDisplay({ product }: ProductDisplayProps) {
  return (
    <div className="bg-white rounded-xl shadow-lg border border-cyan-100">
      <div className="bg-gradient-to-r from-cyan-600 to-blue-600 text-white p-4 rounded-t-xl">
        <h2 className="text-xl font-bold">✅ 検索結果</h2>
      </div>

      <div className="p-6">
        <div className="space-y-4">
          {/* 商品名 */}
          <div className="bg-gradient-to-r from-cyan-50 to-blue-50 p-4 rounded-xl border border-cyan-200">
            <p className="text-sm text-cyan-600 font-medium mb-1">商品名</p>
            <p className="text-xl font-bold text-gray-800">{product.name}</p>
          </div>

          {/* 価格 */}
          <div className="bg-gradient-to-r from-green-50 to-emerald-50 p-4 rounded-xl border border-green-200">
            <p className="text-sm text-green-600 font-medium mb-1">価格</p>
            <p className="text-3xl font-bold text-green-700 flex items-center">
              <span className="mr-2">💰</span>
              {product.price.toLocaleString()}円
            </p>
          </div>

          {/* 商品コード */}
          <div className="bg-gradient-to-r from-gray-50 to-slate-50 p-4 rounded-xl border border-gray-200">
            <p className="text-sm text-gray-600 font-medium mb-1">商品コード</p>
            <p className="text-lg font-mono text-gray-800 bg-gray-100 px-3 py-1 rounded-lg inline-block">
              {product.code}
            </p>
          </div>
        </div>
      </div>
    </div>
  )
}