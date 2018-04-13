list_of_ages = [12, 13, 61, 83, 20, 7, 45, 2]


def calculate_avg(list_of_ages):
    print('Given list of peoples ages: ' + str(list_of_ages))
    sum = 0
    adults = [sum + age for age in list_of_ages if age >= 18]
    for i in range(len(adults)):
        sum += adults[i]
    avg_age_of_adults = sum / len(adults)
    print('Averge number of adults age: ' + str(avg_age_of_adults))
    print('Nuber of children: ' + str(len(list_of_ages) - len(adults)))


calculate_avg(list_of_ages)
