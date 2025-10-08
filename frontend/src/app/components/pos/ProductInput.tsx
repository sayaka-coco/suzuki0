'use client'

interface ProductInputProps {
  productCode: string
  setProductCode: (code: string) => void
  onSearch: () => void
}

export default function ProductInput({ productCode, setProductCode, onSearch }: ProductInputProps) {
  return (
    <div className="bg-white rounded-xl shadow-lg border border-cyan-100">
      <div className="bg-gradient-to-r from-cyan-500 to-cyan-600 text-white p-4 rounded-t-xl">
        <h2 className="text-xl font-bold">🔍 商品コード入力</h2>
      </div>

      <div className="p-6">
        <div className="space-y-4">
          <input
            type="text"
            value={productCode}
            onChange={(e) => setProductCode(e.target.value)}
            placeholder="商品コードを入力（例: 1234567890）"
            className="w-full px-4 py-4 border-2 border-cyan-200 rounded-xl focus:border-cyan-500 focus:outline-none text-lg text-center bg-gradient-to-r from-cyan-50 to-white transition-all duration-200"
            onKeyPress={(e) => e.key === 'Enter' && onSearch()}
          />
          <button
            onClick={onSearch}
            className="w-full bg-gradient-to-r from-cyan-500 to-blue-500 hover:from-cyan-600 hover:to-blue-600 text-white font-bold py-4 px-6 rounded-xl transition-all duration-300 shadow-lg hover:shadow-xl transform hover:scale-105"
          >
            <span className="flex items-center justify-center space-x-2">
              <span>🔎</span>
              <span>商品を検索</span>
            </span>
          </button>
        </div>

        {/* サンプル商品コード表示 */}
        <div className="mt-6 bg-gradient-to-r from-cyan-50 to-blue-50 border border-cyan-200 rounded-xl p-4">
          <h3 className="text-sm font-bold text-cyan-700 mb-3 flex items-center">
            <span className="mr-2">📝</span>
            サンプル商品コード
          </h3>
          <div className="text-xs text-cyan-600 space-y-2">
            <div className="bg-white/70 p-2 rounded-lg border border-cyan-100">
              <span className="font-mono bg-cyan-100 px-2 py-1 rounded text-cyan-800">1234567890</span>
              <span className="mx-2">→</span>
              <span className="font-medium">キャンパスノート B5（180円）</span>
            </div>
            <div className="bg-white/70 p-2 rounded-lg border border-cyan-100">
              <span className="font-mono bg-cyan-100 px-2 py-1 rounded text-cyan-800">2345678901</span>
              <span className="mx-2">→</span>
              <span className="font-medium">鉛筆シャープ 0.5mm（150円）</span>
            </div>
            <div className="bg-white/70 p-2 rounded-lg border border-cyan-100">
              <span className="font-mono bg-cyan-100 px-2 py-1 rounded text-cyan-800">3456789012</span>
              <span className="mx-2">→</span>
              <span className="font-medium">消しゴム リサーレ（120円）</span>
            </div>
            <div className="bg-white/70 p-2 rounded-lg border border-cyan-100">
              <span className="font-mono bg-cyan-100 px-2 py-1 rounded text-cyan-800">4567890123</span>
              <span className="mx-2">→</span>
              <span className="font-medium">定規 アクリル 30cm（280円）</span>
            </div>
            <div className="bg-white/70 p-2 rounded-lg border border-cyan-100">
              <span className="font-mono bg-cyan-100 px-2 py-1 rounded text-cyan-800">5678901234</span>
              <span className="mx-2">→</span>
              <span className="font-medium">ボールペン 黒 0.7mm（200円）</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}