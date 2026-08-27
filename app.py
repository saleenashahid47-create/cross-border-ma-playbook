```python
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Cross-Border M&A & Tech Regulation Playbook",
    page_icon="⚖️",
    layout="wide"
)

# Header Section
st.title("Cross-Border M&A, Tech Regulation, & ESG Playbook")
st.subheader("Interactive Digital Compliance & Due Diligence Framework")
st.markdown("---")

# Sidebar for Navigation
st.sidebar.header("Deal Parameters")
deal_value = st.sidebar.slider("Enterprise Value (£M)", 10, 200, 65)
target_sector = st.sidebar.selectbox(
    "Target Sector",
    ["Advanced Technology & Data Infrastructure", "Standard Commercial Tech", "Clean Energy"]
)
jurisdiction = st.sidebar.selectbox("Acquisition Type", ["US to UK Cross-Border", "Domestic UK"])

st.sidebar.markdown("---")
st.sidebar.info("**Simulated Deal:** Apex Tech Corp acquiring AuraData Ltd.")

# Main Layout with Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "1. Tech Governance & AI", 
    "2. National Security (NSI Act)", 
    "3. ESG & Anti-Greenwashing", 
    "4. Legal Tech & Due Diligence"
])

with tab1:
    st.header("Module 1: Tech-Specific Clause Bank")
    st.write(f"Evaluating IP and AI compliance for a £{deal_value}M tech acquisition.")
    
    with st.expander("View: Artificial Intelligence & Proprietary Technology Warranty"):
        st.markdown("""
        **The Target represents and warrants that:**
        * **(a)** All proprietary software, machine learning models, and algorithms are exclusively owned free from encumbrances or validly licensed.
        * **(b)** Training data and generative AI datasets have been lawfully acquired in compliance with data protection laws and third-party terms of service.
        * **(c)** No open-source software has been integrated in a manner that triggers mandatory copyleft licensing or public source code disclosure obligations.
        """)

with tab2:
    st.header("Module 2: Regulatory & FDI Risk Matrix (UK NSI Act 2021)")
    
    if target_sector == "Advanced Technology & Data Infrastructure" and jurisdiction == "US to UK Cross-Border":
        st.error("🚨 **Mandatory Notification Triggered:** Under the NSI Act 2021, this transaction requires mandatory prior clearance before completion. Closing without approval is legally void.")
    else:
        st.success("✅ Standard notification thresholds apply. Low national security intervention risk.")

    with st.expander("View: Statutory Review Timelines & Deal Execution"):
        st.markdown("""
        * **Initial Review Period:** 30 working days from government acceptance.
        * **Extended Review (Call-in):** Up to an additional 45 working days, with a further 30-day extension possible.
        * **Commercial Strategy:** SPA must include a bespoke Long Stop Date and risk-allocation provisions for Investment Security Unit (ISU) remedies.
        """)

with tab3:
    st.header("Module 3: ESG Due Diligence & Anti-Greenwashing")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Environmental (E)")
        st.write("Vetting public sustainability claims against operational reality (UN SDG 12). Preventing greenwashing risks that breach SRA Integrity Principles.")
    with col2:
        st.markdown("### Social & Governance (S & G)")
        st.write("Aligning internal management practices with transparent diversity reporting, pro bono commitments (SDG 10/16), and ethical oversight.")

    with st.expander("View: SRA Regulatory Alignment & Integrity Risk"):
        st.markdown("Ensuring overstatements of green-tech capabilities do not expose the firm or client to regulatory sanction under emerging anti-greenwashing standards.")

with tab4:
    st.header("Module 4: 'Ashurst Advance' Innovation Note")
    st.write("Optimising due diligence efficiency through alternative legal service delivery models.")
    
    workflow_option = st.selectbox(
        "Select Workflow Tool",
        ["Automated Contract Review (NLP)", "Open-Source Code Audit", "Client Collaboration Portals"]
    )
    
    if workflow_option == "Automated Contract Review (NLP)":
        st.info("Deploys natural language processing tools to scan commercial agreements for change-of-control clauses, IP indemnities, and data-sharing restrictions.")
    elif workflow_option == "Open-Source Code Audit":
        st.info("Utilises automated code-scanning tools alongside legal oversight to flag contaminating copyleft licences hidden within the target's software stack.")
    else:
        st.info("Provides secure digital client portals for real-time status tracking on regulatory filings and condition precedent (CP) satisfaction.")

```
