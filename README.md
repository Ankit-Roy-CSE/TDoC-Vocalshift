# 🎙️ Voice Changer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Built%20with-Python-blue.svg)](https://www.python.org/)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)

Transform your voice effortlessly! This Voice Changer application allows users to input an audio file and outputs the same content in a modified voice. Whether you want to sound like a robot, change your pitch, or apply fun effects, this project is the starting point for all your audio transformation needs.

---

## 🚀 Features

- **Audio Input**: Accepts audio files or real-time microphone input.
- **Voice Transformations**:
  - Pitch adjustment (high/low).
  - Robot voice effect.
  - Echo and reverb effects.
  - Custom transformations.
- **Real-Time Processing**: Transform and play back voice on-the-fly.
- **Multiple Format Support**: Works with common audio formats like `.wav`, `.mp3`, etc.

---

## 🛠️ Installation

### Prerequisites
- Python 3.8 or later
- `pip` package manager
- Basic audio hardware (microphone and speakers)

Ensure you have the necessary dependencies installed. Run:
```bash
pip install -r requirements.txt
```

## 🎛️ Usage Guide

Follow these steps to use the Voice Changer application:

### Using Pre-Recorded Audio Files

For CLI Tool to convert Speech to Text

```
python stt.py --audio-file path/to/input.wav --model-size size
```
Size of the Whisper model to use can be : tiny / base / small / medium / large

You can apply voice effects to existing audio files.

```
python voice_manipulator.py input.wav output.wav --effect <effect_name> --value <val>
```

For CLI Tool to convert Text to Speech

```
# Convert text directly
python main.py --text "Hello, world!" --output output.wav

# Convert from text file
python main.py --input-file input.txt --output output.wav --speaker speaker.wav

```

To convert from an audio file to a different voice :-

```
# Convert audio to text and back to audio with default settings
python vocalshift.py --input-audio input.wav --output-audio output.wav

# Convert audio to text and back to audio with a specific speaker and effect
python vocalshift.py --input-audio input.wav --output-audio output.wav --speaker speaker.wav --effect pitch_up --effect-level 1.5
```
