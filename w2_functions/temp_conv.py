# Temperature Conversions - part I

def k2r(kelvin):
    """Degrees Kelvin to Rankine"""
    return kelvin * 9/5

def r2f(rankine):
    """Degrees Rankine to Fahrenheit"""
    return rankine - 459.67

def f2c(fahrenheit):
    """Degrees Fahrenheit to Celsius"""
    return (fahrenheit-32)*5/9

def c2k(centigrade):
    """Degrees Celsius to Kelvin"""
    return centigrade + 273.15
    

 
# Temperature Conversions - part II

def k2c(kelvin):
    """Degrees Celsius to Rankine - using ONLY above functions"""
    return f2c(r2f(k2r(kelvin)))

def f2r(fahrenheit):
    """Degrees Fahrenheit to Rankine - using ONLY above functions"""
    return k2r(c2k(f2c(fahrenheit)))

