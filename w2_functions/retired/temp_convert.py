# Convert temperatures from one scale to another


def celsius_to_fahrenheit(t_celsius):
    t_fahrenheit = t_celsius * 9 / 5 + 32
    return t_fahrenheit


def fahrenheit_to_celsius(t_fahrenheit):
    t_celsius =  (t_fahrenheit - 32) * 5 / 9
    return t_celsius

# let's have some handy nicknames for these 'big' functions
c2f = celsius_to_fahrenheit
f2c = fahrenheit_to_celsius
