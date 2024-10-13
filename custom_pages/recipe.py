import streamlit as st
import requests

def recipe_page():
    st.markdown("""
        <style>
        h1, h2, h3, h4, h5, h6 {
            color: gold !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("Precise Recipe and Meal Planning Assistant")
    st.write("Ask me for specific recipes, measurements, cooking instructions, and macronutrient information!")

    API_URL = "https://api.perplexity.ai/chat/completions"
    PERPLEXITY_API_KEY = "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"

    def get_perplexity_response(prompt):
        headers = {
            "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
            "Content-Type": "application/json"
        }
        system_message = """
        You are a precise and detail-oriented culinary assistant with nutritional expertise. When answering questions:
        1. Always provide specific measurements (e.g., cups, tablespoons, grams, ounces).
        2. Give step-by-step instructions with clear, numbered steps.
        3. Include cooking times and temperatures where applicable.
        4. Specify the exact quantities of ingredients.
        5. Offer alternatives for ingredients when possible, also with precise measurements.
        6. If a question is vague, ask for clarification to provide the most accurate answer.
        7. Include macronutrient information for each ingredient and the total meal:
           - Calories
           - Protein (in grams)
           - Carbohydrates (in grams)
           - Fat (in grams)
        8. Provide a breakdown of macronutrients for the entire recipe or meal.
        9. Always conclude with a tip for food safety or flavor enhancement.
        """
        data = {
            "model": "llama-3.1-sonar-small-128k-online",
            "messages": [
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ]
        }
        response = requests.post(API_URL, json=data, headers=headers)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"Error: {response.status_code}, {response.text}"

    st.markdown("""
    ### How can I assist you with precise cooking instructions and nutritional information?
    Ask me about:
    - Detailed recipes with exact measurements
    - Step-by-step cooking instructions
    - Specific ingredient quantities
    - Cooking times and temperatures
    - Precise substitution measurements
    - Macronutrient information for ingredients and the entire meal
    - Nutritional breakdown (calories, protein, carbs, fat)
    """)

    user_prompt = st.text_area("What would you like to know? I'll provide specific measurements, instructions, and macronutrient information.")

    if st.button("Get Precise Instructions and Nutrition Info"):
        if user_prompt:
            with st.spinner("Preparing your detailed answer with nutritional information..."):
                response = get_perplexity_response(user_prompt)
            st.write("Here are your precise instructions and nutritional breakdown:")
            st.write(response)
        else:
            st.warning("Please enter a question about recipes or cooking. I'll provide specific measurements, instructions, and macronutrient information.")

    st.markdown("---")
    st.markdown("Note: Always use a kitchen scale and proper measuring tools for the most accurate results. Follow food safety guidelines and adjust recipes to your dietary needs. Nutritional information is approximate and may vary based on specific ingredients and preparation methods.")

if __name__ == "__main__":
    recipe_page()
