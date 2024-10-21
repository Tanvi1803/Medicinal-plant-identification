# Benefits Page Function
def benefits_page():
    st.markdown("<h1 style='text-align: center;'>🌿 Plant Benefits 🌿</h1>", unsafe_allow_html=True)

    # Retrieve the predicted label and benefits from session state
    predicted_label = st.session_state.get('predicted_label', 'Unknown')
    plant_benefit = st.session_state.get('plant_benefit', 'No information available.')

    # Display plant name and benefits
    st.subheader(f"Plant: {predicted_label}")
    st.write(f"**Benefits:** {plant_benefit}")

    # Add a button to navigate back to the home page
    if st.button("Back to Home"):
        st.session_state.page = "home"
