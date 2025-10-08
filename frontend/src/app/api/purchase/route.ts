import { NextResponse } from "next/server";

export async function POST(request: Request) {
  try {
    const body = await request.json();

    // バックエンドAPIのURL（環境変数で設定可能）
    const backendUrl = process.env.BACKEND_API_URL || 'http://localhost:8000';
    const response = await fetch(`${backendUrl}/api/purchase`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body)
    });

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
        total_amount: 0,
        transaction_id: 0,
        message: 'バックエンドAPIへの接続に失敗しました'
      },
      { status: 500 }
    );
  }
}
