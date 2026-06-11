## 👔 Outfit Compatibility Scorer

Problem Statement:

Choosing a well-matched outfit is often subjective and depends on factors such as color harmony, occasion, season, and clothing combinations. Most fashion recommendation systems rely on image-based deep learning models, which can be complex and difficult to interpret.

This project aims to build an explainable Machine Learning system that evaluates the compatibility of outfit combinations and predicts a compatibility score between 0 and 100.
The system learns fashion patterns from clothing metadata and provides a compatibility assessment for a given outfit combination.

Dataset:

The project uses the Fashion Product Dataset containing over 44,000 fashion products.

Key Attributes Used :-
Article Type
Base Colour
Usage
Season
Gender
Examples
Attribute	Examples
Article Type	Tshirts, Shirts, Jeans, Trousers, Casual Shoes
Colour	Black, White, Blue, Grey, Brown
Usage	Casual, Formal, Sports, Ethnic
Season	Summer, Winter, Fall, Spring

After filtering irrelevant categories, only outfit-related items were retained:

Tops
Tshirts
Shirts
Kurtas
Tops
Sweatshirts
Jackets
Sweaters
Bottoms
Jeans
Trousers
Shorts
Track Pants
Leggings
Skirts
Footwear
Casual Shoes
Formal Shoes
Sports Shoes
Sandals
Heels
Flats
Feature Engineering

To train a machine learning model, outfit combinations were generated using:

Top Item
Bottom Item
Footwear Item

Each outfit contained:

Feature
top_type
top_color
top_usage
top_season
bottom_type
bottom_color
bottom_usage
bottom_season
shoe_type
shoe_color
shoe_usage
shoe_season
Encoding

Categorical variables were converted into numerical values using Label Encoding.

Example:

Original	Encoded
Casual	0
Formal	1
Sports	2

The trained encoders were saved using Joblib and reused during deployment.

Scoring Logic:

Since the original dataset did not contain outfit compatibility labels, a rule-based scoring engine was designed to generate training targets.

The compatibility score was calculated using fashion principles.

1. Occasion Matching

Outfits received higher scores when all items belonged to the same usage category.

Example:

Casual + Casual + Casual
Formal + Formal + Formal
Sports + Sports + Sports

2. Seasonal Consistency

Additional points were awarded when all outfit components belonged to the same season.

Example:

Summer Top + Summer Bottom + Summer Shoes

3. Color Harmony

Neutral color combinations received higher scores.

Examples:

Black + White
Navy Blue + Grey
White + Beige

Custom color compatibility rules were also incorporated.

4. Fashion Category Rules

Examples:

Formal Outfit
Shirt
Trouser
Formal Shoes
Casual Outfit
Tshirt
Jeans
Casual Shoes
Sports Outfit
Tshirt
Track Pants
Sports Shoes

These rules generated compatibility scores ranging from 0 to 100.

Model Training
Models Evaluated
Linear Regression

Used as a baseline model.

Random Forest Regressor

Selected as the final model due to its ability to:

Capture non-linear relationships
Handle categorical feature interactions
Reduce overfitting through ensemble learning
Provide feature importance analysis
Train-Test Split
Training Data: 80%
Testing Data: 20%
Model Comparison
Model	MAE	RMSE	R² Score
Linear Regression	10.48	13.23	0.36
Random Forest	5.26	6.88	0.83
Observation

Random Forest significantly outperformed Linear Regression, indicating that outfit compatibility depends on complex non-linear relationships between fashion attributes.

Therefore, Random Forest was selected as the final production model.

Results
Final Model Performance
Metric	Value
MAE	5.26
RMSE	6.88
R² Score	0.83
Most Important Features
Shoe Usage
Top Color
Bottom Usage
Top Usage
Bottom Color

These results indicate that occasion matching and color coordination have the strongest influence on outfit compatibility.

Streamlit Application: 

The trained model was deployed using Streamlit.

Users can:

Select Top, Bottom, and Footwear attributes
Predict Outfit Compatibility Score
View Compatibility Category
Understand reasons behind the prediction
Compatibility Categories
Score Range	Category
80+	Highly Compatible
60–79	Moderately Compatible
Below 60	Poor Match
Future Improvements
Incorporate outfit images using Computer Vision
Use Deep Learning for visual compatibility analysis
Build personalized recommendations based on user preferences
Add real-time outfit suggestions
Deploy on Streamlit Cloud
Tech Stack
Python
Pandas
NumPy
Scikit-learn
Matplotlib
Joblib
Streamlit
Project Outcome

Built an end-to-end Machine Learning solution that combines fashion domain knowledge with predictive modeling to evaluate outfit compatibility and provide explainable recommendations through an interactive web application.