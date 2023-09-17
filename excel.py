import gspread
import json

with open("rosters.json", "r") as json_file:
    data = json.load(json_file)
gc = gspread.service_account(filename="service_account.json")
sh = gc.open("Sleeper Rosters")

worksheet = sh.get_worksheet(0)
# Insert the "display_name" in the first row

display_names = []
players = []
for owner in data:
    display_names.append([owner['display_name']])
    players.append(owner)

worksheet.insert_cols(display_names, 1)
# Iterate through the players and insert their names, amounts, and contracts in cells below the "display_name"
# # Initialize with empty cells to maintain the same number of columns
# row_data = [["", "", ""]]
# for player in data["players"]:
#     row_data.append([f"{player['first_name']} {player['last_name']}",
#                     player["amount"], player["contract"]])

# # Insert the player data starting from the second row
# worksheet.insert_rows(row_data, 2)

print("Data inserted into Google Sheets successfully.")
