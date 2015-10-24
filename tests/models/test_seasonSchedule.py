from unittest import TestCase
import datetime
from basketball_reference_web_scraper.models.season_schedule import SeasonSchedule
from basketball_reference_web_scraper.models.event import Event


class TestSeasonSchedule(TestCase):
    def test_expected(self):

        expected_events = [
            Event(
                datetime.datetime(year=2014, month=11, day=11, hour=11),
                "JAE",
                "BRADLEY"
            ),
            Event(
                datetime.datetime(year=2014, month=11, day=12, hour=12),
                "FOO",
                "BAR"
            )
        ]
        expected_season_start_year = 2014
        expected_season_end_year = 2015
        season_schedule = SeasonSchedule(
            expected_events,
            expected_season_start_year,
            expected_season_end_year
        )

        assert expected_events == season_schedule.events
        assert expected_season_start_year == season_schedule.season_start_year
        assert expected_season_end_year == season_schedule.season_end_year

    def test_assertions(self):
        expected_events = [
            Event(
                datetime.datetime(year=2014, month=11, day=11, hour=11),
                "JAE",
                "BRADLEY"
            ),
            Event(
                datetime.datetime(year=2014, month=11, day=12, hour=12),
                "FOO",
                "BAR"
            )
        ]
        expected_season_start_year = 2014
        expected_season_end_year = 2015

        self.assertRaises(AssertionError, SeasonSchedule, None, expected_season_start_year, expected_season_end_year)
        self.assertRaises(AssertionError, SeasonSchedule, expected_events, None, expected_season_end_year)
        self.assertRaises(AssertionError, SeasonSchedule, expected_events, expected_season_start_year, None)

        self.assertRaises(AssertionError, SeasonSchedule, 5, expected_season_start_year, expected_season_end_year)
        self.assertRaises(AssertionError, SeasonSchedule, expected_events, list(), expected_season_end_year)
        self.assertRaises(AssertionError, SeasonSchedule, expected_events, expected_season_start_year, list())

        self.assertIsNotNone(SeasonSchedule(expected_events, expected_season_start_year, expected_season_start_year))
        self.assertRaises(AssertionError, SeasonSchedule, 5, expected_season_start_year, expected_season_start_year - 1)