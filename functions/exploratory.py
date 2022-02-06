

def had_ciruit(year,circuit):
    '''check if a circuit was raced at in a given year'''
    try:
        id = races[(races['year']==year) & (races['circuitref']==circuit)]
        id = id['raceid'].iloc[0].tolist()
        result = isinstance(id, int)
        return result
    except:
        result = False
        return result

def years_no_race(circuit):
    for year in years:
        if had_ciruit(year,circuit)==True:
            pass
        else:
            print(year)