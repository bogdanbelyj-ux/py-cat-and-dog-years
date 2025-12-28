from app.main import get_human_age


def test_zero_age_returns_zero_human_years() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_age_less_than_first_threshold_returns_zero() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_exact_thresholds_return_correct_human_years() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]


def test_age_between_thresholds_is_calculated_correctly() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_cat_and_dog_have_different_human_years_after_24() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_large_ages_are_calculated_correctly() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_function_returns_list_of_two_integers() -> None:
    result = get_human_age(17, 18)

    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(age, int) for age in result)
