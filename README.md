🌍 Multi-Language Learning Bot with Real-Time Answering on Raspberry Pi

> 🎤 Speak. 🌐 Translate. 🤖 Understand. 🎧 Respond.

A full-stack, AI-powered, multilingual learning bot that runs on Raspberry Pi. It integrates **speech recognition**, **language translation**, and **machine learning** to deliver **real-time voice-based answers** with a modern **React frontend**, **Kafka streaming**, and **Dockerized deployment**.

📚 Features

- 🎙️ Speech Recognition using microphone input
- 🌐 Multi-language translation via Google Cloud API
- 🤖 Real-time AI answering engine using ML
- 📱 React front-end for user interaction
- 🛰️ Google Cloud integration for scalability
- 🔁 Kafka for real-time data streaming
- 🐳 Docker for deployment and portability

🛠️ Hardware Requirements

- Raspberry Pi 4 (or higher)
- 32GB+ MicroSD card
- USB Microphone
- 3.5mm Speaker or USB speaker
- Internet connectivity

🧰 Software Stack

| Component         | Tech Stack                      |
|------------------|----------------------------------|
| Speech Recognition | Python + SpeechRecognition lib |
| Language Translation | Google Cloud Translate API |
| AI Answering Engine | Scikit-learn (Naive Bayes)   |
| Frontend UI        | React.js                      |
| Backend API        | Flask (extendable)            |
| Streaming Layer    | Apache Kafka + Kafka-python   |
| Containerization   | Docker + Docker Compose       |

🧾 Folder Structure

multilang\_learning\_bot/
├── backend/
│   ├── speech\_recognizer.py
│   ├── translator.py
│   └── ml\_answer.py
├── kafka/
│   ├── producer.py
│   └── consumer.py
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── frontend/
│   └── App.js

🚀 Quick Start

1. Clone the Repository

bash
git clone https://github.com/yourusername/multilang_learning_bot.git
cd multilang_learning_bot

2. Setup Google Cloud

* Enable APIs:

  * Google Cloud Translate API
  * Google Speech-to-Text API
* Create Service Account → Download `key.json`
* Set env variable:

bash
export GOOGLE_APPLICATION_CREDENTIALS="/home/pi/key.json"

3. Backend (on Raspberry Pi)

bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python speech_recognizer.py

4. Kafka

Start Kafka service and test producer/consumer:

bash
# Start Kafka and Zookeeper (local or containerized)
cd kafka
python producer.py
python consumer.py

5. Frontend (React)

bash
cd frontend
npm install
npm start

6. Docker Deployment

bash
cd docker
docker-compose up --build

🧪 Testing

* Test microphone input with `arecord -D plughw:1,0 -f cd test.wav`
* Test translation by calling `translator.py`
* Test answer prediction with `ml_answer.py`
* Use frontend to interact with backend via `/api/speak`

📈 Architecture Diagram

text
User (React UI)
   |
   v
Flask API (Raspberry Pi)
   |         \
SpeechRec   Translator API (Cloud)
   |               |
   v               v
AI Response <--- Kafka Streams

🧠 Future Improvements

* 🔊 Add TTS (text-to-speech) for spoken replies
* 🧠 Use GPT or BERT for advanced Q\&A
* 📱 Convert into mobile app with React Native
* 📦 Cloud-first deployment (e.g., AWS Lambda)

 🤝 Contributing

Pull requests and feature suggestions are welcome. For major changes, open an issue first.

📜 License

MIT License © 💻 by L.P. Harisha Lakshan Warnakulasuriya

👨‍💻 Author & Credits

Built with 💡 and 💻 by L.P. Harisha Lakshan Warnakulasuriya

📬 For questions, projects, or consulting: unicornprofessionalbay@gmail.com

📝 License

This project is licensed under the MIT License. Use freely for educational and research purposes.


