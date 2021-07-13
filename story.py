from flask import Flask
from faker import Faker
from faker.providers import company, job, person, geo, lorem

app = Flask(__name__)

@app.route('/')
def story():
    fake = Faker()
    mystory = (
        f"<html><body><p>In a(n) {fake.company()}"
        f" a young {fake.language_name()} stumbles across a(n) "
        f"{fake.domain_word()} which spurs him into conflict with " 
        f"{fake.name()} an {fake.catch_phrase()}"
        f" with the help of a(n) {fake.job()} "
        f" and her {fake.file_name()} culminating in a struggle in "
        f"{fake.company()} where someone shouts: '{fake.sentence()}' </p></body></html>"
    )
    return mystory

