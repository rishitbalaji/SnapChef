# SnapChef: AI-Powered Food Detection and Recipe Assistant

<img width="1435" alt="image" src="https://github.com/user-attachments/assets/74d5f198-b66c-4587-9326-2bc5e79a99da" />


SnapChef is a comprehensive web application that combines food detection, personalized recipe generation, and meal planning assistance. Using advanced AI technologies and integrations with various services, SnapChef aims to revolutionize the way users approach cooking and meal preparation.

## Video Demo

Check out our video demo to see SnapChef in action:

[SnapChef Demo](https://vimeo.com/1019109064?share=copy)

This demo showcases the key features of SnapChef, including:
- User interface and navigation
- Food detection from uploaded images
- Personalized recipe generation
- Meal planning assistance
- Grocery store locator functionality

## Features

- **User Authentication**: Secure login system using Auth0.
- **AI-Powered Food Detection**: Utilizes AWS Rekognition to identify food items in uploaded images with high accuracy.
- **Recipe Generation**: Creates unique recipes based on detected ingredients or user-specified preferences, with options for dietary restrictions.
- **Meal Planning Assistant**: Generates detailed meal plans and ideas using Perplexity AI, tailored to user preferences and ingredient availability.
- **Nutritional Information**: Provides comprehensive macronutrient breakdowns for all recommended recipes.
- **Grocery Store Locator**: Locates nearby grocery stores using Google Maps API integration, helping users source additional ingredients conveniently.
- **Multi-Page Interface**: Includes Home, About, Snap (food detection), Recipe Assistant, and Meal Ideas pages, ensuring intuitive navigation.
- **Interactive Recipe Assistant**: Answers user questions and provides step-by-step instructions for each recipe.

## Technologies Used

- **Backend**:
  - Python
  - Boto3 (AWS SDK for Python)
  - Pandas for data manipulation
- **AI & Machine Learning**:
  - AWS Rekognition for image recognition
  - Perplexity AI for recipe and meal generation
- **Web Development**:
  - Streamlit for a dynamic and user-friendly interface
  - PIL (Python Imaging Library) for image handling
- **Integrations**:
  - Auth0 for secure authentication
  - Google Maps API for location-based services

## Setup and Installation

### Prerequisites

1. Python 3.8 or higher.
2. Required Python libraries listed in `requirements.txt`.
3. AWS account with Rekognition configured.
4. Access to Auth0, Perplexity AI, and Google Maps API credentials.

### Installation Steps

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

Contributions to SnapChef are welcome! Please feel free to submit a Pull Request with bug fixes, feature additions, or enhancements. For major changes, open an issue first to discuss your ideas.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **AWS Rekognition** for providing powerful image recognition capabilities.
- **Auth0** for secure authentication services.
- **Perplexity AI** for powering intelligent recipe and meal plan generation.
- **Google Maps API** for accurate location services.
- **Streamlit** for a seamless web app framework.
- **Contributors**: A heartfelt thanks to everyone who contributed to making SnapChef a success.

## Future Enhancements

- **Ingredient Expiration Tracking**: Notify users of upcoming expiration dates to reduce food waste.
- **Voice Assistance Integration**: Enable voice-activated recipe guidance.
- **Enhanced Meal Planning**: Incorporate weekly meal schedules and shopping lists.
- **Offline Mode**: Allow users to access previously generated recipes without internet connectivity.

## Meta

[Your Name] – [your-email@example.com]

Distributed under the MIT license. See `LICENSE` for more information.

[https://github.com/yourusername/SnapChef]

