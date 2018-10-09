import random

TO_PRIORITIZE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
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
    print(sorted_priorities)
    for i in range(2, len(priorities)):
        next_compare = priorities[i]
        sorted_length = len(sorted_priorities)

        is_even = sorted_length % 2 == 0
        is_odd = sorted_length % 2 != 0

        sorted_start = 0
        sorted_median = int(sorted_length / 2)
        sorted_end = sorted_length - 1
        is_end = check_end(sorted_priorities, sorted_median)

        if is_end is True:
            new_end = sorted_end + 1
            loop_down(next_compare, sorted_median, sorted_end, sorted_length, sorted_priorities)
            print('Loop Count: ' + str(i))
            print('is_end: ' + str(is_end))
            print('Is Even: ' + str(is_even))
            print('Is Odd: ' + str(is_odd))
            print('sorted_start: ' + str(sorted_start))
            print('sorted_median: ' + str(sorted_median))
            print('sorted_end: ' + str(sorted_end))
            print(sorted_priorities)
        elif is_end is False:
            loop_down(next_compare, sorted_median, sorted_end, sorted_length, sorted_priorities)
            print('Loop Count: ' + str(i))
            print('is_end: ' + str(is_end))
            print('Is Even: ' + str(is_even))
            print('Is Odd: ' + str(is_odd))
            print('sorted_start: ' + str(sorted_start))
            print('sorted_median: ' + str(sorted_median))
            print('sorted_end: ' + str(sorted_end))
            print(sorted_priorities)


def loop_down(next_compare, sorted_median, sorted_end, sorted_length, sorted_priorities):
    try:
        for i in range(sorted_length):
            to_compare = sorted_priorities[sorted_median + i]
            print('> Is ' + next_compare + ' more important than ' + to_compare + '?')
            print('> input: n')
    except IndexError:
        to_compare = sorted_priorities[sorted_end]
        new_end = sorted_end + 1
        sorted_priorities.insert(new_end, next_compare)
        print('> ' + next_compare + ' is least important.')
        print('> Inserting ' + next_compare + ' at ' + str(new_end))


def check_end(sorted_priorities, sorted_median):
    try:
        trythis = sorted_priorities[sorted_median + 1]
        return False
    except IndexError:
        return True


SORTED_PRIORITIES = primer(TO_PRIORITIZE, SORTED_PRIORITIES)
print('Primed')
sort_loop(TO_PRIORITIZE, SORTED_PRIORITIES)
