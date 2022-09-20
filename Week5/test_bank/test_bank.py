from bank import value

def test_value_casesensitivity():
    assert value("hello") == 0
    assert value("Hello") == 0

def test_value_firstletter():
    assert value("howdy") == 20
    assert value("Hail Zog!") == 20

def test_value_failure():
    assert value("whashappenin?") == 100
    assert value("1# Customer!") == 100