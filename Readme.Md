🐮 Cattle Vision AI
Indian Indigenous Cattle Breed Identification System
![alt text](https://img.shields.io/badge/Status-Live-brightgreen)

![alt text](https://img.shields.io/badge/Model_Accuracy-97%25-blue)

![alt text](https://img.shields.io/badge/License-MIT-orange)
Cattle Vision AI is an end-to-end Deep Learning application designed to identify 10 distinct Indian Cattle & Buffalo breeds from images. Built with a Microservices architecture, it solves the challenge of distinguishing visibly similar breeds (like Sahiwal vs. Red Sindhi) to aid veterinarians, farmers, and livestock conservation efforts.
🚀 Live Demo & Deployment
⚠️ IMPORTANT NOTE FOR USERS:
This project is hosted on free cloud instances. The AI Brain goes to sleep when not in use.
Please click the "Wake up AI" link first and wait for the page to load (it will show {detail: Not Found}) before using the main website.
Service	Status	URL
Frontend (The App)	🟢 Online	[PASTE_YOUR_FRONTEND_RENDER_LINK_HERE]
AI Brain (Wake Up)	🟡 Sleepy	[PASTE_YOUR_PYTHON_RENDER_LINK_HERE]
🏗️ Architecture
The system follows a Microservices Architecture to ensure scalability and separation of concerns.
code
Mermaid
graph LR
    User[User / Smartphone] -->|Uploads Image| Frontend[React Frontend]
    Frontend -->|POST Request| Backend[Node.js API Gateway]
    Backend -->|Forwards Image| AI[Python FastAPI Service]
    AI -->|EfficientNet Inference| Model[Trained .h5 Model]
    Model -->|JSON Prediction| AI
    AI --> Backend
    Backend --> Frontend
    Frontend -->|Displays Result| User
🛠️ Tech Stack
Frontend
![alt text](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)

![alt text](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)

![alt text](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
Backend & API
![alt text](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)

![alt text](https://img.shields.io/badge/Express.js-000000?style=for-the-badge&logo=express&logoColor=white)

![alt text](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
Deep Learning
![alt text](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)

![alt text](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

![alt text](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
📊 The Data & Model
1. Dataset Collection
Since no public dataset exists for specific Indian breeds, I engineered a custom dataset:
Sources: Google Images, Bing, Agriculture University Repositories.
Cleaning: Manual filtering of over 5,000 images.
Augmentation: Rotation, Zoom, and Shear applied to balance the classes.
Specific Cropping: Applied specific cropping to Buffalo classes to force the model to learn Horn Features (Tight Curl vs. Droopy).
2. Breeds Supported (10 Classes)
Cows: Gir, Sahiwal, Red Sindhi, Kankrej, Hariana, Deoni, Kangayam, Rathi.
Buffaloes: Murrah, Jaffrabadi.
3. Model Performance
Architecture: EfficientNetB0 (Fine-Tuned).
Validation Accuracy: 97.45%.
Test Accuracy (Real World): ~91%.
Key Challenge Solved: Resolved "Double Softmax" scaling issues and 0-255 pixel normalization conflicts.
💻 Local Installation Guide
Want to run this on your own machine? Follow these steps:
1. Clone the Repository
code
Bash
git clone https://github.com/YOUR_USERNAME/Cattle-Vision-AI.git
cd Cattle-Vision-AI
2. Setup AI Service (Python)
code
Bash
cd ai-service
python -m venv .venv
# Activate venv (Windows: .venv\Scripts\activate | Mac: source .venv/bin/activate)
pip install -r requirements.txt
python main.py
# Server runs on localhost:8000
3. Setup Backend (Node.js)
Open a new terminal:
code
Bash
cd backend
npm install
npm run dev
# Server runs on localhost:5000
4. Setup Frontend (React)
Open a new terminal:
code
Bash
cd frontend
npm install
npm run dev
# App runs on localhost:5173
📸 Screenshots
(You should upload 2 screenshots to your repo: one of the homepage and one of a successful prediction result, and link them here like this:)
![alt text](https://via.placeholder.com/800x400?text=Paste+Link+To+Screenshot+Here)
👨‍💻 Author
[Your Name]
GitHub: [Your Profile Link]
LinkedIn: [Your Profile Link]