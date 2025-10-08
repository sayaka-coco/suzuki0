import { useCallback } from "react";
export function usePurchase(){
  return useCallback(async (payload: unknown)=>{
    const res = await fetch('/api/purchase',{ method:'POST', body: JSON.stringify(payload)});
    if(!res.ok) throw new Error('purchase failed');
    return res.json();
  },[]);
}
