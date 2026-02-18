import os
import librosa
import soundfile as sf
import numpy as np

input_root = "./Datalar"
output_root = "./DatasetsFinal"

classes = ["Asthma", "Healthy", "COPD4"]

target_seconds = 15

for cls in classes:
    input_folder = os.path.join(input_root, cls)
    output_folder = os.path.join(output_root, cls)
    os.makedirs(output_folder, exist_ok=True)

    for file in os.listdir(input_folder):
        if not file.lower().endswith(".wav"):
            continue

        in_path = os.path.join(input_folder, file)
        out_path = os.path.join(output_folder, file)

        audio, sr = librosa.load(in_path, sr=None)

        target_len = int(target_seconds * sr)

        if len(audio) > target_len:
            audio = audio[-target_len:]

        sf.write(out_path, audio, sr)
        print(f"Saved -> {out_path}")

print("All files processed 🚀")