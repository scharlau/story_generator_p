from flask import Flask, render_template
from faker import Faker
from faker.providers import company, job, person, geo


app = Flask(__name__)

def story():
    fake = Faker()
    mystory =   "In a(n) " + fake.company()
    mystory = mystory + " a young "
    mystory = mystory + fake.language_name()
    mystory = mystory + " stumbles across a(n) "
    mystory = mystory + fake.domain_word()
    mystory = mystory +  " which spurs him into conflict with " 
    mystory = mystory + fake.name() 
    mystory = mystory + " an " + fake.catch_phrase()
    mystory = mystory + " with the help of a(n) "
    mystory = mystory + fake.job()
    mystory = mystory + " and her "
    mystory = mystory + fake.file_name() 
    mystory = mystory + " culminating in a struggle in "
    mystory = mystory + fake.company()
    mystory = mystory + " where someone shouts "
    mystory = mystory + fake.bs()
    return mystory

@app.route('/')
def index():
    """ We could also add the text to this page and pass in variables
    using {{ variable name }} approach """
    mystory = story()
    return render_template("index.html", story=mystory)

