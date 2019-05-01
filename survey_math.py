import math

def CosI1(inc_1):
    cos_inc_1 = math.cos(math.radians(inc_1))
    return(cos_inc_1)

def CosI2(inc_2):
    cos_inc_2 = math.cos(math.radians(inc_2))
    return(cos_inc_2)

def CosA1(az_1):
    cos_az_1 = math.cos(math.radians(az_1))
    return(cos_az_1)

def CosA2(az_2):
    cos_az_2 = math.cos(math.radians(az_2))
    return(cos_az_2)

def SinI1(inc_1):
    sin_inc_1 = math.sin(math.radians(inc_1))
    return(sin_inc_1)

def SinI2(inc_2):
    sin_inc_2 = math.sin(math.radians(inc_2))
    return(sin_inc_2)

def SinA1(az_1):
    sin_az_1 = math.sin(math.radians(az_1))
    return(sin_az_1)

def SinA2(az_2):
    sin_az_2 = math.sin(math.radians(az_2))
    return(sin_az_2)

def DlFormDeg(inc_2,inc_1,one,az_2,az_1):
    dls_d = math.degrees(math.acos(((math.cos(math.radians(inc_2 - inc_1))) - (math.sin(math.radians(inc_1 * math.sin(math.radians(inc_2))))) * (one-(math.cos(math.radians((az_2 - az_1))))))))
    return(dls_d)

def DlFormRad(inc_2,inc_1,one,az_2,az_1):
    dls_r = math.acos(((math.cos(math.radians(inc_2 - inc_1))) - (math.sin(math.radians(inc_1 * math.sin(math.radians(inc_2))))) * (one-(math.cos(math.radians((az_2 - az_1)))))))
    return(dls_r)

def RatioFactor(two,dls_r,dls_d):
    rf = (two / dls_r) * math.tan(math.radians((dls_d / two)))
    return(rf)

def NorthSouth(cl,two,inc_1,az_1,inc_2,az_2,rf):
    north_south = (cl / two) * (math.sin(math.radians(inc_1)) * math.cos(math.radians(az_1)) + math.sin(math.radians(inc_2)) * math.cos(math.radians(az_2))) * rf
    return(north_south)

def EastWest(cl,two,inc_1,az_1,inc_2,az_2,rf):
    east_west = (cl / two) * (math.sin(math.radians(inc_1)) * math.sin(math.radians(az_1)) + math.sin(math.radians(inc_2)) * math.sin(math.radians(az_2))) * rf
    return(east_west)

def TVD(cl,two,inc_1,inc_2,rf):
    true_vertical_depth = (cl / two) * (math.cos(math.radians(inc_1)) + math.cos(math.radians(inc_2))) * rf
    return(true_vertical_depth)

def VS(cl,two,inc_1,inc_2,rf):
    vertical_section = (cl / two) * (math.sin(math.radians(inc_1)) + math.sin(math.radians(inc_2))) * rf
    return(vertical_section)
