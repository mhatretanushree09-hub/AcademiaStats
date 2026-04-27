# styles.py - CSS for dark theme styling
import streamlit as st

def apply_styles():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        .stApp { background: linear-gradient(135deg, #0f0c29 0%, #1a1a3e 40%, #24243e 100%); font-family: 'Inter', sans-serif; }
        section[data-testid="stSidebar"] { background: linear-gradient(180deg, #16163a 0%, #1a1a3e 100%) !important; border-right: 1px solid rgba(139,92,246,0.15); }
        section[data-testid="stSidebar"] .stMarkdown h1, section[data-testid="stSidebar"] .stMarkdown h2, section[data-testid="stSidebar"] .stMarkdown h3, section[data-testid="stSidebar"] .stMarkdown p, section[data-testid="stSidebar"] .stMarkdown label { color: #e2e8f0 !important; }
        h1,h2,h3,h4,h5,h6 { color: #f1f5f9 !important; font-family: 'Inter', sans-serif !important; }
        p, span, label, div { color: #cbd5e1; }
        .stMarkdown { color: #cbd5e1; }
        div[data-testid="stMetric"] { background: rgba(255,255,255,0.04); backdrop-filter: blur(12px); border: 1px solid rgba(139,92,246,0.2); border-radius: 16px; padding: 20px 24px; transition: all 0.3s ease; box-shadow: 0 8px 32px rgba(0,0,0,0.25); }
        div[data-testid="stMetric"]:hover { border-color: rgba(139,92,246,0.5); box-shadow: 0 8px 32px rgba(139,92,246,0.15); transform: translateY(-2px); }
        div[data-testid="stMetric"] label { color: #a5b4fc !important; font-weight: 500; font-size: 0.85rem; letter-spacing: 0.5px; text-transform: uppercase; }
        div[data-testid="stMetric"] div[data-testid="stMetricValue"] { color: #f8fafc !important; font-weight: 700; font-size: 1.8rem !important; }
        .stTabs [data-baseweb="tab-list"] { gap: 8px; background: rgba(255,255,255,0.03); border-radius: 12px; padding: 6px; }
        .stTabs [data-baseweb="tab"] { border-radius: 8px; color: #94a3b8 !important; font-weight: 500; padding: 10px 20px; }
        .stTabs [aria-selected="true"] { background: rgba(139,92,246,0.2) !important; color: #a78bfa !important; border-bottom-color: #8b5cf6 !important; }
        .stDataFrame { border-radius: 12px; overflow: hidden; border: 1px solid rgba(139,92,246,0.15); }
        hr { border-color: rgba(139,92,246,0.15) !important; }
        div[data-testid="stFileUploader"] { background: rgba(139,92,246,0.08); border-radius: 12px; padding: 16px; border: 1px dashed rgba(139,92,246,0.3); }
        .stButton > button { background: linear-gradient(135deg, #8b5cf6, #6d28d9); color: white; border: none; border-radius: 10px; padding: 8px 24px; font-weight: 600; transition: all 0.3s ease; }
        .stButton > button:hover { box-shadow: 0 0 20px rgba(139,92,246,0.4); transform: scale(1.02); }
        .stTextInput > div > div > input { background: rgba(255,255,255,0.05) !important; border: 1px solid rgba(139,92,246,0.2) !important; border-radius: 10px !important; color: #f1f5f9 !important; }
        .stTextInput > div > div > input:focus { border-color: #8b5cf6 !important; box-shadow: 0 0 0 2px rgba(139,92,246,0.2) !important; }
        .glass-card { background: rgba(255,255,255,0.04); backdrop-filter: blur(12px); border: 1px solid rgba(139,92,246,0.15); border-radius: 20px; padding: 28px; margin-bottom: 20px; box-shadow: 0 8px 32px rgba(0,0,0,0.2); }
        .welcome-container { display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 70vh; text-align: center; }
        .welcome-icon { font-size: 5rem; margin-bottom: 20px; animation: float 3s ease-in-out infinite; }
        @keyframes float { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(-15px); } }
        .welcome-title { font-size: 3.2rem; font-weight: 800; background: linear-gradient(135deg, #a78bfa, #818cf8, #6366f1); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 12px; }
        .welcome-subtitle { font-size: 1.15rem; color: #94a3b8; max-width: 500px; line-height: 1.7; }
        .feature-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 40px; max-width: 700px; }
        .feature-item { background: rgba(255,255,255,0.04); border: 1px solid rgba(139,92,246,0.15); border-radius: 16px; padding: 24px 16px; transition: all 0.3s ease; }
        .feature-item:hover { border-color: rgba(139,92,246,0.4); transform: translateY(-4px); box-shadow: 0 8px 24px rgba(139,92,246,0.12); }
        .feature-icon { font-size: 1.8rem; margin-bottom: 8px; }
        .feature-label { color: #a5b4fc; font-weight: 600; font-size: 0.85rem; }
        .section-header { display: flex; align-items: center; gap: 10px; margin-bottom: 8px; }
        .section-header-icon { background: linear-gradient(135deg, #8b5cf6, #6d28d9); border-radius: 10px; padding: 8px 12px; font-size: 1.2rem; }
        .section-header-text { font-size: 1.2rem; font-weight: 700; color: #f1f5f9 !important; }
        .streamlit-expanderHeader { color: #e2e8f0 !important; font-weight: 600; }
    </style>
    """, unsafe_allow_html=True)
