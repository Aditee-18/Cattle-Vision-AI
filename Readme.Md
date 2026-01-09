# 🐮 Cattle Vision AI
### *Indigenous Cattle Breed Identification System*

![React](https://img.shields.io/badge/Frontend-React-blue)
![Node](https://img.shields.io/badge/Backend-Node.js-green)
![Python](https://img.shields.io/badge/AI_Engine-FastAPI-yellow)
![TensorFlow](https://img.shields.io/badge/Model-EfficientNet-orange)

**Cattle Vision AI** is a full-stack deep learning application designed to identify **10 distinct Indian Cattle & Buffalo breeds** from images. It solves the challenge of distinguishing morphologically similar breeds (like Sahiwal vs. Red Sindhi) to assist veterinarians, farmers, and livestock researchers.

---

## 🚀 Live Demo
> **⚠️ NOTE:** This project is hosted on free cloud instances. The **Python AI Service goes to sleep** after inactivity.
> Please **click the "AI brain" link first** and wait for the page to load before trying the main app.

| Component | Status | URL |
| :--- | :--- | :--- |
| **Main Website** | 🟢 Live | **[https://cattle-frontend-bfp3.onrender.com/]** |
| **AI Service (Wake Up)** | 🟡 Sleepy | **[https://cattle-ai-brain.onrender.com]** |

---

## 🏗️ System Architecture (Microservices)
Unlike standard monolithic scripts, this project uses a decoupled architecture to ensure scalability and non-blocking performance:

1.  **Frontend (React.js):** Handles user interaction and image compression.
2.  **API Gateway (Node.js/Express):** Manages requests, handles security/CORS, and forwards data.
3.  **Inference Engine (Python/FastAPI):** A dedicated service running **EfficientNetB0** to process images and return predictions.

---

## 🛠️ Tech Stack & Key Concepts

### **Computer Vision & AI**
*   **Model:** EfficientNetB0 (Transfer Learning).
*   **Frameworks:** TensorFlow, Keras, NumPy, Pillow.
*   **Performance:** Achieved **97.45% Validation Accuracy** via fine-tuning the top 30 layers.
*   **Data Engineering:** Custom scraping of 5,000+ images, manual cropping for "Horn Feature" extraction, and 20% Data Augmentation (Rotation, Zoom, Shear).

### **Backend Engineering**
*   **Framework:** Python (FastAPI) for AI, Node.js (Express) for Orchestration.
*   **Deployment:** Render (Cloud Hosting).
*   **Communication:** RESTful APIs using Axios and Multer.

### **Frontend Development**
*   **Framework:** React.js (Vite).
*   **Styling:** Modern Glassmorphism UI with CSS3.

---

## 🐂 Supported Breeds
The model is trained to recognize the following classes:
1. **Gir** (Cow)
2. **Sahiwal** (Cow)
3. **Red Sindhi** (Cow)
4. **Kankrej** (Cow)
5. **Hariana** (Cow)
6. **Deoni** (Cow)
7. **Kangayam** (Cow)
8. **Rathi** (Cow)
9. **Murrah** (Buffalo)
10. **Jaffrabadi** (Buffalo)

---

## 💻 Local Installation

If you want to run this locally on your machine:

### 1. Clone the Repo
```bash
git clone https://github.com/Aditee-18/Cattle-Vision-AI.git
cd Cattle-Vision-AI