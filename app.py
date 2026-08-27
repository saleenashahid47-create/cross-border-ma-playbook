import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Cross-Border M&A & Tech Regulation Playbook",
    page_icon="⚖️",
    layout="wide"
)

# Header Section
st.title("Cross-Border M&A, Tech Regulation, & ESG Playbook")
st.subheader("Comprehensive Digital Compliance, Due Diligence & Transaction Framework")
st.markdown("---")

# Sidebar for Navigation & Deal Parameters
st.sidebar.header("Deal Parameters & Configuration")
deal_value = st.sidebar.slider("Enterprise Value (£M)", 10, 500, 120)
target_sector = st.sidebar.selectbox(
    "Target Sector",
    ["Advanced Technology & Data Infrastructure", "Standard Commercial Tech", "Clean Energy & Transition"]
)
jurisdiction = st.sidebar.selectbox("Acquisition Type", ["US to UK Cross-Border", "Domestic UK", "EU to UK Cross-Border"])

st.sidebar.markdown("---")
st.sidebar.info("**Active Transaction Profile:** Apex Tech Corp acquiring AuraData Ltd. (£120M valuation framework).")

# Main Content Sections (Stacked fully open for maximum visibility)

st.header("1. Advanced Technology & Artificial Intelligence Governance")
st.write(f"Comprehensive structural assessment and risk mitigation matrix tailored for a £{deal_value}M cross-border technology acquisition.")

st.markdown("""
### Proprietary Software & Machine Learning Model Warranties
* **Algorithmic Integrity & Ownership:** The Target represents, warrants, and undertakes that all proprietary software code, machine learning architectures, neural network weights, and commercial algorithms are exclusively owned free and clear of all liens, encumbrances, or adverse claims, or are exploited under valid, un-breached commercial licenses.
* **Generative AI & Training Data Provenance:** All training datasets, LLM fine-tuning corpora, and synthetic data streams utilized by the Target have been lawfully acquired and processed in strict compliance with applicable data protection laws, intellectual property rights, and third-party terms of service, insulating the buyer from downstream copyright infringement liability.
* **Open-Source Software (OSS) Contamination Audit:** The Target has conducted a comprehensive source code audit confirming that no copyleft or viral open-source software (such as GPL v3 or AGPL) has been integrated into proprietary commercial products in a manner that triggers mandatory source code disclosure or public licensing obligations.
""")

st.markdown("""
### Data Privacy, Cyber-Security & Cross-Border Transfers
* **GDPR & Data Protection Compliance:** Complete verification of historical and active Data Processing Agreements (DPAs) across all customer and vendor touchpoints, establishing a fully auditable compliance trail under the UK GDPR and Data Protection Act 2018.
* **International Data Transfer Mechanisms:** Audit of cross-border data flows between UK operations, US parent entities, and offshore cloud servers, validated through Standard Contractual Clauses (SCCs) and UK International Data Transfer Agreements (IDTAs) alongside robust Supplementary Measures.
* **Cyber-Security Incident Remediation:** Mandatory pre-closing disclosure framework documenting any unmitigated network vulnerabilities, ransomware events, or data security breaches occurring within the preceding 36 months, backed by specific escrow holdbacks for post-closing remediation.
""")

st.markdown("---")

st.header("2. Regulatory & Foreign Direct Investment (FDI) Risk Matrix")

if target_sector == "Advanced Technology & Data Infrastructure" and "Cross-Border" in jurisdiction:
    st.error("🚨 **CRITICAL: Mandatory Notification Triggered Under the National Security and Investment (NSI) Act 2021.**\n\nBecause this transaction involves a sensitive sector (Advanced Technology / Data Infrastructure) combined with a foreign cross-border acquirer, mandatory prior clearance from the UK Government's Investment Security Unit (ISU) is legally required before completion. **Executing closing actions without formal clearance renders the transaction legally void and exposes directors to severe civil and criminal penalties.**")
else:
    st.success("✅ **Standard Notification Profile:** Transaction falls outside mandatory pre-approval triggers under the NSI Act 2021, though voluntary notification pathways remain open to achieve legal certainty.")

st.markdown("""
### Statutory Review Timelines, Call-In Powers & Execution Strategy
* **Phase 1 Initial Review Period:** 30 working days from the formal government acceptance date of the mandatory filing notice within the Investment Security Unit (ISU).
* **Phase 2 Extended Review (Call-In Notice):** Up to an additional 45 working days if national security risks are identified, with a potential further 30-day voluntary extension window.
* **Transaction Structuring & SPA Risk Allocation:** The Sale and Purchase Agreement (SPA) must integrate bespoke Long Stop Dates, regulatory condition precedent (CP) clauses, and explicit allocation of compliance burdens and remedies demanded by the Secretary of State.
""")

st.markdown("---")

st.header("3. ESG Due Diligence & Anti-Greenwashing Compliance")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### Environmental (E) & UN SDG Alignment")
    st.write("Rrigorous vetting of corporate sustainability disclosures, carbon-offset claims, and net-zero commitments against physical operational realities (supporting UN SDG 12). Mitigating severe reputational and regulatory exposure arising from potential greenwashing violations.")

with col2:
    st.markdown("### Social & Governance (S & G) Oversight")
    st.write("Evaluating workforce diversity metrics, supply chain human rights compliance, modern slavery transparency statements, and executive governance structures to ensure strict alignment with modern institutional investment standards.")

st.markdown("""
### SRA Regulatory Alignment & Integrity Risk Management
* **SRA Principles & Integrity:** Ensuring that all marketing materials, public-facing ESG reports, and technological capability claims made by the Target do not mislead commercial markets or breach professional regulatory integrity principles.
* **Climate-Related Financial Disclosures:** Alignment with mandatory UK climate disclosure rules for large private companies, assessing climate transition risks embedded in physical data centers and software infrastructure portfolios.
""")

st.markdown("---")

st.header("4. 'Ashurst Advance' Legal Tech & Due Diligence Optimization Note")
st.write("Streamlining transaction execution velocity and lowering transaction overhead through advanced Alternative Legal Service Delivery (ALSD) frameworks.")

workflow_option = st.selectbox(
    "Select Workflow Technology Integration",
    ["Automated Contract Review & NLP Extraction", "Open-Source Code Vulnerability Audit", "Secure Client Collaboration & CP Portals"]
)

if workflow_option == "Automated Contract Review & NLP Extraction":
    st.info("**Deployment Note:** Utilizes advanced Natural Language Processing (NLP) models to parse thousands of historical commercial agreements simultaneously, instantly flagging change-of-control triggers, hidden IP indemnities, assignment restrictions, and unusual liability caps.")
elif workflow_option == "Open-Source Code Vulnerability Audit":
    st.info("**Deployment Note:** Integrates automated static application security testing (SAST) and software composition analysis (SCA) code-scanning tools alongside expert legal review to isolate license contamination risks before signing.")
else:
    st.info("**Deployment Note:** Deploys encrypted, real-time digital workspace portals to manage conditions precedent (CP) satisfaction, document execution trackers, and closing binders seamlessly across multi-jurisdictional deal teams.")
