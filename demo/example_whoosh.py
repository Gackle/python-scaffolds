# -*- coding: utf-8 -*-
from whoosh.index import open_dir
from whoosh.qparser import QueryParser

if __name__ == "__main__":
    ix = open_dir("indexdir")
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse("test")
        results = searcher.search(query)
        for hit in results:
            print(hit.highlights("content"))
        print("="*10)
