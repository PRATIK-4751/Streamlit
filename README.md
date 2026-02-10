# 🌌 NeonCoder AI 🌌

<div align="center">

![NeonCoder AI Banner](https://img.shields.io/badge/NeonCoder-AI-00ff41?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white)

**Welcome to NeonCoder AI, a cutting-edge, neon-themed coding assistant built with Streamlit and powered by the Qwen2.5-coder model via Ollama.**

*This tool empowers developers to generate Python code, visualize data with stunning graphs, and deploy apps across platforms like Docker, FastAPI, Streamlit, and AWS Lambda—all wrapped in a futuristic cyber neon interface!* 🚀

**Made by [Pratik](https://github.com/PRATIK-4751)**  
*Last Updated: August 04, 2025, 05:23 AM IST*

</div>

---

## ✨ Features ✨

| Icon | Feature | Description |
|------|---------|-------------|
| 💻 | **Code Wizard** | Generate Python code (e.g., Fibonacci sequence, data analysis) with one click |
| 📊 | **Graph Execution** | Toggle interactive Plotly charts to visualize code output |
| 🎨 | **Neon UI** | Sleek, customizable cyber neon design with glowing green accents |
| ⏱️ | **Real-Time Feedback** | Test your Ollama server connection from the sidebar |
| 🔄 | **User-Friendly Tabs** | Seamlessly switch between coding and deployment tasks |

---

## 🛠️ Prerequisites

Before launching NeonCoder AI, ensure these are installed:

| Requirement | Details |
|-------------|---------|
| 🐍 **Python 3.8+** | Required runtime environment |
| 📂 **Git** | For cloning the repository |
| 🤖 **Ollama** | Local AI model server with qwen2.5-coder:7b |
| 📦 **Python Libraries** | streamlit, requests, pandas, plotly-express |

---

## 📥 Installation

### Step 1: Clone the Repository
```bash
# Navigate to your desired directory
cd ~/Desktop

# Clone the repo
git clone https://github.com/PRATIK-4751/Streamlit.git

# Enter the project directory
cd Streamlit
```

### Step 2: Set Up a Virtual Environment
```bash
# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
# Install required packages
pip install -r requirements.txt
```

If `requirements.txt` is missing, create it with:
```txt
streamlit
requests
pandas
plotly-express
```

### Step 4: Set Up Ollama
```bash
# Install Ollama from https://ollama.ai/
# Pull the model
ollama pull qwen2.5-coder:7b

# Start the server
ollama serve
```

> **Note:** Ensure it runs on `http://localhost:11434` (default port).

---

##  Running the Application

With the virtual environment active and Ollama running, start the app:

```bash
streamlit run app.py
```

1. Open your browser at the URL Streamlit provides (usually `http://localhost:8501`)
2. Test the connection in the sidebar by clicking **"Test Connection"**
3. A  🟢 **Ollama is running** indicates success!

---

##  Usage Instructions

###  Code Wizard Tab

| Action | Instruction |
|--------|-------------|
| 📝 **Describe Task** | Enter a task (e.g., "Create a Fibonacci function") in the text area |
| 🔧 **Generate Code** | Click "Generate Code" to get Python code |
| 📈 **Graph Toggle** | Enable "Enable Graph Execution" for Plotly charts if supported |
| 👁️ **Output** | View generated code and graphs in the UI |
---

## 🎨 Customization

- **Neon UI**: Tweak the CSS in the `st.markdown()` style block to adjust colors or effects
- **Model Config**: Modify `OLLAMA_HOST` or `MODEL` variables for different servers/models

---

## ⚠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| 🔴 **Ollama Error** | Ensure server is running at `http://localhost:11434`; check firewall |
| 📦 **Module Missing** | Run `pip install -r requirements.txt` or install missing packages |
| 📉 **Graph Failure** | Ensure code uses compatible data (e.g., Pandas DataFrames) |

---

---

---
- Built with ❤️ by **[Pratik](https://github.com/PRATIK-4751)**
- Powered by **Streamlit**, **Ollama**, and the **Qwen2.5-coder** model

---

<div align="center">

### ⭐ Star this repository if you found it helpful!

</div>
