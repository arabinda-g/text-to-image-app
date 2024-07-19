# Text-to-Image Generator
A simple AI app for generating images in Python and React.

## Requirements

- Python 3.x
- Node.js and npm
- MongoDB

## Installation

### Backend

1. Clone the repository

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the required Python packages:

    ```bash
    pip install flask flask-pymongo torch diffusers transformers flask-cors
    ```

4. Download the Stable Diffusion model:

    ```bash
    mkdir -p models/stable-diffusion-v1-4
    git lfs install
    git clone https://huggingface.co/CompVis/stable-diffusion-v1-4 models/stable-diffusion-v1-4
    ```

5. Run the Flask server:

    ```bash
    python app.py
    ```

### Frontend

1. Go to the frontend directory:

    ```bash
    cd frontend
    ```

2. Install the required npm packages:

    ```bash
    npm install
    ```

3. Start the React development server:

    ```bash
    npm start
    ```
