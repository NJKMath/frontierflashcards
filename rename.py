import pandas as pd
import json

# Load the CSV file
csv_file = "pokemonmoves.csv"
df = pd.read_csv(csv_file)

# Create a dictionary mapping Move to Type
move_to_type = dict(zip(df["Name"], df["Type"]))

# Write the dictionary to a JSON file
output_file = "move_types.json"
with open(output_file, 'w') as f:
    json.dump(move_to_type, f, indent=4)

print(f"JSON file '{output_file}' created successfully.")