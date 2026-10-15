import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

st.set_page_config(sss
    page_title="MEDICARE AI",
    page_icon="🩺",
    layout="wide"
)

# Website design
st.markdown("""
<style>
.stApp {
    background-color: #f0f7ff;
}
h1 {
    color: #087e8b;
}
h2, h3 {
    color: #075985;
}
</style>
""", unsafe_allow_html=True)

# Header
st.title("🩺 MEDICARE AI")
st.subheader("Your Smart Health Information Assistant")

st.info(
    "Educational project for a school expo. "
    "This website cannot diagnose illnesses or prescribe medicines."
)

# Sidebar
st.sidebar.title("MEDICARE AI")
page = st.sidebar.radio(
    "Choose a module",
    [
        "Home",
        "Health Information",
        "Medical Dictionary",
        "Urgent Warning Signs",
        "Health Data Dashboard",
        "About the Project"
    ]
)

# Sample educational information
health_info = {
    "fever": (
        "Fever means body temperature is higher than normal. "
        "It can occur with infections and other conditions. "
        "Seek medical advice if symptoms are severe or persistent."
    ),
    "headache": (
        "A headache is pain in the head. Causes vary and can include "
        "dehydration, stress, or illness. A sudden, extremely severe "
        "headache needs urgent medical attention."
    ),
    "dehydration": (
        "Dehydration happens when the body loses more fluid than it takes in. "
        "Thirst, dry mouth, and dark urine can be signs. Severe symptoms "
        "need urgent medical care."
    ),
    "anaemia": (
        "Anaemia occurs when the blood does not have enough healthy red "
        "blood cells or haemoglobin. A healthcare professional can assess "
        "the cause using appropriate tests."
    ),
    "blood pressure": (
        "Blood pressure measures the force of blood against artery walls. "
        "One reading alone may not tell the whole story. A healthcare "
        "professional can help interpret readings."
    ),
    "glucose": (
        "Blood glucose is the amount of sugar in the blood. Results depend "
        "on factors such as meal timing and the type of test. A clinician "
        "should interpret test results."
    )
}

medical_dictionary = {
    "Anaemia": "A condition involving low haemoglobin or too few healthy red blood cells.",
    "Dehydration": "A condition caused by losing more fluid than the body takes in.",
    "Glucose": "A type of sugar that provides energy to the body's cells.",
    "Heart rate": "The number of heartbeats per minute.",
    "Blood pressure": "The force of blood pushing against artery walls.",
    "Immunity": "The body's ability to defend itself against infections.",
    "Diagnosis": "A healthcare professional's identification of a condition.",
    "Symptom": "A change or problem a person experiences that may indicate illness."
}

if page == "Home":
    st.header("Welcome to your digital health assistant!")

    st.write(
        "MEDICARE AI is a Python-based educational website designed "
        "to explain basic health concepts in simple language."
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Learning Modules", "5")
    col2.metric("Medical Terms", len(medical_dictionary))
    col3.metric("Project Status", "Prototype")

    st.markdown("### What can this website do?")
    st.write("📚 Explain common health topics")
    st.write("📖 Translate medical terms into simple language")
    st.write("🚨 Explain warning signs that need urgent attention")
    st.write("📊 Display a sample health-data chart")

    st.success("Select a module from the sidebar to begin.")

elif page == "Health Information":
    st.header("📚 Health Information")

    topic = st.selectbox(
        "Choose a topic",
        list(health_info.keys())
    )

    st.subheader(topic.title())
    st.write(health_info[topic])

    st.caption(
        "This is general education, not a personal medical assessment."
    )

    question = st.text_input(
        "Or type a health topic",
        placeholder="Example: What is anaemia?"
    )

    if st.button("Explain Topic"):
        query = question.lower().strip()
        found = False

        for keyword, explanation in health_info.items():
            if keyword in query:
                st.write(explanation)
                found = True
                break

        if not found:
            st.warning(
                "This prototype does not have information about that topic. "
                "Please consult a qualified healthcare professional."
            )

elif page == "Medical Dictionary":
    st.header("📖 Medical Dictionary")

    search_term = st.text_input(
        "Search for a medical word",
        placeholder="Example: Immunity"
    )

    if search_term:
        matches = [
            (term, meaning)
            for term, meaning in medical_dictionary.items()
            if search_term.lower() in term.lower()
        ]

        if matches:
            for term, meaning in matches:
                st.markdown(f"### {term}")
                st.write(meaning)
        else:
            st.warning("Term not found in this demo dictionary.")

    else:
        for term, meaning in medical_dictionary.items():
            with st.expander(term):
                st.write(meaning)

elif page == "Urgent Warning Signs":
    st.header("🚨 Urgent Warning Signs")

    st.warning(
        "This page provides general safety information. "
        "It is not a validated emergency detector."
    )

    st.write("Seek emergency help for warning signs such as:")

    st.markdown("""
    - Severe difficulty breathing
    - Chest pain or pressure
    - Sudden weakness or difficulty speaking
    - Loss of consciousness
    - Severe bleeding
    - A severe allergic reaction
    """)

    st.error(
        "If someone may be experiencing a medical emergency, "
        "contact local emergency services immediately. In India, "
        "the emergency number is 112. Do not wait for this website."
    )

elif page == "Health Data Dashboard":
    st.header("📊 Health Data Dashboard")

    st.info(
        "All numbers below are fictional sample data for demonstrating "
        "charts. They are not real patient records or medical reference values."
    )

    data = pd.DataFrame({
        "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "Sample Visitors": [20, 35, 28, 45, 38]
    })

    st.dataframe(data, use_container_width=True)

    st.subheader("Sample Visitor Chart")

    chart_data = data.set_index("Day")
    st.bar_chart(chart_data)

    st.caption(
        "The chart demonstrates how Python can display data visually."
    )

elif page == "About the Project":
    st.header("🔬 About MEDICARE AI")

    st.write("""
    **Project title:** MEDICARE AI — Smart Health Assistant

    **Programming language:** Python

    **Framework:** Streamlit

    **Purpose:** To make general health information easier to understand.

    **Main features:**
    - Health information explorer
    - Medical dictionary
    - General emergency warning information
    - Interactive sample-data dashboard

    **Future improvements:**
    - Add a larger, reviewed health-information library
    - Improve accessibility and multilingual support
    - Add carefully evaluated natural-language search
    - Protect user privacy and test safety before any public release
    """)

    st.write("Created for a school science and technology expo.")

st.divider()

st.caption(
    "MEDICARE AI Prototype | Built with Python | "
    + datetime.now().strftime("%Y")
)