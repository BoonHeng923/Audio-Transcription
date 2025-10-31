import subprocess
import sys
from googletrans import Translator 
from opencc import OpenCC

def main():
    model = "ggml-base.bin"
    audio = "Sample_Audio.mp3"
    cc = OpenCC('t2s')

    command = [
        "whisper-cli.exe",
        "--model", model,
        "--file", audio,
        "--language", "zh",
        "--print-progress",
    ]

    try:
        print("Transcribing audio with Whisper.cpp...")
        result = subprocess.run(command, capture_output = True, text = True, check = True, encoding = "utf-8")
        text = cc.convert(result.stdout.strip())
    except FileNotFoundError:
        sys.exit("Could not find whisper-cli.exe! Please make sure it is in the same folder!")
    except subprocess.CalledProcessError as e:
        sys.exit("Whisper.cpp failed to run properly!\n{e}")

    print("\nTranscribing into English, Malay, and Mandarin...")
    translator = Translator()

    try:
        en = translator.translate(text, dest = "en").text
        ms = translator.translate(text, dest = "ms").text
        zh = translator.translate(text, dest = "zh-cn").text 
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

if __name__ == "__main__":
    main()