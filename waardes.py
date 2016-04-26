
import math

list afstandenx = []
list afstandeny = []
list hoeveelnaast = []
list hoeveelboven = []
#loop over alle huizen heen
for (j = 0; j < len(huizen); j++)
    # check eerst of huis je boven dit husi ligt
    if huizen[j].y_min + height + freespace > y_min && huizen[j].y_min < y_min + height + freespace
        
        # twee berekeningen, een voor links een voor rechts
        if huizen[j].x_min > x_min
            afstandenx[j] = huizen[j].x_min - x_min - width - freespace
        else
            afstandenx[j] = huizen[j].x_min + x_min - width - freespace
        
        # bereken hoeveel blokjes v/d grid er naast het huis liggen
        if huizen[j].y_min > y_min
            hoeveelnaast[j] = y_min - huizen[j].y_min +height + freespace
        else
            hoeveelnaast[j] = huizen[j].y_min - y_min + height + freespace
    
    # check eerst of huis j naast dit huis ligt        
    if huizen[j].x_min + width + freespace > x_min && huizen[j].x_min < x_min + width + freespace
        
        # twee berekeningen, een voor onder een voor boven
        if huizen[j].y_min > y_min
            afstandeny[j] = huizen[j].y_min - y_min - height - freespace
        else
            afstandeny[j] = huizen[j].y_min + y_min - height - freespace
        
        # bereken hoeveel blokjes v/d grid er boven het huis liggen
        if huizen[j].x_min > x_min
            hoeveelboven[j] = x_min - huizen[j].x_min +width + freespace
        else
            hoeveelboven[j] = huizen[j].x_min - x_min + width + freespace

    