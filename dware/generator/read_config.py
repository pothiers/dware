import configparser
from pathlib import Path
#
import dware.ingest


cfname = Path('~/sandbox/dware/configs/photo.ini').expanduser()

def get_config(ini_fname):

    config = configparser.ConfigParser()
    config.read(cfname)
    config.sections()
    list(config['INGEST'].keys()) # => ['watchdir', 'readfunc']

    config['STORE']['corefields'].split()

    config['STORE']['auxfields'].split()
    config['STORE']['datafields'].split()

    dd = dict(
        watch_dir=Path(config['INGEST']['WatchDir']).expanduser(),
        read_func=config['INGEST']['ReadFunc'],
        core_fields=config['STORE']['CoreFields'].split(),
        aux_fields=config['STORE']['AuxFields'].split(),
        data_fields=config['STORE']['DataFields'].split(),
        )

    return dd
