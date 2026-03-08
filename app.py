import streamlit as st
import pandas as pd

from agents.itinerary_agent import ItineraryBuilderAgent
from agents.cost_agent import CostEstimatorAgent
from agents.culture_agent import LocalCultureCoachAgent
from memory.trip_db import save_trip, get_all_trips

st.set_page_config(page_title="Travel Planning Assistant", layout="wide")

itinerary_agent = ItineraryBuilderAgent()
cost_agent = CostEstimatorAgent()
culture_agent = LocalCultureCoachAgent()

st.title("Travel Planning Assistant")
st.subheader("Multi-Agent Trip Planner")

menu = st.sidebar.selectbox(
    "Choose Option",
    ["Plan a Trip", "Trip Memory", "About"]
)

if menu == "Plan a Trip":
    st.header("Enter Trip Details")

    destination = st.text_input("Destination", "Tokyo")
    budget = st.selectbox("Budget", ["Low", "Medium", "High"])
    interests = st.text_area("Interests", "food, culture, photography, temples")
    days = st.slider("Number of Days", 1, 10, 5)
    notes = st.text_area("Extra Notes", "Prefer walkable areas and local food markets")

    if st.button("Generate Travel Plan"):
        with st.spinner("Building itinerary..."):
            itinerary = itinerary_agent.run(destination, budget, interests, days)

        if itinerary.startswith("ERROR:"):
            st.error(itinerary)
        else:
            with st.spinner("Estimating costs..."):
                cost = cost_agent.run(destination, budget, itinerary)

            if cost.startswith("ERROR:"):
                st.error(cost)
                st.subheader("Itinerary")
                st.write(itinerary)
            else:
                with st.spinner("Collecting local culture advice..."):
                    culture = culture_agent.run(destination, interests)

                if culture.startswith("ERROR:"):
                    st.error(culture)
                    st.subheader("Itinerary")
                    st.write(itinerary)
                    st.subheader("Cost Estimate")
                    st.write(cost)
                else:
                    save_trip(destination, budget, interests, days, itinerary, cost, culture, notes)

                    st.success("Trip plan generated and saved.")

                    st.subheader("Daily Itinerary")
                    st.write(itinerary)

                    st.subheader("Estimated Cost")
                    st.write(cost)

                    st.subheader("Local Culture Coach")
                    st.write(culture)

elif menu == "Trip Memory":
    st.header("Saved Trips")

    trips = get_all_trips()

    if trips:
        df = pd.DataFrame(trips)
        st.dataframe(df[["timestamp", "destination", "budget", "days"]], use_container_width=True)

        selected_index = st.number_input(
            "Select trip index",
            min_value=0,
            max_value=len(trips) - 1,
            step=1
        )

        trip = trips[selected_index]

        st.subheader(f"Destination: {trip['destination']}")
        st.write(f"Saved on: {trip['timestamp']}")
        st.write(f"Budget: {trip['budget']}")
        st.write(f"Interests: {trip['interests']}")
        st.write(f"Extra Notes: {trip['notes']}")

        st.markdown("### Daily Timeline")
        st.write(trip["itinerary"])

        st.markdown("### Cost Estimate")
        st.write(trip["cost"])

        st.markdown("### Local Culture Advice")
        st.write(trip["culture"])
    else:
        st.info("No saved trips found yet.")

else:
    st.header("How It Works")
    st.markdown("""
1. User enters destination, budget, interests, and notes  
2. Itinerary Builder creates a daily travel plan  
3. Cost Estimator checks estimated spending  
4. Local Culture Coach provides practical travel advice  
5. Trip data is stored in memory for future reference  
""")