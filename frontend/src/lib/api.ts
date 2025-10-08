const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

export async function fetcher<T>(url: string, init?: RequestInit): Promise<T>{
  const fullUrl = url.startsWith('http') ? url : `${API_BASE_URL}${url}`
  const res = await fetch(fullUrl, init);
  if(!res.ok) throw new Error('Request failed');
  return res.json() as Promise<T>;
}

// バックエンドAPI型定義
export interface ApiProduct {
  PRD_ID: number
  CODE: string
  NAME: string
  PRICE: number
}

export interface ProductSearchResponse {
  success: boolean
  product: ApiProduct | null
  message: string
}

export interface PurchaseItemRequest {
  PRD_ID: number
  PRD_CODE: string
  PRD_NAME: string
  PRD_PRICE: number
}

export interface PurchaseRequest {
  EMP_CD?: string
  STORE_CD?: string
  POS_NO?: string
  items: PurchaseItemRequest[]
}

export interface PurchaseResponse {
  success: boolean
  total_amount: number
  transaction_id: number
  message: string
}

// API関数
export async function searchProduct(code: string): Promise<ProductSearchResponse> {
  return fetcher<ProductSearchResponse>(`/api/products/${code}`)
}

export async function createPurchase(purchaseData: PurchaseRequest): Promise<PurchaseResponse> {
  return fetcher<PurchaseResponse>('/api/purchase', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(purchaseData)
  })
}
