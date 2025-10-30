import subprocess
from googletrans import Translator 
import os
import sys
from opencc import OpenCC

try:
    cc = OpenCC('t2s')
except ImportError:
    print("Missing OpenCC! Please install it!")
    sys.exit(1)

model = "ggml-base.bin"
audio = "Sample_Audio.mp3"
output = "transcription"

print("Transcribing audio with Whisper.cpp...")

command = [
    "whisper-cli.exe",
    "--model", model,
    "--file", audio,
    "--output-txt",
    "--output-file", output,
    "--language", "zh",
    "--print-progress",
]

try:
    subprocess.run(command, check = True)
except FileNotFoundError:
    print("Could not find whisper-cli.exe! Please make sure it is in the same folder!")
    sys.exit(1)
except subprocess.CalledProcessError as e:
    print(f"Whisper.cpp failed to run properly!\n{e}")
    sys.exit(1)

txt_file = output+ ".txt"
if not os.path.exists(txt_file):
    print("Transcription failed! File not found!", txt_file)
    sys.exit(1)

with open(txt_file, "r", encoding="utf-8") as f:
    text = f.read().strip()

text_simplified = cc.convert(text)

with open(txt_file, "w", encoding = "utf-8") as f:
    f.write(text_simplified)

print("\nTranscription complete!")
print("\n =-=-=-=-Transcript preview=-=-=-=-\n")
print(text_simplified[:500] + "..." if len(text_simplified) > 500 else text_simplified)

print("\nTranslating into English, Malay, and Mandarin...")
translator = Translator()

try:
    en = translator.translate(text_simplified, dest = "en").text
    ms = translator.translate(text_simplified, dest = "ms").text
    zh = translator.translate(text_simplified, dest = "zh-cn").text 
except Exception as e:
    print("Translation failed:", e)
    en = ""
    ms = ""
    zh = ""

with open("translations.txt", "w", encoding = "utf-8") as f:
    f.write("=-=-=-=-English=-=-=-=-\n" + en + "\n\n")
    f.write("=-=-=-=-Malay=-=-=-=-\n" + ms + "\n\n")
    f.write("=-=-=-=-Mandarin=-=-=-=-\n" + zh)

print("All done! Translations saved to translations.txt!")