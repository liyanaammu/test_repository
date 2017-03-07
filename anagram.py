import sys

def check_anagram(input1, input2):
    '''
    @description:
        Function to check if the given two strings are anagram or not
    @params:
        Two string inputs
    @return:
        Returns if the strings are anagram or not
    '''
    if input1.lower() == input2.lower():
	    return "Not an anagram"
    elif count_occurrence(input1.lower()) == count_occurrence(input2.lower()):
        return "An anagram"
    else:
        return "Not an anagram"		

def count_occurrence(input_str):
    '''
    @description:
        Function to count the occurrence of each letter in a string
    @param:
        Input string
    @return:
        Dict of count of occurrences of each letters in the given string
    '''
    count_occurrence_dict = {}
    for char in input_str:
        count_occurrence_dict[char] = input_str.count(char) 	
    return count_occurrence_dict		
	
if __name__=='__main__':
    try:
        print check_anagram(sys.argv[1],sys.argv[2])
    except IndexError:
        ret_argv = len(sys.argv)
        print "\t Usage: anagram.py [input_string1] [input_string2] \n"
        if ret_argv == 1:
            print "[input_string1] [input_string2]"
        elif ret_argv == 2:
            print "[input_string2]"
