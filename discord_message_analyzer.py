import requests

# Задайте свои параметры
TOKEN = 'YOUR_BOT_TOKEN'
CHANNEL_ID = 'YOUR_CHANNEL_ID'
HEADERS = {
    'Authorization': f'Bot {TOKEN}'
}


def get_messages(channel_id):
    """Получает последние 100 сообщений из указанного канала."""
    url = f'https://discord.com/api/v10/channels/{channel_id}/messages'
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return response.json()
    else:
        print(f'Ошибка: {response.status_code} - {response.text}')
        return []


def analyze_messages(messages):
    """Анализирует сообщения и выводит статистику."""
    total_messages = len(messages)
    user_messages = {}

    for message in messages:
        user = message['author']['username']
        user_messages[user] = user_messages.get(user, 0) + 1

    print(f'Всего сообщений: {total_messages}')
    print('Сообщения по пользователям:')

    for user, count in user_messages.items():
        print(f'{user}: {count} сообщений')


def main():
    messages = get_messages(CHANNEL_ID)
    analyze_messages(messages)


if __name__ == '__main__':
    main()