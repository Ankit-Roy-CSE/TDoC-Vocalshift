import argparse
from stt import transcribe_audio
from main import process_tts

def create_vocalshift_cli():
    parser = argparse.ArgumentParser(description='Vocal Shift CLI Tool')
    parser.add_argument('--input-audio', type=str, required=True, help='Path to the input audio file')
    parser.add_argument('--output-audio', type=str, required=True, help='Path to the output audio file')
    parser.add_argument('--stt-model-size', type=str, default='base', choices=['tiny', 'base', 'small', 'medium', 'large'], help='Size of the Whisper model to use for transcription')
    parser.add_argument('--speaker', type=str, help='Path to speaker voice sample')
    parser.add_argument('--effect', type=str, default=None, help='Effect to apply to the audio')
    parser.add_argument('--effect-level', type=float, default=1.0, help='Effect level to apply to the audio')
    return parser

def vocal_shift(input_audio, output_audio, stt_model_size='base', speaker=None, effect=None, effect_level=1.0):
    # Step 1: Transcribe the input audio to text
    print(f"Transcribing audio file: {input_audio}...")
    text = transcribe_audio(input_audio, model_size=stt_model_size)
    
    # Step 2: Convert the transcribed text back to audio
    print(f"Converting text back to audio...")
    success = process_tts(
        text=text,
        output_path=output_audio,
        speaker_path=speaker,
        effect=effect,
        effect_level=effect_level
    )
    
    if success:
        print(f"Audio saved to: {output_audio}")
        return True
    else:
        print("Conversion failed")
        return False

def main():
    parser = create_vocalshift_cli()
    args = parser.parse_args()

    vocal_shift(
        input_audio=args.input_audio,
        output_audio=args.output_audio,
        stt_model_size=args.stt_model_size,
        speaker=args.speaker,
        effect=args.effect,
        effect_level=args.effect_level
    )

if __name__ == "__main__":
    main()