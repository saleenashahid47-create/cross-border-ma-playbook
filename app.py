import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Cross-Border M&A & Tech Regulation Playbook",
    page_icon="⚖️",
    layout="wide"
)

# Header Section
st.title("Cross-Border M&A, Tech Regulation, & ESG Playbook")
st.subheader("Transaction Compliance & Due Diligence Framework")
st.markdown("---")

# Sidebar for Navigation & Deal Parameters
st.sidebar.header("Deal Parameters")
deal_value = st.sidebar.slider("Enterprise Value (£M)", 10, 500, 120)
target_sector = st.sidebar.selectbox(
    "Target Sector",
    ["Advanced Technology & Data Infrastructure", "Standard Commercial Tech", "Clean Energy & Transition"]
)
jurisdiction = st.sidebar.selectbox("Acquisition Type", ["US to UK Cross-Border", "Domestic UK", "EU to UK Cross-Border"])

st.sidebar.markdown("---")
st.sidebar.info("**Active Deal:** Apex Tech Corp buying AuraData Ltd. (£120M valuation).")

# Main Content Sections

st.header("1. Technology and Artificial Intelligence Governance")
st.write(f"Key legal issues for IP and AI compliance in a £{deal_value}M tech acquisition under English law.")

st.markdown("""
### Intellectual Property and Software Ownership
When buying a tech company, the main priority is making sure they actually own their software code and algorithms rather than relying on weak licences. Buyers must check that developers have signed proper assignment agreements so the company holds clear title. 

### Artificial Intelligence and Data Provenance
Generative AI models create legal risks if they are trained on copyrighted material without permission. Legal teams need to verify where the training data came from. If the target company used data unlawfully, the buyer could face copyright claims after the deal closes.

### Open-Source Software Risks
Developers often use open-source code to save time. However, some open-source licences have viral terms that force companies to make their own proprietary source code public. Due diligence must identify any risky code before contracts are exchanged.
""")

st.markdown("""
### Data Protection and Cyber Security
* **GDPR Compliance:** The target must show a clear record of data processing agreements and compliance with the UK GDPR.
* **International Transfers:** If data moves between the UK, US, and foreign cloud servers, valid transfer mechanisms like UK IDTAs must be in place.
* **Past Breaches:** Any major cyber security incidents or data leaks from the last three years need to be declared, with money held back in escrow to cover potential fallout.
""")

st.markdown("---")

st.header("2. National Security and Foreign Direct Investment (FDI)")

if target_sector == "Advanced Technology & Data Infrastructure" and "Cross-Border" in jurisdiction:
    st.error("🚨 **Mandatory Notification Required:** Under the National Security and Investment Act 2021, foreign takeovers of sensitive tech sectors need clearance before completion. Closing the deal without government approval makes the transaction legally void.")
else:
    st.success("✅ **Standard Profile:** This deal does not trigger mandatory pre-approval under the NSI Act, though voluntary clearance can be sought for legal certainty.")

st.markdown("""
### Statutory Review Timelines and Deal Execution
* **Initial Review:** The government Investment Security Unit has 30 working days to review a mandatory filing.
* **Extended Review:** If national security concerns arise, the review can be extended by another 45 working days.
* **Contract Protection:** The Sale and Purchase Agreement must include flexible long stop dates and clear rules on who pays if government remedies delay the timetable.
""")

st.markdown("---")

st.header("3. ESG Due Diligence and Anti-Greenwashing")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### Environmental Due Diligence")
    st.write("Checking whether corporate sustainability claims and net-zero targets match reality. Exaggerated eco-friendly marketing creates severe reputational damage and regulatory liability under UK consumer protection laws.")

with col2:
    st.markdown("### Social and Governance Standards")
    st.write("Reviewing workforce diversity, modern slavery statements, and supply chain ethics to ensure the business meets the standards expected by institutional investors and lenders.")

st.markdown("""
### SRA Integrity and Regulatory Alignment
Solicitors must ensure that corporate statements made during the deal do not mislead the market. Under SRA principles, lawyers cannot act in transactions where client claims cross the line into greenwashing or fraud.
""")

st.markdown("---")

st.header("4. Legal Tech and Due Diligence Optimisation")
st.write("Using alternative legal service delivery models to handle large volumes of contract review efficiently.")

workflow_option = st.selectbox(
    "Select Workflow Technology",
    ["Automated Contract Review", "Open-Source Code Audit", "Client Collaboration Portals"]
)

if workflow_option == "Automated Contract Review":
    st.info("Natural language processing tools scan hundreds of commercial agreements quickly to find change-of-control clauses, hidden liabilities, and unusual indemnities.")
elif workflow_option == "Open-Source Code Audit":
    st.info("Automated code scanning software works alongside lawyer oversight to flag licensing risks in the software stack before completion.")
else:
    st.info("Secure online workspaces allow multi-jurisdictional legal teams to track conditions precedent and manage closing documents in real time.")
