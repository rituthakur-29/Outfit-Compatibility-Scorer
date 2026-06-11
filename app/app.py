
# Imports
import streamlit as st
import pandas as pd
import joblib

# Load the model and encoders
model = joblib.load('models/random_forest.pkl')
encoders = joblib.load('models/encoders.pkl')

# Page title
st.title("👔 Outfit Compatibility Scorer")

st.write(
    "Predict compatibility score for a fashion outfit combination."
)


# Create dropdowns for user input
top_type = st.selectbox(
    "Top Type",
    encoders['top_type'].classes_
)

top_color = st.selectbox(
    "Top Color",
    encoders['top_color'].classes_
)

top_usage = st.selectbox(
    "Top Usage",
    encoders['top_usage'].classes_
)

top_season = st.selectbox(
    "Top Season",
    encoders['top_season'].classes_
)

# Bottoms section 
bottom_type = st.selectbox(
    "Bottom Type",
    encoders['bottom_type'].classes_
)

bottom_color = st.selectbox(
    "Bottom Color",
    encoders['bottom_color'].classes_
)

bottom_usage = st.selectbox(
    "Bottom Usage",
    encoders['bottom_usage'].classes_
)

bottom_season = st.selectbox(
    "Bottom Season",
    encoders['bottom_season'].classes_
)

# Shoe section
shoe_type = st.selectbox(
    "Shoe Type",
    encoders['shoe_type'].classes_
)

shoe_color = st.selectbox(
    "Shoe Color",
    encoders['shoe_color'].classes_
)

shoe_usage = st.selectbox(
    "Shoe Usage",
    encoders['shoe_usage'].classes_
)

shoe_season = st.selectbox(
    "Shoe Season",
    encoders['shoe_season'].classes_
)

# Predict button
if st.button("Predict Compatibility"):
    input_data = pd.DataFrame({
    'top_type': [
        encoders['top_type'].transform(
            [top_type]
        )[0]
    ],

    'top_color': [
        encoders['top_color'].transform(
            [top_color]
        )[0]
    ],

    'top_usage': [
        encoders['top_usage'].transform(
            [top_usage]
        )[0]
    ],

    'top_season': [
        encoders['top_season'].transform(
            [top_season]
        )[0]
    ],

    'bottom_type': [
        encoders['bottom_type'].transform(
            [bottom_type]
        )[0]
    ],

    'bottom_color': [
        encoders['bottom_color'].transform(
            [bottom_color]
        )[0]
    ],

    'bottom_usage': [
        encoders['bottom_usage'].transform(
            [bottom_usage]
        )[0]
    ],

    'bottom_season': [
        encoders['bottom_season'].transform(
            [bottom_season]
        )[0]
    ],

    'shoe_type': [
        encoders['shoe_type'].transform(
            [shoe_type]
        )[0]
    ],

    'shoe_color': [
        encoders['shoe_color'].transform(
            [shoe_color]
        )[0]
    ],

    'shoe_usage': [
        encoders['shoe_usage'].transform(
            [shoe_usage]
        )[0]
    ],

    'shoe_season': [
        encoders['shoe_season'].transform(
            [shoe_season]
        )[0]
    ]
})
    

    prediction = model.predict(input_data)[0]

    st.subheader(
        f'Compatibility Score: {prediction:.0f}/100'
        )

    if prediction >= 80:
        label = "Highly Compatible"
        st.success(label)
        st.balloons()

    elif prediction >= 60:
        label = "Moderately Compatible"
        st.warning(label)

    else:
        label = "Poor Match"
        st.error(label)
    
    st.progress(
        min(int(prediction), 100)
    )

    reason = []

    if top_usage == bottom_usage == shoe_usage:
        reason.append(
            "All items match the same occasion."
        )

    if top_season == bottom_season == shoe_season:
        reason.append(
            "All items belong to the same season."
        )

    if top_color == bottom_color:
        reason.append(
            "Top and bottom colors complement each other."
        )

    st.subheader("Why this score?")

    for r in reason:
        st.write("✅", r)

    # Display results
    st.write(
    f"Category: {label}"
    )



    