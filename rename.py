import os
import pandas as pd

# Load the CSV file
csv_file = "index_to_dex.csv"
df = pd.read_csv(csv_file)

# Create a dictionary mapping Dex Number to Pokémon name
dex_to_name = dict(zip(df["Dex Number"].astype(str).str.zfill(3), df["Pokemon"]))

# Directory containing the images
image_dir = "pokemon_sprites_centered"  # Adjust if your images are in a different folder

# Iterate through files in the directory
for filename in os.listdir(image_dir):
    if filename.startswith("Spr_3e_") and filename.endswith(".png"):
        # Extract the Dex number from the filename
        dex_number = filename[len("Spr_3e_"):len("Spr_3e_")+3]
        
        # Check if the Dex number exists in the CSV
        if dex_number in dex_to_name:
            pokemon_name = dex_to_name[dex_number]
            old_path = os.path.join(image_dir, filename)
            new_filename = f"{pokemon_name}.png"
            new_path = os.path.join(image_dir, new_filename)
            
            try:
                # Rename the file
                os.rename(old_path, new_path)
                print(f"Renamed {filename} to {new_filename}")
            except Exception as e:
                # Log error if rename fails (e.g., due to special characters)
                print(f"Failed to rename {filename} to {new_filename}: {e}")
        else:
            print(f"No Pokémon found for Dex number {dex_number} in {filename}")