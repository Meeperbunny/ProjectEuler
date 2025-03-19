def find_centroids(n, adj):
    deg = [len(adj[u]) for u in range(n)]
    leaves = [u for u in range(n) if deg[u] <= 1]
    remaining = n
    while remaining > 2:
        new_leaves = []
        remaining -= len(leaves)
        for leaf in leaves:
            deg[leaf] = 0
            for nei in adj[leaf]:
                if deg[nei] > 0:
                    deg[nei] -= 1
                    if deg[nei] == 1:
                        new_leaves.append(nei)
        leaves = new_leaves
    return leaves

def canonical_dfs(u, parent, adj):
    forms = []
    for v in adj[u]:
        if v != parent:
            forms.append(canonical_dfs(v, u, adj))
    forms.sort()
    return "(" + "".join(forms) + ")"

def canonical_form(n, edges):
    # Build adjacency
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a].append(b)
        adj[b].append(a)

    # Find centroid(s) and build the canonical parentheses form
    cents = find_centroids(n, adj)
    candidates = []
    for c in cents:
        candidates.append(canonical_dfs(c, -1, adj))
    return min(candidates)

def paren_to_tree(parens):
    """
    Converts a parenthesis representation into an edge list and number of nodes.
    """
    stack = []
    edges = []
    next_id = 0
    n = len(parens)//2  # number of nodes
    for ch in parens:
        if ch == '(':
            node = next_id
            next_id += 1
            if stack:
                parent = stack[-1]
                edges.append((parent, node))
            stack.append(node)
        elif ch == ')':
            stack.pop()
    return edges, n

def generate_unlabeled_trees_up_to(N):
    """
    Returns a list 'trees' of length N+1, where trees[n] is a list of
    canonical forms (strings) for all unlabeled trees on n nodes.
    """
    from tqdm import tqdm

    trees = [[] for _ in range(N+1)]
    if N < 3:
        return trees

    # Base case for n=3: the only (unlabeled) tree is the path 0--1--2
    base_canon = canonical_form(3, [(0,1), (1,2)])
    trees[3] = [base_canon]

    for cnt in range(4, N+1):
        print(f"Generating size={cnt} trees...")
        seen = set()
        for old_canon in trees[cnt - 1]:
            # Convert old canonical form back to edges
            old_edges, old_size = paren_to_tree(old_canon)

            # Attach a new node 'old_size' to each existing node in [0..old_size-1]
            for attach_point in range(old_size):
                new_edges = old_edges + [(old_size, attach_point)]
                # Get canonical form of the resulting bigger tree
                new_canon = canonical_form(cnt, new_edges)
                seen.add(new_canon)
        trees[cnt] = list(seen)

    return trees

if __name__ == "__main__":
    N = 20
    all_trees = generate_unlabeled_trees_up_to(N)

    # Now filter out any trees that have an edge with same-degree endpoints.
    total_valid = 0

    tv = []
    for n in range(3, N+1):
        count_for_n = 0
        for cform in all_trees[n]:
            # Convert parentheses -> edges
            edges, _ = paren_to_tree(cform)

            # Compute degrees
            deg = [0]*n
            for (u, v) in edges:
                deg[u] += 1
                deg[v] += 1

            # Check each edge for deg[u] == deg[v]
            invalid = False
            for (u, v) in edges:
                if deg[u] == deg[v]:
                    invalid = True
                    break

            if not invalid:
                count_for_n += 1

        print(f"n={n}: number of valid trees =", count_for_n)
        tv.append(str(count_for_n))
        total_valid += count_for_n

    print(",".join(tv))

    print("Overall valid trees across all n:", total_valid)
