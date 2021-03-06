# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/Blog-With-GitHub-Boilerplate/"
template = {
    "name": "Galileo",
    "type": "git",
    "url": "https://github.com/Si-Huan/Maverick-Theme-Galileo.git",
    "branch": "latest"
}
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {
    "enabled": True,
    "repo": "Si-Huan/Blog-With-GitHub-Boilerplate@gh-pages"
}

# 站点设置
site_name = "SiHuan's Blog"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "SiHuan"
email = "sihuan@sakuya.love"
author_homepage = "https://www.sakuya.love"
description = "道阻且长，君子思还。"
key_words = ['SiHuan', '思还', 'Blog', '博客', 'GitBlog']
language = 'zh-CN'
external_links = [
    {
        "name": "SiHuan-Wiki",
        "url": "https://wiki.sakuya.love",
        "brief": "我的知识积累。"
    },
    {
        "name": "SiHuan-Sakuya",
        "url": "https://www.sakuya.love",
        "brief": "思还的主页。"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Telegram",
        "url": "https://twitter.com/AlanDecode",
        "icon": "gi gi-telegram"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/AlanDecode",
        "icon": "gi gi-github"
    },
    {
        "name": "QQ",
        "url": "https://weibo.com/5245109677/",
        "icon": "gi gi-twitter"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
