from unittest import TestCase
import datetime
import pytz
from basketball_reference_web_scraper.helper_functions.schedule.parsed_raw_event_start_time_in_utc_returner import ParsedRawEventStartTimeInUtcReturner


class TestParsedRawEventStartTimeInUtcReturner(TestCase):
    def test_expected(self):
        expected_date_string = "Sat, Oct 24, 2015"
        expected_time_of_day_string = "5:30 PM"
        expected_result = pytz.timezone("US/Eastern").localize(datetime.datetime(2015, 10, 24, 17, 30, 0, 0)).astimezone(pytz.utc)
        result = ParsedRawEventStartTimeInUtcReturner.return_parsed_start_time_in_utc(
            expected_date_string,
            expected_time_of_day_string
        )

        assert result == expected_result

    def test_assertions(self):
        expected_date_string = "Sat, Oct 24, 2015"
        expected_time_of_day_string = "5:30 PM"

        self.assertRaises(AssertionError, ParsedRawEventStartTimeInUtcReturner.return_parsed_start_time_in_utc, None, expected_time_of_day_string)
        self.assertRaises(AssertionError, ParsedRawEventStartTimeInUtcReturner.return_parsed_start_time_in_utc, expected_date_string, None)

        self.assertRaises(AssertionError, ParsedRawEventStartTimeInUtcReturner.return_parsed_start_time_in_utc, 5, expected_time_of_day_string)
        self.assertRaises(AssertionError, ParsedRawEventStartTimeInUtcReturner.return_parsed_start_time_in_utc, expected_date_string, 5)