from plates import is_valid


def test_too_short():
  assert is_valid("A") == False

def test_valid_length():
  assert is_valid("AB") == True
  assert is_valid("ABC123") == True
  assert is_valid("ABC1234") == False

def test_first_letter():
  assert is_valid("12") == False
  assert is_valid("BO") == True


def test_number_place():
    assert is_valid("AB2C34") == False
    assert is_valid("ABC123") == True


def test_first_number_zero():
    assert is_valid("AB01") == False
    assert is_valid("AB12") == True


def test_special_characters():
    assert is_valid("AB.123") == False
    assert is_valid("AB 123") == False
    assert is_valid("AB123!") == False
