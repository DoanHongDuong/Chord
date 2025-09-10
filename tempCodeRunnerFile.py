import hashlib

# ============ HÀM BĂM ==============
def hash_key(value, m):
    return int(hashlib.sha1(value.encode()).hexdigest(), 16) % (2 ** m)

# ============ HÀM TÌM SUCCESSOR ==========
def find_successor(key, sorted_nodes):
    for node in sorted_nodes:
        if node >= key:
            return node
    return sorted_nodes[0]  # quay vòng nếu vượt quá max ID

# ============ XÂY DỰNG FINGER TABLE ==========
def build_finger_table(nodes, m):
    finger_tables = {}
    sorted_nodes = sorted(nodes)
    for node in sorted_nodes:
        finger_tables[node] = []
        for i in range(m):
            start = (node + 2 ** i) % (2 ** m)
            successor = find_successor(start, sorted_nodes)
            finger_tables[node].append((start, successor))
    return finger_tables

# ============ TEST THUẬT TOÁN ==========
if __name__ == "__main__":
    # Định nghĩa thông số
    m = 4  # số bit
    nodes = [1, 5, 9, 12]
    sorted_nodes = sorted(nodes)

    # Xây dựng finger table
    finger_tables = build_finger_table(nodes, m)

    print("=== Finger Table ===")
    for node, table in finger_tables.items():
        print(f"\nNode {node}:")
        for i, (start, successor) in enumerate(table):
            print(f"  Finger {i+1}: start={start}, successor={successor}")

    # Test lookup
    keys = ["Huy", "An", "Lan", "Tuan"]
    print("\n=== Test Lookup Key ===")
    for key in keys:
        hashed_key = hash_key(key, m)
        successor = find_successor(hashed_key, sorted_nodes)
        print(f"Key {key} (hash={hashed_key}) -> Node {successor}")
