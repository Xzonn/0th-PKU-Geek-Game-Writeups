# Source: https://www.jianshu.com/p/43928fd58afb
# Author: WAY_elegant
# Date: 2019-02-24
import json

class Node:
    def __init__(self):
        self.frequency = 0
        self.name = None
        self.lchild = None
        self.rchild = None
        self.code = None

    def __lt__(self, other):
        return self.frequency < other.frequency

# establish the Huffman Tree
def estblishHuffmanTree(info_dict):
    #output: the base node
    node_list=[]
    for i in info_dict:
        a = Node()
        a.frequency = info_dict[i]
        a.name = i
        node_list.append(a)
    while len(node_list) > 1:
        node_list.sort(reverse=True)
        node_1 = node_list.pop()
        node_2 = node_list.pop()
        new_node = Node()
        new_node.frequency=node_1.frequency+node_2.frequency
        new_node.lchild=node_1
        new_node.rchild=node_2
        node_list.append(new_node)
    return new_node

result = {
    'e': 70,
    '2': 274,
    '9': 81,
    '4': 124,
    '7': 311,
    '1': 77,
    '6': 649,
    'd': 35,
    'f': 69,
    '0': 208,
    '5': 119,
    'c': 35,
    'a': 3,
    '8': 55,
    '3': 94,
    'b': 6
}

base_node = estblishHuffmanTree(result)
def encode(node,rst_dict,code):
    if node.name:
        rst_dict.append([node.name, code])
        return
    code += '0'
    encode(node.lchild,rst_dict,code)
    code = code[:-1]
    code += '1'
    encode(node.rchild,rst_dict,code)
    return rst_dict

code_dict = encode(base_node, [], '')

with open("table.json", "w") as f:
    json.dump(code_dict, f)