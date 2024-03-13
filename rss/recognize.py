import numpy as np
import ffmpeg
import warnings
warnings.filterwarnings("ignore", message=".*The 'nopython' keyword.*")
import whisper  # noqa: E402


model = whisper.load_model("base")

# FROM
# https://github.com/openai/whisper/discussions/908#discussioncomment-5429636
def load_audio(  # noqa: E302
    file_bytes: bytes,
    sr: int = 16_000,
) -> np.ndarray:
    """
    Use file's bytes and transform to mono waveform, resampling as necessary
    Parameters
    ----------
    file: bytes
        The bytes of the audio file
    sr: int
        The sample rate to resample the audio if necessary
    Returns
    -------
    A NumPy array containing the audio waveform, in float32 dtype.
    """
    try:
        # This launches a subprocess to decode audio while down-mixing 
        # and resampling as necessary.
        # Requires the ffmpeg CLI and `ffmpeg-python` package to be installed.
        out, _ = (
            ffmpeg.input('pipe:', threads=0)
            .output("pipe:", format="s16le", acodec="pcm_s16le", ac=1, ar=sr)
            .run_async(pipe_stdin=True, pipe_stdout=True)
        ).communicate(input=file_bytes)

    except Exception as e:
        raise RuntimeError(f"Failed to load audio: {e}") from e

    return np.frombuffer(out, np.int16).flatten().astype(np.float32) / 32768.0


def get_text_from_speach(audio_bytes: bytes):
    audio = load_audio(audio_bytes)
    transcript = model.transcribe(audio, language="ru")
    return transcript.get('text')


if __name__ == '__main__':
    with open('assets/chatgpt-is.mp3', 'rb') as f:
        file_bytes = f.read()
    text = get_text_from_speach(file_bytes)
    print(text)
