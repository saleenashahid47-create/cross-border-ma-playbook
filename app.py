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
st.subheader("Transaction Compliance & Academic Due Diligence Framework")
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
st.sidebar.info("**Active Transaction Profile:** Apex Tech Corp acquiring AuraData Ltd. (£120M valuation).")

# Main Content Sections

st.header("1. Generative AI Governance, Risk, and Corporate Control")
st.write(f"Critical legal analysis examining why generative AI cannot be left solely to profit-driven businesses, evaluated within a £{deal_value}M tech acquisition under English law.")

st.markdown("""
### The Tension Between Commercial Utilisation and Social Risk
Generative artificial intelligence drives commercial efficiency, automates complex workflows, and enhances company performance. However, because businesses inherently prioritise revenue growth over social accountability, leaving AI regulation solely to corporate management creates severe regulatory blind spots. 

### Bias, Discrimination, and Data Privacy Dangers
* **Algorithmic Bias:** Training datasets frequently encode historical societal biases. As demonstrated in recruitment tools that penalise female candidates or steer women toward lower-paying roles, unchecked corporate deployment institutionalises discrimination.
* **Data Privacy and GDPR Compliance:** Complex deep learning systems make data minimisation difficult to enforce. While Article 35 of the GDPR requires rigorous Data Protection Impact Assessments, companies routinely shield these evaluations under trade secret and intellectual property exemptions, evading external accountability.
""")

# Visual Graphic / Metrics for AI Risk Distribution
st.markdown("### Industry Sentiment on Gen AI Deployment Risks")
st.write("Survey data reflecting IT leader concerns regarding operational generative AI adoption:")

ai_risk_data = pd.DataFrame({
    'Risk Category': ['Data Security & Privacy Breaks', 'Unintentional Bias & Discrimination', 'Regulatory Non-Compliance', 'Intellectual Property Taints'],
    'Concern Level (%)': [79, 73, 68, 55]
})
st.bar_chart(ai_risk_data.set_index('Risk Category'))

st.markdown("---")

st.header("2. Regulatory Frameworks: EU AI Act vs. UK Pro-Innovation Model")

col_reg1, col_reg2 = st.columns(2)
with col_reg1:
    st.markdown("### The EU AI Act Risk-Based Approach")
    st.write("Classifies systems into unacceptable, high, limited, and minimal risk tiers, alongside strict rules for General-Purpose AI (GPAI) models. However, interpretive ambiguity regarding high-risk definitions allows commercial entities to exploit loopholes and bypass full compliance.")

with col_reg2:
    st.markdown("### The UK Pro-Innovation Framework")
    st.write("Relies on existing regulators (such as the ICO and FCA) guided by core principles like safety, transparency, and fairness. While more flexible than the EU model, it risks regulatory fragmentation across different business sectors.")

if target_sector == "Advanced Technology & Data Infrastructure" and "Cross-Border" in jurisdiction:
    st.error("🚨 **Mandatory Notification Required:** Under the National Security and Investment Act 2021, cross-border acquisitions in sensitive technology sectors require prior government clearance. Closing without approval is legally void.")
else:
    st.success("✅ **Standard Profile:** This deal bypasses mandatory pre-approval under the NSI Act, though voluntary clearance can be sought for regulatory certainty.")

st.markdown("### Comparative Regulatory Review Timelines")
st.write("Working day limits imposed by the Investment Security Unit (ISU) during government national security reviews:")

timeline_data = pd.DataFrame({
    'Review Phase': ['Phase 1 Initial Review', 'Phase 2 Extended Review', 'Potential Extension'],
    'Working Days': [30, 45, 30]
})
st.bar_chart(timeline_data.set_index('Review Phase'))

st.markdown("---")

st.header("3. ESG Due Diligence and Anti-Greenwashing Compliance")

col_esg1, col_esg2 = st.columns(2)
with col_esg1:
    st.markdown("### Environmental Claims and UN SDG 12")
    st.write("Vetting corporate sustainability reports and carbon reduction targets against operational reality. Unsubstantiated eco-friendly claims expose businesses to severe reputational harm and regulatory sanctions under UK consumer protection laws.")

with col_esg2:
    st.markdown("### Social, Governance, and SRA Integrity")
    st.write("Evaluating workforce diversity, supply chain transparency, and modern slavery statements. Solicitors must ensure client statements do not breach Solicitors Regulation Authority principles against misleading the market.")

st.markdown("---")

st.header("4. Legal Tech and Alternative Legal Services (Ashurst Advance Model)")
st.write("Evaluating how alternative legal service delivery models and automated technology optimize transaction efficiency and document review in corporate acquisitions.")

# Interactive metrics reflecting high-tier academic research
col_m1, col_m2, col_m3 = st.columns(3)
col_m1.metric("Review Speed Increase", "400%", "+4x faster vs manual review")
col_m2.metric("Document Cost Reduction", "35%", "Average client savings")
col_m3.metric("Data Accuracy Rate", "98.5%", "NLP extraction benchmark")

st.markdown("### Efficiency Comparison: Traditional Review vs. Legal Tech Workflow")
st.write("Estimated time allocation across major transaction phases comparing conventional resourcing with an integrated NewLaw approach:")

efficiency_data = pd.DataFrame({
    'Workflow Stage': ['Initial NDA & Due Diligence', 'Contract Discovery & NLP', 'Redacting & Risk Tagging', 'Final Closing Binders'],
    'Traditional Method (Hours)': [120, 250, 90, 40],
    'Legal Tech / ALSP Method (Hours)': [30, 45, 20, 10]
})
st.bar_chart(efficiency_data.set_index('Workflow Stage'))

workflow_option = st.selectbox(
    "Select Workflow Technology for Detailed Analysis",
    ["Automated Contract Review & NLP", "Open-Source Code Vulnerability Auditing", "Client Collaboration Portals"]
)

if workflow_option == "Automated Contract Review & NLP":
    st.markdown("""
    **Academic Analysis:** 
    Natural language processing tools scan hundreds of commercial agreements concurrently. Instead of junior lawyers manually reading boilerplate text, algorithms flag change-of-control triggers, hidden liabilities, and unusual indemnities rapidly, transforming review bottlenecks into structured data assets.
    """)
elif workflow_option == "Open-Source Code Vulnerability Auditing":
    st.markdown("""
    **Academic Analysis:** 
    Static application security testing software parses the target company's codebase to expose hidden open-source dependencies and dangerous copyleft licence infections prior to contract exchange, protecting the buyer from acquiring tainted proprietary assets.
    """)
else:
    st.markdown("""
    **Academic Analysis:** 
    Secure digital workspaces allow multi-jurisdictional legal teams, accountants, and client executives to track conditions precedent and manage closing checklists in real time, eliminating version control errors across complex cross-border transactions.
    """)
