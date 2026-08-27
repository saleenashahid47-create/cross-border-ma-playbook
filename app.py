import streamlit as st
import pandas as pd

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
st.write(f"Key legal issues for intellectual property and AI compliance in a £{deal_value}M tech acquisition under English law.")

st.markdown("""
### Intellectual Property and Software Ownership
When acquiring a technology business, the primary risk is whether the company holds clear legal title to its core software and algorithms, or whether ownership is fragmented through third-party contractors. Under English contract law, intellectual property created by independent developers does not automatically vest in the company unless specific assignment clauses were executed. Due diligence must trace the chain of title to ensure no founder or developer retains lingering claims.

### Artificial Intelligence and Data Provenance
Generative AI tools introduce complex compliance challenges. If the target company trained its machine learning models using copyrighted data without proper licensing, the buyer inherits substantial third-party infringement liability. Legal teams must inspect dataset acquisition logs and verify that the target has indemnity protections built into its vendor agreements.

### Open-Source Software and Viral Licences
Software development frequently relies on open-source libraries to accelerate product development. However, certain licences—such as copyleft terms under the GPL—mandate that any software combined with them must also be made publicly available as open source. Uncovering these dependencies before exchange of contracts prevents catastrophic loss of proprietary value.
""")

st.markdown("""
### Data Protection and Cyber Security Covenants
* **GDPR Verification:** Comprehensive review of customer and supplier data processing agreements to confirm full adherence to the UK GDPR.
* **Cross-Border Transfers:** Verification of valid data transfer mechanisms, such as UK International Data Transfer Agreements (IDTAs), for data moving between UK servers and international cloud hosts.
* **Cyber Security Retentions:** Establishing specific escrow accounts or price reductions if past data breaches or network vulnerabilities from the preceding three years require costly technical remediation.
""")

st.markdown("---")

st.header("2. National Security and Foreign Direct Investment (FDI)")

if target_sector == "Advanced Technology & Data Infrastructure" and "Cross-Border" in jurisdiction:
    st.error("🚨 **Mandatory Notification Required:** Under the National Security and Investment Act 2021, foreign acquisitions within sensitive technology sectors require mandatory prior clearance. Closing the transaction without government approval renders the deal legally void.")
else:
    st.success("✅ **Standard Profile:** This deal does not trigger mandatory pre-approval under the NSI Act, though voluntary clearance can be submitted to remove legal risk.")

st.markdown("### Statutory Review Timelines Breakdown")
st.write("Visualising the working day limits imposed by the Investment Security Unit (ISU) during government scrutiny:")

# Data for the NSI Timeline Chart
timeline_data = pd.DataFrame({
    'Review Phase': ['Phase 1 Initial Review', 'Phase 2 Extended Review', 'Potential Extension'],
    'Working Days': [30, 45, 30]
})

st.bar_chart(timeline_data.set_index('Review Phase'))

st.markdown("""
### Contractual Risk Allocation
Because regulatory reviews can significantly delay deal completion, the Sale and Purchase Agreement (SPA) must contain carefully negotiated long stop dates. Parties must explicitly outline who bears the financial risk if the Secretary of State imposes conditions or remedies before giving clearance.
""")

st.markdown("---")

st.header("3. ESG Due Diligence and Anti-Greenwashing")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### Environmental Due Diligence")
    st.write("Scrutinising corporate sustainability claims against physical operational realities. Exaggerated eco-friendly credentials expose companies to severe reputational damage and regulatory fines under UK consumer protection standards and greenwashing rules.")

with col2:
    st.markdown("### Social and Governance Standards")
    st.write("Assessing modern slavery compliance, workforce diversity metrics, and supply chain transparency to ensure the business meets institutional investment criteria and lending expectations.")

st.markdown("""
### SRA Integrity and Regulatory Alignment
Solicitors must ensure that marketing statements and corporate disclosures made during the transaction do not mislead the market. Under Solicitors Regulation Authority principles, lawyers must not facilitate transactions involving misleading disclosures or greenwashing.
""")

st.markdown("---")

st.header("4. Legal Tech and Due Diligence Optimisation")
st.write("Utilising modern alternative legal service delivery models to handle large-scale document reviews efficiently.")

workflow_option = st.selectbox(
    "Select Workflow Technology",
    ["Automated Contract Review", "Open-Source Code Audit", "Client Collaboration Portals"]
)

if workflow_option == "Automated Contract Review":
    st.info("Natural language processing tools scan hundreds of commercial contracts concurrently, rapidly detecting change-of-control clauses, hidden liabilities, and unusual indemnities.")
elif workflow_option == "Open-Source Code Audit":
    st.info("Automated code scanning software works alongside expert legal review to flag licence contamination risks within the software stack before completion.")
else:
    st.info("Secure online workspaces allow multi-jurisdictional legal teams to track conditions precedent and manage closing documents in real time.")
