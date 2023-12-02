from os import getenv

import shimoku_api_python as Shimoku
from dotenv import load_dotenv

load_dotenv("../.env")
access_token = getenv("SHIMOKU_TOKEN")
universe_id: str = getenv("UNIVERSE_ID")
workspace_id: str = getenv("WORKSPACE_ID")


s = Shimoku.Client(
    access_token=access_token,
    universe_id=universe_id,
)
s.set_workspace(uuid=workspace_id)


s.set_board("Data App")

s.set_menu_path("Presidental Election", "First Round")

presidential_elections_results = [
    {"Candidate": "Milei", "Percentage": 29.99},
    {"Candidate": "Massa", "Percentage": 36.78},
    {"Candidate": "Bullrich", "Percentage": 23.81},
    {"Candidate": "Schiaretti", "Percentage": 6.73},
    {"Candidate": "Bregman", "Percentage": 2.69},
]

s.plt.bar(
    order=0,
    title="Presidental Election Results",
    data=presidential_elections_results,
    x="Candidate",
    y=["Percentage"],
    x_axis_name="Candidates",
    y_axis_name="Percentages",
)
