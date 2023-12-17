from typing import Optional
from fastapi import APIRouter
from fastapi.responses import StreamingResponse, FileResponse
from pydantic import BaseModel
from scipy.io import wavfile
import soundfile as sf

#from typing import Optional
from app import tts

router = APIRouter(
   # prefix="/",
   # tags=["generate"],
   # responses={404: {"description": "Not found"}},
)

class Generation(BaseModel):
    model_name: str  # RVC Model
    f0_key_up: int = 0 #Pitch
    f0_method: str = "rmvpe"  # Added this line
    index_rate: int = 1
    protect0: float = 0.33
    tts_voice: str = "ru-RU-DmitryNeural-Male"
    speed: int = 0
    tts_text: str  #tts prompt
    output_file_path: str
    #edge_tts_output: Optional[str] 

@router.post("/generate")
def generate(gen: Generation):

    info, edge_tts_output, tts_out, tgt  = tts(
                gen.model_name,
                gen.speed,
                gen.tts_text,
                gen.tts_voice,
                gen.f0_key_up,
                gen.f0_method,
                gen.index_rate,
                gen.protect0
    )
    #if info:
  #      return StreamingResponse(tts_out, media_type="audio/x-wav")
  #  else:
    print(info)
    fullpath = "E:\\rvc-tts-webui\\"+gen.output_file_path+".ogg"
    #wavfile.write(fullpath, tgt, tts_out)
    sf.write(file=fullpath, samplerate=tgt, data=tts_out, format='ogg')
    print(f"\nFile finished writing to: {fullpath}")
    return FileResponse(fullpath, media_type="audio/ogg")
