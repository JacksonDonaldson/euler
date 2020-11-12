import math
def b(value, array):
    length =len(array);
    point= math.floor(length/2);
    while array[point] != value:
        #code
        bad=False
        if array[point]<value:
            #print('up from ' + str(point))
            last=point
            point+=math.floor((length-point)/2)
            if last==point:
                return None
            if point-last==1:
                if bad:
                    return None
                bad=True
            #print('to '+str(point))
        if array[point]>value:
            #print('down')
            last=point
            point-=math.ceil(point/2)
            if last==point:
                return None          
            if last-point ==1:
                if bad:
                    return None
                bad=True
    return point
