"""Day 10 — 哈希表 & LeetCode 1 两数之和"""


# ============================================================
# 第一部分：手写简易 HashMap（链地址法）
# ============================================================

class HashMap:
    """简易哈希表，用 数组 + 链表（每个桶是 [(k,v), ...] 列表）实现"""

    def __init__(self, size=10):
        # TODO: 初始化 size 个空桶，每个桶是 []
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        """哈希函数：把 key 转成字符串 → 每个字符的 ord 求和 → 取模"""
        # TODO
        return sum(ord(c) for c in key) % self.size

    def put(self, key, value):
        """存入键值对。key 已存在则更新 value"""
        # TODO: ① 算 hash 找到桶 ② 遍历桶，key 存在则更新 ③ 不存在则 append
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i,(k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key,value)
                return
        bucket.append((key,value))

    def get(self, key):
        """取值，key 不存在返回 None"""
        # TODO
        idx = self._hash(key)
        for k,v in buckets[idx]:
            if k == key:
                return v
        return None

    def remove(self, key):
        """删除键值对，key 不存在则什么都不做"""
        # TODO
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i,(k,v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return

    def contains(self, key):
        """判断 key 是否存在，返回 True/False"""
        # TODO
        idx = self._hash(key)
        for k,v in self.buckets[idx]:
            if k == key:
                return True
        return False

    def keys(self):
        """返回所有 key 的列表"""
        # TODO
        result = []
        for bucket in self.buckets:
            for k,v in bucket:
                result.append(k)
        return result

    def __str__(self):
        """打印哈希表：每行一个桶"""
        # TODO: 格式如 "Bucket 0: [(key, val), ...]"
        lines = []
        for i, bucket in enumerate(self.buckets):
            if bucket:
                lines.append(f"Bucket {i}:{bucket}")
        return "\n".join(lines) if lines else "(空哈希表)"


# ============================================================
# 第二部分：LeetCode 1 — 两数之和
# ============================================================

def two_sum(nums, target):
    """
    给定整数数组 nums 和目标值 target，返回和为 target 的两个数的下标。

    示例:
    >>> two_sum([2, 7, 11, 15], 9)
    [0, 1]
    >>> two_sum([3, 2, 4], 6)
    [1, 2]

    要求: O(n) 时间，用 dict（哈希表）一次遍历完成。
    思路: 遍历时，查 target - 当前值 是否已经在 dict 里。
    """
    # TODO
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# ============================================================
# 测试代码（写完实现后运行）
# ============================================================

if __name__ == '__main__':
    # 测试 HashMap
    print("=" * 40)
    print("测试 HashMap")
    print("=" * 40)
    h = HashMap()
    h.put("name", "阿米娅")
    h.put("race", "卡特斯")
    h.put("class", "术师")
    h.put("origin", "罗德岛")
    print("put 4 个键值对后:")
    print(h)
    print(f"get('name'): {h.get('name')}")          # 阿米娅
    print(f"get('race'): {h.get('race')}")          # 卡特斯
    print(f"contains('class'): {h.contains('class')}")  # True
    print(f"contains('weapon'): {h.contains('weapon')}") # False
    print(f"keys(): {h.keys()}")

    h.put("name", "博士")  # 更新
    print(f"更新后 get('name'): {h.get('name')}")    # 博士

    h.remove("race")
    print(f"删除 race 后 contains('race'): {h.contains('race')}")  # False
    print("最终哈希表:")
    print(h)

    # 测试碰撞：选两个 hash 值相同的 key
    print("=" * 40)
    print("测试哈希碰撞")
    print("=" * 40)
    h2 = HashMap(size=3)
    # "ab" 和 "ba" 的 ord 和相同 → 同一个桶
    h2.put("ab", "第一个")
    h2.put("ba", "第二个")
    print(h2)
    print(f"get('ab'): {h2.get('ab')}")  # 第一个
    print(f"get('ba'): {h2.get('ba')}")  # 第二个（碰撞后仍能正确取值）

    # 测试 LeetCode 1
    print("=" * 40)
    print("测试 LeetCode 1 — 两数之和")
    print("=" * 40)
    result1 = two_sum([2, 7, 11, 15], 9)
    print(f"two_sum([2,7,11,15], 9) = {result1}")  # [0, 1]
    result2 = two_sum([3, 2, 4], 6)
    print(f"two_sum([3,2,4], 6) = {result2}")       # [1, 2]
    result3 = two_sum([3, 3], 6)
    print(f"two_sum([3,3], 6) = {result3}")         # [0, 1]
