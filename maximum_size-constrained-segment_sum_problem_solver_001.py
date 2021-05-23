import sys
import json

def maximum_size_constrained_segment_sum_problem_solver(input_file):

    # Find subset with maximum sum, under the constraint that the size of subset,
    # how many elements are in the subset, is given in advance.
    # It is achived by sorting elements and taking larger elements.

    json_open = open(input_file, 'r')
    problem_info = json.load(json_open)

    size_of_subset = problem_info['size of subset']
    elems = problem_info['elements']

    print('The problem infomation is read from ', input_file, ' .')
    print('The original set is ', elems, '.')
    print()

    print('Start searching maximum subset sum,')
    print('under the constraint that the size of subset is ', size_of_subset, '.')


    subset = []

    elems = sorted(elems, reverse=True)


    for i in range(size_of_subset):
        subset.append(elems[i])

    print('Maximum subset sum is ', sum(subset))
    print('The subset is ', subset)



if __name__ == '__main__':

    input_file = sys.argv[1]
    maximum_size_constrained_segment_sum_problem_solver(input_file)
    
