import os
from generate_critique import generate_critique
from generate_audio import text_to_speech

def run_pipeline(image_path):
    print("Generating critique...")
    critique_text = generate_critique(image_path)  # Get generated text

    # Generate audio filename based on image name
    output_name = os.path.basename(image_path).split('.')[0]

    print("Generating speech...")
    audio_file = text_to_speech(critique_text, output_name)

    print("Pipeline completed.")
    print(f"Text file: output/{output_name}.txt")
    print(f"Audio file: {audio_file}")

if __name__ == "__main__":
    image_file = "images/day1.png"  # Change this to your actual image
    run_pipeline(image_file)
