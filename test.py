import requests
import json
import time

url = "http://127.0.0.1:8000/generate"

payload = json.dumps({
  "model_name": "Rohan",
  "tts_text": "Джоске, какого черта! Прекрати этот беспредел. Коичи и мой друг, мы будем вместе дружить.",
  "output_file_path":"jop",
  "edge_tts_output":"edge.wav"
  
})
headers = {
  'Content-Type': 'application/json'
}

start_time = time.time()  # Start the timer

response = requests.request("POST", url, headers=headers, data=payload)

end_time = time.time()  # Stop the timer

if response.status_code == 200:
    audio_content = response.content
    
    # Save the audio to a file
    with open("generated_audio.wav", "wb") as audio_file:
        audio_file.write(audio_content)
        
    print("Audio saved successfully.")
    print("Time taken:", end_time - start_time, "seconds")
else:
    print("Error:", response.text)
