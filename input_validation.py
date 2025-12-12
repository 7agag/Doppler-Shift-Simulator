class InputValidator:
    @staticmethod
    def validate_fc(fc, conversion):
        try:
            fc_val = float(fc)
            if conversion == 0:
                fc = fc_val
            elif conversion == 1:
                fc = fc_val * 1e6
            elif conversion == 2:
                fc = fc_val * 1e9
            else:
                return False, "Invalid unit conversion.", None

            if fc > 0:
                return True, "", fc
            return False, "Carrier Frequency should be > 0.", None
        except ValueError:
            if fc == "":
                return False, "Carrier Frequency Required.", None
            return False, "Carrier Frequency should be a number.", None

    @staticmethod
    def validate_speed(v):
        try:
            v = float(v)
            if v >= 0:
                return True, "", v
            return False, "Speed should be > 0.", None
        except ValueError:
            if v == "":
                return False, "Speed Required.", None
            return False, "Speed should be a number.", None

    @staticmethod
    def validate_angle(angle):
        try:
            angle = float(angle)
            if angle < 0 or angle > 360:
                return False, "Angle should be between 0 and 360.", None
            return True, "", angle
        except ValueError:
            if angle == "":
                return False, "Angle Required.", None
            return False, "Angle should be a number.", None
