from twttr import shorten

def test_shorten():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("Shorten") == "Shrtn"
    assert shorten("The rain in spain.") == "Th rn n spn."
    assert shorten("1a2b3c4f5e") == "12b3c4f5"