import os
import subprocess

# Configuration
INPUT_DIR = "pokemon_cries_aif"  # Directory with .aif files
OUTPUT_DIR = "pokemon_cries_converted"  # Where to save MP3s

def convert_aif_to_mp3(input_path, output_path):
    """Convert a single .aif file to .mp3 using ffmpeg"""
    try:
        # Use ffmpeg to convert
        subprocess.run([
            'ffmpeg',
            '-i', input_path,
            '-acodec', 'libmp3lame',
            '-ab', '128k',
            '-y',  # Overwrite output file if it exists
            output_path
        ], check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return False
    except FileNotFoundError:
        print("Error: ffmpeg not found. Please install ffmpeg first.")
        print("Windows: Download from https://ffmpeg.org/download.html")
        print("Or use: winget install ffmpeg")
        return False

def main():
    # Create output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    if not os.path.exists(INPUT_DIR):
        print(f"Input directory {INPUT_DIR} not found!")
        return
    
    aif_files = [f for f in os.listdir(INPUT_DIR) if f.endswith('.aif')]
    
    if not aif_files:
        print("No .aif files found!")
        return
    
    print(f"Found {len(aif_files)} .aif files to convert\n")
    
    successful = 0
    failed = 0
    
    for aif_file in aif_files:
        input_path = os.path.join(INPUT_DIR, aif_file)
        # Simply replace .aif with .mp3 (same pokemon name)
        mp3_filename = aif_file.replace('.aif', '.mp3')
        output_path = os.path.join(OUTPUT_DIR, mp3_filename)
        
        print(f"Converting: {aif_file} → {mp3_filename}", end=" ... ")
        
        if convert_aif_to_mp3(input_path, output_path):
            print("✓")
            successful += 1
        else:
            print("✗")
            failed += 1
    
    print(f"\n{'='*50}")
    print(f"Conversion complete!")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Files saved to: {OUTPUT_DIR}")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()