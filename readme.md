# Internship applications tracking bot

Internship applications can be overheaded and keep tracking your application numbers and information could be even worse. To organise and simplify this process, I decide to develop a telegram bot. Telegram offers an complete and adaptable interface for my application.
I wanted the bot to get informations about my different applications, to stock those informatuons, to manage the potential update and to be able to produce some summary of the application process.

The first version of the bot application can achieve the first two objectives. 
Firstly, the bot can receive the informations about user's applications. Those inforrmations have to contain:
- an URL of internship offer
- the intern position
- the compagny
The bot process those informations and store them in a SQL database table. 
Once you receive a reponse to your internship application, you can update the status of the application trough the bot. The update informations will be store in a other table of same SQL database. The URL of internship is set to be the join key of two table. In the second table. You have the possibility to store:
- an URL of internship offer
- if you get an interview (Yes/No)
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
    BotFather is a natif telegram bot that help you create and manage your bot on the message application.
    To create your bot use the command keyword `/newbot` and follow the instructions. Once you create your bot, it comes with a token to access telegram API. Keep it, you will need it later.
    You have to set to keyword commands to your bot:
    - `/addapplication` to add application
    - `/updateapplication` to update applicatio
    You can do all of this trough BotFather. You only need to call `/mybots` and follow the instructions. You are ready to clone the repository.

2. Clone the repository
```bash
git clone
```
## Usage

Instructions on how to use the project and any relevant examples.
<!---
## Contributing

Guidelines for contributing to the project and how to submit pull requests.

## License

Information about the project's license and any relevant terms.
--->