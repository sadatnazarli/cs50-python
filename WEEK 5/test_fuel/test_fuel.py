from fuel import convert, gauge
import pytest


def test_convert_normal():
  assert convert("3/4") == 75
  assert convert("1/2") == 50
  assert convert("1/4") == 25


def test_convert_negative():
    with pytest.raises(ValueError):
        convert("-1/4")
    with pytest.raises(ValueError):
        convert("1/-4")


def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
  assert gauge(1) == "E"
  assert gauge(99) == "F"
  assert gauge(75) == "75%"
