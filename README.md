# SnapChef: AI-Powered Food Detection and Recipe Assistant

SnapChef is a comprehensive web application that combines food detection, personalized recipe generation, and meal planning assistance. Using advanced AI technologies and integrations with various services, SnapChef aims to revolutionize the way users approach cooking and meal preparation.

## Video Demo

Check out our video demo to see SnapChef in action:

[![SnapChef Demo](https://vimeo.com/1019109064?share=copy)](https://opensource.org/licenses/MIT)


This demo showcases the key features of SnapChef, including:
- User interface and navigation
- Food detection from uploaded images
- Personalized recipe generation
- Meal planning assistance
- Grocery store locator functionality

## Features

- **User Authentication**: Secure login system using Auth0.
- **Food Detection**: Utilizes AWS Rekognition to identify food items in uploaded images.
- **Recipe Generation**: Creates unique recipes based on detected ingredients or user preferences.
- **AI-Powered Meal Planning**: Generates meal ideas and detailed recipes using Perplexity AI.
- **Grocery Store Locator**: Finds nearby grocery stores using Google Maps API.
- **Nutritional Information**: Provides macronutrient breakdowns for recipes.
- **Multi-page Interface**: Includes Home, About, Snap (food detection), Recipe Assistant, and Meal Ideas pages.

## Technologies Used

- Python
- Streamlit
- AWS Rekognition
- Auth0 for authentication
- Perplexity AI for recipe and meal idea generation
- Google Maps API for locating grocery stores
- PIL (Python Imaging Library)
- Boto3 (AWS SDK for Python)
- Pandas for data manipulation

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/snapchef.git
   cd snapchef
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory and add the following:
   ```
   AUTH0_CLIENT_ID=your_auth0_client_id
   AUTH0_CLIENT_SECRET=your_auth0_client_secret
   AUTH0_DOMAIN=your_auth0_domain
   AWS_ACCESS_KEY=your_aws_access_key
   AWS_SECRET_KEY=your_aws_secret_key
   PERPLEXITY_API_KEY=your_perplexity_api_key
   GOOGLE_MAPS_API_KEY=your_google_maps_api_key
   ```

4. Configure AWS Rekognition:
   Update the `project_arn`, `model_arn`, and `version_name` variables in the `snap.py` file with your Rekognition model details.

5. Run the application:
   ```
   streamlit run app.py
   ```

## Usage

1. **Home Page**: Introduces users to SnapChef and its features.
2. **About Page**: Provides detailed information about SnapChef's mission and functionality.
3. **Snap Page**: Allows users to upload food images for detection and recipe generation.
4. **Recipe Assistant**: Offers precise recipe instructions and nutritional information based on user queries.
5. **Meal Ideas**: Generates personalized meal suggestions based on user preferences and helps locate nearby grocery stores.

## File Structure

- `app.py`: Main application file, handles routing and authentication.
- `custom_pages/`:
  - `home.py`: Home page content.
  - `about.py`: About page content.
  - `snap.py`: Food detection and recipe generation page.
  - `recipe.py`: AI-powered recipe assistant page.
  - `meal.py`: Meal idea generator and grocery store locator page.

## Contributing

Contributions to SnapChef are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- AWS for providing the Rekognition service.
- Auth0 for authentication services.
- Perplexity AI for powering recipe and meal idea generation.
- Google Maps for grocery store location services.
- Streamlit for the web app framework.
- All contributors and supporters of this project.
