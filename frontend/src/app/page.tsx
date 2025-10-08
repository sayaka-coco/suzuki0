import Link from 'next/link'

export default function Home() {
  return (
    <div className="container mx-auto px-4 py-16">
      <div className="text-center">
        <h1 className="text-4xl font-bold mb-8">POSシステム</h1>
        <div className="space-y-4">
          <Link 
            href="/pos" 
            className="inline-block bg-blue-500 hover:bg-blue-600 text-white font-bold py-3 px-6 rounded-lg text-xl transition-colors"
          >
            POSレジを開く
          </Link>
          <br />
          <Link 
            href="/admin" 
            className="inline-block bg-green-500 hover:bg-green-600 text-white font-bold py-3 px-6 rounded-lg text-xl transition-colors"
          >
            管理画面
          </Link>
        </div>
      </div>
    </div>
  )
}