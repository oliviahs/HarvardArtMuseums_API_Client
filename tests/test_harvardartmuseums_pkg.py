from harvardartmuseums_pkg import harvardartmuseums_pkg

import pytest

# function 1
def get_url_for_exhibition(after, before, apikey):
    your_url= "https://api.harvardartmuseums.org/exhibition?after=" + after + "&before=" + before + "&apikey=" + apikey
    return your_url

# pytest
@pytest.mark.parametrize('after, before, apikey, expected',[
    ("1985", "2006", "d7a856a1-f4df-4726-958f-957b2762b17f", 'https://api.harvardartmuseums.org/exhibition?after=1985&before=2006&apikey=d7a856a1-f4df-4726-958f-957b2762b17f'),
    ("1965", "1990", "d7a856a1-f4df-4726-958f-957b2762b17f", 'https://api.harvardartmuseums.org/exhibition?after=1965&before=1990&apikey=d7a856a1-f4df-4726-958f-957b2762b17f'),
    ("1935", "1970", "d7a856a1-f4df-4726-958f-957b2762b17f", 'https://api.harvardartmuseums.org/exhibition?after=1935&before=1970&apikey=d7a856a1-f4df-4726-958f-957b2762b17f')
])

# function for test
def test_exhibition_url(after, before, apikey, expected):
    result = get_url_for_exhibition(after, before, apikey)
    assert result == expected


# function 2
def get_url_for_title(text, apikey):
    your_url = "https://api.harvardartmuseums.org/object?title=" + str(text) + "&apikey=" + str(apikey)
    return your_url

# pytest
@pytest.mark.parametrize('text, apikey, expected',[
    ("cat", "d7a856a1-f4df-4726-958f-957b2762b17f", 'https://api.harvardartmuseums.org/object?title=cat&apikey=d7a856a1-f4df-4726-958f-957b2762b17f'),
    ("war", "d7a856a1-f4df-4726-958f-957b2762b17f", 'https://api.harvardartmuseums.org/object?title=war&apikey=d7a856a1-f4df-4726-958f-957b2762b17f'),
    ("home", "d7a856a1-f4df-4726-958f-957b2762b17f", 'https://api.harvardartmuseums.org/object?title=home&apikey=d7a856a1-f4df-4726-958f-957b2762b17f')
])

# function for test
def test_title_url(text, apikey, expected):
    result = get_url_for_title(text, apikey)
    assert result == expected