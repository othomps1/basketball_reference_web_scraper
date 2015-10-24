from unittest import TestCase
from basketball_reference_web_scraper.web_scrapers import return_schedule


class TestReturn_schedule(TestCase):
    def test_expected(self):
        # TODO: only basic test assertions, make better assertions
        result_schedule = return_schedule(2014)

        assert result_schedule is not None
        assert result_schedule.events is not None
        assert result_schedule.season_start_year is not None
        assert result_schedule.season_end_year is not None

        for event in result_schedule.events:
            assert event is not None