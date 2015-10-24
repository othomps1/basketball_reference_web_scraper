import json

from basketball_reference_web_scraper.models.schedule import SeasonSchedule


class ScheduleJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, SeasonSchedule):
            return super(ScheduleJsonEncoder, self).default(obj)

        return obj.__dict__
