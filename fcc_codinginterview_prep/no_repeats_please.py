"""
Return the number of total permutations of the provided string that don't have repeated consecutive letters. Assume that all characters in the provided string are each unique.

For example, aab should return 2 because it has 6 total permutations (aab, aab, aba, aba, baa, baa), but only 2 of them (aba and aba) don't have the same letter (in this case a) repeating.
"""
import re
# import regex

def count_repeated_string(test_string: str) -> int:
    reg = "([A-Za-z]{1})\\1"
    # print(re.search(reg, test_string))

    start_list = []
    complete_list = ['']   # Empty string to have a starting point in string generation.

    for char in test_string:
        start_list = complete_list
        complete_list = []
        
        for item in start_list:
            for i in range(len(item)+1):
                new_string = item[0:i] + char + item[i:]
                complete_list.append(new_string)
    
    # print('Done running')
    result_list = list(filter(lambda x: re.search(reg, x)==None, complete_list))
    return len(result_list)

if __name__=="__main__":
    repeated_string_count = count_repeated_string('aaabb')    # 12  Expected answer.
    # repeated_string_count = count_repeated_string('abcdefa')  # 3600  Expected answer.
    # repeated_string_count = count_repeated_string('abfdefa')    # 2640 Expected answer.
    print(repeated_string_count)