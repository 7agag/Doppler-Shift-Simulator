def validate_fc(fc, conversion):
    try:
        fc_val = float(fc)
        fc = fc_val if conversion == 0 else fc_val * 1e6 if conversion == 1 else fc_val *1e9
        if fc >= 0:
            return True, "", fc
        return False, "Carrier Frequency should be > 0.", None
    except:
        if(fc == ""):
            return False, "Carrier Frequency Required.", None
        return False, "Carrier Frequency should be a \nnumber.", None
    
def validate_speed(v):
    try:
        v = float(v)
        if v >= 0:
            return True, ""
        return False, "Speed should be > 0."
    except:
        if(v == ""):
            return False, "Speed Required."
        return False, "Speed should be a \nnumber."
    
def validate_angle(angle):
    try:
        angle = float(angle)
        if angle < 0 or angle > 360:
            return False, "Angle should be \nbetween 0 and 360."
        return True, ""
    except:
        if(angle == ""):
            return False, "Angle Frequency Required."
        return False, "Angle should be a\n number."
