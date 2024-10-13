import boto3
import os
import streamlit as st
from io import BytesIO
from PIL import Image
from botocore.exceptions import ClientError
import random

# AWS credentials and configuration
AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')
REGION_NAME = 'us-east-1'  # Choose your region

# Rekognition Model ARNs
project_arn = 'arn:aws:rekognition:us-east-1:090615365495:project/SnapChef-Scenario/1728807313171'
model_arn = 'arn:aws:rekognition:us-east-1:090615365495:project/SnapChef-Scenario/version/SnapChef-Scenario.2024-10-13T01.15.13/1728807313171'
version_name = 'SnapChef-Scenario.2024-10-13T01.15.13'

# Initialize Rekognition client
rekognition = boto3.client(
    'rekognition',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=REGION_NAME
)

def start_model_if_not_running():
    try:
        response = rekognition.describe_project_versions(ProjectArn=project_arn, VersionNames=[version_name])
        status = response['ProjectVersionDescriptions'][0]['Status']

        if status != 'RUNNING':
            st.info('Starting the model...')
            rekognition.start_project_version(ProjectVersionArn=model_arn, MinInferenceUnits=1)
            st.success('Model start request sent successfully.')
        else:
            st.info('Model is already running.')
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            st.write("")
        else:
            st.error(f"AWS Error: {e.response['Error']['Code']} - {e.response['Error']['Message']}")
    except Exception as e:
        st.warning(f"Unexpected error checking model status: {str(e)}. Proceeding with detection anyway.")

def detect_food_labels(image_bytes):
    try:
        response = rekognition.detect_custom_labels(
            ProjectVersionArn=model_arn,
            Image={'Bytes': image_bytes},
            MaxResults=30,
            MinConfidence=20
        )
        return response['CustomLabels']
    except ClientError as e:
        st.error(f"AWS Error in detect_food_labels: {e.response['Error']['Code']} - {e.response['Error']['Message']}")
    except Exception as e:
        st.error(f"Unexpected error in detect_food_labels: {str(e)}")
    return []

def generate_recipe(ingredients):
    recipe_templates = [
        "Hearty {main} Stew with {side}",
        "Spicy {main} Stir-fry with {side}",
        "Creamy {main} Pasta with {side}",
        "Grilled {main} Salad with {side}",
        "Roasted {main} with {side} Medley",
        "Savory {main} Soup with {side}",
        "{main} and {side} Casserole"
    ]

    # Convert ingredients to a set to remove duplicates
    unique_ingredients = list(set(ingredients))

    if len(unique_ingredients) < 2:
        unique_ingredients.append("mixed vegetables")  # Add a generic ingredient if we don't have enough

    main_ingredient = random.choice(unique_ingredients)
    unique_ingredients.remove(main_ingredient)
    side_ingredient = random.choice(unique_ingredients)
    unique_ingredients.remove(side_ingredient)

    recipe_name = random.choice(recipe_templates).format(main=main_ingredient.capitalize(), side=side_ingredient)

    # Select 1-3 additional unique ingredients for the recipe
    additional_ingredients = random.sample(unique_ingredients, min(len(unique_ingredients), random.randint(1, 3)))

    # Combine all ingredients, ensuring no duplicates
    recipe_ingredients = list(set([main_ingredient, side_ingredient] + additional_ingredients))

    instructions = [
        f"Prepare the {main_ingredient} by washing and cutting into appropriate sizes.",
        f"In a large pan or pot, start cooking the {main_ingredient}.",
        f"Add the {side_ingredient} and other ingredients: {', '.join(additional_ingredients)}.",
        "Season with salt, pepper, and your choice of herbs or spices.",
        "Cook until all ingredients are properly done.",
        "Adjust seasoning to taste and serve hot."
    ]

    return f"""
    Title: {recipe_name}

    Ingredients:
    {chr(10).join([f"- {ingredient.capitalize()}" for ingredient in recipe_ingredients])}
    - Salt and pepper to taste
    - Cooking oil or butter as needed

    Instructions:
    {chr(10).join([f"{i+1}. {step}" for i, step in enumerate(instructions)])}

    Note: This is a generated recipe based on detected ingredients. Adjust quantities and cooking methods as needed for best results.
    """

def snap_page():
    st.markdown("""
        <style>
        h1, h2, h3, h4, h5, h6 {
            color: gold !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("Enhanced Food Detection and Recipe Generator")
    st.write("Upload an image to detect food items and get recipe suggestions!")

    start_model_if_not_running()

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        if st.button('Detect Food and Generate Recipe'):
            with st.spinner('Detecting food items...'):
                img_byte_arr = BytesIO()
                image.save(img_byte_arr, format='JPEG' if uploaded_file.type.startswith('image/jpeg') else 'PNG')
                img_byte_arr = img_byte_arr.getvalue()

                labels = detect_food_labels(img_byte_arr)
                if labels:
                    # Create a list of unique detected groceries
                    unique_groceries = list(set(label['Name'] for label in labels))

                    st.subheader("Detected Unique Groceries:")
                    st.write(unique_groceries)

                    st.subheader("Generated Recipe:")
                    with st.spinner('Generating recipe...'):
                        recipe = generate_recipe(unique_groceries)
                        st.write(recipe)
                else:
                    st.warning("No food items were detected in the image. Please try another image.")

    st.sidebar.warning("Note: Ensure your AWS_ACCESS_KEY and AWS_SECRET_KEY environment variables are set.")
    
if __name__ == "__main__":
    snap_page()
