
# 🤖 Jarvis - Your Personal Voice Assistant

Welcome to **Jarvis**, a voice-activated personal assistant! Inspired by popular AIs like Alexa and Google Assistant, Jarvis can open websites, play music, fetch the latest news, and even answer your questions with the power of AI! 🌐🎶📰

## 🚀 Features

- **Speech Recognition**: Listen for commands using Google’s Speech API. 🗣️
- **AI-powered Responses**: Jarvis uses GPT-3.5 to process commands and generate intelligent responses. 🧠
- **Open Websites**: Automatically open websites from the extensive web library. 🌍
- **Play Music**: Request and play classic Kishore Kumar songs! 🎶
- **Fetch News**: Get the latest headlines using the News API. 📰
- **Customizable Voice**: Choose between `pyttsx3` and Google TTS for voice responses. 🔊

## 📁 Project Structure

```bash
.
├── client.py                    # Handles interaction with the OpenAI API
├── dataset.py                   # Contains datasets for websites and songs
├── main.py                      # Main script for the Jarvis assistant
├── requirements_brew.txt        # Homebrew dependencies (portaudio)
├── requirements_pip_install.txt # Python dependencies (SpeechRecognition, OpenAI, etc.)
```

### `client.py`
This script manages the communication with OpenAI's API. It defines a virtual assistant named Jarvis, who responds to general tasks, such as answering questions.

### `dataset.py`
Contains two datasets:
- **webLibrary**: A collection of popular website URLs (Google, Facebook, GitHub, etc.).
- **music**: A collection of Kishore Kumar's timeless songs with YouTube links.

### `main.py`
The heart of the assistant, this script uses:
- **Speech Recognition**: Listens for the wake word "Jarvis" and processes user commands.
- **Text-to-Speech**: Speaks back responses using `pyttsx3` or Google TTS.
- **Web and Music Commands**: Opens websites and plays songs from the dataset.
- **News Integration**: Fetches and reads out the latest news using the NewsAPI.

## 🛠️ Installation

### 1. Install Dependencies

- First, install **PortAudio** via Homebrew:
  
  ```bash
  brew install portaudio
  ```

- Then, install the Python dependencies:

  ```bash
  pip install -r requirements_pip_install.txt
  ```

### 2. Set Up Environment Variables

Add your API keys:
- **OpenAI API key** for GPT-3.5.
- **NewsAPI key** for fetching news headlines.

### 3. Run the Assistant

Simply run `main.py` to activate Jarvis:

```bash
python main.py
```

## 📦 Dependencies

### Homebrew (`requirements_brew.txt`)
- `portaudio`: Required for audio input/output in speech recognition.

### Pip (`requirements_pip_install.txt`)
- `speechrecognition`: For recognizing speech from the microphone.
- `pyaudio`: For handling microphone input.
- `setuptools`: For managing packages.
- `pyttsx3`: For text-to-speech capabilities.
- `pocketsphinx`: Another speech recognition engine (optional).
- `openai`: To interface with OpenAI's API.
- `gtts`: Google Text-to-Speech for more natural voice responses.
- `pygame`: For audio playback when using Google TTS.

## ✨ Future Improvements

- 🗺️ **Add more datasets**: Expand the website and music libraries.
- 🧑‍💻 **Voice customization**: Add different voice options.
- 🌎 **Multi-language support**: Enable support for more languages.
