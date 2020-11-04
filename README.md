# story_generator_p
A remake of the story generator exercise for python, which was originally in ruby https://github.com/scharlau/Story_Generator .

## First, create the app basics
When working with python apps you should use a virtual environment so that your applications are self-contained and you can change the version of python and associated libraries as required. We'll use https://github.com/pyenv/pyenv in this example.

Create a new project folder called 'story_generator' and then cd into the folder via the terminal and execute these commands:

        pyenv local 3.7.0 # this sets the local version of python to 3.7.0
        python3 -m venv .venv # this creates the virtual environment for you
        source .venv/bin/activate # this activates the virtual environment
        pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.

We will use Flask (https://flask.palletsprojects.com/en/1.1.x/) as our web framework for the application. We install that with 
        pip install flask
And that will install flask with its associated dependencies. We can now start to build the application.

## Start the web components 
Create a new file called story.py in the main folder.
Put this code in the file:
        from flask import Flask
        app = Flask(__name__)

        @app.route('/')
        def story():
            mystory = """In a(n) ADJECTIVE +  NOUN"
            " a young PERSON " 
            " stumbles across a(n) OBJECT " 
            " which spurs him into conflict with NAME ANIMAL " 
            " with the help of a(n) ASSISTANT " 
            " and her OBJECT/TOOL " 
            " culminating in ACTION  where someone shouts 'QUOTE'."""
            return mystory

We can confirm this runs by setting a few variables in your environment via the terminal (this assumes you're either using Linus or MacOS)
        export FLASK_APP=story.py
        export FLASK_ENV=development
        python3 -m flask run

You can now view your site at localhost:5000 in the browser. It won't show much other than 'my story goes here', but is enough to confirm that everything works correctly.

## Add in 
We can now add in some random content for the story using the Faker library from https://pypi.org/project/Faker/. 
Install Faker with the command:
        pip install Faker

Now we can set about changing the nouns, adjectives and other parts of mystory with values from Faker. Go to https://faker.readthedocs.io/en/stable/providers.html and look through the options for Standard Providers and make some changes to mystory by swapping the mystory variable with the following:
        fake = Faker()
        mystory =   "<html><body><p>In a(n) " + fake.company()
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
        mystory = mystory + " </p></body></html>"

You should now be able to generate a simple random story each time you refresh the page in the browser. This is the most basic version you could do. 

## Second, do the work
Now we come to the part where we can explore how to make the code more readable, and also more easily maintainable by removing repetion and breaking up the code into more methods.

We can do this via a few different ways.


