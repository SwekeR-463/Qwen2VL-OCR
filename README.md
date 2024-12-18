# Qwen2VL-OCR

This web application allows users to upload images, extract text in Hindi & English using a pre-trained vision-language model (Qwen2-VL), and search for specific keywords within the extracted text. The application uses Gradio for the user interface.

### [Live Demo](https://huggingface.co/spaces/Swekerr/Qwen2VL-OCR)  


## Project Details

### Key Features:
- **OCR:** Extracts text in English, Sanskrit, and Hindi from images using the Qwen2-VL model.
- **Keyword Search:** Search for keywords within the extracted text.
- **Multilingual Support:** Works for images containing hindi and english texts.

### Technology Stack:
- **Gradio:** Provides the user interface for image uploading and interaction.
- **Transformers:** Handles the model loading and text extraction process.
- **Torch:** Used for computation on the CPU during inference.

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- Python 3.8 or later
- Virtualenv or any Python environment management tool
- `pip` (Python package manager)

### Installation
1. **Clone the repository:**

   Open your terminal and run:
   ```bash
   git clone https://github.com/SwekeR-463/Qwen2VL-OCR.git
   cd Qwen2VL-OCR
   ```

2. **Create a virtual environment:**

   Use virtualenv or venv to create an isolated environment:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   On Windows:
   ```bash
   venv\Scripts\activate
   ```

   On Mac/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install the Dependencies:**

   After activating the virtual environment, install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Web App locally

Once the environment is set up and dependencies are installed, you can run the application locally:

1. **Start the Gradio App:**
   
   In the project directory, run:
   ```bash
   python app.py
   ```

2. **Open the Application:**
   
   Once the app starts, it will display a URL (e.g., http://127.0.0.1:7860). Open this URL in your browser to access the web application interface.

3. **Using the App:**

   <ul>
      <li>Upload Image: Click on "Upload an Image" and select an image file (JPEG, JPG, PNG).</li>
      <li>Keyword Search: Enter the keyword to search for within the extracted text.</li>
      <li>Results: The app will display the extracted text, highlight search results, and show a JSON output of the extraction.</li>
   </ul>
   

### Deployment on Hugging Face Spaces

You can deploy this application easily on Hugging Face Spaces, which supports Gradio applications natively. Follow these steps:

1. **Create a Hugging Face Account:**

   Sign up or log in to [Hugging Face.](https://huggingface.co/)


2. **Create a New Space:**

   <ul>
      <li>Navigate to the [Spaces](https://huggingface.co/spaces) section.</li>
      <li>Click on "Create a Space."</li>
      <li>Choose Gradio as the template for your Space.</li>
   </ul>

4. **Set Up the Repository:**

   <ul>
      <li>Clone the repository on Hugging Face Spaces by connecting your GitHub repository or uploading the files manually.</li>
      <li>Make sure to include the requirements.txt file to install the necessary dependencies (e.g., gradio, transformers, torch).</li>
   </ul>
   
5. **Add the Required Files:**
   Ensure the following files are in the repository:

   <ul>
      <li>app.py: The main Python script running the Gradio app.</li>
      <li>requirements.txt: The list of dependencies.</li>
   </ul>

   Hugging Face will automatically install the dependencies from requirements.txt.

6. **Push Your Changes:**

   <ul>
      <li>Once the repository is set up, commit and push your changes to Hugging Face.</li>
      <li>Hugging Face Spaces will automatically build and deploy your app.</li>
   </ul>

7. **Access Your Space:**

   <ul>
      <li>After a successful build, you will get a URL for your Space (e.g., https://huggingface.co/spaces/yourusername/your-space-name).</li>
      <li>Open this link in your browser to use the deployed application.</li>
   </ul>
   
