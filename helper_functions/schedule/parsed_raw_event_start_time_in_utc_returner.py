import datetime
import pytz


class ParsedRawEventStartTimeInUtcReturner:
    def __init__(self):
        pass

    @staticmethod
    def return_parsed_start_time_in_utc(raw_event_date_string, raw_event_time_of_day_string):

        assert raw_event_date_string is not None
        assert raw_event_time_of_day_string is not None

        assert isinstance(raw_event_date_string, str)
        assert isinstance(raw_event_time_of_day_string, str)

        parsed_event_start_time = datetime.datetime.strptime(raw_event_date_string + raw_event_time_of_day_string, "%a, %b %d, %Y%I:%M %p")
        est = pytz.timezone("US/Eastern")
        parsed_est_start_time = est.localize(parsed_event_start_time)
        return parsed_est_start_time.astimezone(pytz.utc)
