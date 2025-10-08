import { useEffect, useState } from "react";
import type { Product } from "@/lib/types";
export function useProducts(){
  const [data,setData] = useState<Product[]>([]);
  useEffect(()=>{ fetch('/api/products').then(r=>r.json()).then(d=>setData(d.products||[])) },[]);
  return data;
}
