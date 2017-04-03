# lambot

Lambot is a Slack bot written in Python 2.7, and architected for a serverless hosting environment using AWS Lambda and API Gateway, managed using Zappa.io, and extensible using a simple plugin API. This project was created to encourage collaborative bot hacking on the Code && Coffee Slack.


## Notes for writing a Lambot plugin
1. Open a new issue with a brief description about your plugin - this will give us a place to discuss the plugin, discuss any enhancements to Lambot that might be needed to support it, and just to give your project some visibility.
2. Create a new branch from `development`, and name your branch `plugin-xxxxx` where xxxxx is the name of your plugin. Eg., if you're working on a plugin named `chaos`, name your branch `plugin-chaos`.
3. Commit often, tracking changes as atomically as possible, and always use coherent commit messages.
4. Please push your changes regularly. When you're confident your plugin is ready for testing and deployment, please open a pull request to merge it with the `development` branch.

## Notes for fixing bugs and adding features to Lambot
1. Open a new issue with a description of the bug or enhancement. No changes will be accepted without an issue.
2. For each issue you must create a branch from `development`, and name your branch `#x/yy_yyy` where x is the issue number, and yy_yyy is a search-friendly version of the issue title, in all lowercase, with spaces and punctuation converted to underscores. Eg., if you have issue #5 named "Making Lambot great again", name your branch `#5/making_lambot_great_again`.
3. Commit often, tracking atomic changes where possible, and always use coherent commit messages.
4. Push your changes to your branch regularly. When you're confident your plugin is ready for testing and deployment, please open a pull request to merge it with the `development` branch.

## Deployment note

The Code && Coffee instance of Lambot is hosted within a private AWS cloud, and can only be deployed to by @rogerhoward; after merging your pull request, Roger will deploy the changes, but if you're not seeing them or have any questions, find him on Slack.


## Setting up your dev environment

### Create, activate, and configure a Python 2.7 virtualenv

1. Create your virtualenv. If you're new to this, I recommend virtualenv-burrito; just install by pasting `curl -sL https://raw.githubusercontent.com/brainsik/virtualenv-burrito/master/virtualenv-burrito.sh | $SHELL` in your terminal; when you're done you should be able to create a virtualenv with the following command (you may need to open a new terminal window first): `mkvirtualenv lambot`.
2. Activate your virtualenv. If you used virtualenv-burrito, then it should already be activated; if it's not, run `workon lambot`.
3. With your virtualenv active, install all project dependencies. Make sure you're in the project directory, then just run `pip install -r requirements.txt`

Voila! You now have a virtualenv for this project, with all the dependencies installed. Whenever you want to work on lambot, just run `workon lambot` first.

### Running the test server

1. First, activate your virtualenv
2. Then, from within the project directory, run `./server.py`

You now have a dev server running on port 5000!

### Using the test client

1. First, make sure the test server is running in its own terminal window
2. In another terminal, with your virtualenv activated, run `./test_client.py` - this will simulate a Slack client, and send a simulated bot command to the test server you have running.

* Watch the terminal window your server.py is running in to see the simulated response the bot would have sent to Slack.
* Run `./test_client.py --help` to see various options you can set to customize the simulated bot client.