import configparser


def load(path="settings.ini"):
    parser = configparser.ConfigParser()
    parser.read(path)
    return {
        "retries": parser.getint("network", "retry"),
        "timeout": parser.getint("network", "timeout"),
    }
