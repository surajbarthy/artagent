## CONTEXT SUMMARY: AI Critique Agent Project

**Project Overview:**
I built an automated AI pipeline that critiques my daily render artworks and outputs video content for social platforms. The system can be considered an AI agent because it processes inputs, makes decisions, and takes actions autonomously.

---

### Pipeline Stages:

### Stage 1 - Text & Audio Generation:
1. **Input:** Daily render image (stored in `/images`)
2. **Text Generation:** Uses OpenAI’s GPT-4o Vision API to analyze the image and generate an art critique.  
   ✅ Later replaced OpenAI with **free local LLMs like Mistral or Llama3 using Ollama.**
3. **Audio Generation:** Converts the critique text to speech using OpenAI TTS.  
   ✅ Also explored free alternatives like **Coqui TTS or Piper TTS** to keep the process free.
4. **Outputs:**
   - Critique text file saved in `/output`
   - Audio narration saved in `/audio`

---

### Stage 2 - Video Generation:
1. Uses **FFmpeg** to combine:
   - The daily render image (static video background)
   - The generated audio narration
2. Saves final video in `/videos` as `.mp4`.

---

### Free Alternatives Implemented:
- **Text Generation:** Local LLMs via **Ollama (Mistral, Llama3, etc.)**
- **Text-to-Speech:** **Coqui TTS** or **Piper TTS**
- **Video:** FFmpeg (open-source)
- **Posting to Platforms:** Free APIs (YouTube Data API, Meta Graph API)

---

### Key Takeaways:
- This pipeline behaves like an **AI Agent** because it has:
  - **Perception:** Takes input image
  - **Reasoning/Decision-making:** Generates critique text
  - **Action:** Produces audio + video, and prepares for posting
- It’s a **multi-modal, autonomous creative AI system.**
- Potential extensions include:
  - Adding auto-posting to YouTube/Instagram
  - Implementing feedback loops (engagement-driven content)
  - Scheduling fully autonomous daily outputs

---

### Relevant Phrases for Portfolio/Resume:
- Multi-modal AI Agent pipeline for creative content
- End-to-end AI-driven system (image → text → speech → video)
- Autonomous content generation workflow using free/local AI models
- Integration of LLMs, TTS, and video processing tools
- AI Agent exhibiting perception, reasoning, and action

---

**For Future Conversations:**  
This context is about building an AI-powered daily art critique & video generation agent, using both paid APIs (OpenAI) and free local alternatives (Ollama, Coqui TTS, FFmpeg), with an emphasis on autonomous creative workflows.
