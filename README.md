# Qwen2VL-OCR

This web application allows users to upload images, extract text in Hindi & English using a pre-trained vision-language model (Qwen2-VL), and search for specific keywords within the extracted text. The application uses Gradio for the user interface.

### [Live Demo](https://huggingface.co/spaces/Swekerr/Qwen2VL-OCR)  

![Screenshot](https://github.com/user-attachments/assets/74f6f6fe-c50e-43ce-a1c6-02ff6f64b2da)

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
   
