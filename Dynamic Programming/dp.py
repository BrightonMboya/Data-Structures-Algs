def checkMonthCode(month):
    if month.lower() == 'january' or month.lower() == 'october':
        monthCode = 0
    elif month.lower() == 'february' or month.lower() == 'march' or month.lower() == 'november':
        monthCode = 3
    elif month.lower() == 'april' or month.lower() == 'july':
        monthCode = 6
    elif month.lower() == 'may':
        monthCode = 1
    elif month.lower() == 'june':
        monthCode = 4
    elif month.lower() == 'august':
        monthCode = 2
    else:
        monthCode = 5
    return monthCode
    

checkMonthCode('february')
