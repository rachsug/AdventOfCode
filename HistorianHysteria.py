from collections import Counter

def historian_hysteria():
    f = open('day1_input.txt', 'r')
    data = f.read()
    pairs_of_data = data.split('\n')
    list_length = len(pairs_of_data)
    list_1 = [] 
    list_2 = []

    for pairs in pairs_of_data:
        list_1.append(pairs[:5])
        list_2.append(pairs[-5:])

    list_1.sort()
    list_2.sort()

    ### Part 1
    distance = []
    for i in range(list_length):
        distance.append(abs(int(list_1[i]) - int(list_2[i])))
    
    res = sum(distance)

    ### Part 2
    amount_of_numbers = Counter(list_2)
    mul = 0
    res = 0
    for i in range(list_length):
        if list_1[i] in amount_of_numbers.keys():
            mul = int(list_1[i]) * int(amount_of_numbers[list_1[i]])
            res += mul
        
    return print(res)
    

historian_hysteria()