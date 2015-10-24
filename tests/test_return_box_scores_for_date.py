from unittest import TestCase
import datetime
from basketball_reference_web_scraper.web_scrapers import return_box_scores_for_date


class TestReturn_box_scores_for_date(TestCase):
    def test_expected(self):
        #TODO: update basic test checks

        test_date = datetime.date(year=2014, month=10, day=28)
        test_result_box_scores = return_box_scores_for_date(date=test_date)

        assert test_result_box_scores is not None
        assert test_result_box_scores[0] is not None

        expected_anthony_davis_box_score = test_result_box_scores[0]
        assert expected_anthony_davis_box_score.first_name == "Anthony"
        assert expected_anthony_davis_box_score.last_name == "Davis"
        assert expected_anthony_davis_box_score.date == test_date
        assert expected_anthony_davis_box_score.team == "NOP"