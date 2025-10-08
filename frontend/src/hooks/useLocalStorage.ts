import { useEffect, useState } from "react";
export function useLocalStorage<T>(key:string, initial:T){
  const [v,setV] = useState<T>(initial);
  useEffect(()=>{ const s = localStorage.getItem(key); if(s) setV(JSON.parse(s)); },[key]);
  useEffect(()=>{ localStorage.setItem(key, JSON.stringify(v)); },[key,v]);
  return [v,setV] as const;
}
