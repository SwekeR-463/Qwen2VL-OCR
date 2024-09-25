import gradio as gr
from PIL import Image
import json
from byaldi import RAGMultiModalModel
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor
from qwen_vl_utils import process_vision_info
import torch

# Load models
def load_models():
    RAG = RAGMultiModalModel.from_pretrained("vidore/colpali")
    model = Qwen2VLForConditionalGeneration.from_pretrained("Qwen/Qwen2-VL-2B-Instruct",
                                                            trust_remote_code=True, torch_dtype=torch.float32)  # float32 for CPU
    processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-2B-Instruct", trust_remote_code=True)
    return RAG, model, processor

RAG, model, processor = load_models()

# Function for OCR and search
def ocr_and_search(image, keyword):
    
    text_query = "Extract all the text in Sanskrit and English from the image."
    
    # Prepare message for Qwen model
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image", "image": image},
                {"type": "text", "text": text_query},
            ],
        }
    ]
    
    # Process the image
    text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    image_inputs, video_inputs = process_vision_info(messages)
    inputs = processor(
        text=[text],
        images=image_inputs,
        videos=video_inputs,
        padding=True,
        return_tensors="pt",
    ).to("cpu")  # Use CPU

    # Generate text
    with torch.no_grad():
        generated_ids = model.generate(**inputs, max_new_tokens=2000)
        generated_ids_trimmed = [out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)]
        extracted_text = processor.batch_decode(
            generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
        )[0]
    
    # Save extracted text to JSON
    output_json = {"query": text_query, "extracted_text": extracted_text}
    json_output = json.dumps(output_json, ensure_ascii=False, indent=4)
    
    # Perform keyword search
    keyword_lower = keyword.lower()
    sentences = extracted_text.split('. ')
    matched_sentences = [sentence for sentence in sentences if keyword_lower in sentence.lower()]
    
    return extracted_text, matched_sentences, json_output


# Gradio App 
def app(image, keyword):
    
    extracted_text, search_results, json_output = ocr_and_search(image, keyword)
    
    search_results_str = "\n".join(search_results) if search_results else "No matches found."
    
    return extracted_text, search_results_str, json_output

# Gradio Interface
iface = gr.Interface(
    fn=app, 
    inputs=[
        gr.Image(type="pil", label="Upload an Image"),  
        gr.Textbox(label="Enter keyword to search in extracted text", placeholder="Keyword")
    ], 
    outputs=[
        gr.Textbox(label="Extracted Text"),
        gr.Textbox(label="Search Results"),
        gr.JSON(label="JSON Output")
    ],
    title="OCR and Keyword Search in Images",
)

# Launch Gradio App
iface.launch()