import heapq

class LogisticsOptimizer:
    """
    A simple Dijkstra-based route optimizer for logistics planning.
    Calculates the shortest distance between distribution hubs.
    """
    def __init__(self):
        self.graph = {}

    def add_hub(self, hub, neighbors):
        # neighbors is a list of tuples: (neighbor_name, distance)
        self.graph[hub] = neighbors

    def find_shortest_path(self, start, end):
        queue = [(0, start, [])]
        visited = set()
        
        while queue:
            (cost, current, path) = heapq.heappop(queue)
            if current in visited:
                continue
            
            path = path + [current]
            visited.add(current)
            
            if current == end:
                return cost, path
            
            for neighbor, weight in self.graph.get(current, []):
                heapq.heappush(queue, (cost + weight, neighbor, path))
        return float("inf"), []

# --- Demonstration ---
if __name__ == "__main__":
    optimizer = LogisticsOptimizer()
    optimizer.add_hub("Austin", [("Dallas", 200), ("Houston", 160)])
    optimizer.add_hub("Dallas", [("Austin", 200), ("Oklahoma City", 180)])
    optimizer.add_hub("Houston", [("Austin", 160), ("San Antonio", 80)])
    optimizer.add_hub("San Antonio", [("Houston", 80), ("Oklahoma City", 350)])
    
    cost, path = optimizer.find_shortest_path("Austin", "Oklahoma City")
    print(f"Optimal Logistics Route: {' -> '.join(path)}")
    print(f"Total Distance: {cost} miles")
