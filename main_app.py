import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import os

# Set page configuration
st.set_page_config(page_title="Plant Classification App", page_icon="🌿", layout="wide")

# Load the model using caching
@st.cache_resource
def load_model_mobilenet():
    try:
        return load_model(r"C:\Users\shara\OneDrive\Desktop\Stream_Plant\Plant+leafnew.h5")
    except Exception as e:
        st.error(f"Error loading MobileNet Model: {e}")
        return None

model = load_model_mobilenet()

# Function to classify the image
def classify_image(image, model):
    try:
        img = image.convert('RGB')
        img = img.resize((224, 224))  # MobileNet input size
        img_array = img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        predictions = model.predict(img_array)
        confidence = np.max(predictions)
        class_index = np.argmax(predictions)

        labels = {0: 'Aloevera', 1: 'Lemon', 2: 'Mango', 3: 'Neem', 4: 'Tulsi', 5: 'Turmeric'}
        predicted_label = labels.get(class_index, "Unknown Plant")

        return predicted_label, confidence
    except Exception as e:
        st.error(f"Error classifying the image: {e}")
        return None, None

# Add title and header
st.title("🌿 Medicinal Plant Classification App 🌿")
st.header("Identify medicinal plants by uploading an image or taking a photo")

# Upload or capture image
image = None
option = st.radio("Choose input method:", ("Upload Image", "Take a Photo"))
if option == "Upload Image":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image = Image.open(uploaded_file)
elif option == "Take a Photo":
    camera_photo = st.camera_input("Take a photo")
    if camera_photo:
        image = Image.open(camera_photo)

# Initialize session state if not already done
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

# Display image and predictions
if image:
    st.image(image, caption="Uploaded Image", width=200)
    predicted_label, confidence = classify_image(image, model)

    if confidence and confidence > 0.6:
        st.success(f"Plant: **{predicted_label}** ")

        # Button to learn more
        if st.button("Learn More"):
            st.session_state.plant = predicted_label  # Store plant name in session state
            st.session_state.current_page = 'details'  # Set the current page to details
    else:
        st.error("This plant is not recognized as a medicinal plant.")

# Navigation logic based on session state
if st.session_state.current_page == 'details':
    st.session_state.current_page = 'details'

# Page routing
if st.session_state.current_page == 'home':
    # Render home page content
    st.write("### Identify medicinal plants by uploading an image or taking a photo.")
