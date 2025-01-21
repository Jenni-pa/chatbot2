import os
from jinja2 import Environment, FileSystemLoader
import PyPDF2

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

# Function to render extracted text into HTML using Jinja2
def render_to_html(extracted_text, output_html_path):
    # Get the directory of the current Python script dynamically
    script_dir = os.path.dirname(os.path.abspath(__file__))  # This gives us the absolute path of the current folder

    # Construct the path to the template.html file (assumed to be in the same directory as the script)
    template_file_path = os.path.join(script_dir, "template.html")

    # Debugging: Print the exact template path the script is looking for
    print(f"Looking for template at: {template_file_path}")

    # Check if the template file exists in the script directory
    if not os.path.exists(template_file_path):
        print(f"Template file not found at: {template_file_path}")
        return
    else:
        print(f"Template file found at: {template_file_path}")

    # Configure Jinja2 environment with the script's directory
    env = Environment(loader=FileSystemLoader(script_dir))
    
    # Load the template by name
    template = env.get_template("template.html")
    
    # Render the HTML content
    html_content = template.render(extracted_text=extracted_text)
    
    # Save the rendered HTML content to a file
    with open(output_html_path, "w", encoding="utf-8") as file:
        file.write(html_content)

# Main function to perform the entire PDF-to-HTML conversion
def main(pdf_file, output_html_file):
    # Extract text from the PDF
    extracted_text = extract_text_from_pdf(pdf_file)
    
    # Render the extracted text to HTML
    render_to_html(extracted_text, output_html_file)

# Run the main function with your PDF and output HTML filenames
if __name__ == "__main__":
    main("CNR.pdf", "output.html")
