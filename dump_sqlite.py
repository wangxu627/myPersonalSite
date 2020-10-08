import codecs
import sqlite3
from collections import namedtuple

import html2text

ArticleBase = namedtuple("ArticleBase", "id title content summary create_time update_time num_of_view source_id")

class Article(ArticleBase):
    __slots__ = ()
    def __new__(cls, **kwargs):
        return super(Article, cls).__new__(cls, **kwargs)

def main():
    conn = sqlite3.connect('data.sqlite')
    cursor = conn.execute("SELECT * from articles")
    for data in cursor:
        ab = ArticleBase(*data)
        article = Article(**ab._asdict())
        # print(article.id, article.title, article.content, article.create_time)
        md_content = convert_html_2_md(article.content)
        # article._replace(content=md_content)
        # print(article.content, md_content)

        d = dict(article._asdict())
        d["content"] = md_content
        generate_md(d)


def convert_html_2_md(html):
    h = html2text.HTML2Text()
    return h.handle(html)

def generate_md(article):
    format_str = '''
---
title: {title}
date: {create_time}
Description: ""
Tags: []
Categories: []
DisableComments: false
---
{content}
'''
    formatted_str = format_str.format(**article)
    with codecs.open("article-" + str(article["id"]) + ".md", "w", "utf-8") as f:
        f.write(formatted_str)

main()