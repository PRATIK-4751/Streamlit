🌌 NeonCoder AI 🌌
Welcome to NeonCoder AI, a cutting-edge, neon-themed coding assistant built with Streamlit and powered by the Qwen2.5-coder model via Ollama. This tool empowers developers to generate Python code, visualize data with stunning graphs, and deploy apps across platforms like Docker, FastAPI, Streamlit, and AWS Lambda—all wrapped in a futuristic cyber neon interface! 🚀
Made by Pratik (PRATIK-4751 on GitHub)Last Updated: August 04, 2025, 05:23 AM IST

✨ Features ✨



Icon
Feature
Description



💻
Code Wizard
Generate Python code (e.g., Fibonacci sequence, data analysis) with one click.


📊
Graph Execution
Toggle interactive Plotly charts to visualize code output.


🚀
Deploy Master
Create deployment configs for Docker, FastAPI, Streamlit, or AWS Lambda.


🎨
Neon UI
Sleek, customizable cyber neon design with glowing green accents.


⏱️
Real-Time Feedback
Test your Ollama server connection from the sidebar.


🔄
User-Friendly Tabs
Seamlessly switch between coding and deployment tasks.



🛠️ Prerequisites 🛠️
Before launching NeonCoder AI, ensure these are installed:



Requirement
Details



🐍 Python 3.8+
Required runtime environment.


📂 Git
For cloning the repository.


🤖 Ollama
Local AI model server with qwen2.5-coder:7b.


📦 Python Libraries
streamlit, requests, pandas, plotly-express.



📥 Installation 📥
Step 1: Clone the Repository
# Navigate to your desired directory
cd ~/Desktop

# Clone the repo
git clone https://github.com/PRATIK-4751/Streamlit_coder-Deployer.git

# Enter the project directory
cd Streamlit_coder-Deployer

Step 2: Set Up a Virtual Environment
# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

Step 3: Install Dependencies
# Install required packages
pip install -r requirements.txt

If requirements.txt is missing, create it with:
streamlit
requests
pandas
plotly-express

Step 4: Set Up Ollama
# Install Ollama from https://ollama.ai/
# Pull the model
ollama pull qwen2.5-coder:7b

# Start the server
ollama serve

Ensure it runs on http://localhost:11434 (default port).

▶️ Running the Application ▶️

With the virtual environment active and Ollama running, start the app:
streamlit run app.py

(Replace app.py with your script name if different.)

Open your browser at the URL Streamlit provides (usually http://localhost:8501).

Test the connection in the sidebar by clicking "Test Connection". A ✅ 🟢 Ollama is running indicates success!



🎮 Usage Instructions 🎮
💻 Code Wizard Tab



Action
Instruction



📝 Describe Task
Enter a task (e.g., "Create a Fibonacci function") in the text area.


🔧 Generate Code
Click "Generate Code" to get Python code.


📈 Graph Toggle
Enable "Enable Graph Execution" for Plotly charts if supported.


👁️ Output
View generated code and graphs in the UI.


🚀 Deploy Master Tab



Action
Instruction



🌐 Select Platform
Choose Docker, FastAPI, Streamlit, or AWS Lambda.


📝 Describe Deployment
Enter details (e.g., "Docker for a web app").


🛠️ Build Deployment
Click "Build Deployment" for scripts/configs.



🎨 Customization 🎨

Neon UI: Tweak the CSS in the st.markdown() style block to adjust colors or effects.
Model Config: Modify OLLAMA_HOST or MODEL variables for different servers/models.


⚠️ Troubleshooting ⚠️



Issue
Solution



🔴 Ollama Error
Ensure server is running at http://localhost:11434; check firewall.


📦 Module Missing
Run `pip list


📉 Graph Failure
Ensure code uses compatible data (e.g., Pandas DataFrames).



🤝 Contributing 🤝
Fork this repo, enhance it, and submit pull requests! Collaborate via GitHub or add contributors in the repo settings.

📜 License 📜
Open-source project. Use and modify freely, but credit Pratik (PRATIK-4751).

🙌 Acknowledgments 🙌

Built with ❤️ by Pratik.
Powered by Streamlit, Ollama, and the Qwen2.5-coder model.
Gratitude to the open-source community! 🌍
