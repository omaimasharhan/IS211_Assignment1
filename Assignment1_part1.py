#PART 1
def list_divide(numbers, divide = 2):
    elements = 0
    for num in numbers:
        if num % divide == 0:
            elements +=1
    return elements
class ListDivideException(Exception):
    pass
def test_list_divide():
    try:
        assert list_divide([1, 2, 3, 4, 5]) == 2
        assert list_divide([2, 4, 6, 8, 10]) == 5
        assert list_divide([30, 54, 63, 98, 100], divide=10) == 2
        assert list_divide([]) == 0
        assert list_divide([1, 2, 3, 4, 5], 1) == 5
    except AssertionError:
        raise ListDivideException ("Test Faile9999d")

test_list_divide()
