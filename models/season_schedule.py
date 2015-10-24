class SeasonSchedule:
    def __init__(self, events, season_start_year, season_end_year):

        assert events is not None
        assert season_start_year is not None
        assert season_end_year is not None

        assert isinstance(events, list)
        assert isinstance(season_start_year, int)
        assert isinstance(season_end_year, int)

        self.season_end_year = season_end_year
        self.season_start_year = season_start_year
        self.events = events