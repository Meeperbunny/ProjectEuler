maxn = 10**8

class TrieNode:
    def __init__(self):
        self.cnt = 0
        self.left = None
        self.right = None
        
def dfs(node, N):
    left_sum = 0
    right_sum = 0
    cnt = 0
    ma = 0
    if node.left or node.right:
        if node.left:
            cnt += node.left.cnt
            ma = max(ma, node.left.cnt)
            left_sum = dfs(node.left, N)
        if node.right:
            cnt += node.right.cnt
            ma = max(ma, node.right.cnt)
            right_sum = dfs(node.right, N)
    if not cnt:
        cnt += 1
    my_add = (ma * cnt) / (cnt * N)
#     print("Current Node has cnt", node.cnt, cnt, ma)
#     print("\tAdding", my_add)
    return my_add + left_sum + right_sum

print("Generating Sieve")
sieve = [True] * (maxn + 1)
primes = []
for i in range(2, maxn + 1):
    if sieve[i]:
        primes.append(i)
        for q in range(2 * i, maxn + 1, i):
            sieve[q] = False
print("Done With Sieve")

print("Constructing Trie")

root = TrieNode()

for p in primes:
    bstring = "".join(reversed("{0:b}".format(p)))
    curr = root
    curr.cnt += 1
    for c in bstring:
        if c == '0':
            if not curr.left:
                curr.left = TrieNode()
            curr = curr.left
        else:
            if not curr.right:
                curr.right = TrieNode()
            curr = curr.right
        curr.cnt += 1

print("Done Constructing Trie")
print("Traversing Trie")

print("Answer:", dfs(root, len(primes)))