import streamlit as st
from PIL import Image, ImageEnhance
from rembg import remove
import io

st.set_page_config(page_title="Photo Manipulation App", layout="centered")

st.title("🖼️ Photo Manipulation App")
st.markdown("Upload an image, remove background, and adjust brightness with ease!")

# Upload image
uploaded_file = st.file_uploader("📤 Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)

    # Show original image
    st.image(image, caption="Original Image", use_container_width=True)

    # Background removal
    if st.button("🧼 Remove Background"):
        with st.spinner("Removing background..."):
            result = remove(image)
            st.image(result, caption="Background Removed", use_container_width=True)

            # Brightness Adjustment
            brightness = st.slider("🔆 Adjust Brightness", 0.1, 2.0, 1.0, 0.1)
            enhancer = ImageEnhance.Brightness(result)
            bright_image = enhancer.enhance(brightness)
            st.image(bright_image, caption="Final Image", use_container_width=True)

            # Save locally
            bright_image.save("final_output.png")
            st.success("✅ Image saved locally as final_output.png")

            
            
            # Download Button
            img_byte_arr = io.BytesIO()
            bright_image.save(img_byte_arr, format="PNG")
            st.download_button("📥 Download Final Image", img_byte_arr.getvalue(), file_name="edited_image.png")
else:
    st.info("Please upload an image to begin.")
 