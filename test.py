def e_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
