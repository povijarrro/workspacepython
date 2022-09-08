#!python
class Solution:
    def myAtoi(self, s: str) -> int:
        stripped=s.strip()
        if stripped=="" or stripped =="+" or stripped=="-":
            return 0
        goodS=stripped[0] if stripped[0] in ["+", "-"] else ""
       
        
        
        for ch in (stripped[1:] if goodS else stripped):
            if ch not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                if goodS=="" or goodS=="-" or goodS=="+":
                    return 0
                goodS = goodS[1:] if goodS[0]=="+" else goodS
                print(goodS)
                return 0 if not goodS else min(max(int(goodS),-2**31),2**31-1)
            else:
                goodS+=ch     
        return 0 if not goodS else min(max(int(goodS),-2**31),2**31-1)      
            
    
        