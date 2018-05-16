#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python实现二叉树的四种遍历

class node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# 深度
def depth(tree):
    if tree is None:
        return 0
    left, right = depth(tree.left), depth(tree.right)
    return max(left, right) + 1


# 前序遍历
def pre_order(tree):
    if tree is None:
        return
    print tree.data
    pre_order(tree.left)
    pre_order(tree.right)


# 中序遍历
def mid_order(tree):
    if tree is None:
        return
    mid_order(tree.left)
    print tree.data
    mid_order(tree.right)


# 后序遍历
def post_order(tree):
    if tree is None:
        return
    post_order(tree.left)
    post_order(tree.right)
    print tree.data


# 层次遍历
def level_order(tree):
    if tree is None:
        return
    q = [tree]
    while q:
        current = q.pop(0)
        print current.data
        if current.left != None:
            q.append(current.left)
        if current.right != None:
            q.append(current.right)


# 按层次打印
def level2_order(tree):
    if tree is None:
        return
    q = [tree]
    results = {}
    level = 0
    current_level_num = 1
    next_level_num = 0
    d = []
    while q:
        current = q.pop(0)
        current_level_num -= 1
        d.append(current.data)
        if current.left != None:
            q.append(current.left)
            next_level_num += 1
        if current.right is not None:
            q.append(current.right)
            next_level_num += 1
        if current_level_num == 0:
            current_level_num = next_level_num
            next_level_num = 0
            results[level] = d
            d = []
            level += 1
    print results


if __name__ == '__main__':
    tree = node('D', node('B', node('A'), node('C')),
                node('E', right=node('G', node('F'))))
    print '前序遍历'
    pre_order(tree)
    print '\n'
    print '中序遍历'
    mid_order(tree)
    print '\n'
    print '后序遍历'
    post_order(tree)
    print '\n'
    print '层次遍历'
    level2_order(tree)
