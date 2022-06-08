from mypkg.company.microsoft import max_num


def test_max_sum():
    # nums = [(15958, 1958), 15258, 5000, -5000, -15958, -15258, 125, -125, 5, -5, 1256, 1525, -1525]
    # expected_nums = [1958, 1528, 0, 0, -1598, -1258, 12, -12, 0, 0, 126, 152, -125]
    assert max_num(15958) == 1958
    assert max_num(-1500) == -100
    # for i in range(len(nums)):
    #     assert max_num(nums[i]) == expected_nums[i]
