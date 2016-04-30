def afstand(house, houses): 
    
    del afstandschuin[:] 
    del afstandenx[:]
    del afstandeny[:]
    
    for (j = 0; j < len(houses); j++):
        # check eerst of huis je boven of onder dit huis ligt
        if houses[j].y_max > house.y_min and houses[j].y_min < house.y_max:
            
            # twee berekeningen, een voor links een voor rechts
            if houses[j].x_min > house.x_min:
                afstand = houses[j].x_min - house.x_min - house.width - house.freespace 
            else:
                afstand = house.x_min - houses[j].x_min - houses[j].width - house.freespace 

            afstandenx.append(afstand)
                
        # fake value to fill up list
        else:
            afstandenx.append(10000)
        
        # check eerst of huis j naast dit huis ligt        
        if houses[j].x_max > house.x_min and houses[j].x_min < house.x_max:
        
            # twee berekeningen, een voor onder een voor boven
            if houses[j].y_min > house.y_min:
                afstand = houses[j].y_min - house.y_min - house.height - house.freespace 
            else:
                afstand = house.y_min - houses[j].y_min - houses[j].height - house.freespace 
            afstandeny.append(afstand)
            
        else:
            afstandeny.append(10000)
        
        if houses[j].x_min >= house.x_min and houses[j].y_min >= house.y_min:
            a = houses[j].x_min - house.x_max - house.freespace
            b = houses[j].y_min - house.y_max - house.freespace
        elif houses[j].x_min >= house.x_min and houses[j].y_min <= house.y_min:
            a = houses[j].x_min - house.x_max - house.freespace
            b = house.y_min - houses[j].y_max - house.freespace
        elif houses[j].x_min <= house.x_min and houses[j].y_min >= house.y_min:
            a = house.x_min - houses[j].x_max - house.freespace
            b = houses[j].y_min - house.y_max - house.freespace
        elif houses[j].x_min <= house.x_min and houses[j].y_min <= house.y_min:
            a = house.x_min - houses[j].x_max - house.freespace
            b = house.y_min - houses[j].y_max - house.freespace
        else:
            afstandschuin.append(10000)
        if a > 0 and b > 0:
            c = (a**2 + b**2)**0.5
            afstandschuin.append(c)
        else:
            c = -1


# minimum distance is the only one relevant to value
minafst = min(min(afstandenx), min(afstandeny), min(afstandschuin))

# save closest neighbour of house


return minafst
    