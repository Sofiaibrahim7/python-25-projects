import streamlit as st
import qrcode
from PIL import Image
import io

st.title("QR Code Generator")

data = st.text_input("Enter text or URL to generate QR Code")

if st.button("Generate QR Code") and data:
    # Create QR Code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Convert to bytes for Streamlit
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    st.image(buf.getvalue(), caption="Your QR Code", use_container_width=True)

    # Optional download button
    st.download_button("Download QR Code", data=buf.getvalue(), file_name="qrcode.png", mime="image/png")
