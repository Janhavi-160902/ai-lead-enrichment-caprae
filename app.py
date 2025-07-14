import streamlit as st
import pandas as pd
from enrich import enrich_company_data

# 🖼️ Page setup
st.set_page_config(page_title="AI Lead Enricher", layout="centered", page_icon="🔍")

# 🎨 Custom styling
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .css-1d391kg { visibility: hidden; }  /* Hide "Made with Streamlit" footer */
        th, td {
            text-align: center !important;
        }
    </style>
""", unsafe_allow_html=True)

# 🧠 Title + Description
st.markdown("""
<h1 style='text-align: center; font-size: 2.8em; margin-bottom: 0.2em;'>🔍 AI-Powered Lead Enrichment Tool</h1>
<p style='text-align: center; font-size: 1.1em; color: gray;'>
Upload domains → Enrich leads → Score them → Export high-priority targets
</p>
<hr style='border: 1px solid #f0f0f0;' />
""", unsafe_allow_html=True)

# 📤 Upload section
uploaded_file = st.file_uploader("📁 Upload a CSV with a column named `domain`", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    if 'domain' not in df.columns:
        st.error("❌ CSV must contain a column named 'domain'")
    else:
        st.markdown("### 📄 Uploaded Data")
        st.dataframe(df.head(), use_container_width=True)

        if st.button("🚀 Enrich Leads"):
            enriched_df = enrich_company_data(df)
            st.success("✅ Leads enriched successfully!")

            st.markdown("### 🔎 Enriched Leads with Scores")
            st.dataframe(enriched_df, use_container_width=True)

            # 📊 Scoring guide
            with st.expander("📊 What does the score mean?"):
                st.markdown("""
                - **70+** → 🔥 High-Potential Lead  
                - **40–70** → ⚠️ Moderate Fit  
                - **Below 40** → ❌ Low Fit  
                """)

            # 📥 Download enriched results
            enriched_df.to_csv("enriched_leads.csv", index=False)
            with open("enriched_leads.csv", "rb") as file:
                st.download_button("📥 Download Enriched CSV", file, file_name="enriched_leads.csv", mime="text/csv")
