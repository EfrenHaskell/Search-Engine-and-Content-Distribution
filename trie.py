#!usr/bin/env Python
"""
Trie data structure and helper methods for printing and building tries
"""

__author__ = "Efren Haskell"
__email__ = "efrenhask@gmail.com"


class TrieNode:
    def __init__(self, val: chr):
        self.children: dict[chr, TrieNode] = {}
        self.char: chr = val
        self.is_EOW = False

    def __insert(self, val: chr):
        """ internal --- Insert new node into trie data structure

        :param val:
        :return:
        """
        self.children[val] = TrieNode(val)

    def _add(self, string: str, index: int, depth: int):
        """internal --- add char to trie if not current node value or already a child
                        recursively work through string until all chars have been added

        :param string:
        :param index:
        :return:
        """
        if index >= len(string):
            self.is_EOW = True
            return
        curr: chr = string[index]
        if curr not in self.children:
            self.__insert(curr)
        self.children[curr]._add(string, index+1, depth+1)

    def add(self, string: str):
        """ Add new chars to trie from string input

        :param string:
        """
        self._add(string, 0, 0)

    def get_children(self):
        """ get children of TrieNode

        :return:
        """
        return self.children

    def get_val(self):
        """ get value of TrieNode

        :return:
        """
        return self.char

    def seek(self, query: str, index: int):
        if index >= len(query):
            return self
        char: chr = query[index]
        if char not in self.children:
            return None
        return self.children[query[index]].seek(query, index+1)

    def follow(self, constraint: int, elements: list[str], element):
        if len(elements) >= constraint != -1:
            return 0
        if len(self.children) == 0:
            elements.append(element)
            return 1
        else:
            if self.is_EOW:
                elements.append(element)
            for child in self.children.values():
                code: int = child.follow(constraint, elements, element + child.char)
                if code == 0:
                    return 0


def build_trie(values: iter):
    """ builds trie from given collection, returns root node

    :param values:
    :return:
    """
    trie: TrieNode = TrieNode(None)
    # TrieNode root initialized to None
    for value in values:
        trie.add(value)
    return trie


def get_by_query(query: str, trie: TrieNode, constraint: int) -> list[str]:
    seek_value: TrieNode = trie.seek(query, 0)
    if seek_value is None:
        return []
    elements = []
    seek_value.follow(constraint, elements, query)
    return elements


def print_trie(trie: TrieNode, level: int):
    """ print a trie by depth

    :param trie:
    :param level:
    :return:
    """
    children = trie.get_children()
    for child in children.values():
        print(child.char, end=" ")
    if len(children) > 0:
        print()
    for child in children.values():
        print_trie(child, level+1)
