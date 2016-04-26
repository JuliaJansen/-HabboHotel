def afstand(house, houses): 
    
    del afstandschuin[:] 
    del afstandenx[:]
    del afstandeny[:]
    
    for j = 0; j < len(houses); j++:
        # check eerst of huis je boven of onder dit huis ligt
        if houses[j].y_max > house.y_min and houses[j].y_min < house.y_max:
            
            # twee berekeningen, een voor links een voor rechts
            if houses[j].x_min > house.x_min:
                afstand = houses[j].x_min - house.x_min - house.width 
            else:
                afstand = house.x_min - houses[j].x_min - houses[j].width 

            afstandenx.append(afstand)
                
        # fake value to fill up list
        else:
            afstandenx.append(10000)
        
        # check eerst of huis j naast dit huis ligt        
        if houses[j].x_max > house.x_min and houses[j].x_min < house.x_max:
        
            # twee berekeningen, een voor onder een voor boven
            if houses[j].y_min > house.y_min:
                afstand = houses[j].y_min - house.y_min - house.height  
            else:
                afstand = house.y_min - houses[j].y_min - houses[j].height  
            afstandeny.append(afstand)
            
        else:
            afstandeny.append(10000)
        
        if houses[j].x_min >= house.x_min and houses[j].y_min >= house.y_min:
            a = houses[j].x_min - house.x_max 
            b = houses[j].y_min - house.y_max 
            c = (a**2 + b**2)**0.5
            afstandschuin.append(c)
        elif houses[j].x_min >= house.x_min and houses[j].y_min <= house.y_min:
            a = houses[j].x_min - house.x_max 
            b = house.y_min - houses[j].y_max 
            c = (a**2 + b**2)**0.5
            afstandschuin.append(c)
        elif houses[j].x_min <= house.x_min and houses[j].y_min >= house.y_min:
            a = house.x_min - houses[j].x_max 
            b = houses[j].y_min - house.y_max 
            c = (a**2 + b**2)**0.5
            afstandschuin.append(c)
        elif houses[j].x_min <= house.x_min and houses[j].y_min <= house.y_min:
            a = house.x_min - houses[j].x_max 
            b = house.y_min - houses[j].y_max 
            c = (a**2 + b**2)**0.5
            afstandschuin.append(c)
        else:
            afstandschuin.append(10000)
        
    # minimum distance is the only one relevant to value
    minafstx = min(afstandenx)
    minafsty = min(afstandeny)
    minafstschuin = min(afstandschuin)

    minafst = min(minafstx,minafsty,minafstschuin)

    # save closest neighbour of house
    if minafst == minafstx:
        closest = afstandenx.index(minafstx)
    elif minafst == minafsty:
        closest = afstandeny.index(minafsty)
    elif minafst == minafstschuin
        closest = afstandschuin.index(minafstschuin)

    neighbour = houses[closest]
    if house.freespace > neighbour.freespace:
    freespace = house.freespace
    else:
    freespace = neighbour.freespace

    if minafst < freespace:
    return minafst - freespace

    # update closest neighbour of house
    house.distance = minafst
    house.neighbour = neighbour

    if neighbour.distance > minafst:
    neighbour.distance = minafst
    neighbour.neighbour = house

    return minafst
    