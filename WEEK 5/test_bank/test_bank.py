from bank import value

def test_hello_uppercase():
  assert value("HELLO") == 0


def test_hello_mixed_case():
  assert value("HeLLo") == 0

def test_h_uppercase():
  assert value("H") == 20

def test_hello_with_phrase():
  assert value("hello world") == 0

def test_h_with_phrase():
  assert value("hey there") == 20

def test_other_phrases():
  assert value("CS50 is the best course") == 100
