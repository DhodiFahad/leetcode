from sum import my2sum


# Example 1:
def test_1():
    nums = [2,7,11,15]
    target = 9
    assert my2sum(nums, target) == [0,1]


def test_2():
    nums = [3,2,4]
    target = 6
    assert my2sum(nums, target) ==  [1,2]


def test_3():
    nums = [3,3]
    target = 6
    assert my2sum(nums, target) == [0,1]