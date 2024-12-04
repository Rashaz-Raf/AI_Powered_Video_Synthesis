from openai import OpenAI
import requests
import re, os
from gtts import gTTS
import os

from moviepy.editor import *

client = OpenAI(api_key="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")

with open("generated_text.txt", "r") as file:
    text = file.read()

paragraphs = re.split(r"[,.]", text)

os.makedirs("audio", exist_ok=True)
os.makedirs("images", exist_ok=True)
os.makedirs("videos", exist_ok=True)

i = 1
for para in paragraphs[:-1]:
    response = client.images.generate(prompt=para.strip(),
                                       n=1,
                                       size="1024x1024")
    print("Generate New AI Image From Paragraph...")
    image_url = response.data[0].url

    try:
        response = requests.get(image_url, stream=True, verify=True)
        response.raise_for_status()

        with open(f"images/image{i}.jpg", "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print("The Generated Image Saved in Images Folder!")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")

    tts = gTTS(text=para, lang='en', slow=False)
    tts.save(f"audio/voiceover{i}.mp3")
    print("The Paragraph Converted into VoiceOver & Saved in Audio Folder!")

    print("Extract voiceover and get duration...")
    audio_clip = AudioFileClip(f"audio/voiceover{i}.mp3")
    audio_duration = audio_clip.duration

    print("Extract Image Clip and Set Duration...")
    image_clip = ImageClip(f"images/image{i}.jpg").set_duration(audio_duration)

    print("Customize The Text Clip...")
    text_clip = TextClip(para, fontsize=35, color="red")
    text_clip = text_clip.set_position('bottom').set_duration(audio_duration)

    print("Concatenate Audio, Image, Text to Create Final Clip...")
    clip = image_clip.set_audio(audio_clip)
    video = CompositeVideoClip([clip, text_clip])

    video = video.write_videofile(f"videos/video{i}.mp4", fps=24)
    print(f"The Video{i} Has Been Created Successfully!")
    i += 1

clips = []
l_files = os.listdir("videos")
for file in l_files:
    clip = VideoFileClip(f"videos/{file}")
    clips.append(clip)

print("Concatenate All The Clips to Create a Final Video...")
final_video = concatenate_videoclips(clips, method="compose")
final_video = final_video.write_videofile("final_video.mp4")
print("The Final Video Has Been Created Successfully!")
