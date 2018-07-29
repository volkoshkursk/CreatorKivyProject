# -*- coding: utf-8 -*-

import os
import sys

import argparse
import traceback
import shutil

from kivy.logger import Logger
from kivy.logger import PY2


if PY2:
    FileNotFoundError = IOError


def write_file(in_file, out_file, values=False):
    string_file = open(out_file).read()
    if values:
        for key in values.keys():
            if not values[key]:
                continue
            string_file = string_file.replace(key, values[key])
        if PY2:
            open(in_file, 'w').write(string_file)
        else:
            open(in_file, 'w', encoding='utf-8').write(string_file)
    else:
        if PY2:
            open(in_file, 'w').write(string_file)
        else:
            open(in_file, 'w', encoding='utf-8').write(string_file)


def copy_files(directory):
    print(directory)
    for directory, dirs, files in os.walk(directory):
        directory_created = directory.split(prog_path)[1]
        print(FULL_PATH_TO_PROJECT + directory_created)
        os.mkdir(FULL_PATH_TO_PROJECT + directory_created)
        for file in files:
            file_created = \
                FULL_PATH_TO_PROJECT + os.path.join(directory_created, file)
            print('        ' + file_created)
            shutil.copyfile(os.path.join(directory, file), file_created)
        print()


__version__ = '2.2.2'
Logger.info('Creator Kivy Project version: ' + __version__)

if len(sys.argv) <= 1:
    Logger.warning('''
Используйте скрипт со строковыми аргументами:

'name' - Имя проекта
'version' - Версия проекта
'path' - Директория проекта
'repo' - Адрес репозитория на GitHub (необязательный параметр)
'author' - Имя автора проекта (необязательный параметр)
'mail' - Почта автора проекта (необязательный параметр)
'site' - Сайт проекта (необязательный параметр)
''')
    sys.exit(0)

prog_path = os.path.split(os.path.abspath(sys.argv[0]))[0]
sys.dont_write_bytecode = True

parser = argparse.ArgumentParser()
parser.add_argument('name', type=str, help='Имя проекта')
parser.add_argument('version', type=str, help='Версия проекта')
parser.add_argument('copyright', type=str, help='Копирайт')
parser.add_argument('path', type=str, help='Директория проекта')
parser.add_argument('-repo', type=str, help='Адрес репозитория на GitHub')
parser.add_argument('-author', type=str, help='Имя автора проекта')
parser.add_argument('-mail', type=str, help='Почта автора проекта')
parser.add_argument('-site', type=str, help='Сайт проекта')

SITE_PROJECT = parser.parse_args().site
VERSION_PROJECT = parser.parse_args().version
COPYRIGHT_PROJECT = parser.parse_args().copyright
NAME_PROJECT = parser.parse_args().name
DIR_PROJECT = parser.parse_args().path
REPO_PROJECT = parser.parse_args().repo
NAME_AUTHOR = parser.parse_args().author
ADDRESS_MAIL = parser.parse_args().mail
FULL_PATH_TO_PROJECT = os.path.join(DIR_PROJECT, NAME_PROJECT)

if os.path.exists(FULL_PATH_TO_PROJECT):
    Logger.error('Проект {} уже существует!'.format(NAME_PROJECT))
    sys.exit(0)

try:
    os.makedirs(FULL_PATH_TO_PROJECT)
    Logger.info(
        'Создана директория проекта {} ...'.format(FULL_PATH_TO_PROJECT))
except FileNotFoundError:
    Logger.error(
        'Указанная директория {} не существует!'.format(DIR_PROJECT))
except Exception:
    print(traceback.format_exc())
    Logger.error(
        'У вас нет прав для создания проекта в директории {}!'.format(
            DIR_PROJECT))

try:
    Logger.info('Создание точки входа main.py ...')
    write_file(
        os.path.join(FULL_PATH_TO_PROJECT, 'main.py'),
        os.path.join(prog_path, 'files', 'main'),
        {
            'REPO_PROJECT': REPO_PROJECT, 'VERSION_PROJECT': VERSION_PROJECT,
            'name_project': NAME_PROJECT.lower(), 'NAME_PROJECT': NAME_PROJECT
        }
    )
    Logger.info('Создание файла README.md ...')
    open(os.path.join(FULL_PATH_TO_PROJECT, 'README.md'), 'w').write('')
    Logger.info('Создание файла программного кода program.py ...')
    write_file(
        os.path.join(FULL_PATH_TO_PROJECT, '%s.py' % NAME_PROJECT.lower()),
        os.path.join(prog_path, 'files',  'program'),
         {
             'NAME_PROJECT': NAME_PROJECT,
             'NAME_AUTHOR': NAME_AUTHOR, 'REPO_PROJECT': REPO_PROJECT,
             'name_project': NAME_PROJECT.lower()
         }
     )
    Logger.info(
        'Создание Makefile для компиляции файлов языковых локализаций...'
    )
    write_file(
        os.path.join(FULL_PATH_TO_PROJECT, 'Makefile'),
        os.path.join(prog_path, 'files', 'Makefile'),
        {'NAME_PROJECT': NAME_PROJECT}
    )
    Logger.info('Создание файла лицензии ...')
    write_file(
        os.path.join(
            FULL_PATH_TO_PROJECT, 'LICENSE'),
            os.path.join(prog_path, 'files', 'LICENSE'),
        {'COPYRIGHT_PROJECT': COPYRIGHT_PROJECT}
    )

    Logger.info('Copying files project...')
    copy_files(os.path.join(prog_path, 'libs'))
    copy_files(os.path.join(prog_path, 'data'))
    copy_files(os.path.join(prog_path, 'test'))
    Logger.info('Создание файла navdrawer.kv ...')
    write_file(
        os.path.join(
            FULL_PATH_TO_PROJECT, 'libs', 'uix', 'kv', 'navdrawer.kv'),
            os.path.join(prog_path, 'files', 'navdrawer'),
        {'VERSION_PROJECT': VERSION_PROJECT}
    )
except FileNotFoundError as exc:
    Logger.error('Не могу найти файл проекта - ' + str(exc))
    shutil.rmtree(FULL_PATH_TO_PROJECT)
    sys.exit(0)
except Exception as exc:
    Logger.error('Неизвестная ошибка - \n' + traceback.format_exc())
    shutil.rmtree(FULL_PATH_TO_PROJECT)
    sys.exit(0)

Logger.info('Проект {} успешно создан!'.format(NAME_PROJECT))
