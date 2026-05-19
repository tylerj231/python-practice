import pytest

from tasks.countdown_iterator import Countdown


def test_countdown_list_output():
    countdown = Countdown(6)

    assert list(countdown) == [5, 4, 3, 2, 1]


def test_countdown_manual_next():
    countdown = Countdown(6)
    assert next(countdown) == 5
    assert next(countdown) == 4
    assert next(countdown) == 3
    assert next(countdown) == 2
    assert next(countdown) == 1


def test_countdown_stop_iteration():
    countdown = Countdown(6)
    with pytest.raises(StopIteration):
        next(countdown)
        next(countdown)
        next(countdown)
        next(countdown)
        next(countdown)
        next(countdown)


def test_countdown_for_loop():
    countdown = Countdown(6)
    expected = 5
    for actual in countdown:
        assert actual == expected
        expected -= 1


def test_countdown_is_own_iterator():
    countdown = Countdown(6)
    assert iter(countdown) == iter(countdown)
