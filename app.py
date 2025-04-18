from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "development-secret-key")

# Description data pulled and rephrased from the Cymate-style overview for Syncura Legacy
company_overview = {
    "title": "Syncura Legacy - Final Expense Insurance Solutions",
    "subtitle": "Empowering agents with lead generation services inspired by industry leaders",
    "sections": [
        {
            "heading": "Direct Mail Campaign Expertise",
            "content": "Syncura Legacy follows a proven direct mail strategy based on Lead Concepts' successful approach. By targeting seniors with compelling messages, we ensure high response rates and qualified final expense leads."
        },
        {
            "heading": "Exclusive Telemarketing Leads",
            "content": "Drawing from Lead Heroes' model, we generate exclusive telemarketing leads with personalized scripts that encourage meaningful conversations and optimized conversion paths."
        },
        {
            "heading": "Compliance & Conversion",
            "content": "Inspired by The Leads Warehouse, Syncura Legacy prioritizes TCPA-compliant leads. Our data handling ensures legal protection for agents while delivering high-quality, conversion-ready prospects."
        },
        {
            "heading": "Pay-Per-Lead Flexibility",
            "content": "Our system, modeled after TTC Leads, enables agents to pay only for the leads they receive. We empower over 20,000 agents with flexible budgeting tools and scalable options."
        },
        {
            "heading": "Affordable Fixed-Price Packages",
            "content": "Mirroring CABoom Leads, we offer set-price lead packages to help clients plan their outreach campaigns effectively while maintaining affordability and high returns."
        },
        {
            "heading": "Real Client Case Studies",
            "content": [
                "An elderly man in the U.S. was assisted by Syncura Legacy in securing Final Expense Insurance. Our tailored services helped him optimize his profile and access maximum state benefits available to him.",
                "An elderly woman benefitted from our consultative approach, enhancing her health and medical benefits while leveraging rights-based assistance to structure her coverage smartly."
            ]
        },
        {
            "heading": "Payment Plans",
            "content": [
                "Basic Plan: $299/month - Includes up to 25 leads, direct mail option only",
                "Professional Plan: $599/month - Includes up to 50 leads, telemarketing and direct mail",
                "Enterprise Plan: Custom pricing - High-volume lead access, personalized scripts, dedicated account manager"
            ]
        }
    ]
}

@app.route("/")
def home():
    return render_template("index.html", data=company_overview)

@app.route("/api/overview")
def api_overview():
    return jsonify(company_overview)

if __name__ == "__main__":
    app.run(debug=True)
