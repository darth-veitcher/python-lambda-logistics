import os
import yaml
from jinja2 import Environment, PackageLoader, select_autoescape
import subprocess

BASEDIR = os.getcwd()


def load_config(path=None):
    """Loads a yaml config file from optional path or searches immediate directory"""
    if path:
        config_path = path
    else:
        basedir = BASEDIR
        config_path = os.path.join(basedir, 'pll.yaml')

    if not os.path.isfile(config_path):
        raise Exception(f"Unable to find config file at {config_path}")

    with open(config_path) as ymlfile:
        cfg = yaml.load(ymlfile)
        print(cfg)

        for path in cfg.get('packaging'):
            if not os.path.exists(path):
                # Probably relative
                abs_path = os.path.join(BASEDIR, cfg.get('packaging')[path])
                if not os.path.exists(abs_path):
                    raise Exception(f'Unable to find a valid path for {path}')
                cfg.get('packaging')[path] = abs_path

        return cfg


def get_cli_args(config_path=None):
    """Uses configuration object to template out the CLI args to run docker with"""
    cfg = load_config(config_path)
    env = Environment(
        loader=PackageLoader('pll', 'templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('cli.j2')
    return template.render(cfg.get('packaging'))


def package(config_path=None):
    """Packages up application for AWS deployment using docker"""
    subprocess.run(get_cli_args(config_path), shell=True, check=False)