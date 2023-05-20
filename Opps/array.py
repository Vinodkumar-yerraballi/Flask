from collections import deque



def array_to_char(array):
    result=deque(maxlen=5)
    output=[]
    for element in array:
        if element in result:
            result.remove(element)
        result.append(element)
        output=list(result)
    return '-'.join(output)
# Testing the function with the given examples
print(array_to_char(["A", "B", "A", "C", "A", "B"]))
print(array_to_char(["A", "B", "C", "D", "E", "D", "Q", "Z", "C"]))

def arrayChannllenge(array):
    one=array.index(1) if 1 in array else array -1
    two=array.index(2) if 2 in array else array -1
    if one==-1 or two==-1:
        return 0
    return abs(one-two) 
print(arrayChannllenge([1, 0, 0, 0, 2, 2, 2]))