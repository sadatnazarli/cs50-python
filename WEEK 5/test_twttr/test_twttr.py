from twttr import shorten

def test_lowercase_letters():
  assert shorten("hello") == "hll"

def test_uppercase_letters():
  assert shorten("HELLO") == "HLL"

def test_mixed_letters():
  assert shorten("hello123!") == "hll123!"

def test_only_vowels():
  assert shorten("aeiou") == ""
