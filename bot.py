import time
from slackclient import SlackClient

token = 'kekmao'
sc = SlackClient(token)
team_join_event = 'team_join'

with open('template.txt') as f:
    template = f.read()


def _get_admin_ids():
    users = sc.api_call('users.list')
    return [u['id'] for u in users['members'] if u.get('is_admin') is True]


def get_admin_dm_channels():
    global admin_dm_channels
    for admin_id in _get_admin_ids():
        response = sc.api_call('im.open', user=admin_id)
        admin_dm_channels.append(response['channel']['id'])
    return admin_dm_channels


def notify_admin(username):
    for dm_channel_id in admin_dm_channels:
        m = 'User: {} successfully on-boarded'.format(username)
        sc.rtm_send_message(channel=dm_channel_id, message=m)


def send_welcome_message(user):
    user_id = user['id']
    response = sc.api_call('im.open', user=user_id)
    try:
        dm_channel_id = response['channel']['id']
    except (KeyError, ValueError):
        print('Shite happened')
        return
    sc.rtm_send_message(channel=dm_channel_id, message=template)
    notify_admin(username=user['name'])


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
    get_admin_dm_channels()
    main()
