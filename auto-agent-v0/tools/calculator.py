def calculate(expression):
    print('inside calculator')
    try:
        ans = eval(expression)
    except Exception as e:
        ans = 'error'
    return ans