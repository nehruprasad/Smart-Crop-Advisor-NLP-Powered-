# Smart-Crop-Advisor-NLP-Powered-
# Smart Crop Advisor 🌱

A **Streamlit-based Python application** that uses NLP to analyze farm conditions and provide **crop recommendations, yield predictions, and risk analysis** for farmers.

---

## **Features**

1. **Describe Farm Conditions**  
   - Enter natural language descriptions of soil, climate, water availability, and previous crops.

2. **Crop Recommendations**  
   - Suggests suitable crops based on the farm conditions.

3. **Yield Predictions**  
   - Estimates potential crop yield (tons/acre) using simple rule-based calculations.

4. **Risk Analysis**  
   - Highlights environmental or climate risks such as water scarcity or climate mismatch.

---

## **Requirements**

- Python 3.8+  
- Streamlit  
- pandas  
- NLTK  
- spaCy  

---

## **Setup Instructions**

1. **Clone the repository**:

```bash
git clone <repository-url>
cd smart_crop_advisor
Create a virtual environment (recommended):

bash
Copy code
python -m venv venv
Activate the virtual environment:

Windows

bash
Copy code
venv\Scripts\activate
Linux / Mac

bash
Copy code
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install streamlit pandas nltk spacy
Download NLTK punkt tokenizer:

python
Copy code
import nltk
nltk.download('punkt')
Download spaCy English model:

bash
Copy code
python -m spacy download en_core_web_sm
Running the App
Ensure your virtual environment is active.

Run Streamlit:

bash
Copy code
streamlit run app.py
Open the URL displayed in the terminal (usually http://localhost:8501).

Enter a description of your farm conditions and click "Get Crop Recommendations".

Sample Input
csharp
Copy code
My farm has loamy soil with moderate water availability. 
The climate is temperate and the previous crop was maize. 
I have good irrigation facilities but occasional dry spells.
Expected Output
Detected Farm Conditions

Soil: loamy

Climate: temperate

Water: moderate

Recommended Crops

wheat, maize, soybean

Yield Predictions

wheat: 3.0 tons/acre

maize: 4.0 tons/acre

soybean: 2.5 tons/acre

Risk Analysis

wheat: Low risk

maize: Low risk

soybean: Low risk

