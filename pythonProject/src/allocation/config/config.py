import os


def get_postgres_config():
    host = os.environ.get('DB_HOST', 'localhost')
    port = os.environ.get('DB_PORT', '5432')
    db_name = os.environ.get('DB_NAME', 'alchemy')
    username = os.environ.get('DB_USERNAME', 'postgres')
    password = os.environ.get('DB_PASSWORD', 'postgres')

    return f'postgresql://{username}:{password}@{host}:{port}/{db_name}'


def server_config():
    host = os.environ.get('SERVER_HOST', 'localhost')
    port = os.environ.get('SERVER_PORT', '8080')
    return host, port
