# Design a data structure that follows the constraints of a Least Recently Used 
# (LRU) cache. 
# 
#  Implement the LRUCache class: 
# 
#  
#  LRUCache(int capacity) Initialize the LRU cache with positive size capacity. 
# 
#  int get(int key) Return the value of the key if the key exists, otherwise return -1.
#  void put(int key, int value) Update the value of the key if the key exists.
#  Otherwise, add the key-value pair to the cache.
#  If the number of keys exceeds the capacity from this operation, evict the least recently used key.
#  
# 
#  Follow up: 
# Could you do get and put in O(1) time complexity?
# get 和 put 方法必须都是 O(1) 的时间复杂度
# 
#  
#  Example 1: 
# 
#  
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3} ,因为此时1是最近最少使用，所以废弃了1，保留了3.
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= capacity <= 3000 
#  0 <= key <= 3000 
#  0 <= value <= 104 
#  At most 3 * 104 calls will be made to get and put. 


# leetcode submit region begin(Prohibit modification and deletion)
class DBlinkedNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        # 设置哨兵头部和尾部
        self.top = DBlinkedNode(None, -1)
        self.tail = DBlinkedNode(None, -1)
        self.top.next = self.tail
        self.tail.prev = self.top
        # 设置哈希存储变量
        self.hkeys = {}
        self.size = 0

    def get(self, key):
        """
        对于 get 操作，首先判断 key 是否存在：
            如果 key 不存在，则返回 -1−1；
            如果 key 存在，则 key 对应的节点是最近被使用的节点。通过哈希表定位到该节点在双向链表中的位置，并将其移动到双向链表的头部，最后返回该节点的值。
        :type key: int
        :rtype: int
        """
        if key not in self.hkeys.keys():
            return -1
        # 如果存在，就先通过哈希表定位，然后移动到头部
        node = self.hkeys[key]
        self.move_to_head(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # 如果key存在，先通过哈希表定位，将对应节点的值更新为value,然后将节点移动到双向链表的头部
        if key in self.hkeys.keys():
            node = self.hkeys[key]
            node.val = value
            self.add_to_head(node)
        # 如果 key 不存在，使用 key 和 value 创建一个新的节点，在双向链表的头部添加该节点，并将 key 和该节点添加进哈希表中。
        # 然后判断双向链表的节点数是否超出容量，如果超出容量，则删除双向链表的尾部节点，并删除哈希表中对应的项
        else:
            # 创建一个新的节点
            node = DBlinkedNode(key, value)
            self.hkeys[key] = node
            # 将节点移动到头部
            self.add_to_head(node)
            self.size += 1
            if self.size > self.cap:
                # 删除尾节点
                removed = self.remove_tail()
                # 删除哈希表中对应的项
                self.hkeys.pop(removed.key)
                self.size -= 1

    def add_to_head(self, node):
        """
        将节点添加到头部
        :param node:
        :return:
        """
        top_node = self.top.next
        self.top.next = node
        node.prev = self.top
        node.next = top_node
        top_node.prev = node

    def remove_node(self, node):
        """
        删除节点
        :param node:
        :return:
        """
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_head(self, node):
        """
        将节点移动到头部
        :param node:
        :return:
        """
        self.remove_node(node)
        self.add_to_head(node)

    def remove_tail(self,):
        """
        删除尾节点,定位到尾节点，然后利用remove方法删除节点
        :return: 返回尾节点，在put操作中根据尾节点的key删除哈希表中的值
        """
        node = self.tail.prev
        self.remove_node(node)
        return node

    def __repr__(self):
        vals = []
        p = self.top.next
        while p.next:
            vals.append(str(p.val))
            p = p.next
        return '->'.join(vals)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # Example 1:
    #
    #
    # Input
    # ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    # [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    # Output
    # [null, null, null, 1, null, -1, null, -1, 3, 4]
    #
    # Explanation
    # LRUCache lRUCache = new LRUCache(2);
    # lRUCache.put(1, 1); // cache is {1=1}
    # lRUCache.put(2, 2); // cache is {1=1, 2=2}
    # lRUCache.get(1);    // return 1
    # lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    # lRUCache.get(2);    // returns -1 (not found)
    # lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3} ,因为此时1是最近最少使用，所以废弃了1，保留了3.
    # lRUCache.get(1);    // return -1 (not found)
    # lRUCache.get(3);    // return 3
    # lRUCache.get(4);    // return 4
    cache = LRUCache(capacity=2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache)  # cache is {1=1, 2=2}
    cache.get(1)
    cache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    print(cache)
    cache.put(4, 4)
    print(cache)
    cache.get(1)
    cache.get(3)
    print(cache)
    cache.get(4)
    print(cache)