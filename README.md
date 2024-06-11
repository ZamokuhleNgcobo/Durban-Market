# Durban-Market POTATO SIFRA (WASHED) Average Price Prediction App
This repository contains a Streamlit web application that predicts the average price of POTATO SIFRA (WASHED) based on user inputs. The application uses a pre-trained machine learning model to make predictions.

Features
User-friendly web interface for entering input data
Sidebar with descriptions of required input fields
Real-time prediction of the average price based on user inputs
Visualization enhancements like background images and celebratory balloons for successful predictions

Getting Started
Prerequisites
Python 3.7 or higher
Streamlit
Pandas
NumPy
scikit-learn
Installation
Clone the repository:

git clone https://github.com/your-username/potato-sifra-price-prediction.git
cd potato-sifra-price-prediction
Install the required packages:
pip install -r requirements.txt
Running the App
Place the pre-trained model file (potato_sifra__model.pkl) in the project directory.

Run the Streamlit app:
streamlit run app.py
Open your web browser and go to the URL provided by Streamlit (usually http://localhost:8501).
Usage
Select input values:

Province: Choose the province from which the POTATO SIFRA (WASHED) is produced.
Size Grade: Select the size grade of the POTATO SIFRA (WASHED) packages.
Weight per kilo (kg): Enter the weight of the POTATO SIFRA (WASHED) in kilograms.
Low Price (R): Enter the lowest market price for the POTATO SIFRA (WASHED).
Total Sale (R): Enter the total sales value for the POTATO SIFRA (WASHED).
Stock on Hand: Enter the current stock available in the warehouse.
Month: Select the month for which the prediction is to be made.
Day: Select the day for which the prediction is to be made.
Click the "🔮 Predict" button to get the predicted average price.

Files in the Repository
app.py: The main Streamlit application file.
requirements.txt: List of required Python packages.
potato_sifra__model.pkl: The pre-trained machine learning model (not included; to be added separately).
README.md: This file, providing an overview of the project.

Model Details
The model used in this application is a machine learning model trained to predict the average price of POTATO SIFRA (WASHED) based on historical data. The model was trained using scikit-learn and saved as a pickle file (potato_sifra__model.pkl).

Deployment
To deploy this application, you can use platforms like Heroku, AWS, or any other hosting services that support Python applications. Make sure to set up the environment and dependencies as mentioned in the requirements.txt.

Contributing
Contributions are welcome! Please open an issue or create a pull request for any enhancements or bug fixes.