elif st.session_state.current_page == 'details':
    # Render details page content
    plant_name = st.session_state.get('plant', None)

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

    # Define detailed information for each plant
    detailed_plant_details = {
    "Neem": {
        "Scientific Name": "Azadirachta indica",
        "Description": "Neem is a fast-growing tree native to the Indian subcontinent and other tropical and subtropical regions. Known for its wide range of medicinal properties, it is often referred to as the 'pharmacy of the village'. Neem has a long history of use in Ayurvedic medicine and is cherished for its ability to promote health and wellness.",
        "Benefits": "Rich in antioxidants, neem possesses anti-inflammatory properties that can aid in skin health. It helps to combat infections and has been known to lower blood sugar levels.",
        "Uses": "Neem is widely used in skincare products, dental care, and as a natural pesticide in agriculture. Its oil is also incorporated into various health products due to its antifungal and antibacterial effects.",
        "Culinary Uses": "The young leaves can be used in salads and are known for their slightly bitter flavor. Neem oil is sometimes used in cooking, though it is more commonly applied in therapeutic contexts.",
        "Medicinal Properties": "Neem is effective against a variety of infections, assists in blood purification, and is traditionally used for treating fevers and skin conditions. It is also noted for its potential to improve liver health.",
        "Precautions": "Neem is generally safe but may cause allergic reactions in some individuals. It is not recommended for pregnant or breastfeeding women due to its strong effects."
    },
    "Aloevera": {
        "Scientific Name": "Aloe barbadensis miller",
        "Description": "Aloe vera is a succulent plant species cultivated for its leaves, which contain a soothing gel-like substance. This plant thrives in arid climates and is widely known for its health benefits and skincare properties.",
        "Benefits": "Aloe vera is renowned for its ability to hydrate the skin, facilitate wound healing, and provide anti-inflammatory benefits. Its gel is often applied topically to treat burns and skin irritations.",
        "Uses": "Aloe vera is commonly used in cosmetics, skincare products, and dietary supplements. It is valued for its soothing properties and is frequently included in sunburn relief products.",
        "Culinary Uses": "Aloe vera juice is consumed for its health benefits, particularly for digestion and hydration. It is sometimes added to smoothies and health drinks.",
        "Medicinal Properties": "The plant aids in digestion and may help in reducing blood sugar levels, making it popular among those managing diabetes. It is also known for its antioxidant properties.",
        "Precautions": "Some individuals may experience gastrointestinal issues when consuming aloe vera. It is advisable to consult a healthcare professional before use, especially for those with pre-existing health conditions."
    },
    "Mint": {
        "Scientific Name": "Mentha",
        "Description": "Mint is a fragrant herb characterized by its fresh aroma and cooling flavor. This versatile herb thrives in various climates and is easily recognizable by its distinct smell.",
        "Benefits": "Mint is known to promote digestion, relieve headaches, and act as a natural decongestant. Its aroma is often used in aromatherapy for stress relief.",
        "Uses": "Mint is used in cooking, herbal teas, and as a flavoring agent in numerous recipes, enhancing both sweet and savory dishes.",
        "Culinary Uses": "It is commonly used in salads, beverages (like mojitos), and desserts (such as mint chocolate). The leaves can also be infused into syrups and sauces for added flavor.",
        "Medicinal Properties": "Mint has been shown to alleviate digestive issues, improve oral health, and may also provide relief from symptoms of nausea and respiratory conditions.",
        "Precautions": "Excessive consumption of mint may lead to heartburn or digestive discomfort in some individuals. It is advisable to consume it in moderation."
    },
    "Turmeric": {
        "Scientific Name": "Curcuma longa",
        "Description": "Turmeric is a flowering plant in the ginger family, notable for its rhizome, which is commonly used as a spice and medicinal herb. Known for its vibrant yellow color, it has a rich history in both culinary and medicinal applications.",
        "Benefits": "Turmeric is celebrated for its anti-inflammatory and antioxidant properties. Curcumin, the active compound in turmeric, has been extensively studied for its health benefits.",
        "Uses": "It is widely used as a spice in cooking and is also a key ingredient in traditional medicine practices, particularly in Ayurveda.",
        "Culinary Uses": "Turmeric is a staple in curries, soups, and rice dishes, imparting a warm, earthy flavor and bright yellow color. It is also used as a natural coloring agent in various foods.",
        "Medicinal Properties": "Turmeric supports joint health, boosts the immune system, and may reduce the risk of chronic diseases. Its anti-inflammatory properties make it beneficial for conditions like arthritis.",
        "Precautions": "Turmeric may interact with blood-thinning medications and should be used cautiously by individuals with certain health conditions. Consulting a healthcare provider is advisable."
    },
    "Mango": {
        "Scientific Name": "Mangifera indica",
        "Description": "Mango is a tropical stone fruit, known as the 'king of fruits'. It is celebrated for its sweet flavor and juicy texture, making it a popular choice around the world.",
        "Benefits": "Mango is rich in vitamins A, C, and E, and antioxidants, which contribute to overall health. It supports eye health, skin health, and boosts the immune system.",
        "Uses": "The fruit is enjoyed fresh, in smoothies, salads, or desserts, and is often used in various culinary dishes.",
        "Culinary Uses": "Mangoes are commonly used in chutneys, jams, and juices, enhancing both flavor and nutritional value. The fruit can also be used in savory dishes.",
        "Medicinal Properties": "Mango supports digestion, promotes skin health, and is known for its potential to boost immunity due to its high vitamin content.",
        "Precautions": "Due to its high sugar content, individuals with diabetes should consume mango in moderation. It is also advisable to be cautious with mango skin, as some people may have allergic reactions."
    },
    "Tulsi": {
        "Scientific Name": "Ocimum sanctum",
        "Description": "Tulsi, or Holy Basil, is revered in Indian culture for its healing properties. Often referred to as the 'Queen of Herbs', it is considered sacred and is frequently found in homes and temples.",
        "Benefits": "Tulsi is known for its antioxidant, anti-inflammatory, and antibacterial effects. It is believed to promote overall health and well-being.",
        "Uses": "The leaves are used in teas, supplements, and traditional medicine. Tulsi is often consumed to enhance immunity and manage stress.",
        "Culinary Uses": "Tulsi leaves can be added to cooking, particularly in Indian dishes, where they impart a unique flavor and aroma.",
        "Medicinal Properties": "Tulsi helps reduce stress, improves digestion, and boosts immunity. It is also used for respiratory issues and promoting mental clarity.",
        "Precautions": "While generally safe, Tulsi may interact with certain medications, especially those for diabetes or blood thinning. Consultation with a healthcare provider is recommended before use."
    }
    
}



    # Render details page content
    plant_name = st.session_state.get('plant', None)

    # Display the details of the identified plant
    if plant_name in detailed_plant_details:
        st.header(f"Details of {plant_name}")

        # Display each detail in an expander
        for detail, description in detailed_plant_details[plant_name].items():
            with st.expander(detail, expanded=False):
                st.write(description)

        # Display images of the plant
        image_folder = os.path.join("plant_images", plant_name)
        image_files = os.listdir(image_folder)

        st.subheader("Similar Images")
        if image_files:
            cols = st.columns(3)
            for i, file in enumerate(image_files[:3]):  # Show up to 3 images
                with cols[i % 3]:
                    img_path = os.path.join(image_folder, file)
                    st.image(img_path, caption=file)
    else:
        st.error("Details not available for this plant.")

# Footer
st.write("<footer style='text-align: center; color: gray;'>Made with ❤️ by Your Name</footer>", unsafe_allow_html=True)
