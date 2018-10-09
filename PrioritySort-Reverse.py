import random

TO_PRIORITIZE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
SORTED_PRIORITIES = []


def prioritize(to_prioritize, sorted_priorities):
    print('=== prioritize Inputs ===')
    print('input: ' + str(to_prioritize))
    print('input: ' + str(sorted_priorities))

    # Get positions
    compare(to_prioritize, sorted_priorities)


def compare(to_prioritize, sorted_priorities):
    # Compare to prioritize 1 and 2
    positions = Positions(to_prioritize, sorted_priorities)
    to_compare_a = to_prioritize[1]
    to_compare_b = to_prioritize[0]
    sorted_priorities = seed_sorted_list(to_compare_a, to_compare_b, positions, sorted_priorities)
    sort_the_rest(to_prioritize, sorted_priorities, positions)


def sort_the_rest(to_prioritize, sorted_priorities, positions):
    print(sorted_priorities)

    i = 2
    while i < positions.unsorted_priorities.end:
        last_response = ''
        positions = Positions(to_prioritize, sorted_priorities)
        to_compare_a = to_prioritize[i]
        j = positions.sorted_priorities.median
        while j < positions.sorted_priorities.end:
            if j >= 0:
                print('j: ' + str(j))
                to_compare_b = sorted_priorities[j]
                compare_message(to_compare_a, to_compare_b)
                response = get_input()
                input_message(response)
                if last_response == '':
                    if response == 'n':
                        last_response = response
                        j += 1
                    if response == 'y':
                        last_response = response
                        j -= 1
                elif last_response == 'n':
                    if response == 'y':
                        break
                    if response == 'n':
                        last_response = response
                        j += 1
                elif last_response == 'y':
                    if response == 'n':
                        break
                    if response == 'y':
                        last_response = response
                        j -= 1
            elif j < 0:
                break
        end = True
        if end is True:
            if response == 'n':
                if j == positions.sorted_priorities.end:
                    sorted_priorities.insert(j + 1, to_compare_a)
                    print(sorted_priorities)
                else:
                    sorted_priorities.insert(j + 1, to_compare_a)
                    print(sorted_priorities)
            if response == 'y':
                if j < 0:
                    sorted_priorities.insert(positions.sorted_priorities.start, to_compare_a)
                    print(sorted_priorities)
                else:
                    sorted_priorities.insert(j, to_compare_a)
                    print(sorted_priorities)
        i += 1


def seed_sorted_list(to_compare_a, to_compare_b, positions, sorted_priorities):
    compare_message(to_compare_a, to_compare_b)
    response = get_input()
    input_message(response)
    if response == 'n':
        if (positions.sorted_priorities.end == positions.sorted_priorities.median):
            sorted_priorities.insert(positions.sorted_priorities.end, to_compare_a)
            sorted_priorities.insert(positions.sorted_priorities.end, to_compare_b)
            return sorted_priorities
    elif response == 'y':
        if (positions.sorted_priorities.end == positions.sorted_priorities.median):
            sorted_priorities.insert(positions.sorted_priorities.end, to_compare_b)
            sorted_priorities.insert(positions.sorted_priorities.end, to_compare_a)
            return sorted_priorities


class Position:
    def __init__(self, array_to_get):
        array_length = len(array_to_get)
        self.start = 0
        self.median = int(array_length / 2)
        self.end = array_length


class Positions:
    def __init__(self, to_sort_array, end_array):
        self.unsorted_priorities = Position(to_sort_array)
        self.sorted_priorities = Position(end_array)
        print('sorted_positions start: ' + str(self.sorted_priorities.start))
        print('sorted_positions median: ' + str(self.sorted_priorities.median))
        print('sorted_positions end: ' + str(self.sorted_priorities.end))
        print('unsorted_positions start: ' + str(self.unsorted_priorities.start))
        print('unsorted_positions median: ' + str(self.unsorted_priorities.median))
        print('unsorted_positions end: ' + str(self.unsorted_priorities.end))


def yes_no(response):
    if response == 'y':
        print('> input: ' + response)
        return
    elif response == 'n':
        print('> input: ' + response)
        return


def compare_message(compare_a, compare_b):
    print('> Is ' + compare_a + ' more important than ' + compare_b + '? (y/n)')
    return


def input_message(response):
    print('> input: ' + response)
    return


def get_input():
    response = input()
    return response


prioritize(TO_PRIORITIZE, SORTED_PRIORITIES)
