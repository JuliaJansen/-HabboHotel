
import math

list afstandenx = []
list afstandeny = []
list minafstand = []
list waardes = []
#loop over alle huizen heen
for (i=0; i < len(huizen); i++):
    for (j = 0; j < len(huizen); j++):
        # check eerst of huis je boven dit huis ligt
        if huizen[j].y_min + height > huizen[i].y_min && huizen[j].y_min < huizen[i].y_min + height && huizen[j].y_min !== huizen[i].y_min:
            
            # twee berekeningen, een voor links een voor rechts
            if huizen[j].x_min > huizen[i].x_min:
                afstand = huizen[j].x_min - huizen[i].x_min - width - freespace
                afstandenx.append(afstand)
            else:
                afstand = huizen[j].x_min + huizen[i].x_min - width - freespace
                afstandenx.append(afstand)
                
        # fake value to fill up list
        else:
            afstandenx.append(10000)
        
        # check eerst of huis j naast dit huis ligt        
        if huizen[j].x_min + width > huizen[i].x_min && huizen[j].x_min < huizen[i].x_min + width && huizen[j].x_min !== huizen[i].x_min:
        
            # twee berekeningen, een voor onder een voor boven
            if huizen[j].y_min > huizen[i].y_min:
                afstand = huizen[j].y_min - huizen[i].y_min - height - freespace
                afstandeny.append(afstand)
            else:
                afstand = huizen[j].y_min + huizen[i].y_min - height - freespace
                afstandeny.append(afstand)
        else:
            afstandeny.append(10000)
    
    # minimum distance is the only one relevant to value
    minafst = min(min(afstandenx), min(afstandeny))
    
    # check the type of house to determine the value
    if huizen[i].type_huis == EGW:
        waarde = 285000 * (1+(0.03*minafst))
    else if huizen[i].type_huis == BUNG:
        waarde = 399000 * (1+(0.04*minafst))
    else if huizen[i].type_huis == MAIS:
        waarde = 610000 * (1+(0.06*minafst))
    
    # save the free space and value into a list
    minafstand.append(minafst)
    waardes.append(waarde)

# sum all the values
totalewaarde = sum(waardes)