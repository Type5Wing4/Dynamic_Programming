import sys
import json

def subset_sum_problem_solver_by_dynamic_programming(input_file):

    json_open = open(input_file, 'r')
    problem_info = json.load(json_open)

    target = problem_info['target']
    elems = problem_info['elements']

    print('The problem infomation is read from ', input_file, ' .')
    print('The target total sum is ',  target, '.')
    print('The original set is ', elems, '.')
    print()

    records = [-1 for i in range(target+1)]
    records[0] = 0

    solved = False
    for m in elems:

        nega_pos = -1
        for p_i in records[::-1]:
            if p_i != -1:
                i = len(records) + nega_pos 
                if i + m <= target and records[i+m] == -1:
                    records[i+m] = m
                print(i, m, records)
            nega_pos -= 1

            if records[target] != -1:
                solved = True
                break


    if solved:
        subset = []
        i = target
        while(True):
            subset.append(records[i])
            i -= records[i]
            if i == 0:
                break

        print()
        print('A solution has found.')
        print(subset, 'with its sum is ', sum(subset), ' .')

    else:
        print()
        print('There is no solution.')


if __name__ == '__main__':

    input_file = sys.argv[1]
    subset_sum_problem_solver_by_dynamic_programming(input_file)
    
