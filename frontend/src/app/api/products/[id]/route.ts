import { NextResponse } from "next/server";

export async function GET(_: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;

  try {
    // バックエンドAPIのURL（環境変数で設定可能）
    const backendUrl = process.env.BACKEND_API_URL || 'http://localhost:8000';
    const response = await fetch(`${backendUrl}/api/products/${id}`);

    if (!response.ok) {
      throw new Error(`Backend API returned ${response.status}`);
    }

    const data = await response.json();
    return NextResponse.json(data);

  } catch (error) {
    console.error('Backend API error:', error);
    return NextResponse.json(
      {
        success: false,
        product: null,
        message: 'バックエンドAPIへの接続に失敗しました'
      },
      { status: 500 }
    );
  }
}
