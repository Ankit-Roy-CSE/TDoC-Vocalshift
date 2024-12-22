import argparse
import os
from TTS.TTS.api import TTS
from pathlib import Path
from voice_manipulator import manipulate_audio

def create_tts_cli():
    parser = argparse.ArgumentParser(description='Text to Speech CLI Tool')
    parser.add_argument('--text', type=str, help='Text to convert to speech')
    parser.add_argument('--input-file', type=str, help='Text file to convert to speech')
    parser.add_argument('--output', type=str, default='output.wav', help='Output audio file path')
    parser.add_argument('--speaker', type=str, help='Path to speaker voice sample')
    # parser.add_argument('--language', type=str, help='Language code (default: en)')
    parser.add_argument('--effect', type=str, default=None , help='Effect to apply to the audio')
    parser.add_argument('--effect-level', type=float, default=1.0 , help='Effect level to apply to the audio')
    return parser

def process_tts(text, output_path, speaker_path=None, language='en',effect=None, effect_level=None):
    try:
        tts = TTS("tts_models/en/ljspeech/tacotron2-DDC")
        temp_path = Path(output_path).parent / "temp.wav"
        print(f"Converting text to speech...")
        if effect:
            tts.tts_to_file(
                text=text,
                file_path=temp_path,
                speaker_wav=speaker_path if speaker_path else None,
                split_sentences=True
            )
        else:
            tts.tts_to_file(
                text=text,
                file_path=output_path,
                speaker_wav=speaker_path if speaker_path else None,
                split_sentences=True
            )

        if effect:
            print(f"Applying effect: {effect} with level: {effect_level}")
            manipulate_audio(temp_path, output_path, effect, effect_level)
            print(f"Effect applied and audio saved to: {output_path}")
        else:
            os.rename(temp_path, output_path)
            print(f"Audio saved to: {output_path}")

    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        return False
    return True

def main():
    parser = create_tts_cli()
    args = parser.parse_args()

    if not args.text and not args.input_file:
        parser.error("Either --text or --input-file must be provided")

    output_dir = os.path.dirname(args.output)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    if args.input_file:
        try:
            with open(args.input_file, 'r') as f:
                text = f.read()
        except Exception as e:
            print(f"Error reading input file: {str(e)}")
            return
    else:
        text = args.text

    success = process_tts(
        text=text,
        output_path=args.output,
        speaker_path=args.speaker,
        effect=args.effect,
        effect_level=args.effect_level,
        # language=args.language
    )

    if not success:
        print("TTS conversion failed")
        return

if __name__ == "__main__":
    main()