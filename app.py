import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# Configuration
OLLAMA_HOST = "http://localhost:11434"
MODEL = "qwen2.5-coder:7b"


st.set_page_config(layout="wide", page_title="NeonCoder AI", page_icon="🔥")

st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background: #0a0a0a;
        color: #0afc0a;
    }
    h1 {
        text-shadow: 0 0 5px #0afc0a;
        text-align: center;
    }
    .neon-card {
        border: 1px solid #0afc0a;
        border-radius: 8px;
        padding: 20px;
        background: rgba(10,10,10,0.7);
        margin-bottom: 20px;
    }
    .stButton>button {
        background: transparent !important;
        color: #0afc0a !important;
        border: 1px solid #0afc0a !important;
    }
    [data-baseweb="tab"] {
        color: #8b949e !important;
        background: transparent !important;
    }
    [data-baseweb="tab"][aria-selected="true"] {
        color: #0afc0a !important;
        border-bottom: 2px solid #0afc0a !important;
    }
    pre {
        background: #111 !important;
        border: 1px solid #0afc0a !important;
    }
</style>
""", unsafe_allow_html=True)

def query_ollama(prompt):
    try:
        response = requests.post(
            f"{OLLAMA_HOST}/api/generate",
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )
        if response.status_code == 200:
            return response.json().get("response", "")
        return None
    except Exception as e:
        st.error(f"Connection error: {str(e)}")
        return None


st.title("NEONCODER AI")

tab1, tab2 = st.tabs(["💻 Code Wizard", "🚀 Deploy Master"])

with tab1:
    with st.container():
        st.markdown("<div class='neon-card'>", unsafe_allow_html=True)
        
        
        show_graph = st.checkbox("Enable Graph Execution", value=False, key="graph_toggle")
        
        prompt = st.text_area(
            "Describe your coding task:",
            value="Create a function to calculate Fibonacci sequence",
            height=150
        )
        
        if st.button("Generate Code"):
            if not prompt.strip():
                st.warning("Please enter a coding task")
            else:
                with st.spinner("Generating..."):
                    
                    raw_code = query_ollama(f"Generate Python code for: {prompt}. Return ONLY the code.")
                    
                    if raw_code:
                        
                        clean_code = raw_code.replace('```python', '').replace('```', '').strip()
                        
                        
                        st.code(clean_code, language="python")
                        
                        
                        if show_graph:
                            try:
                                
                                exec_env = {
                                    'pd': pd,
                                    'px': px,
                                    'st': st,
                                    'fig': None
                                }
                                
                                
                                if "df" not in clean_code:
                                    exec_env['df'] = pd.DataFrame({
                                        'x': range(10),
                                        'y': [i**2 for i in range(10)]
                                    })
                                
                              
                                exec(clean_code, exec_env)
                                
                                
                                if exec_env.get('fig'):
                                    st.plotly_chart(exec_env['fig'], use_container_width=True)
                                    
                            except Exception as e:
                                st.error(f"Execution error: {str(e)}")
        
        st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    with st.container():
        st.markdown("<div class='neon-card'>", unsafe_allow_html=True)
        
        platform = st.selectbox(
            "Target Platform:",
            ["Docker", "FastAPI", "Streamlit", "AWS Lambda"]
        )
        
        prompt = st.text_area(
            "Describe your deployment:",
            value=f"Create {platform} deployment for:",
            height=100
        )
        
        if st.button("Build Deployment"):
            with st.spinner("Building..."):
                deployment = query_ollama(
                    f"Generate complete {platform} deployment code for: {prompt}. Include all necessary files."
                )
                if deployment:
                    st.code(deployment, language='bash')
        
        st.markdown("</div>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### 🔌 Connection Status")
    if st.button("Test Connection"):
        try:
            requests.get(OLLAMA_HOST, timeout=5)
            st.success("🟢 Ollama is running")
        except:
            st.error("🔴 Ollama not detected")