from src.week2 import win_percentage


def test_win_percentage():
    matches = [
        ("Exeter", "Bath", 24, 18),
        ("Sale", "Exeter", 15, 20),
        ("Exeter", "Bristol", 10, 20),
    ]
    two_thirds = 100 * 2 / 3
    assert win_percentage(matches, "Exeter") == two_thirds


def test_win_percentage_no_wins():
    matches = [
        ("Exeter", "Bath", 18, 24),
        ("Sale", "Exeter", 30, 10),
    ]
    assert win_percentage(matches, "Exeter") == 0.0


def test_win_percentage_all_wins():
    matches = [
        ("Exeter", "Bath", 24, 18),
        ("Exeter", "Sale", 20, 10),
    ]
    assert win_percentage(matches, "Exeter") == 100.0
