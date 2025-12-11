import time
import wave
import numpy as np
import whisper
from datetime import datetime
from pathlib import Path
import subprocess
import tempfile


CAMINHO_AUDIOS = Path("/mnt/windows/_insta/instagram-ma._.ria._.edu._.arda/your_instagram_activity/messages/inbox/").resolve()
CAMINHO_SAIDA = Path("/home/nonaka/Documentos/Vaults/Notes/+").resolve()


def listar_audios(pasta):
    exts = ['.mp3', '.wav', '.ogg', '.opus', '.m4a', '.mp4', '.flac']
    return [f for f in pasta.iterdir() if f.suffix.lower() in exts]


def has_audio_stream(path: Path) -> bool:
    try:
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-select_streams", "a",
             "-show_entries", "stream=codec_type", "-of", "default=nw=1",
             str(path)],
            capture_output=True, text=True
        )
        return "codec_type=audio" in result.stdout
    except:
        return False


def converter_para_wav(arquivo: Path) -> Path:
    temp_file = Path(tempfile.gettempdir()) / f"{arquivo.stem}.wav"
    cmd = [
        "ffmpeg", "-y", "-i", str(arquivo),
        "-ac", "1", "-ar", "16000",
        "-vn",  # remove vídeo
        str(temp_file)
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return temp_file


def wav_valido(wav_path: Path) -> bool:
    """
    Verifica se o WAV é silencioso ou inválido.
    """
    try:
        with wave.open(str(wav_path), "rb") as wav:
            nframes = wav.getnframes()
            framerate = wav.getframerate()

            # duração mínima real
            dur = nframes / float(framerate)
            if dur < 0.2:  # <200 ms → inválido
                return False

            frames = wav.readframes(nframes)
            audio = np.frombuffer(frames, dtype=np.int16)

            # checa silêncio total
            if np.all(audio == 0):
                return False

        return True

    except Exception:
        return False


def transcrever_audio(caminho_audio, modelo):
    print(f"\n▶️ Transcrevendo: {caminho_audio.name}")

    if not has_audio_stream(caminho_audio):
        print(f"❌ Sem faixa de áudio → ignorado.")
        return None

    wav_temp = converter_para_wav(caminho_audio)

    if not wav_valido(wav_temp):
        print(f"❌ Áudio inválido/silencioso → ignorado.")
        return None

    try:
        inicio = time.time()
        resultado = modelo.transcribe(str(wav_temp), fp16=False)
        print(f"✔️ Finalizado em {time.time() - inicio:.2f}s")
        return resultado["text"]
    except Exception as e:
        print(f"❌ Erro ao transcrever {caminho_audio.name}: {e}")
        return None


def gerar_nome_arquivo_md():
    agora = datetime.now()
    return f"transcricoes_{agora.strftime('%Y-%m-%d_%H-%M-%S')}.md"


def gerar_frontmatter():
    hoje = datetime.now().strftime("%Y-%m-%d")
    return f"""---
created: "[[{hoje}]]"
tags:
  - transcriptions
---\n\n"""


def processar_todos_audios(modelo_nome="medium"):
    audios = listar_audios(CAMINHO_AUDIOS)
    print(f"📥 {len(audios)} arquivos encontrados.")

    modelo = whisper.load_model(modelo_nome)
    print("Modelo carregado.")

    CAMINHO_SAIDA.mkdir(parents=True, exist_ok=True)
    markdown_path = CAMINHO_SAIDA / gerar_nome_arquivo_md()

    with open(markdown_path, "w", encoding="utf-8") as md:
        md.write(gerar_frontmatter())

        for audio in audios:
            texto = transcrever_audio(audio, modelo)
            if texto:
                md.write("\n---\n\n")
                md.write(f"[[{audio.name}]]\n\n")
                md.write(texto.strip() + "\n\n")
                md.write("---\n")

    print(f"\n📄 Salvo em:\n{markdown_path}")


if __name__ == "__main__":
    processar_todos_audios("medium")


