# allie

allie is a welcome bot written for Slack teams in Python 3.

## Features

- Sends a private message to newly joined team member
- And then sends acknowledgement message to all admins that a new member has been joined

## Installation

### System Requirements

- Python 3 (should work on Python 2 as well, but not tested)

### Python Requirements
    pip install -r requirements.txt

### Instructions

 - Change `template.txt` as per your requirements. Make sure the channel and user IDs are correct.
 - Create a new bot from Custom Integrations (URL is https://teamname.slack.com/apps/build/custom-integration) and keep the API token somewhere safe.
 - Rename `sample_settings.py` to `settings.py` and update API Token in the file.
 - Run `python3 bot.py`
 - Bonus: use `supervisor.conf` to manage the process.

## To do 

- [ ] Better log messages
- [ ] Better error handling

## Name

The name Allie comes from the book The Notebook by Nicholas Sparks, where protagonist's name is Allie Nelson.

## License

The mighty MIT license. Please check `LICENSE` for more details.
