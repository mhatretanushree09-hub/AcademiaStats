# main_app.py - AcademiaStats Dashboard
# Run: streamlit run main_app.py

import streamlit as st
import pandas as pd
import numpy as np
from styles import apply_styles
from charts import bar_chart, gpa_chart, radar_chart, heatmap, scatter_chart

# --- page setup ---
st.set_page_config(page_title="AcademiaStats", layout="wide", page_icon="🎓", initial_sidebar_state="expanded")
apply_styles()

# --- sidebar ---
with st.sidebar:
    st.markdown("""<div style="text-align:center; padding:16px 0 8px;">
        <div style="font-size:2.5rem;">🎓</div>
        <div style="font-size:1.3rem; font-weight:700; color:#a78bfa; margin-top:4px;">AcademiaStats</div>
        <div style="font-size:0.75rem; color:#64748b; letter-spacing:2px; text-transform:uppercase;">Analysis at Fingertips</div>
    </div>""", unsafe_allow_html=True)
    st.divider()
    st.markdown("##### 📂 Data Source")
    uploaded = st.file_uploader("Upload CSV/Excel", type=["csv", "xlsx"], label_visibility="collapsed")
    st.divider()
    st.markdown("##### 🔍 Quick Search")
    search = st.text_input("Search by name", placeholder="e.g. Priya, Sharma...", label_visibility="collapsed")


# --- helper to show section title ---
def header(icon, title):
    st.markdown(f'<div class="section-header"><span class="section-header-icon">{icon}</span><span class="section-header-text">{title}</span></div>', unsafe_allow_html=True)


# --- main dashboard ---
if uploaded:
    # load data
    df = pd.read_csv(uploaded) if uploaded.name.endswith(".csv") else pd.read_excel(uploaded)
    df.columns = df.columns.str.strip()
    df = df.dropna(how="all")

    
    skip = ["attendance", "gpa", "id", "roll", "year", "mobile", "phone"]
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    subjects = [c for c in num_cols if not any(k in c.lower() for k in skip)]
    att_col = next((c for c in df.columns if "attendance" in c.lower()), None)
    gpa_col = next((c for c in df.columns if "gpa" in c.lower()), None)
    name_col = next((c for c in df.columns if "name" in c.lower()), df.columns[0])
    gender_col = next((c for c in df.columns if "gender" in c.lower()), None)

    
    if search:
        df = df[df[name_col].str.contains(search, case=False, na=False)]

    
    st.markdown(f"""<div style="margin-bottom:8px;">
        <h1 style="font-size:2.2rem; font-weight:800; margin-bottom:2px;">🎓 Academic Performance Dashboard</h1>
        <p style="color:#64748b; font-size:0.95rem; margin-top:0;">
            Real-time analytics for <strong style="color:#a78bfa;">{len(df)}</strong> students
            across <strong style="color:#a78bfa;">{len(subjects)}</strong> subjects</p>
    </div>""", unsafe_allow_html=True)

    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("👥 Total Students", len(df))
    if att_col:
        avg_att = df[att_col].mean()
        m2.metric("📋 Avg Attendance", f"{avg_att:.1f}%", delta="Good" if avg_att >= 75 else "Low")
    if gpa_col:
        avg_gpa = df[gpa_col].mean()
        m3.metric("🏆 Avg GPA", f"{avg_gpa:.2f}", delta="Above Avg" if avg_gpa >= 7 else "Needs Focus")
    m4.metric("📚 Subjects", len(subjects))
    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

    
    left, right = st.columns(2)
    with left:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        header("📊", "Subject Performance")
        if subjects:
            st.plotly_chart(bar_chart(df, subjects), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with right:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        header("📈", "GPA Distribution")
        if gpa_col:
            st.plotly_chart(gpa_chart(df, gpa_col, gender_col), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    
    left, right = st.columns(2)
    with left:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        header("🎯", "Subject Radar")
        if len(subjects) >= 3:
            st.plotly_chart(radar_chart(df, subjects), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with right:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        header("🔥", "Correlation Heatmap")
        corr_cols = subjects + ([att_col] if att_col else []) + ([gpa_col] if gpa_col else [])
        if len(corr_cols) >= 2:
            st.plotly_chart(heatmap(df, corr_cols), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # scatter plot: attendance vs gpa
    if att_col and gpa_col:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        header("🔗", "Attendance vs GPA")
        st.plotly_chart(scatter_chart(df, att_col, gpa_col, name_col), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # risk management tabs
    header("🚨", "Risk Management & Alerts")
    tab1, tab2, tab3 = st.tabs(["📉 Low Attendance", "⚠️ Academic Gap", "🌟 Top Performers"])

    with tab1:
        if att_col:
            risky = df[df[att_col] < 75].sort_values(att_col)
            if not risky.empty:
                st.markdown(f"<p style='color:#f87171;font-weight:600;'>⚠ {len(risky)} students below 75%</p>", unsafe_allow_html=True)
                st.dataframe(risky.style.background_gradient(subset=[att_col], cmap="RdYlGn"), use_container_width=True, hide_index=True, height=300)
            else:
                st.success("✅ All students have attendance ≥ 75%!")

    with tab2:
        if att_col and gpa_col:
            gap = df[(df[att_col] > 85) & (df[gpa_col] < 6.0)]
            if not gap.empty:
                st.markdown(f"<p style='color:#fbbf24;font-weight:600;'>🔍 {len(gap)} students need tutoring support</p>", unsafe_allow_html=True)
                st.dataframe(gap, use_container_width=True, hide_index=True, height=300)
            else:
                st.success("✅ No academic gap detected.")

    with tab3:
        if gpa_col:
            top = df.nlargest(10, gpa_col)
            st.markdown("<p style='color:#4ade80;font-weight:600;'>🏅 Top 10 by GPA</p>", unsafe_allow_html=True)
            st.dataframe(top.style.background_gradient(subset=[gpa_col], cmap="Greens"), use_container_width=True, hide_index=True, height=300)

    # raw data section
    with st.expander("📋 View Raw Data"):
        st.dataframe(df, use_container_width=True, hide_index=True, height=400)
        st.download_button("⬇️ Download CSV", df.to_csv(index=False).encode("utf-8"), "students_filtered.csv", "text/csv")

else:
    # welcome page when no file uploaded
    st.markdown("""<div class="welcome-container">
        <div class="welcome-icon">🎓</div>
        <div class="welcome-title">AcademiaStats</div>
        <p class="welcome-subtitle">A comprehensive analytics suite designed to monitor student performance, identify academic trends, and provide data-driven insights for improved academic outcomes.</p>
        <div class="feature-grid">
            <div class="feature-item"><div class="feature-icon">📊</div><div class="feature-label">Subject Analysis</div></div>
            <div class="feature-item"><div class="feature-icon">🎯</div><div class="feature-label">Radar Charts</div></div>
            <div class="feature-item"><div class="feature-icon">🚨</div><div class="feature-label">Risk Alerts</div></div>
        </div>
    </div>""", unsafe_allow_html=True)