
from datetime import datetime, date


'''
def check_date(date_lent):
    date_lent = datetime.strptime(date_lent, '%Y-%m-%d')
    today = datetime.now()
    days_borrowed = today.day - date_lent.day   
    period = [0,1,2,3,4,5,6]
    list_of_charges = [[0,0], [0,0], [0,0], [3,0.2], [5,0.4], [5,0.4], [7,0.6]]
    max_count = len(list_of_charges)
    for i in range(max_count):
        if days_borrowed == i or i > 5 :
            penalty = list_of_charges[i][0]
            interest = list_of_charges[i][1]
            return print({'days_overdue':days_borrowed, 'penalty':f'{penalty}%', 'interest_per_day':f'{interest}%'})
'''



'''
def check_date(date_lent, value):
    date_lent = datetime.strptime(date_lent, '%Y-%m-%d')
    today = datetime.now()
    days_borrowed = today.day - date_lent.day   
    list_of_penalties = [0, 0, 0, 3, 5, 5, 7]
    list_of_interest = [1, 1, 1, 0.2, 0.4, 0.4, 0.6]
    list_to_math_interest = [1, 1, 1, 1.02, 1.04, 1.04, 1.06]
    max_penalty = len(list_of_penalties)-1
    index = 0
    while index <= days_borrowed:
        if days_borrowed == index and index <= max_penalty:
            penalty = list_of_penalties[index]
            interest = list_of_interest[index]
        elif days_borrowed == index and index > max_penalty:
            penalty = list_of_penalties[max_penalty]
            interest = list_of_interest[max_penalty]
        elif index < max_penalty:
            value *= list_to_math_interest[index]
        else:
            value *= list_to_math_interest[max_penalty]
        index += 1
    
    return print({'days_overdue':days_borrowed, 'penalty':f'{penalty}%', 'interest_per_day':f'{interest}%', 'value_to_charge':f'R${value}'})


check_date('2021-04-10',1)

'''

    
def check_date(date_lent, value):
   # date_lent = datetime.strptime(date_lent, '%Y-%m-%d')
    print('datelent type:', date_lent)
    print('datelent type:', type(date_lent))
    today = datetime.now()
    days_borrowed = (today - date_lent).days
    list_of_penalties = [0, 0, 0,   3,   4,   5,   7]
    list_of_interest =  [0, 0, 0, 0.2, 0.4, 0.4, 0.6]
    max_penalty = len(list_of_penalties)-1
    index = 0
    while index <= days_borrowed:
        if days_borrowed == index and index <= max_penalty:
            penalty = list_of_penalties[index]
            interest = list_of_interest[index]
            response = math_fine(days_borrowed, penalty, interest, value)
        elif index > max_penalty:
            penalty = list_of_penalties[max_penalty]
            interest = list_of_interest[max_penalty]
            response = math_fine(days_borrowed, penalty, interest, value)
            break
        index += 1

    return print(response)


def math_fine(days_borrowed, penalty, interest, value):
    value *= 1+(penalty/100)
    for index in range(days_borrowed):
        value *= 1+(interest/100)
    return {'days_overdue':days_borrowed, 'penalty':f'{penalty}%', 'interest_per_day':f'{interest}%', 'value_to_charge':f'R${value}'}

check_date('2020-04-20', 1)


'''

#  class 
class Calculate_fine():
    
    def check_date(self, date_lent, value):
        date_lent = datetime.strptime(date_lent, '%Y-%m-%d')
        today = datetime.now()
        days_borrowed = (today - date_lent).days
        list_of_penalties = [0, 0, 0,   3,   4,   5,   7]
        list_of_interest =  [0, 0, 0, 0.2, 0.4, 0.4, 0.6]
        max_penalty = len(list_of_penalties)-1
        index = 0
        while index <= days_borrowed:
            if days_borrowed == index and index <= max_penalty:
                penalty = list_of_penalties[index]
                interest = list_of_interest[index]
                response = self.math_fine(days_borrowed, penalty, interest, value)
            elif index > max_penalty:
                penalty = list_of_penalties[max_penalty]
                interest = list_of_interest[max_penalty]
                response = self.math_fine(days_borrowed, penalty, interest, value)
                break
            index += 1

        return print(response)

    @staticmethod
    def math_fine(days_borrowed, penalty, interest, value):
        value *= 1+(penalty/100)
        for index in range(days_borrowed):
            value *= 1+(interest/100)
        return {'days_overdue':days_borrowed, 'penalty':f'{penalty}%', 'interest_per_day':f'{interest}%', 'value_to_charge':f'R${value}'}



hoje = Calculate_fine()

hoje.check_date('2020-04-20', 1)

'''
