import subprocess
from googletrans import Translator 
import sys
from opencc import OpenCC

cc = OpenCC('t2s')

model = "ggml-base.bin"
audio = "Sample_Audio.mp3"

print("Transcribing audio with Whisper.cpp...")

command = [
    "whisper-cli.exe",
    "--model", model,
    "--file", audio,
    "--language", "zh",
    "--print-progress",
]

try:
    result = subprocess.run(command, capture_output = True, text = True, check = True, encoding = "utf-8")
    text = result.stdout.strip()
except FileNotFoundError:
    print("Could not find whisper-cli.exe! Please make sure it is in the same folder!")
    sys.exit(1)
except subprocess.CalledProcessError as e:
    print(f"Whisper.cpp failed to run properly!\n{e}")
    sys.exit(1)

text_simplified = cc.convert(text)

print("\nTranscribing into English, Malay, and Mandarin...")
translator = Translator()

try:
    en = translator.translate(text_simplified, dest = "en").text
    ms = translator.translate(text_simplified, dest = "ms").text
    zh = translator.translate(text_simplified, dest = "zh-cn").text 
except Exception as e:
    print("Transcription failed:", e)
    en = ""
    ms = ""
    zh = ""

with open("transcriptions.txt", "w", encoding = "utf-8") as f:
    f.write("=-=-=-=-English=-=-=-=-\n" + en + "\n\n")
    f.write("=-=-=-=-Malay=-=-=-=-\n" + ms + "\n\n")
    f.write("=-=-=-=-Mandarin=-=-=-=-\n" + zh)

print("All done! Transcription saved to transcriptions.txt!")