import sys
import json

def maximum_segment_sum_problem_solver(input_file):

    # Find subset with maximum sum.
    # It is can be achivable by taking only positive elements.

    json_open = open(input_file, 'r')
    problem_info = json.load(json_open)

    elems = problem_info['elements']

    print('The problem infomation is read from ', input_file, ' .')
    print('The original set is ', elems, '.')
    print()

    print('Start searching maximum subset sum.')


    subset = []

    for elem in elems:
        if  elem > 0:
            subset.append(elem)

    print('Maximum subset sum is ', sum(subset))
    print('The subset is ', subset)



if __name__ == '__main__':

    input_file = sys.argv[1]
    maximum_segment_sum_problem_solver(input_file)
    
