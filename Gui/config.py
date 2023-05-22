import os
import configparser


def check_exist(filename='config.ini'):
    if not os.path.isfile(filename):
        conf = configparser.ConfigParser()
        conf['DEFAULT'] = {'default_host': '31.10.97.79',
                           'default_port': 80}
        conf['forge.last'] = {}
        with open(filename, 'w') as f:
            conf.write(f)


def load_config(filename='config.ini', default=False):
    config = configparser.ConfigParser()
    config.read(filename)
    if 'host' in config['forge.last'] and 'port' in config['forge.last'] and not default:
        return config['forge.last']['host'], config['forge.last']['port']
    else:
        return config['DEFAULT']['default_host'], config['DEFAULT']['default_port']


def save_config(to_save: dict, filename='config.ini'):
    conf = configparser.ConfigParser()
    conf['DEFAULT'] = {'default_host': '31.10.97.79',
                       'default_port': 80}
    conf['forge.last'] = to_save
    with open(filename, 'w') as f:
        conf.write(f)


if __name__ == '__main__':
    check_exist()
    print(load_config())
    save_conf({'host': '1.1.1.1', 'port': '80'})
