# Internship applications tracking bot

Applying for internships can be tedious and keeping track of your application numbers and information can be even worse. To organise and simplify this process, I decided to develop a Telegram bot. Telegram offers a complete interface that can be adapted to my application.
I wanted the bot to obtain information about my various applications, store this information, manage potential updates and be able to produce a summary of the application process.

The first version of the bot application can achieve the first two objectives. 
Firstly, the bot can receive information about the user's applications. This information should contain
- the URL of the internship offer
- the trainee's position
- the company

The bot processes this information and stores it in a table in the SQL database. 
Once you have received a response to your internship application, you can update the status of your application via the bot. The update information will be stored in another table in the same SQL database. The internship URL is defined as the linking key for the two tables. In the second table. You can store
- the URL of the internship offer
- whether you are granted an interview (Yes/No)
- the potential date of the interview.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
<!---
- [Contributing](#contributing)
- [License](#license)
--->
## Installation

You can use this application in few steps:
1. Create a telegram bot

    [BotFather](https://core.telegram.org/api) is a natif telegram bot that help you create and manage your bot on telegram message application.
    To create your bot use the command keyword `/newbot` and follow the instructions. Once you create your bot, it comes with an API token to access telegram. Keep it, you will need it later.
    You have to set to keyword commands to your bot:
    - `/addapplication` to add application
    - `/updateapplication` to update application

    You can do all of this trough BotFather. You only need to call `/mybots` and follow the instructions. 
    
    You are ready to clone the repository.

2. Clone the repository

    Copy and run the below code in your favorite command line interface.
    ```bash
    git clone https://github.com/Datadoulla/intern.git
    ```
    Once you clone the repo, you have to add ans .env file to store and protect the access to your sensible token for accessing telegram API.

3. Run the application

    At the step, you have two possibilities. The first one is more elegant. If you are familliar with docker, open your docker application and build the following docker image with the cloned repo Dockerfile.
    ```bash
    docker build -t internbot_img . 
    ```
    After that, you can run the application in a safe docker container excuting thi command line code
    ```bash
    docker run --name interbot  internbot_img
    ```

    The second option is to create an environnement and install the applicaion requirements.
    ```python
    pip3 install -r requirements.txt
    ```
    And run the main.py

    ```python
    python -m main.py
    ```

## Usage

The application utilisation is pretty simple but have to follow a strict format. To add track application, you have to call `/addapplication` keyword follow by the URL of application, a position one word description and the compagny.

Example:
> https://cacf.talentview.io/jobs/d9q8nk?source=carriere&utm_source=carriere DS (for data scientist) Crédit agricole

To update an application, you need to response to the application message with `/updateapplication` keyword and precise Yes if you get an interview and the date of interview and No else.

Example:
> Yes 20/02 (Day/month format)

**I personnaly recommand you to host you application on api plateforme like *pythonanywhere* to have a perment access and running application.**

<!---
## Contributing

Guidelines for contributing to the project and how to submit pull requests.

## License

Information about the project's license and any relevant terms.
--->