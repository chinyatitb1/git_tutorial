def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def configure_app(**kwargs):
    """
    Configure the application with optional parameters.

    :param kwargs: Arbitrary keyword arguments representing configuration options.
    Supported Keys include:
    - theme (str): UI theme eg "light", "dark"
    - Language (str): Language code eg "en
    - notifications (bool): Wether notifications should be enabled or not
    :return:
    dict
        A dictionary containing configuration options after applying defaults and any overrides passed via kwargs
    """
    defaults = {
        "theme": 'light',
        'language': 'en',
        'notifications': True
    }

    defaults.update(kwargs)
    return defaults

settings = configure_app(theme='dark', notifications=False)

print(configure_app.__doc__)
print(configure_app.__name__)
print(configure_app.__module__)

print(settings)