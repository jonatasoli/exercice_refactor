def validate(_str):
    if _str != None:
        if _str != "":
            if len(_str) >= 11 and len(_str) <= 14:
                _str=_str.replace('.','').replace('.','').replace('-','').replace(" ","")
                if not len(set(_str)) == 1:
                    try:
                        d1 = d2 = 0
                        dg1 = dg2 = rest = 0
                        digito = None
                        nDigResult = None
                            
                        for nCount in range(1, (len(_str) - 1)):
                            # if not int(_str[nCount -1: nCount])
                            # 	return false
                            # else
            
                            digito = int(_str[nCount -1: nCount])  							
                            d1 = d1 + ( 11 - nCount ) * digito  
                    
                            d2 = d2 + ( 12 - nCount ) * digito  
                            
                        rest = (d1 % 11)  
                
                        dg1 = dg1 = 0 if rest < 2 else 11 - rest  
                        d2 += 2 * dg1  
                        rest = (d2 % 11)  
                        if rest < 2:  
                            dg2 = 0  
                        else:  
                            dg2 = 11 - rest  
                
                        nDigVerific = _str[len(_str)-2: len(_str)]  
                        nDigResult = "" + str(dg1) + "" + str(dg2)  
                        return nDigVerific == nDigResult
                    except Exception as e:  
                        print("Erro !"+str(e)  )
            
                        return False
                       
                else:
                    return False
    
            else:
                return False
   


    else:
        return False
