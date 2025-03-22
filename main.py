import asyncio
from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import openai, silero
from livekit.plugins.elevenlabs import tts as elevenlabs_tts
from livekit.agents import llm as agents_llm
from livekit.plugins import openai
from livekit.plugins.deepgram import stt as deepgram_stt

load_dotenv()

eleven_tts = elevenlabs_tts.TTS(model="eleven_turbo_v2_5",
        voice=elevenlabs_tts.Voice(
            id="21m00Tcm4TlvDq8ikWAM",  
            name="Rachel",  
            category="premade",
            settings=elevenlabs_tts.VoiceSettings(
                stability=0.71,
                similarity_boost=0.5,
                style=0.0,
                use_speaker_boost=True
            )
        ),
        language="en",
        streaming_latency=3,
        enable_ssml_parsing=False,
        chunk_length_schedule=[80, 120, 200, 260]
    )
groq_llm = openai.LLM.with_groq(model="llama3-8b-8192", temperature=0.8)
deepgram_stt = deepgram_stt.STT(api_key="96415dfefddbcc881b55bcd8a31212009f2ce54c",
                                model="nova-3")

async def entrypoint(ctx: JobContext):
    initial_ctx = agents_llm.ChatContext().append(
        role = 'system',
        text = """
You are a specialized medical AI doctor designed to provide information and guidance related to user-described health issues. Act as if you are the doctor speacialized in medical field.

Your primary function is to:

1.  **Analyze user descriptions:** Carefully examine reported symptoms, concerns, and any provided medical history to understand the user's situation.
2.  **Offer relevant medical information:** Provide accurate and helpful information based on established medical knowledge and best practices.
3.  **Prioritize clarity:** Use clear, concise language and avoid medical jargon whenever possible. If technical terms are necessary, explain them thoroughly.
4.  **Guide, not diagnose:** Offer information and potential explanations, but explicitly state that you cannot provide diagnoses or treatment plans.
5.  **Encourage professional consultation:** Emphasize the importance of seeking advice from qualified healthcare professionals when necessary.
6.  **Engage in conversational clarification:** If needed, ask short, focused follow-up questions one at a time to better understand the user's needs, creating a conversational flow. DO NOT GIVE LONG ANSWERS.

Your goal is to be a reliable source of medical information and a helpful guide, while always emphasizing the need for professional medical advice.
"""
    )
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)
    
    assistant = VoiceAssistant(
                    vad=silero.VAD.load(),
                    stt=deepgram_stt,
                    llm=groq_llm,
                    tts=eleven_tts,
                    chat_ctx=initial_ctx
                )
    assistant.start(ctx.room)

    await asyncio.sleep(1)
    await assistant.say("Hello, I'm here to help you with any medical questions. Please describe your symptoms or concerns, and I'll do my best to provide you with accurate information and guidance.", allow_interruptions=True)



if __name__ == '__main__':
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))