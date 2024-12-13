# Disclaimer: Prototype Status

**Korrektor** is an experimental prototype developed in just 30 minutes to explore the capabilities of modern tools paired with GenAI. This prototype is intended solely for demonstration purposes and will not undergo further development. It serves as a proof-of-concept to showcase how quickly and easily a basic code-refactoring application can be created.

---

# Korrektor

An AI Code Assistant built with Streamlit, Streamlit Monaco, and Ollama.

## Description

**Korrektor** is a web-based AI Code Assistant designed to refactor and optimize your code. It leverages the power of Ollama's language model to enhance code readability, efficiency, and maintainability, following Clean Code principles. The intuitive interface allows users to input code snippets and receive refactored code instantly.

## Features

- **Integrated Code Editor**: Write or paste code using the Monaco editor embedded in the app.
- **AI-Powered Refactoring**: Utilize Ollama's AI capabilities to improve your code.
- **User-Friendly Interface**: Interactive web application built with Streamlit.

## Installation

Ensure you have Python 3.12 or higher installed on your system.

1. **Clone the Repository**

   ```bash
   git clone https://github.com/trbndev/korrektor.git
   cd korrektor
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   *Alternatively, if using `pyproject.toml`:*

   ```bash
   pip install .
   ```

## Usage

1. **Run the Application**

   ```bash
   streamlit run app.py
   ```

2. **Access the App**

   The app will open in your default web browser at `http://localhost:8501/`.

3. **Refactor Your Code**

   - Write or paste your code into the Monaco editor labeled "YOUR CODE HERE".
   - Click the "Process code" button to refactor.
   - View the refactored code displayed below the editor.


## Dependencies

- **Ollama** (>=0.4.4): Language model for code refactoring.
- **Streamlit** (>=1.41.0): Web application framework.
- **Streamlit-Monaco** (>=0.1.3): Integration of Monaco code editor into Streamlit.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Ollama](https://ollama.ai/) for providing the language model.
- [Streamlit](https://streamlit.io/) for the web application framework.
- [Streamlit-Monaco](https://pypi.org/project/streamlit-monaco/) for the Monaco editor integration.
