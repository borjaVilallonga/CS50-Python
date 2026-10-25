from datetime import date
from seasons import minutes_since_birth
from unittest.mock import patch

def test_minutes_since_birth():

    with patch("seasons.date") as mock_date:
        mock_date.today.return_value = date(2000, 1, 1)
        assert minutes_since_birth(date(1999, 1, 1)) == "Five hundred twenty-five thousand, six hundred minutes"
        assert minutes_since_birth(date(1995, 1, 1)) == "Two million, six hundred twenty-nine thousand, four hundred forty minutes"
        assert minutes_since_birth(date(1998, 6, 20)) == "Eight hundred six thousand, four hundred minutes"

    with patch("seasons.date") as mock_date:
        mock_date.today.return_value = date(2003, 1, 1)
        assert minutes_since_birth(date(2001, 1, 1)) == "One million, fifty-one thousand, two hundred minutes"

    with patch("seasons.date") as mock_date:
        mock_date.today.return_value = date(2032, 1, 1)
        assert minutes_since_birth(date(2020, 6, 1)) == "Six million, ninety-two thousand, six hundred forty minutes"

