import { NextResponse } from 'next/server'
import { sampleProducts } from '@/data/sampleProducts'

export async function GET() {
  return NextResponse.json(sampleProducts)
}