export interface Product {
  id?: number
  code: string
  name: string
  price: number
}

export interface PurchaseItem extends Product {
  quantity: number
  total: number
}

export interface Transaction {
  id: string
  items: PurchaseItem[]
  totalAmount: number
  timestamp: Date
}