#!usr/bin/env Python
"""
Collection of search engines and utilities
"""

__author__ = "Efren Haskell"
__email__ = "efrenhask@gmail.com"

import trie


class Engine:
    """
    Super class for search engine objects
    """

    def __init__(self):
        pass

    def __query(self, query: str):
        """ abstract method for query (with specified constraint)

        :param query:
        :return:
        """
        pass

    def __query_all(self, query: str):
        """ abstract method for query (for all engine elements)

        :param query:
        :return:
        """
        pass

    def make_recommendation(self, query: str):
        """ abstract method for recommendation delivery

        :param query:
        :return:
        """
        pass

    def deliver(self, query: str):
        """ deliver content by query

        :param query:
        :return:
        """
        results = self.__query_all(query)


class Thomas(Engine):
    """
    Thomas the Tank Engine
    Features:
        - Unoptimized
        - Uses internal trie (tank)
        - Constrained delivery of trie elements by load order
    """

    def __init__(self, constraint: int):
        super().__init__()
        self.tank = trie.TrieNode(None)
        self.constraint = constraint
        self.priority_map: dict[str, str] = {}

    def __query(self, query: str):
        """ implements Engine query - gets a constrained list of trie elements by query

        :param query:
        :return:
        """
        return trie.get_by_query(query, self.tank, self.constraint)

    def __query_all(self, query: str):
        """ implements Engine query - gets a list of all trie elements by query

        :param query:
        :return:
        """
        return trie.get_by_query(query, self.tank, -1)

    def load_trie(self, build_file: str):
        """ Load trie contents from build file and build subsequent trie

        :param build_file:
        :return:
        """
        with open(file=build_file, mode="r") as file:
            lines = file.readlines()
        assert lines is not None

        self.tank = trie.build_trie(lines)

    def manual_create_trie(self, collection: list[str]):
        """ Create trie from collection

        :param collection:
        :return:
        """
        self.tank = trie.build_trie(collection)

    def make_recommendation(self, query: str):
        """ return recommended search results by query

        :param query:
        :return:
        """
        if len(query) == 0:
            return []
        return self.__query(query)

    def populate_priority_map(self):
        pass

    def priority_recommendation(self, query: str):
        pass


class James(Engine):

    def __init__(self):
        super().__init__()
        self.tank = trie.TrieNode(None)

