const express = require('express');
const cors = require('cors');
const multer = require('multer');
const axios = require('axios');
const FormData = require('form-data');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 5000; // Node runs on Port 5000

// Middleware
app.use(cors()); // Allow React to talk to us
app.use(express.json());

// Configure Multer (Temporary storage for uploaded images)
const upload = multer({ dest: 'uploads/' });

// --- THE MAIN ROUTE ---
// React sends image here -> We send to Python -> We send answer back
app.post('/analyze', upload.single('image'), async (req, res) => {
    try {
        if (!req.file) {
            return res.status(400).json({ error: "No image uploaded" });
        }

        console.log("📸 Image Received:", req.file.originalname);

        // 1. Prepare to send image to Python
        const formData = new FormData();
        const imagePath = path.join(__dirname, req.file.path);
        
        // Read file from disk and append to form data
        formData.append('file', fs.createReadStream(imagePath));

        // 2. Call the Python AI Service (running on port 8000)
        console.log("🚀 Sending to AI Brain...");
        const aiResponse = await axios.post('http://127.0.0.1:8000/predict', formData, {
            headers: {
                ...formData.getHeaders()
            }
        });

        // 3. Get Result
        const result = aiResponse.data;
        console.log("✅ AI Answer:", result);

        // 4. Cleanup: Delete the temp file to save space
        fs.unlinkSync(imagePath);

        // 5. Send Answer to React
        res.json(result);

    } catch (error) {
        console.error("❌ Error communicating with AI:", error.message);
        // Clean up even if error
        if (req.file && fs.existsSync(req.file.path)) {
            fs.unlinkSync(req.file.path);
        }
        res.status(500).json({ error: "AI Service Failed. Is main.py running?" });
    }
});

app.listen(PORT, () => {
    console.log(`🤖 Node Server running on http://localhost:${PORT}`);
});