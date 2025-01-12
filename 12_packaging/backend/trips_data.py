from backend.connect_to_api import ResRobot

resrobot = ResRobot()

# check explorations to find id 

umea_id = 740000190
gothenburg_id = 740000002

trips = resrobot.trips(umea_id, gothenburg_id)["Trip"]

number_trips = len(trips)


print(number_trips)