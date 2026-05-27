from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():

    payment_link = "upi://pay?pa=6361004454@upi&pn=YellowRedServices&cu=INR"

    whatsapp_message = (
        "Hello Welcome to Yellow and Red Services Pvt Ltd\n"
        "\n"
        "sharath Graphic Designer\n"
        "Our Services:\n"
        "1. Logo Design\n"
        "2. Poster Design\n"
        "3. Banner Design\n"
        "4. Diary Design\n"
        "5. Invitation Card Design\n"
        "6. Social Media Posts\n"
        "7. Custom Design Work\n"
        "\n"
        "Please reply with the service number you need."
    )

    whatsapp_link = (
        "https://wa.me/916361004454"
        "?text=" + whatsapp_message.replace("\n", "%0A")
    )

    return f"""
    <html>
    <head>
        <title>Scan2Service</title>
    </head>

    <body style="font-family:Arial;text-align:center;margin-top:80px;">

        <h1>Yellow and Red Services Pvt Ltd</h1>

        <p>Select an option</p>

        <div style="margin:20px;">
            <a href="{payment_link}"
            style="padding:15px 30px;background:green;color:white;text-decoration:none;border-radius:10px;">
            Payment
            </a>
        </div>

        <div style="margin:20px;">
            <a href="{whatsapp_link}" target="_blank"
            style="padding:15px 30px;background:#25D366;color:white;text-decoration:none;border-radius:10px;">
            WhatsApp Services
            </a>
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)