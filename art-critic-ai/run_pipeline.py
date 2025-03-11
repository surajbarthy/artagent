import os
from generate_critique import generate_critique
from text_to_speech import text_to_speech

def run_pipeline(image_path):
    print("Generating critique...")
    critique_text = generate_critique(image_path)

    text_file = f"output/{os.path.basename(image_path).split('.')[0]}.txt"
    print("Generating speech...")
    audio_file = text_to_speech(text_file)

    print("Pipeline completed.")
    return critique_text, audio_file

if __name__ == "__main__":
    image_file = "images/day1.png"  # Change this for other images
    run_pipeline(image_file)
