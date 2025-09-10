def find_successor(key, sorted_nodes):
    for node in sorted_nodes:
        if node >= key:
            return node
    return sorted_nodes[0]  

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

if __name__ == "__main__":

    m = 4  
    nodes = [2, 6, 8, 13]
    sorted_nodes = sorted(nodes)

    finger_tables = build_finger_table(nodes, m)

    print("=== Finger Table ===")
    for node, table in finger_tables.items():
        print(f"\nNode {node}:")
        for i, (start, successor) in enumerate(table):
            print(f"  Finger {i+1}: start={start}, successor={successor}")

    keys = {
        "Dung": 9,
        "Duong": 12,
        "Nhung": 6,
        "Mai": 3,
        "Long": 14
    }

    print("\n=== Test Lookup Key ===")
    for key, key_id in keys.items():
        successor = find_successor(key_id, sorted_nodes)
        print(f"Key {key} (ID={key_id}) -> Node {successor}")
