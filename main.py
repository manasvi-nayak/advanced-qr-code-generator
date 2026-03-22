import streamlit as st
from utils import generate_qr, wifi_qr, contact_qr
from io import BytesIO

st.set_page_config(page_title="QR Generator", page_icon="📱")

st.title("📱 Advanced QR Code Generator")
st.write("Generate QR codes for URLs, WiFi, and Contacts 🚀")

# Select QR type
qr_type = st.selectbox("Choose QR Type", ["URL/Text", "WiFi", "Contact"])


img = None

# 🔹 URL / TEXT
if qr_type == "URL/Text":
    data = st.text_input("Enter text or URL")

    if st.button("Generate QR"):
        if data:
            img = generate_qr(data)
        else:
            st.warning("Enter something!")

# 🔹 WiFi QR
elif qr_type == "WiFi":
    ssid = st.text_input("WiFi Name (SSID)")
    password = st.text_input("Password")

    if st.button("Generate WiFi QR"):
        if ssid and password:
            img = wifi_qr(ssid, password)
        else:
            st.warning("Enter WiFi details!")

# 🔹 Contact QR
elif qr_type == "Contact":
    name = st.text_input("Name")
    phone = st.text_input("Phone")
    email = st.text_input("Email")

    if st.button("Generate Contact QR"):
        if name and phone:
            img = contact_qr(name, phone, email)
        else:
            st.warning("Fill required fields!")


# 📷 Show + Download
if img is not None:
    st.subheader("✅ Your QR Code")
    st.image(img, width=250)

    buffer = BytesIO()
    img.save(buffer, format="PNG")

    st.download_button(
        label="⬇️ Download QR Code",
        data=buffer.getvalue(),
        file_name="qr_code.png",
        mime="image/png"
    )