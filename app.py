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

# Key Statistics Metrics Display
st.markdown("### Key Industry Statistics: Gen AI Adoption Risks")
col_stat1, col_stat2, col_stat3 = st.columns(3)
col_stat1.metric("IT Leader Concern", "79%", "Worried about security & data leaks")
col_stat2.metric("Bias Vulnerability", "73%", "Unintentional reinforcement of inequalities")
col_stat3.metric("Data Leak Risk", "70%+", "Apps sharing unencrypted third-party data")

# Visual Flow: Corporate Gen AI Risk Lifecycle
st.markdown("### Visual Process: The Corporate AI Risk Escalation Cycle")
st.info("""
**[ Profit-Driven Objective ]** ➔ Prioritising speed, automation, and cost reduction over compliance.
   ⬇
**[ Opaque Training Data ]** ➔ Utilizing unvetted datasets containing hidden historical biases and copyright taints.
   ⬇
**[ Flawed Deployment ]** ➔ Institutionalizing algorithmic discrimination (e.g., recruitment or lending bias).
   ⬇
**[ Regulatory Evasion ]** ➔ Shielding DPIAs under trade secret exemptions to bypass external oversight.
   ⬇
**[ Societal Harms & Liability ]** ➔ Severe consumer harm, data breaches, and downstream buyer legal exposure.
""")

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

st.markdown("### Comparative Regulatory Review Timelines (Area Chart Visualisation)")
st.write("Cumulative working day impact across ISU review stages:")

timeline_data = pd.DataFrame({
    'Review Phase': ['Phase 1 Initial', 'Phase 2 Extended', 'Potential Extension'],
    'Cumulative Working Days': [30, 75, 105]
})
st.area_chart(timeline_data.set_index('Review Phase'))

st.markdown("---")

st.header("3. ESG Due Diligence and Anti-Greenwashing Compliance")

col_esg1, col_esg2 = st.columns(2)
with col_esg1:
    st.markdown("### Environmental Claims and UN SDG 12")
    st.write("Vetting corporate sustainability reports and carbon reduction targets against operational reality. Unsubstantiated eco-friendly claims expose businesses to severe reputational harm and regulatory sanctions under UK consumer protection laws.")

with col_esg2:
    st.markdown("### Social, Governance, and SRA Integrity")
    st.write("Evaluating workforce diversity, supply chain transparency, and modern slavery statements. Solicitors must ensure client statements do not breach Solicitors Regulation Authority principles against misleading the market.")

# Interactive Structured Data Table for ESG / Greenwashing Audit Checkpoints
st.markdown("### Interactive Matrix: ESG Compliance Audit Checkpoints")
esg_table_data = pd.DataFrame({
    'Due Diligence Area': ['Environmental Claims', 'Supply Chain Transparency', 'Workforce Diversity', 'SRA Integrity Rules'],
    'Key Risk Factor': ['Greenwashing / False Net-Zero', 'Modern Slavery & Forced Labour', 'Unbalanced Board Metrics', 'Misleading Market Disclosures'],
    'Regulatory Standard': ['UK Digital Markets Act / CMA', 'Modern Slavery Act 2015', 'Listing Rules & Quotas', 'SRA Principles 2019']
})
st.dataframe(esg_table_data, use_container_width=True)

st.markdown("---")

st.header("4. Legal Tech and Alternative Legal Services (Ashurst Advance Model)")
st.write("Evaluating how alternative legal service delivery models and automated technology optimize transaction efficiency and document review in corporate acquisitions.")

# Key metrics layout
col_m1, col_m2, col_m3 = st.columns(3)
col_m1.metric("Review Speed Increase", "400%", "+4x faster vs manual review")
col_m2.metric("Document Cost Reduction", "35%", "Average client savings")
col_m3.metric("Data Accuracy Rate", "98.5%", "NLP extraction benchmark")

st.markdown("### Workflow Efficiency Analysis (Hours Spent per Transaction Phase)")
st.write("Comparison table detailing time savings achieved through NewLaw integration:")

efficiency_table = pd.DataFrame({
    'Workflow Stage': ['Initial NDA & Due Diligence', 'Contract Discovery & NLP', 'Redacting & Risk Tagging', 'Final Closing Binders'],
    'Traditional Method (Hours)': [120, 250, 90, 40],
    'Legal Tech / ALSP Method (Hours)': [30, 45, 20, 10],
    'Efficiency Gain (%)': ['75% Saved', '82% Saved', '78% Saved', '75% Saved']
})
st.dataframe(efficiency_table, use_container_width=True)

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
