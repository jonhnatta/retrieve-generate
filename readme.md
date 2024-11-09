# Retrieve Generate

## Introduction

This project implements a system for retrieving arguments using the "Retrieve and Generate" (RAG) technique. The code is capable of extracting information from a Word document (in `.docx` format) and generating answers based on the questions asked. The goal is to facilitate the consultation of information contained in the document, allowing users to obtain answers quickly and efficiently.

## How to Run

To execute the project, follow the steps below:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jonhnatta/retrieve-generate.git
   cd retrieve-generate
   ```

2. **Install the dependencies**:
   Make sure you have Python and `pip` installed. Then, install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the document**:
   The file you want to read must be present in the root of the project.
   - The file must be of the `.docx` type.

4. **Change the code**:
5. Look for the variable `document_link` in the code and change the file name to what you placed in the root of the project.
   ```python
   document_link = "./<file_name>.docx"  # Change the path
   ```

6. **Configure the template**:
   In addition to changing the `document_link`, you should also modify the instructions in the template. Look for the following line in the code:
   ```python
   TEMPLATE = """
       <agent instruction>
       ...
   """
   ```
   Replace the instruction with another that fits your agent.

7. **Configure the API key**:
   Create a `.env` file in the root of the project and add the following line:
   ```
   OPENAI_API_KEY=<your_api_key>
   ```

8. **Run the code**:
   After ensuring that the document is in the correct place and that all dependencies are installed, you can run the code:
   ```bash
   python main.py
   ```

## Contributions

Feel free to contribute with improvements or fixes. To do this, create a fork of the repository and submit a pull request with your changes.