#!/usr/local/bin/python3

import json, os, tarfile
from os.path import expanduser

def main():
    config = loadConfig()
    print(config)
    archive = tarfile.open(config['backupFile'], 'w:gz')
    archive.add(config['path'], filter=lambda tarInfo :
            filterIgnores(tarInfo, config['ignores']))
    archive.close()

def filterIgnores(tarInfo, ignores):
    print(tarInfo.name)
    return None if ('/' + tarInfo.name) in ignores else tarInfo

def loadConfig():
    filepath = expanduser('~/.backeruper')
    file = open(filepath, 'r')
    config = json.load(file)
    config['backupFile'] = expanduser(config['backupFile'])
    config['path'] = expanduser(config['path'])
    config['ignores'] = \
        [config['path'] + ignore for ignore in config['ignores']]
    return config

if(__name__ == '__main__'):
    main()
