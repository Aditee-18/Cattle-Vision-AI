import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // 1. Handle File Selection
  const onSelectFile = (e) => {
    if (!e.target.files || e.target.files.length === 0) {
      return;
    }
    const file = e.target.files[0];
    setSelectedFile(file);
    setResult(null); // Reset old result
    setError(null);

    // Create a preview URL so we can show the image immediately
    const objectUrl = URL.createObjectURL(file);
    setPreview(objectUrl);
  };

  // 2. Send to Node Backend
  const handleScan = async () => {
    if (!selectedFile) return;

    setLoading(true);
    setError(null);

    const formData = new FormData();
    formData.append('image', selectedFile);

    try {
      // POST to Node.js (Port 5000)
      // Node.js will forward it to Python
      const response = await axios.post('https://cattle-backend-uw82.onrender.com/analyze', formData);
      
      console.log("Response from Backend:", response.data);
      setResult(response.data);
    } catch (err) {
      console.error(err);
      setError("Failed to analyze. Is the backend running?");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <div className="header">
        <h1>🐮 Cattle Vision AI</h1>
        <p>Indian Cattle Breed Identification System</p>
      </div>

      <div className="scanner-card">
        
        {/* Clickable Image Area */}
        <label htmlFor="fileInput">
          <div className="image-preview-area">
            {preview ? (
              <img src={preview} alt="Upload Preview" />
            ) : (
              <div className="placeholder-text">
                📂 Click to Upload Image
              </div>
            )}
          </div>
        </label>
        
        <input 
          id="fileInput" 
          type="file" 
          accept="image/*" 
          onChange={onSelectFile} 
        />

        {/* Action Button */}
        {loading ? (
          <div className="loader"></div>
        ) : (
          <button 
            className="analyze-btn" 
            onClick={handleScan}
            disabled={!selectedFile}
          >
            {selectedFile ? "🔍 Identify Breed" : "Select an Image"}
          </button>
        )}

        {/* Error Message */}
        {error && <p style={{color: '#ff6b6b', marginTop: '10px'}}>{error}</p>}

        {/* RESULTS SECTION */}
        {result && (
          <div className="result-box">
            <p style={{fontSize: '0.9rem', marginBottom: '5px'}}>Identified Breed:</p>
            <h2 className="breed-title">{result.class}</h2>
            
            <div className="confidence-section">
              <p>{result.confidence.toFixed(1)}% Match</p>
              <div className="confidence-bar-bg">
                <div 
                  className="confidence-bar-fill" 
                  style={{width: `${result.confidence}%`}}
                ></div>
              </div>
            </div>
          </div>
        )}

      </div>
    </div>
  );
}

export default App;