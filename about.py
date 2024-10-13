import streamlit as st
import pandas as pd
from custom_pages.snap import snap_page

def about_page():
    st.markdown("""
        <style>
        h1, h2, h3, h4, h5, h6 {
            color: gold !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("Welcome to SnapChef!")

    st.subheader("Our Mission")
    st.write("""
        At SnapChef, we believe that healthy eating should be easy, fun, and delicious. Our AI-powered platform turns your grocery snapshots into personalized, nutritious meal ideas in seconds.
    """)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("📸 Snap a pic of your groceries")
    with col2:
        st.write("🤖 AI analyzes your ingredients")
    with col3:
        st.write("🍽️ Get personalized meal ideas")

    st.subheader("Why Choose SnapChef?")
    st.write("""
    - 🚀 **Fast**: Get meal ideas in seconds
    - 🎨 **Creative**: Discover new recipe combinations
    - 🥗 **Healthy**: Focus on nutritious, balanced meals
    - 💡 **Smart**: AI learns your preferences over time
    """)

    st.subheader("Get Started Today!")
    if st.button('Try SnapChef Now!'):
        st.session_state['current_page'] = 'snap'  # Set the session state to 'snap'
        st.rerun()  # This will cause the app to rerun, applying the new page state

    st.write("Join thousands of happy users who have revolutionized their meal planning with SnapChef!")

    st.subheader("About SnapChef")
    st.write("""
    Unlock the magic of healthy cooking with SnapChef! Simply snap a photo of your ingredients or groceries, 
    and our intelligent app will suggest delicious, nutritious recipes tailored just for you. Have a meal in mind? 
    Just ask our interactive Recipe AI for step-by-step instructions and ingredient lists, making cooking a breeze. 
    Complete a quick questionnaire about your dietary preferences, and watch as the SnapChef curates personalized 
    meal suggestions. Plus, using your location, we'll guide you to nearby stores where you can find the fresh 
    ingredients needed for your chosen recipes. Transform your cooking experience and embrace a healthier lifestyle today!
    """)

    st.subheader("Frequently Asked Questions")
    faq_expander = st.expander("Click here to view FAQs")
    with faq_expander:
        st.write("### What is SnapChef?")
        st.write("SnapChef is a platform that uses AI to turn your grocery photos into personalized recipe suggestions, making healthy cooking easy and fun.")

        st.write("### How does SnapChef work?")
        st.write("SnapChef uses advanced image recognition and AI algorithms to identify ingredients in your photos and suggest recipes based on what you have available.")

        st.write("### Is my data safe with SnapChef?")
        st.write("Yes, we take data security very seriously. All your data is encrypted and we never share your personal information with third parties.")

    st.subheader("Get in Touch")
    st.write("Have questions? We'd love to hear from you!")
    st.write("**Email:** contact@snapchef.com")
    st.write("**Phone:** +1 (123) 456-7890")

    st.subheader("Stay Updated")
    email = st.text_input("Enter your email to subscribe to our newsletter")
    if st.button("Subscribe"):
        st.success(f"Thanks for subscribing! We've sent a confirmation to {email}")

    st.subheader("Follow Us")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("[Twitter](https://twitter.com/snapchef)")
    with col2:
        st.write("[LinkedIn](https://linkedin.com/company/snapchef)")
    with col3:
        st.write("[Facebook](https://facebook.com/snapchef)")

if __name__ == "__main__":
    about_page()
