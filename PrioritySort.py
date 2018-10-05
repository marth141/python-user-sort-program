import random
TO_PRIORITIZE = ['A', 'B', 'C', 'D', 'E']
SORTED_PRIORITIES = []


def primer(priorities, sorted_priorities):
    first_item = priorities[0]
    second_item = priorities[1]
    print('Is ' + first_item + ' more important than ' + second_item + '? (y/n)')
    response = input()
    if response == 'y':
        sorted_priorities.append(first_item)
        sorted_priorities.append(second_item)
        return sorted_priorities
    elif response == 'n':
        sorted_priorities.append(second_item)
        sorted_priorities.append(first_item)
        return sorted_priorities


def sort_loop(priorities, sorted_priorities):
    for i in range(2, len(priorities)):
        next_compare = priorities[i]

        is_even = len(sorted_priorities) % 2 == 0
        is_odd = len(sorted_priorities) % 2 != 0

        sorted_start = 0
        sorted_median = int(len(sorted_priorities) / 2)
        sorted_end = len(sorted_priorities) - 1

        if is_even:
            if (len(sorted_priorities)) / 2 == 1:
                sorted_to_compare_start = sorted_priorities[sorted_start]
                sorted_to_compare_end = sorted_priorities[sorted_end]
                print('Is ' + next_compare + ' more important than ' + sorted_to_compare_start + '? (y/n)')
                response = input()
                if response == 'y':
                    insert_point = sorted_priorities.index(sorted_to_compare_start)
                    sorted_priorities.insert(insert_point, next_compare)
                    print(sorted_priorities)
                elif response == 'n':
                    print('Is ' + next_compare + ' more important than ' + sorted_to_compare_end + '? (y/n)')
                    response = input()
                    if response == 'y':
                        insert_point = sorted_priorities.index(sorted_to_compare_end)
                        sorted_priorities.insert(insert_point, next_compare)
                        print(sorted_priorities)
                    elif response == 'n':
                        insert_point = sorted_priorities.index(sorted_to_compare_end) + 1
                        sorted_priorities.insert(insert_point, next_compare)
                        print(sorted_priorities)
            elif (len(sorted_priorities) / 2 > 1):
                sorted_to_compare_start = sorted_priorities[sorted_start]
                sorted_even_middle1 = sorted_priorities[int((sorted_start + 1) * (len(sorted_priorities) / 2) - 1)]
                sorted_even_middle2 = sorted_priorities[int((sorted_start + 1) * (len(sorted_priorities) / 2))]
                sorted_to_compare_end = sorted_priorities[sorted_end]
                print('Is ' + next_compare + ' more important than ' + sorted_even_middle1 + '? (y/n)')
                response = input()
                if response == 'y':
                    print('Is ' + next_compare + ' more important than ' + sorted_to_compare_start + '? (y/n)')
                    response = input()
                    if response == 'y':
                        insert_point = sorted_priorities.index(sorted_to_compare_start)
                        sorted_priorities.insert(insert_point, next_compare)
                        print(sorted_priorities)
                    elif response == 'n':
                        insert_point = sorted_priorities.index(sorted_to_compare_start) + 1
                        sorted_priorities.insert(insert_point, next_compare)
                        print(sorted_priorities)
                elif response == 'n':
                    print('Is ' + next_compare + ' more important than ' + sorted_even_middle2 + '? (y/n)')
                    response = input()
                    if response == 'y':
                        insert_point = sorted_priorities.index(sorted_even_middle2)
                        sorted_priorities.insert(insert_point, next_compare)
                        print(sorted_priorities)
                    elif response == 'n':
                        print('Is ' + next_compare + ' more important than ' + sorted_to_compare_end + '? (y/n)')
                        response = input()
                        if response == 'y':
                            insert_point = sorted_priorities.index(sorted_to_compare_end) + 1
                            sorted_priorities.insert(insert_point, next_compare)
                            print(sorted_priorities)
                        elif response == 'n':
                            insert_point = sorted_priorities.index(sorted_to_compare_end) + 1
                            sorted_priorities.insert(insert_point, next_compare)
                            print(sorted_priorities)
        elif is_odd:
            sorted_to_compare_median = sorted_priorities[sorted_median]
            print('Is ' + next_compare + ' more important than ' + sorted_to_compare_median + '? (y/n)')
            response = input()
            if response == 'y':
                sorted_to_compare_end = sorted_priorities[sorted_median - 1]
                print('Is ' + next_compare + ' more important than ' + sorted_to_compare_end + '? (y/n)')
                response = input()
                if response == 'y':
                    insert_point = sorted_priorities.index(sorted_to_compare_end)
                    sorted_priorities.insert(insert_point, next_compare)
                    print(sorted_priorities)
                elif response == 'n':
                    insert_point = sorted_priorities.index(sorted_to_compare_end) + 1
                    sorted_priorities.insert(insert_point, next_compare)
                    print(sorted_priorities)
            elif response == 'n':
                sorted_to_compare_end = sorted_priorities[sorted_median + 1]
                print('Is ' + next_compare + ' more important than ' + sorted_to_compare_end + '? (y/n)')
                response = input()
                if response == 'y':
                    insert_point = sorted_priorities.index(sorted_to_compare_end)
                    sorted_priorities.insert(insert_point, next_compare)
                    print(sorted_priorities)
                elif response == 'n':
                    insert_point = sorted_priorities.index(sorted_to_compare_end) + 1
                    sorted_priorities.insert(insert_point, next_compare)
                    print(sorted_priorities)


SORTED_PRIORITIES = primer(TO_PRIORITIZE, SORTED_PRIORITIES)
print(SORTED_PRIORITIES)
sort_loop(TO_PRIORITIZE, SORTED_PRIORITIES)
