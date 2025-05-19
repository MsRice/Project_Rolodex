def bmi_calc(weight , w_unit , height , h_unit):
    ## This functions' default is kilograms and meters
    if w_unit == 'lbs':
        weight =  weight * 0.45359237

    if h_unit == 'inches':
        height = height * 0.0254

    ##BMI == weight kg / height m^2
    return weight /  height ** 2

rice = {
    "weight" : 175,
    "w_unit" : "lbs",
    "height" : 63,
    'h_unit' : 'inches'
}

print(bmi_calc(rice['weight'], rice['w_unit'] , rice['height'] , rice['h_unit']))