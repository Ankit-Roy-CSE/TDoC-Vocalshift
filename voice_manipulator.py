import argparse
import librosa
import soundfile as sf

def audio_manipulator(input_file, output_file, effect, value):
    audio, sr=librosa.load(input_file, sr=None)
    if effect=="speed":
        audio=librosa.effects.time_stretch(y=audio, rate=value)
    if effect=="pitch":
        audio=librosa.effects.pitch_shift(y=audio, sr=sr, n_steps=value)
    if effect=="rev":
        audio=audio[::-1]
    if effect=="echo":
        echo = librosa.util.fix_length(audio, size=(len(audio) +int(sr * value)))
        echo[-len(audio):] += audio * 0.6
        audio=echo
    sf.write(output_file, audio, sr)
    print(f"Audio file {output_file} generated with effect {effect}")

if __name__ == "__main__":
    parser=argparse.ArgumentParser(description="Voice Manipulator using CLI")
    parser.add_argument("input_file", type=str, help="input file name")
    parser.add_argument("output_file", type=str, help="output file name")
    parser.add_argument("--effect", type=str, choices=["pitch", "speed", "rev", "echo"], help="effect name")
    parser.add_argument("--value", type=int, help="Magnitude of the effect")
    args=parser.parse_args()
    audio_manipulator(args.input_file, args.output_file, args.effect, args.value)