def size_of_str(str):
    # return size of string
    return len(str)

def concat_strings(first, second):
    # return concatination of first and second strings
    return first + second

def duplicate_string(str, copy):
    # return new string which is copy of str copy times
    # example -> duplicate_string('s', 2) == 'ss'
    compy_sum = ""
    for i in range(copy):
    	copy_sum =  copy_sum + str
    return copy_sum

def reverse(str):
    # return reverse of the string
    leng = len(str)
    slicing = str[leng::-1]
    return slicing

p = reverse("")
print(p)
#def is_substring(str, substr):
    # return true if substr is the substring of str, false otherwise