""" Converting between temperature scales

        Fahrenheit
        Celsius
        Kelvin
        others ...
"""


def celsius_to_fahrenheit(t_celsius):
    """ Convert a temperature from the Fahrenheit scale to Celsius

    :param t_celsius: The temperature in degrees Celsius
    :return: The equivalent temperature in degrees Fahrenheit"""
    t_fahrenheit = t_celsius * 9 / 5 + 32
    return t_fahrenheit


def fahrenheit_to_celsius(t_fahrenheit):
    """ Convert a temperature from the Celsius scale to Fahrenheit

    :param t_celsius: The temperature in degrees Celsius
    :return: The equivalent temperature in degrees Fahrenheit """
    t_celsius =  (t_fahrenheit - 32) * 5 / 9
    return t_celsius


# let's have some handy nicknames for these 'big' functions
c2f = celsius_to_fahrenheit
f2c = fahrenheit_to_celsius
