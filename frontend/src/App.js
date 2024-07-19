import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
    const [prompt, setPrompt] = useState('');
    const [imageUrl, setImageUrl] = useState('');
    const [isGenerating, setIsGenerating] = useState(false);

    const handleSubmit = async (event) => {
        event.preventDefault();
        setIsGenerating(true);
        try {
            const response = await axios.post('http://localhost:5000/generate-image', { prompt });
            setImageUrl(response.data.image_url);
        } catch (error) {
            console.error('Error generating image:', error);
        } finally {
            setIsGenerating(false);
        }
    };

    return (
        <div className="App">
            <header className="App-header">
                <h1>Text-to-Image Generator</h1>
                <form onSubmit={handleSubmit}>
                    <input
                        type="text"
                        value={prompt}
                        onChange={(e) => setPrompt(e.target.value)}
                        placeholder="Enter a text description"
                        required
                    />
                    <button type="submit" disabled={isGenerating}>
                        {isGenerating ? 'Generating image...' : 'Generate Image'}
                    </button>
                </form>
                {imageUrl && <img src={imageUrl} alt="Generated from prompt" />}
            </header>
        </div>
    );
}

export default App;
