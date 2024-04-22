<p align="center">
    <b>
        <h1 align="center">Google Meet Bot</h1>
    </b>
</p>
<p align="center">
<a href="https://dev.azure.com/cplusoft-org/minerva-ai/_git/minerva-ai">
    <img src="https://readme-typing-svg.demolab.com?font=Georgia&c=g&size=18&duration=3000&pause=6000&multiline=True&center=true&width=800&height=40&lines= Record google meeting with this bot;" alt="Typing SVG" />
</a>
</p>
<p align="center">
<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=15&pause=1000&color=18F715&center=true&random=false&width=435&lines=Python3+%7C+FastAPI+%7C+Selenium+%7C+OpenCV" alt="Typing SVG" /></a>

</p>

<p align="center">
    <a href="https://www.python.org/downloads/">
        <img alt="License" src="https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-g.svg">
    </a>
    <a href="https://cplusoft-org@dev.azure.com/cplusoft-org/minerva-ai/_git/minerva-ai">
        <img alt="Last Commit" src="https://img.shields.io/github/last-commit/hassi34/iot-device-identification/main?color=g">
    </a>
    <a href="https://cplusoft-org@dev.azure.com/cplusoft-org/minerva-ai/_git/minerva-ai">
        <img alt="Code Size" src="https://img.shields.io/github/languages/code-size/hassi34/iot-device-identification?color=g">
    </a>
    <a href="https://cplusoft-org@dev.azure.com/cplusoft-org/minerva-ai/_git/minerva-ai">
        <img alt="Repo Size" src="https://img.shields.io/github/repo-size/hassi34/iot-device-identification?color=g">
    </a>
    <a href="https://cplusoft-org@dev.azure.com/cplusoft-org/minerva-ai/_git/minerva-ai">
        <img alt="License" src="https://img.shields.io/github/license/hassi34/iot-device-identification?color=g">
    </a>
    <a href="https://cplusoft-org@dev.azure.com/cplusoft-org/minerva-ai/_git/minerva-ai">
        <img alt="Issue Tracking" src="https://img.shields.io/badge/issue_tracking-github-brightgreen.svg">
    </a>
    <a href="https://cplusoft-org@dev.azure.com/cplusoft-org/minerva-ai/_git/minerva-ai">
        <img alt="Open Issues" src="https://img.shields.io/github/issues/hassi34/iot-device-identification">
    </a>
</p>

Following are the main contents to follow, you can jump to any section:

> - [Introduction](#project-intro) `<br>`
> - [Run Locally](#run-local) `<br>`
>
>   - [Environment Setup](#env-setup) `<br>`
>   - [Environment Variables](#env-vars) `<br>`
>   - [Run Application](run-app)

### Introduction `<a id='project-intro'></a>`

This project aims to record the Google Meeting. It is a back-end webserver created

with FastAPI. It uses Selenium for automation like sigining in to google account and

joining google meet. It uses OpenCV module for recording the meeting. It uses pyaudio

module for audio and then audio is also transcribe through an AI model.

## Run Locally `<a id='run-local'></a>`

- Ensure you have [Python 3.8+](https://www.python.org/downloads/) installed.
- Create a new Python Conda environment:`<a id='env-setup'></a>`

```bash
conda create -p venv python=3.11
conda activate ./venv
```

OR

- Create a new Python virtual environment with pip:

```bash
virtualenv venv
source venv/Scripts/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Clone the project

```bash
  git clone https://cplusoft-org@dev.azure.com/cplusoft-org/minerva-ai/_git/minerva-ai
```

Go to the project directory

```bash
  cd minerva-ai
```

#### Export the environment variable `<a id='env-vars'></a>`

```bash
# FastAPI
API_TITLE = "Title"
API_DESCRIPTION = "Description."
API_VERSION = "1"

# Google
GOOGLE_SIGNIN_LINK='https://accounts.google.com'
GOOGLE_EMAIL='email'
GOOGLE_PASSWORD='password'

# Logs path
WEBDRIVER_LOG_PATH='chromedriver.log'

```

#### Run Application `<a id='run-app'></a>`

```
uvicorn main:app
```
