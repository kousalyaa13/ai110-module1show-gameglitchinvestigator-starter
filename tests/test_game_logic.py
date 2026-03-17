from logic_utils import check_guess, parse_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_parse_guess_valid():
    # Valid guess should return True with the int value
    ok, value, err = parse_guess("50")
    assert ok == True
    assert value == 50
    assert err == None


def test_parse_guess_out_of_bounds_too_high():
    # Guess above 100 should return False with out of bounds message
    ok, value, err = parse_guess("150")
    assert ok == False
    assert value == None
    assert "1 and 100" in err


def test_parse_guess_out_of_bounds_too_low():
    # Guess below 1 should return False with out of bounds message
    ok, value, err = parse_guess("0")
    assert ok == False
    assert value == None
    assert "1 and 100" in err


def test_parse_guess_negative():
    # Negative guess should return False with out of bounds message
    ok, value, err = parse_guess("-5")
    assert ok == False
    assert value == None
    assert "1 and 100" in err


def test_parse_guess_boundary_low():
    # Guess at boundary (1) should be valid
    ok, value, err = parse_guess("1")
    assert ok == True
    assert value == 1


def test_parse_guess_boundary_high():
    # Guess at boundary (100) should be valid
    ok, value, err = parse_guess("100")
    assert ok == True
    assert value == 100


# FIX: Added test to verify secret number doesn't change across multiple checks in same game session
def test_secret_consistency_across_checks():
    # Simulating multiple guesses against the same secret number (should not change)
    secret = 42
    
    # First check
    outcome1, _ = check_guess(50, secret)
    assert outcome1 == "Too High"
    
    # Second check with different guess, secret is same
    outcome2, _ = check_guess(30, secret)
    assert outcome2 == "Too Low"
    
    # Third check with winning guess, secret is still same
    outcome3, _ = check_guess(42, secret)
    assert outcome3 == "Win"
