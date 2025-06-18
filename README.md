# IPL Match Prediction App

A machine learning-based web application that predicts the outcome of Indian Premier League (IPL) cricket matches using historical data.

## Features

- **Match Outcome Prediction**: Predicts the winner of IPL matches based on historical data
- **Interactive Web Interface**: Built with Streamlit for easy user interaction
- **Machine Learning Model**: Uses scikit-learn pipeline with Logistic Regression
- **Historical Data Analysis**: Based on comprehensive IPL match and delivery data
- **AI-Powered Explanations**: Uses Google's Gemini AI to explain predictions

## Project Structure

```
IPL-pred/
├── app.py              # Main Streamlit application
├── Model.ipynb         # Jupyter notebook with model development
├── pipe.pkl            # Trained machine learning pipeline
├── players.pkl         # Player data
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd IPL-pred
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. **Important**: You'll need to obtain the following data files to run the application:
   - `matches.csv` - Historical IPL match data
   - `deliveries.csv` - Ball-by-ball delivery data
   
   These files are not included in the repository due to size constraints. You can find IPL datasets on platforms like Kaggle or official IPL data sources.

## API Key Setup

### For Local Development:
1. Create a `.streamlit/secrets.toml` file in your project directory:
```toml
GOOGLE_API_KEY = "your_google_api_key_here"
```

### For Streamlit Cloud Deployment:
1. Go to your app on [Streamlit Cloud](https://share.streamlit.io/)
2. Navigate to Settings → Secrets
3. Add your Google API key:
```toml
GOOGLE_API_KEY = "your_google_api_key_here"
```

**Note**: The API key is required for AI-powered explanations. The app will work without it, but explanations will be disabled.

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser and navigate to `http://localhost:8501`

3. Use the interactive interface to:
   - Select teams
   - Choose venue
   - Set match parameters
   - Get match predictions with AI explanations

## Dependencies

- streamlit
- pandas
- numpy
- scikit-learn
- google-generativeai

## Model Information

The prediction model uses:
- **Algorithm**: Logistic Regression
- **Features**: Team performance, venue statistics, historical head-to-head records
- **Data**: IPL match data from multiple seasons
- **Pipeline**: Scikit-learn pipeline with preprocessing and feature engineering
- **AI Integration**: Google Gemini for explaining predictions

## Data Sources

- IPL match data (matches.csv) - **Not included in repository**
- Ball-by-ball delivery data (deliveries.csv) - **Not included in repository**
- Player statistics (players.pkl)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- IPL for providing the match data
- Streamlit for the web framework
- Scikit-learn for machine learning tools
- Google Gemini for AI explanations 