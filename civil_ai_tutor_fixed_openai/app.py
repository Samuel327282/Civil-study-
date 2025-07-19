
import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

st.set_page_config(page_title="Civil & Fluid Mechanics AI Tutor", page_icon="🏗️💧")

st.title("🏗️💧 Civil & Fluid Mechanics AI Tutor")
st.markdown("""
Ask me any question related to **Civil Engineering** or **Fluid Mechanics & Dynamics**.  
I'll provide detailed, professional answers with formulas, examples, and references where possible.
""")

# User input
question = st.text_input("Enter your Engineering Question:")

if st.button("Get Answer") and question.strip() != "":
    with st.spinner("Thinking..."):
        prompt = f"""
        You are a professional Civil Engineer and an expert tutor. Provide a clear, concise, and accurate answer to the following question.
        
        The question can be from:
        - Civil Engineering (Structures, Geotech, Concrete, Steel, Codes, Construction)
        - Fluid Mechanics and Fluid Dynamics (Hydraulics, Flow, Fluid Properties)

        Instructions:
        - Use technical terms where appropriate.
        - Include formulas and real-world examples when possible.
        - Reference engineering standards (like ACI, ASCE, IS Codes) if relevant.
        - Base your explanations primarily on the following references:
            - R.K. Bansal, Strength of Materials / Fluid Mechanics
            - R.C. Hibbeler (8th Edition), Structural Analysis
            - M.S. Shetty, Concrete Technology
            - B.C. Punmia, Soil Mechanics and Foundations
            - S. Ramamrutham, Theory of Structures
            - IS 456:2000, Plain and Reinforced Concrete Code of Practice
            - IS 800:2007, General Construction in Steel
            - ACI 318, Building Code Requirements for Structural Concrete
            - ASCE Manuals and Reports
            - John Douglas, Fluid Mechanics (6th Edition or later)
        
        - Do not answer questions outside these fields.

        Question: {question}

        After the answer, list the references used.
        """

        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2
            )
            answer = response.choices[0].message.content
            st.success("Answer Generated:")
            st.markdown(answer)
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("---")
st.markdown("**Powered by OpenAI & Streamlit**")
