import whisper
import argparse

def transcribe_audio(audio_file, model_size="base"):
    # Step 1: Load the Whisper model
    print(f"Loading Whisper model ({model_size})...")
    model = whisper.load_model(model_size)

    # Step 2: Transcribe the audio file
    print(f"Transcribing file: {audio_file}...")
    result = model.transcribe(audio_file)

    # Step 3: Output the transcription
    print("\nTranscription:")
    print(result["text"])
    return result["text"]

def create_stt_cli():
    parser = argparse.ArgumentParser(description='Speech to Text CLI Tool')
    parser.add_argument('--audio-file', type=str, required=True, help='Path to the input .wav file')
    parser.add_argument('--model-size', type=str, default='base', choices=['tiny', 'base', 'small', 'medium', 'large'], help='Size of the Whisper model to use')
    return parser

def main():
    parser = create_stt_cli()
    args = parser.parse_args()

    transcribe_audio(args.audio_file, args.model_size)

if __name__ == "__main__":
    main()