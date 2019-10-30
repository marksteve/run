import os

import requests

from flask import Flask, request, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def render_rows(form):
    return "".join(
        map(lambda f: f"""
            <tr>
                <th align=left>{f[0]}</th>
                <td>{f[1]}</td>
            </tr>
        """, form.items())
    )


def create_message(form):
    subject = "New submission"
    for key in "name", "Name", "email", "Email":
        name = form.get(key)
        if name:
            subject += f" from {name}"
            break
    html = f"""
<h1>New submission</h1>
<table cellpadding=10 cellspacing=0>
    {render_rows(form)}
<table>
"""
    return {
        "from": os.environ["EMAIL_FROM"],
        "to": os.environ["EMAIL_TO"],
        "subject": subject,
        "html": html,
    }


@app.route("/", methods=["POST"])
def send_email():
    domain = os.environ["MG_DOMAIN"]
    key = os.environ["MG_API_KEY"]
    url = f"https://api.mailgun.net/v3/{domain}/messages"
    form = request.form
    resp = requests.post(url, data=create_message(form), auth=("api", key))
    resp.raise_for_status()
    return redirect(os.environ["REDIRECT_URL"])

