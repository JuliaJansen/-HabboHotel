
import math

list afstandenx = []
list afstandeny = []
list minafstand = []
list waardes = []
list afstandschuin = []
#loop over alle houses heen
for (i=0; i < len(houses); i++):
    for (j = 0; j < len(houses); j++):
        # check eerst of huis je boven dit huis ligt
        if houses[j].y_min + houses[j].height > houses[i].y_min and houses[j].y_min < houses[i].y_min + houses[i].height and houses[j].y_min !== houses[i].y_min:
            
            # twee berekeningen, een voor links een voor rechts
            if houses[j].x_min > houses[i].x_min:
                afstand = houses[j].x_min - houses[i].x_min - houses[i].width - houses[i].freespace 
            else:
                afstand = houses[i].x_min - houses[j].x_min - houses[j].width - houses[i].freespace 

            afstandenx.append(afstand)
                
        # fake value to fill up list
        else:
            afstandenx.append(10000)
        
        # check eerst of huis j naast dit huis ligt        
        if houses[j].x_min + houses[j].width > houses[i].x_min and houses[j].x_min < houses[i].x_min + houses[i].width and houses[j].x_min !== houses[i].x_min:
        
            # twee berekeningen, een voor onder een voor boven
            if houses[j].y_min > houses[i].y_min:
                afstand = houses[j].y_min - houses[i].y_min - houses[i].height - houses[i].freespace 
            else:
                afstand = houses[i].y_min - houses[j].y_min - houses[j].height - houses[i].freespace 
            
            afstandeny.append(afstand)
        else:
            afstandeny.append(10000)
        
        if houses[j].x_min >= houses[i].x_max and houses[j].y_min >= houses[i].y_max:
            a = houses[j].x_min - houses[i].x_max - houses[i].freespace
            b = houses[j].y_min - houses[i].y_max - houses[i].freespace
            c = (a**2 + b**2)**0.5
            afstandschuin.append(c)
        elif houses[j].x_min >= houses[i].x_max and houses[j].y_max <= houses[i].y_min:
            a = houses[j].x_min - houses[i].x_max - houses[i].freespace
            b = houses[i].y_min - houses[j].y_max - houses[i].freespace
            c = (a**2+b**2)**0.5
            afstandschuin.append(c)
        elif houses[j].x_max <= houses[i].x_min and houses[j].y_min >= houses[i].y_max:
            a = houses[i].x_min - houses[j].x_max - houses[i].freespace
            b = houses[j].y_min - houses[i].y_max - houses[i].freespace
            c = (a**2 + b**2)**0.5
            afstandschuin.append(c)
        elif houses[j].x_max <= houses[i].x_min and houses[j].y_max <= houses[i].y_min:
            a = houses[i].x_min - houses[j].x_max - houses[i].freespace
            b = houses[i].y_min - houses[j].y_max - houses[i].freespace
            c = (a**2 + b**2)**0.5
            afstandschuin.append(c)
        else:
            afstandschuin.append(10000)
    
    
    # minimum distance is the only one relevant to value
    minafst = min(min(afstandenx), min(afstandeny), min(afstandschuin                       ))
    
    # check the type of house to determine the value
    if houses[i].type_huis == egw:
        waarde = 285000 * (1+(0.03*minafst))
    else if houses[i].type_huis == bung:
        waarde = 399000 * (1+(0.04*minafst))
    else if houses[i].type_huis == mais:
        waarde = 610000 * (1+(0.06*minafst))
    
    # save the free space and value into a list
    minafstand.append(minafst)
    waardes.append(waarde)
    del afstandschuin[:] 
    del afstandenx[:]
    del afstandeny[:]

# sum all the values
totalewaarde = sum(waardes)