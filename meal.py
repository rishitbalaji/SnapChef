import streamlit as st
import requests
import json
import googlemaps
import pandas as pd

PERPLEXITY_API_KEY = "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"
GOOGLE_MAPS_API_KEY = "AIzaSyCCz3s_tAbN8ye4FE9k48Aq967EGUkfBk8"  


gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)

def meal_page():
 
    st.markdown("""
        <style>
        h1, h2, h3, h4, h5, h6 {
            color: gold !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("AI-Powered Meal Idea Generator")

   
    if 'step' not in st.session_state:
        st.session_state.step = 1
    if 'answers' not in st.session_state:
        st.session_state.answers = {}
    if 'meals' not in st.session_state:
        st.session_state.meals = []
    if 'user_location' not in st.session_state:
        st.session_state.user_location = None


    questions = [
        "What type of cuisine do you prefer?",
        "Any dietary restrictions?",
        "How much time do you have for cooking? (Quick, Medium, or Lengthy)",
        "Preferred protein source?",
        "Any ingredients you want to use?"
    ]

   
    def generate_meals_ai(answers):
        prompt = f"""Generate 3 meal ideas based on the following preferences:
        Cuisine: {answers.get('What type of cuisine do you prefer?', 'Any')}
        Dietary restrictions: {answers.get('Any dietary restrictions?', 'None')}
        Cooking time: {answers.get('How much time do you have for cooking? (Quick, Medium, or Lengthy)', 'Any')}
        Protein source: {answers.get('Preferred protein source?', 'Any')}
        Ingredients to use: {answers.get('Any ingredients you want to use?', 'Any')}

        Please provide the meal names only, separated by commas."""

        response = requests.post(
            "https://api.perplexity.ai/chat/completions",
            headers={
                "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "model": "llama-3.1-sonar-small-128k-online",
                "messages": [{"role": "user", "content": prompt}]
            })
        )

        if response.status_code == 200:
            meals = response.json()["choices"][0]["message"]["content"].strip().split(", ")
            return meals
        else:
            st.error(f"Error: {response.status_code}, {response.text}")
            return []


    def get_meal_details_ai(meal):
        prompt = f"""Provide a grocery list and cooking instructions for {meal}.
        Format the response as follows:
        Grocery List:
        - Item 1
        - Item 2
        - ...

        Instructions:
        1. Step 1
        2. Step 2
        3. ...
        """

        response = requests.post(
            "https://api.perplexity.ai/chat/completions",
            headers={
                "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "model": "llama-3.1-sonar-small-128k-online",
                "messages": [{"role": "user", "content": prompt}]
            })
        )

        if response.status_code == 200:
            details = response.json()["choices"][0]["message"]["content"].strip()

            
            parts = details.split("Instructions:")
            if len(parts) == 2:
                grocery_list = parts[0].split("Grocery List:")[-1].strip()
                instructions = parts[1].strip()
            else:
                
                grocery_list = "Unable to parse grocery list"
                instructions = details

            grocery_items = [item.strip("- ").strip() for item in grocery_list.split("\n") if item.strip()]

            instruction_steps = [step.strip() for step in instructions.split("\n") if step.strip()]

            return {
                "groceries": grocery_items,
                "instructions": instruction_steps
            }
        else:
            st.error(f"Error: {response.status_code}, {response.text}")
            return {"groceries": [], "instructions": []}

    def get_nearby_grocery_stores(location, radius=5000):
        try:
            places_result = gmaps.places_nearby(
                location=location,
                radius=radius,
                type='grocery_or_supermarket'
            )
            return places_result.get('results', [])
        except Exception as e:
            st.error(f"Error fetching nearby stores: {str(e)}")
            return []

    if st.session_state.step <= len(questions):
        st.write(f"Question {st.session_state.step}/{len(questions)}")
        question = questions[st.session_state.step - 1]
        answer = st.text_input(question, key=f"q{st.session_state.step}")
        if st.button("Next"):
            st.session_state.answers[question] = answer
            st.session_state.step += 1
            st.rerun()

    elif st.session_state.step == len(questions) + 1:
        st.write("Based on your preferences, here are some AI-generated meal ideas:")
        with st.spinner("Generating meal ideas..."):
            st.session_state.meals = generate_meals_ai(st.session_state.answers)
        for meal in st.session_state.meals:
            st.write(f"- {meal}")
        selected_meal = st.selectbox("Choose a meal:", st.session_state.meals)
        if st.button("Get Recipe"):
            st.session_state.selected_meal = selected_meal
            st.session_state.step += 1
            st.rerun()

    elif st.session_state.step == len(questions) + 2:
        with st.spinner("Generating recipe details..."):
            meal_details = get_meal_details_ai(st.session_state.selected_meal)

        st.write(f"Recipe for {st.session_state.selected_meal}")
        st.write("Grocery List:")
        if meal_details["groceries"]:
            for item in meal_details["groceries"]:
                st.write(f"- {item}")
        else:
            st.write("No grocery list available.")

        st.write("Instructions:")
        if meal_details["instructions"]:
            for step in meal_details["instructions"]:
                st.write(step)
        else:
            st.write("No instructions available.")

        st.write("\nFind Nearby Grocery Stores:")
        user_address = st.text_input("Enter your address to find nearby grocery stores:")

        if user_address:
            try:
                geocode_result = gmaps.geocode(user_address)
                if geocode_result:
                    location = geocode_result[0]['geometry']['location']
                    st.session_state.user_location = (location['lat'], location['lng'])

                    st.write("Your Location:")
                    user_df = pd.DataFrame({'lat': [location['lat']], 'lon': [location['lng']]})
                    st.map(user_df, zoom=13)

                    if st.button("Search Nearby Stores"):
                        nearby_stores = get_nearby_grocery_stores(st.session_state.user_location)
                        if nearby_stores:
                            st.write("Nearby Grocery Stores:")
                            store_data = []
                            for i, store in enumerate(nearby_stores[:5], 1):  
                                st.write(f"{i}. {store['name']}: {store['vicinity']}")
                                store_data.append({
                                    'lat': store['geometry']['location']['lat'],
                                    'lon': store['geometry']['location']['lng'],
                                    'name': store['name']
                                })

                       
                            st.write("Map of Nearby Grocery Stores:")
                            stores_df = pd.DataFrame(store_data)
                            st.map(stores_df, zoom=13)
                        else:
                            st.write("No nearby grocery stores found.")
                else:
                    st.error("Unable to find the location. Please try a different address.")
            except Exception as e:
                st.error(f"Error: {str(e)}")

        if st.button("Start Over"):
            st.session_state.step = 1
            st.session_state.answers = {}
            st.session_state.meals = []
            st.session_state.user_location = None
            st.rerun()