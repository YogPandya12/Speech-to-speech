# LiveKit Voice Assistant

This project is a voice assistant application that leverages LiveKit for real-time communications. It integrates speech-to-text (STT), a language learning model (LLM), and text-to-speech (TTS) services to facilitate seamless voice interactions. Users provide voice input, which is transcribed to text via STT, processed by the LLM, and then converted back to speech using TTS for output on the LiveKit UI.

## Features

- **Real-Time Voice Interaction**: Engage in live conversations with the assistant.
- **Speech Recognition**: Converts user voice input into text.
- **Language Processing**: Utilizes an LLM to process and generate responses.
- **Speech Synthesis**: Converts text responses back into speech for seamless interaction.

## Prerequisites

Before running the script, ensure you have the following:

- **LiveKit Credentials**:
  - **URL**: Your LiveKit server URL.
  - **API Key**: Obtainable from your LiveKit dashboard.
  - **API Secret**: Obtainable from your LiveKit dashboard.
- **Project Name**: A unique name for your LiveKit project.
- **Python**: Version 3.9 to 3.12 installed on your system.
- **API Keys**:
  - **Deepgram**: For speech-to-text services.
  - **Groq**: For language model processing.
  - **ElevenLabs**: For text-to-speech services.

## Setup Instructions

Follow these steps to set up and run the project:

1.  **Clone the Repository**:

    ```bash
    git clone https://github.com/YogPandya12/Speech-to-speech.git
    cd Speech-to-speech
    ```

2.  **Create a Virtual Environment**:

    ```bash
    python -m venv env
    ```

3.  **Activate the Virtual Environment**:

    -   On Windows:

        ```bash
        env\Scripts\activate
        ```

    -   On macOS/Linux:

        ```bash
        source env/bin/activate
        ```

4.  **Install Required Packages**:

    ```bash
    pip install -r requirements.txt
    ```

5.  **Set Environment Variables**:

    -   Create a `.env` file in the project root directory and add the following:

        ```env
        LIVEKIT_URL=your_livekit_url
        LIVEKIT_API_KEY=your_livekit_api_key
        LIVEKIT_API_SECRET=your_livekit_api_secret
        DEEPGRAM_API_KEY=your_deepgram_api_key
        GROQ_API_KEY=your_groq_api_key
        ELEVENLABS_API_KEY=your_elevenlabs_api_key
        PROJECT_NAME=your_project_name
        ```

    -   Replace the placeholder values with your actual credentials.

6.  **Run the Application**:

    ```bash
    python main.py start
    ```

## Accessing the LiveKit Agent Playground

To interact with your voice assistant:

1.  Open the LiveKit Agent Playground in your web browser.
2.  Select your project name from the list.
3.  Click "Connect" to start the voice assistant.

## Additional Resources

-   LiveKit Documentation: [AI Voice Assistant Quickstart](your_livekit_documentation_link)
-   Deepgram Documentation: [Deepgram API Reference](your_deepgram_documentation_link)
-   Groq Documentation: [Groq API Reference](your_groq_documentation_link)
-   ElevenLabs Documentation: [ElevenLabs API Reference](your_elevenlabs_documentation_link)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.

**Note**: This project is for educational and experimental purposes. Ensure you comply with the terms of service of the APIs and services used.
