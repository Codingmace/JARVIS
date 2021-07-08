import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr

recognizer = sr.Recognizer()

def load_chunks(filename):
    long_audio = AudioSegment.from_file(filename)
    audio_chunks = split_on_silence(
        long_audio, min_silence_len=1800,
        silence_thresh=-17
    )
    return audio_chunks

def main():
#    audio_filename = input("Input the audio file path: ")
    audio_filename = "./long_audio.mp3"
    ext_index = audio_filename.rindex(".")
    text_filename = audio_filename[:ext_index] + ".txt"
    if os.path.exists(text_filename):
        overwrite = input("That path exists. Would you like Overwrite (Y/N): ")
        if overwrite == "N":
            print("You don't want to. Good thing I checked. Quitting now.")
            return;
        else:
            print("Ok we will overwrite the file")
    f = open(text_filename, "w")
    audio_chunks = load_chunks(audio_filename)
    for audio_chunk in audio_chunks:
        audio_chunk.export("temp", format="wav")
        with sr.AudioFile("temp") as source:
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio)
                f.write(text+" ") # Clean this up later
                f.flush()
                print("Chunk: {}".format(text))
            except Exception as ex:
                print("Error occured: " + ex)
    print("Cleaning up")
    os.remove("temp")
    f.close()
    print("Ok done. Have a nice day")

main()
