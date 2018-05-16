#!/usr/bin/bash
# - - coding: utf-8 -*-

#一致性哈希算法
import collections


class ConsistentHash(object):
    def __init__(self, servers):
        self.servers = collections.OrderedDict
        for server in servers:
            self.servers.setdefault(hash(server), server)

    @classmethod
    def getServer(self, key):
        hash = hash(key)



def hash(s):
    p = 16777619
    hash = 2166136261
    for i in range(1, len(s), 1):
        hash += hash << 13
        hash ^= hash >> 7
        hash += hash << 3
        hash ^= hash >> 17
        hash += hash << 5

        # 如果计算出负数  取绝对值
        if hash < 0:
            hash = abs(hash)
        return hash








