import qrcode

def generate_qr(data):
    img = qrcode.make(data)
    return img.convert("RGB")   # ✅ IMPORTANT FIX

# 🔹 WiFi QR Generator
def wifi_qr(ssid, password):
    data = f"WIFI:T:WPA;S:{ssid};P:{password};;"
    return generate_qr(data)


# 🔹 Contact QR Generator (vCard)
def contact_qr(name, phone, email):
    data = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
END:VCARD"""
    return generate_qr(data)