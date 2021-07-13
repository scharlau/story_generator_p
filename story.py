from flask import Flask, render_template
from faker import Faker
from faker.providers import company, job, person, geo, lorem

app = Flask(__name__)

def story():
    fake = Faker()
    mystory = (
        f"In a(n) {fake.company()}"
        f" a young {fake.language_name()} stumbles across a(n) "
        f"{fake.domain_word()} which spurs him into conflict with " 
        f"{fake.name()} an {fake.catch_phrase()}"
        f" with the help of a(n) {fake.job()} "
        f" and her {fake.file_name()} culminating in a struggle in "
        f"{fake.company()} where someone shouts: '{fake.sentence()}' "
    )
    return mystory

@app.route('/')
def index():
    """ We could also add the text to this page and pass in variables
    using {{ variable name }} approach """
    mystory = story()
    return render_template("index.html", story=mystory)

