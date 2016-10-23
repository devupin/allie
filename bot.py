import time
from slackclient import SlackClient

token = 'kekmao'
sc = SlackClient(token)
team_join_event = 'team_join'

with open('template.txt') as f:
    template = f.read()


def send_welcome_message(user):
    user_id = user['id']
    response = sc.api_call('im.open', user=user_id)
    try:
        dm_channel_id = response['channel']['id']
    except (KeyError, ValueError):
        print('Shite happened')
        return
    sc.rtm_send_message(channel=dm_channel_id, message=template)


def main():
    if sc.rtm_connect():
        while True:
            for event in sc.rtm_read():
                if event.get('type') == team_join_event and (
                        event['user']['is_bot'] is False):
                    send_welcome_message(user=event['user'])
            time.sleep(1)
    else:
        print ("Connection Failed, invalid token?")


if __name__ == '__main__':
    main()
