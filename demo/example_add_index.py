# -*- coding: utf-8 -*-
from whoosh.index import create_in
from whoosh.fields import Schema, ID, TEXT
from jieba.analyse import ChineseAnalyzer

analyzer = ChineseAnalyzer()
schema = Schema(
    title=TEXT(stored=True),
    path=ID(stored=True),
    content=TEXT(stored=True, analyzer=analyzer),
)


if __name__ == "__main__":
    idx = create_in("indexdir", schema)
    writer = idx.writer()
    documents = [
        {
            "title": "First document",
            "path": "/a",
            "content": "This is the document for test",
        },
        {
            "title": "First document",
            "path": "/a",
            "content": "This is the first document we've added!",
        },
        {
            "title": "Second document",
            "path": "/b",
            "content": "The second one is even more interesting!",
        },
    ]
    for document in documents:
        writer.add_document(**document)
    writer.commit()
