# Audio Transcription

## Overview
This project is a simple audio transcription tool powered by Whisper.cpp and Google Translate API via google trans. It takes an audio file, transcribes it into English, Malay, and Mandarin. The final results are saved into a single text file named *transcriptions.txt*.

## Approach & Key Ideas
**1. Speech Recognition (Transcription)**
- The program calls Whisper.cpp using Python's subprocess module.
- Whisper trancribes the Maindarin speech in the audio file into text.

**2. Simplified Chinese Conversion**
- The output text is converted from Traditional Chinese to Simplified Chinese using the *OpenCC* library for standardization.

**3. Translation**
- The converted text is translated into three languages (English, Malay, and Mandarin) using Google Translate API via the *googletrans* Python library.

**4. Output**
- The transcriptions are saved into a file called *transciptions.txt* with clearly labeled language sections.
- Each sentence in the transcription is labeled with its corresponding timestamp ( start time -> end time). This helps users identiy when each line was spoken in the audio.

## Technologies and Tools Used
- **Programming Language:** Python
- **Speech-to-text engine:** Whisper.cpp
- **Automatic translation to multiple languages:** googletrans
- **Converts Traditional Chinese text to Simplified Chinese:** OpenCC
- **Runs Whisper.cpp as an external command-line process:** subprocess

## Required Binaries
- Before running the program, make sure the following files are in the same directory as the script:
  - ggml-base.bin
  - ggml-base.dll
  - ggml-cpu.dll
  - ggml.dll
  - SDL2.dll
  - whisper-cli.exe
  - whisper.dll

**How to Get Them**

***.exe* and *.dll* files**
1. Go to the official Whisper.cpp Github repsoitory.
2. Open the Releases section.
3. Download the precompiled Windows binaries *(whisper-bin-x64.zip)*.
4. Extract all *.exe* and *.dll* files.
5. Place them in the same folder as *audio_transcription.py*.

***.bin* file**
1. Go to the Hugging Face model repository.
2. Click on *ggml-base.bin* and download it.
3. Place them in the same folder as *audio_transcription.py*.

## Steps to Reproduce the Results
**Step 1: Clone the Repository**
- Clone the project repository from GitHub to the local computer.
  
**Step 2: Install dependencies**
- Install all required packages for this audio transcription program. *(pip install googletrans==4.0.0-rc1 opencc-python-reimplemented)*.

**Step 3: Place Files in the Same Folder**
- Make sure the following files are in the same directory:
  - audio_transcription.py
  - ggml-base.bin
  - ggml-base.dll
  - ggml-cpu.dll
  - ggml.dll
  - Sample_Audio.mp3
  - SDL2.dll
  - whisper-cli.exe
  - whisper.dll

**Step 4: Write the Code for the Main Program**
- Writing the main Python program that will transcribe the audio text into English, Malay, and Mandarin.

**Step 5: Run the Program**
- Ensure the main Python file transcribe audio to text (English, Malay, and Mandarin).

## How to Run
1. Put your input audio in the project folder and name it *Sample_Audio.mp4* (or change the constant in the script).
2. Run the main script: *python audio_transcription.py*
3. The output will be saved as *transcriptions.txt* in the same folder.

## Output
<img width="1060" height="526" alt="image" src="https://github.com/user-attachments/assets/33fb0836-982a-47ab-ae12-1d4b7b2a6a1f" />
<img width="1258" height="529" alt="image" src="https://github.com/user-attachments/assets/c8c0c70f-eee5-4f78-b425-a4c8efba68bc" />
<img width="966" height="536" alt="image" src="https://github.com/user-attachments/assets/5968d7b1-3697-4139-96ef-63a5966a3b78" />



## Credit
**Developer:** Ong Boon Heng <br>
**Date:** October 2025

