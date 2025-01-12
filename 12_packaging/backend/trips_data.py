from backend.connect_to_api import ResRobot
import pandas as pd

resrobot = ResRobot()


class TripData:
    # check explorations to find id
    def __init__(self, origin_id, destination_id) -> None:
        # umea_id = 740000190
        # gothenburg_id = 740000002

        self.trips = resrobot.trips(origin_id, destination_id).get("Trip")
        self.number_trips = len(self.trips)

    def next_available_trip(self) -> pd.DataFrame:
        next_trip = self.trips[0]

        leglist = next_trip.get("LegList").get("Leg")

        df_legs = pd.DataFrame(leglist)

        df_stops = pd.json_normalize(df_legs["Stops"].dropna(), "Stop", errors="ignore")

        df_stops["time"] = df_stops["arrTime"].fillna(df_stops["depTime"])
        df_stops["date"] = df_stops["arrDate"].fillna(df_stops["depDate"])

        return df_stops[
            [
                "name",
                "extId",
                "lon",
                "lat",
                "depTime",
                "depDate",
                "arrTime",
                "arrDate",
                "time",
                "date",
            ]
        ]

    def next_available_trips_today(self) -> list(pd.DataFrame):
        """Fetches all available trips today between the origin_id and destination_id
        It returns a list of DataFrame objects, where each item corresponds to a trip
        """
        # TODO: implement this method


if __name__ == "__main__":
    data = TripData(
        740000190,
    )
    print(data.next_available_trip()[["arrTime", "depTime", "time", "date"]])
