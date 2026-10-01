from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


PROJECT_DIR = Path(__file__).resolve().parent
MODEL_PATH = PROJECT_DIR / "logistics_regression.pkl"

st.set_page_config(
    page_title="Airline Satisfaction Predictor",
    page_icon="✈️",
    layout="wide",
)
st.markdown(
    """
    <style>
    .block-container {max-width: 1200px; padding-top: 2rem;}
    .prediction-card {
        padding: 1.25rem 1.5rem; border-radius: 0.75rem;
        background: linear-gradient(135deg, #e8f4ff, #f5fbff);
        border: 1px solid #b9ddf5;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


def rating(label: str, key: str, default: int = 3) -> int:
    return st.slider(label, min_value=1, max_value=5, value=default, key=key)


st.title("✈️ Airline Passenger Satisfaction")
st.write(
    "Enter a passenger's journey details to estimate whether they will be satisfied "
    "with the airline experience."
)

try:
    model = load_model()
except FileNotFoundError:
    st.error(f"Model file not found: {MODEL_PATH.name}")
    st.stop()
except (ImportError, ModuleNotFoundError, ValueError) as exc:
    st.error("The saved model could not be loaded. Install the dependencies in requirements.txt.")
    st.exception(exc)
    st.stop()

with st.form("prediction_form"):
    st.subheader("Passenger and trip details")
    passenger_col, trip_col = st.columns(2)
    with passenger_col:
        gender = st.selectbox("Gender", ["Male", "Female"])
        customer_type = st.selectbox(
            "Customer type", ["Loyal Customer", "disloyal Customer"]
        )
        age = st.number_input("Age", min_value=1, max_value=100, value=35, step=1)
    with trip_col:
        travel_type = st.selectbox(
            "Type of travel", ["Business travel", "Personal Travel"]
        )
        travel_class = st.selectbox("Class", ["Business", "Eco Plus", "Eco"])
        flight_distance = st.number_input(
            "Flight distance (miles)", min_value=1, max_value=10000, value=1000, step=10
        )

    st.subheader("Service ratings")
    rating_col1, rating_col2, rating_col3 = st.columns(3)
    with rating_col1:
        wifi = rating("Inflight wifi service", "wifi")
        departure_time = rating("Departure/arrival time convenient", "departure_time")
        online_booking = rating("Ease of online booking", "online_booking")
        gate_location = rating("Gate location", "gate_location")
        food = rating("Food and drink", "food")
        online_boarding = rating("Online boarding", "online_boarding")
        seat_comfort = rating("Seat comfort", "seat_comfort")
    with rating_col2:
        entertainment = rating("Inflight entertainment", "entertainment")
        onboard_service = rating("On-board service", "onboard_service")
        leg_room = rating("Leg room service", "leg_room")
        baggage = rating("Baggage handling", "baggage")
        checkin = rating("Checkin service", "checkin")
        cleanliness = rating("Cleanliness", "cleanliness")
    with rating_col3:
        departure_delay = st.number_input(
            "Departure delay (minutes)", min_value=0, max_value=2000, value=0, step=1
        )
        arrival_delay = st.number_input(
            "Arrival delay (minutes)", min_value=0, max_value=2000, value=0, step=1
        )
        st.caption("Use 1 (very poor) to 5 (excellent) for service ratings.")

    submitted = st.form_submit_button("Predict satisfaction", type="primary")

if submitted:
    features = pd.DataFrame(
        [
            {
                "Gender": {"Male": 1, "Female": 0}[gender],
                "Customer Type": {"Loyal Customer": 1, "disloyal Customer": 0}[customer_type],
                "Age": age,
                "Type of Travel": {"Business travel": 1, "Personal Travel": 0}[travel_type],
                "Class": {"Business": 1, "Eco Plus": 2, "Eco": 3}[travel_class],
                "Flight Distance": flight_distance,
                "Inflight wifi service": wifi,
                "Departure/Arrival time convenient": departure_time,
                "Ease of Online booking": online_booking,
                "Gate location": gate_location,
                "Food and drink": food,
                "Online boarding": online_boarding,
                "Seat comfort": seat_comfort,
                "Inflight entertainment": entertainment,
                "On-board service": onboard_service,
                "Leg room service": leg_room,
                "Baggage handling": baggage,
                "Checkin service": checkin,
                "Cleanliness": cleanliness,
                "Departure Delay in Minutes": departure_delay,
                "Arrival Delay in Minutes": arrival_delay,
            }
        ]
    )

    prediction = model.predict(features)[0]
    satisfied = bool(prediction)
    probability = None
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(features)[0]
        classes = list(model.classes_)
        if satisfied in classes:
            probability = float(probabilities[classes.index(satisfied)])

    st.divider()
    result_col, detail_col = st.columns([1, 2])
    with result_col:
        if satisfied:
            st.success("Likely satisfied")
        else:
            st.warning("Likely neutral or dissatisfied")
    with detail_col:
        if probability is not None:
            st.metric("Model confidence", f"{probability:.1%}")
        st.caption("This estimate is generated from the trained logistic regression model.")

