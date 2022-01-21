import mypkg.misc.bit_manipulation as bm


def test_count_bits():
    assert bm.count_bits(7) == 3
    assert bm.count_bits(8) == 4
    assert bm.count_bits(65) == 7

    assert bm.count_bits2(7) == 3
    assert bm.count_bits2(8) == 4
    assert bm.count_bits2(65) == 7


def test_bitwise_complement():
    assert bm.bitwise_complement(5) == 2
    assert bm.bitwise_complement(7) == 0
    assert bm.bitwise_complement(10) == 5
    assert bm.bitwise_complement(0) == 1
    assert bm.bitwise_complement(1) == 0

    assert bm.bitwise_complement2(5) == 2
    assert bm.bitwise_complement2(7) == 0
    assert bm.bitwise_complement2(10) == 5
    assert bm.bitwise_complement2(0) == 1
    assert bm.bitwise_complement2(1) == 0


def test_generate_padded_binary():
    assert bm.generate_padded_binary(3) == ["00", "01", "10"]
    assert bm.generate_padded_binary(6) == ["000", "001", "010", "011", "100", "101"]
    assert bm.generate_padded_binary(9) == ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000"]
