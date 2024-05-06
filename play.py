# from dotenv import load_dotenv
# load_dotenv()

# from openai import OpenAI
from playsound import playsound

# client = OpenAI()

# response = client.audio.speech.create(
#     model="tts-1",
#     voice="nova",
#     input="Hello world! This is a streaming test.",
# )

# response.stream_to_file("output.mp3")


# speech_file_path = Path(__file__).parent / "speech.mp3"
# response = client.audio.speech.create(
#     model="tts-1",
#     voice="nova",
#     input="Today is a wonderful day to build something people love!",
# )

# response.stream_to_file(speech_file_path)
playsound("output.mp3")
