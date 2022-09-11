from mypkg.misc.tic_tac_toe import TicTacToe, TicTacToeOpt


def test_tic_tac_toe():
    obj = TicTacToe(3)
    assert obj.move(0, 0, 1) == 0
    assert obj.move(0, 2, 2) == 0
    assert obj.move(2, 2, 1) == 0
    assert obj.move(1, 1, 2) == 0
    assert obj.move(2, 0, 1) == 0
    assert obj.move(1, 0, 2) == 0
    assert obj.move(2, 1, 1) == 1


def test_tec_tac_toe_opt():
    obj = TicTacToeOpt(3)
    assert obj.move(0, 0, 1) == 0
    assert obj.move(0, 2, 2) == 0
    assert obj.move(2, 2, 1) == 0
    assert obj.move(1, 1, 2) == 0
    assert obj.move(2, 0, 1) == 0
    assert obj.move(1, 0, 2) == 0
    assert obj.move(2, 1, 1) == 1
