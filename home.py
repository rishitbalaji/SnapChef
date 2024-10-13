import streamlit as st
from PIL import Image

def home_page():

    st.markdown("""
        <style>
        h1, h2, h3, h4, h5, h6 {
            color: gold !important;
        }
        </style>
    """, unsafe_allow_html=True)

    
    st.title("Welcome to Snap Chef!")

   
    image = Image.open('custom_pages/SNAP.png')
    st.image(image, use_column_width=True)

    
    st.subheader("Tired of wondering how you can cook healthy with the groceries you have?")
    st.write("""
        Snap Chef makes meal planning easy, healthy, and fun! Whether you're looking for recipe ideas, 
        step-by-step instructions, or a nearby grocery store to grab missing ingredients, Snap Chef is here to help.
    """)

 
    st.subheader("How Does Snap Chef Work?")
    st.markdown("""
    1. **Snap a Picture of Your Groceries**  
       Simply upload a photo of your groceries using our image uploader. Our advanced AI, powered by AWS Rekognition, 
       will detect and identify the ingredients from your image.
    2. **Get Personalized Recipe Suggestions**  
       Based on the ingredients we recognize from your photo, Snap Chef will provide recipe ideas with the best nutritional values you can make right now. 
       You'll get step-by-step instructions with precise measurements to make cooking a breeze.
    3. **Customize Your Meal Preferences**  
       Want a specific type of cuisine? Have dietary restrictions? No problem! Answer a few quick questions, and Snap Chef 
       will generate meals that match your preferences. We provide recipes that include alternatives for missing ingredients, 
       so you're never stuck.
    4. **Find Nearby Grocery Stores**  
       Missing an ingredient? Enter your location, and we'll show you nearby grocery stores where you can pick up what you need. 
       Thanks to Google Maps integration, finding grocery stores is fast and simple.
    5. **AI-Powered Meal Ideas**  
       Snap Chef uses the power of Perplexity AI to not only generate meal ideas but also provide a detailed grocery list and 
       step-by-step cooking instructions. Whether you need a quick meal, a health-conscious option, or something gourmet, 
       Snap Chef helps you plan and prepare with ease.
    """)


    st.subheader("Why You'll Love Snap Chef:")
    st.markdown("""
    - **No More Guesswork**: Instantly discover what you can cook with the groceries you already have.
    - **Precise Recipes**: Receive exact ingredient quantities, cooking times, and instructions to make cooking easier.
    - **Personalized to You**: Snap Chef's meal suggestions are tailored to your dietary preferences and cooking style.
    - **Nearby Grocery Finder**: Quickly find nearby stores to complete your meal without any extra hassle.
    """)

  
    st.markdown("""
    ---
    Start cooking smarter with **Snap Chef** today! Snap a picture, plan your meals, and enjoy delicious food made from the groceries you have on hand.
    """)