import os
import librosa
import soundfile as sf

input_root = "./Datalar"
output_root = "./Datasets"   # <-- burada

classes = ["Asthma", "Healthy", "COPD4"]

remove_seconds = 2

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

        start = int(remove_seconds * sr)
        trimmed = audio[start:]

        sf.write(out_path, trimmed, sr)

        print(f"Saved -> {out_path}")

print("All files processed 🚀")
