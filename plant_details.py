import streamlit as st

# Check if the plant name is stored in session state
if 'plant' in st.session_state:
    plant_name = st.session_state['plant']
    
    # Define benefits for each plant
    plant_details = {
        "Aloevera": {
            "Benefits": "Aloe Vera is known for its skin-healing properties. It's often used to soothe burns and skin irritations.",
            "Uses": "Commonly used in cosmetics and skin care products."
        },
        "Lemon": {
            "Benefits": "Lemons are rich in Vitamin C and have antioxidant properties. They aid digestion and can help in weight loss.",
            "Uses": "Used in drinks, desserts, and as a natural disinfectant."
        },
        "Mango": {
            "Benefits": "Mangoes are a good source of vitamins A and C. They improve immunity and are great for skin health.",
            "Uses": "Eaten fresh, in smoothies, or desserts."
        },
        "Neem": {
            "Benefits": "Neem leaves have antibacterial and antifungal properties. They are often used in traditional medicine for skin problems.",
            "Uses": "Used in herbal medicines and cosmetics."
        },
        "Tulsi": {
            "Benefits": "Tulsi, or holy basil, is known for its adaptogenic properties. It helps the body cope with stress and boosts immunity.",
            "Uses": "Used in teas and herbal supplements."
        },
        "Turmeric": {
            "Benefits": "Turmeric contains curcumin, which has anti-inflammatory and antioxidant properties. It's commonly used in traditional remedies.",
            "Uses": "Used in cooking and supplements."
        }
    }

    # Display the details of the identified plant
    if plant_name in plant_details:
        st.header(f"Details of {plant_name}")
        st.subheader("Benefits")
        st.write(plant_details[plant_name]["Benefits"])
        st.subheader("Uses")
        st.write(plant_details[plant_name]["Uses"])
    else:
        st.write("No information available for this plant.")
else:
    st.write("No plant selected. Please go back to the main page and identify a plant.")

st.write("---")
st.markdown("<p style='text-align: center;'>🌱 Powered by Deep Learning 🌱</p>", unsafe_allow_html=True)
