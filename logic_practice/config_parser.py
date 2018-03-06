# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com
import configparser
import os

file_dir = os.path.split(os.path.realpath(__file__))[0]
config_file_path = os.path.join(file_dir, 'config.ini')
test = os.path.join(file_dir, 'test.ini')


class config:
    def __init__(self, filename):
        self.file = filename
        self.cf = configparser.ConfigParser()

    def get_section(self, section):
        self.cf.read(self.file)
        all_sections = self.cf.sections()
        all_sections = [x.upper() for x in all_sections]
        try:
            section.upper() in all_sections
        except:
            raise (
            "configparser.NoSectionError: No section: {}".format(section))
        else:
            return section

    # 获取section分组下指定name的值
    def get_section_value(self, section, name):
        # section = self.cf.sections()[section]
        section = self.get_section(section)
        value = self.cf.get(self.get_section(section), name)
        return value

    #  定义方法，修改section分组下指定name的值value
    def set_section_value(self, section, name, value):
        cfg = self.cf.set(self.get_section(section), name, value)
        fp = open(self.file, 'w')
        cfg.write(fp)


if __name__ == "__main__":
    # cfg = config(config_file_path)
    # value = cfg.get_section_value("DATABASE","Username")
    # print(value)
    # pass
    from selenium import webdriver
    google = webdriver.Chrome()
    google.m