import myfile

def test_sum():
    assert myfile.array_sum([1,2,3]) == 6

def test_sum_fail():
    assert myfile.array_sum([1,2,3]) == 7