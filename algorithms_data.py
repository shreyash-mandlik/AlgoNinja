# ================================
# AlgoNinja — All Algorithms Data
# ================================

algorithms = {

    # ================================
    # SEARCH ALGORITHMS
    # ================================
    "Search Algorithms": {

        "BFS": {
            "full_name": "Breadth First Search",
            "category": "Search",
            "difficulty": "Easy",
            "description": """
BFS explores all nodes at the present depth level before moving to nodes at the next depth level. It uses a **Queue** (FIFO) data structure.

**How it works:**
- Start at a source node
- Visit all neighbors at current level first
- Then move to next level
- Continue until goal is found or all nodes visited

**Key property:** BFS always finds the **shortest path** in an unweighted graph!

**Real world uses:**
- Facebook friend suggestions (nearest friends first)
- GPS Navigation shortest path
- Web crawlers
- Social network analysis
- Peer to peer networks (finding nearest peers)
            """,
            "pseudocode": """
BFS(graph, start):
    queue = [start]
    visited = {start}

    while queue not empty:
        node = queue.dequeue()
        process(node)

        for each neighbor of node:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
            """,
            "code": {
                "Python": """
from collections import deque

def bfs(graph, start):
    # Initialize visited set and queue
    visited = set([start])
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()  # dequeue from front
        result.append(node)

        # Visit all unvisited neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)  # enqueue to back

    return result

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}
print(bfs(graph, 'A'))
# Output: ['A', 'B', 'C', 'D', 'E', 'F']
                """,
                "C++": """
#include <iostream>
#include <queue>
#include <vector>
#include <unordered_set>
using namespace std;

void bfs(vector<vector<int>>& graph, int start) {
    unordered_set<int> visited;
    queue<int> q;

    q.push(start);
    visited.insert(start);

    while (!q.empty()) {
        int node = q.front();
        q.pop();
        cout << node << " ";

        for (int neighbor : graph[node]) {
            if (visited.find(neighbor) == visited.end()) {
                visited.insert(neighbor);
                q.push(neighbor);
            }
        }
    }
}
                """,
                "Java": """
import java.util.*;

public class BFS {
    public static void bfs(
        Map<Integer, List<Integer>> graph, int start) {

        Set<Integer> visited = new HashSet<>();
        Queue<Integer> queue = new LinkedList<>();

        queue.add(start);
        visited.add(start);

        while (!queue.isEmpty()) {
            int node = queue.poll();
            System.out.print(node + " ");

            for (int neighbor : graph.get(node)) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    queue.add(neighbor);
                }
            }
        }
    }
}
                """,
                "JavaScript": """
function bfs(graph, start) {
    const visited = new Set([start]);
    const queue = [start];
    const result = [];

    while (queue.length > 0) {
        const node = queue.shift(); // dequeue from front
        result.push(node);

        for (const neighbor of graph[node]) {
            if (!visited.has(neighbor)) {
                visited.add(neighbor);
                queue.push(neighbor);
            }
        }
    }
    return result;
}
                """
            },
            "time_complexity": "O(V + E)",
            "space_complexity": "O(V)",
            "best_case": "O(1)",
            "worst_case": "O(V + E)",
            "steps": [
                "Start at node A — add to queue. Queue: [A]",
                "Dequeue A — visit A. Add neighbors B, C. Queue: [B, C]",
                "Dequeue B — visit B. Add neighbors D, E. Queue: [C, D, E]",
                "Dequeue C — visit C. Add neighbor F. Queue: [D, E, F]",
                "Dequeue D — visit D. No unvisited neighbors. Queue: [E, F]",
                "Dequeue E — visit E. No unvisited neighbors. Queue: [F]",
                "Dequeue F — visit F. Queue empty — BFS complete! ✅"
            ],
            "quiz": [
                {
                    "question": "What data structure does BFS use?",
                    "options": ["Stack", "Queue", "Heap", "Tree"],
                    "answer": "Queue"
                },
                {
                    "question": "What is the time complexity of BFS?",
                    "options": ["O(V)", "O(E)", "O(V+E)", "O(V*E)"],
                    "answer": "O(V+E)"
                },
                {
                    "question": "BFS finds the shortest path in?",
                    "options": ["Weighted graphs", "Unweighted graphs", "Both", "Neither"],
                    "answer": "Unweighted graphs"
                },
                {
                    "question": "BFS traversal order for a tree is?",
                    "options": ["Inorder", "Preorder", "Level order", "Postorder"],
                    "answer": "Level order"
                }
            ]
        },

        "DFS": {
            "full_name": "Depth First Search",
            "category": "Search",
            "difficulty": "Easy",
            "description": """
DFS explores as far as possible along each branch before backtracking. It uses a **Stack** (LIFO) or recursion.

**How it works:**
- Start at source node
- Go as deep as possible along one path
- Backtrack when no unvisited neighbors
- Continue until all nodes visited

**Key difference from BFS:**
- BFS = Level by level (wide)
- DFS = Branch by branch (deep)

**Real world uses:**
- Maze solving
- Topological sorting (scheduling)
- Detecting cycles in graphs
- Finding connected components
- File system traversal
- Solving puzzles with backtracking
            """,
            "pseudocode": """
DFS(graph, start):
    stack = [start]
    visited = {}

    while stack not empty:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            process(node)
            for each neighbor of node:
                stack.push(neighbor)
            """,
            "code": {
                "Python": """
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    result = [start]

    # Recursively visit all unvisited neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            result += dfs(graph, neighbor, visited)

    return result

# Iterative version using stack
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()  # pop from top
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return result

# Example
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}
print(dfs(graph, 'A'))
# Output: ['A', 'B', 'D', 'E', 'C', 'F']
                """,
                "C++": """
#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

void dfs(vector<vector<int>>& graph,
         int node, unordered_set<int>& visited) {
    visited.insert(node);
    cout << node << " ";

    for (int neighbor : graph[node]) {
        if (visited.find(neighbor) == visited.end()) {
            dfs(graph, neighbor, visited);
        }
    }
}
                """,
                "Java": """
import java.util.*;

public class DFS {
    public static void dfs(
        Map<Integer, List<Integer>> graph,
        int node, Set<Integer> visited) {

        visited.add(node);
        System.out.print(node + " ");

        for (int neighbor : graph.get(node)) {
            if (!visited.contains(neighbor)) {
                dfs(graph, neighbor, visited);
            }
        }
    }
}
                """,
                "JavaScript": """
function dfs(graph, start, visited = new Set()) {
    visited.add(start);
    const result = [start];

    for (const neighbor of graph[start]) {
        if (!visited.has(neighbor)) {
            result.push(...dfs(graph, neighbor, visited));
        }
    }
    return result;
}
                """
            },
            "time_complexity": "O(V + E)",
            "space_complexity": "O(V)",
            "best_case": "O(1)",
            "worst_case": "O(V + E)",
            "steps": [
                "Start at A — push to stack. Stack: [A]",
                "Pop A — visit A. Push neighbors C, B. Stack: [C, B]",
                "Pop B — visit B. Push neighbors E, D. Stack: [C, E, D]",
                "Pop D — visit D. No neighbors. Stack: [C, E]",
                "Pop E — visit E. No neighbors. Stack: [C]",
                "Pop C — visit C. Push neighbor F. Stack: [F]",
                "Pop F — visit F. Stack empty — DFS complete! ✅"
            ],
            "quiz": [
                {
                    "question": "What data structure does DFS use?",
                    "options": ["Queue", "Stack", "Heap", "Array"],
                    "answer": "Stack"
                },
                {
                    "question": "DFS can be implemented using?",
                    "options": ["Iteration only", "Recursion only", "Both", "Neither"],
                    "answer": "Both"
                },
                {
                    "question": "Which is NOT a use case of DFS?",
                    "options": ["Maze solving", "Shortest path in unweighted graph", "Cycle detection", "Topological sort"],
                    "answer": "Shortest path in unweighted graph"
                },
                {
                    "question": "DFS uses which traversal strategy?",
                    "options": ["Level order", "Breadth first", "Depth first", "Random"],
                    "answer": "Depth first"
                }
            ]
        },

        "Binary Search": {
            "full_name": "Binary Search",
            "category": "Search",
            "difficulty": "Easy",
            "description": """
Binary Search finds an element in a **sorted array** by repeatedly dividing the search interval in half.

**How it works:**
- Compare target with middle element
- If equal — found!
- If target < middle — search left half
- If target > middle — search right half
- Repeat until found or interval empty

**Key requirement:** Array MUST be sorted!

**Why it's fast:**
- Each step eliminates HALF the remaining elements
- 1000 elements → max 10 comparisons!
- 1 million elements → max 20 comparisons!

**Real world uses:**
- Dictionary lookup
- Phone book search
- Database indexing
- Finding bugs (git bisect)
- Square root calculation
            """,
            "pseudocode": """
BinarySearch(arr, target):
    low = 0
    high = length(arr) - 1

    while low <= high:
        mid = (low + high) / 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  // not found
            """,
            "code": {
                "Python": """
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid          # found!
        elif arr[mid] < target:
            low = mid + 1       # search right half
        else:
            high = mid - 1      # search left half

    return -1  # not found

# Recursive version
def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid+1, high)
    else:
        return binary_search_recursive(arr, target, low, mid-1)

# Example
arr = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(arr, 7))   # Output: 3 (index)
print(binary_search(arr, 6))   # Output: -1 (not found)
                """,
                "C++": """
#include <iostream>
#include <vector>
using namespace std;

int binarySearch(vector<int>& arr, int target) {
    int low = 0, high = arr.size() - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}
                """,
                "Java": """
public class BinarySearch {
    public static int binarySearch(int[] arr, int target) {
        int low = 0, high = arr.length - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (arr[mid] == target) return mid;
            else if (arr[mid] < target) low = mid + 1;
            else high = mid - 1;
        }
        return -1;
    }
}
                """,
                "JavaScript": """
function binarySearch(arr, target) {
    let low = 0, high = arr.length - 1;

    while (low <= high) {
        const mid = Math.floor((low + high) / 2);

        if (arr[mid] === target) return mid;
        else if (arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}
                """
            },
            "time_complexity": "O(log n)",
            "space_complexity": "O(1)",
            "best_case": "O(1)",
            "worst_case": "O(log n)",
            "steps": [
                "Array: [1, 3, 5, 7, 9, 11, 13, 15], Target: 7",
                "low=0, high=7, mid=3. arr[3]=7 == target!",
                "Found at index 3! ✅",
                "Second example: Target=11",
                "low=0, high=7, mid=3. arr[3]=7 < 11 → search right",
                "low=4, high=7, mid=5. arr[5]=11 == target!",
                "Found at index 5! ✅"
            ],
            "quiz": [
                {
                    "question": "What is the time complexity of Binary Search?",
                    "options": ["O(n)", "O(log n)", "O(n log n)", "O(1)"],
                    "answer": "O(log n)"
                },
                {
                    "question": "Binary Search requires the array to be?",
                    "options": ["Unsorted", "Sorted", "Reversed", "Unique elements only"],
                    "answer": "Sorted"
                },
                {
                    "question": "How many comparisons to find element in 1024 elements?",
                    "options": ["1024", "512", "10", "100"],
                    "answer": "10"
                },
                {
                    "question": "Binary Search returns what when element not found?",
                    "options": ["0", "null", "-1", "undefined"],
                    "answer": "-1"
                }
            ]
        },

        "A* Search": {
            "full_name": "A* Search Algorithm",
            "category": "Search",
            "difficulty": "Hard",
            "description": """
A* (A-Star) is the most popular pathfinding algorithm. It finds the shortest path using a **heuristic function** to guide the search efficiently.

**The magic formula: f(n) = g(n) + h(n)**
- **g(n)** = actual cost from start to current node
- **h(n)** = estimated cost from current node to goal (heuristic)
- **f(n)** = total estimated cost of path through n

**Why A* beats Dijkstra:**
- Dijkstra explores ALL directions equally → slow
- A* uses heuristic to guide towards goal → fast!
- A* with h=0 becomes Dijkstra!

**Admissible heuristic:**
The heuristic must NEVER overestimate the true cost — otherwise A* won't find optimal path!

**Common heuristics:**
- Manhattan distance: |x1-x2| + |y1-y2| (grid movement)
- Euclidean distance: sqrt((x1-x2)² + (y1-y2)²) (any direction)

**Real world uses:**
- Google Maps / GPS navigation
- Video game pathfinding (NPCs avoiding obstacles)
- Robot navigation
- Network routing
            """,
            "pseudocode": """
AStar(start, goal, heuristic):
    open_set = PriorityQueue()
    open_set.put(start, f=0)

    g_score[start] = 0
    f_score[start] = heuristic(start, goal)

    while open_set not empty:
        current = open_set.get_min()

        if current == goal:
            return reconstruct_path()

        for neighbor of current:
            tentative_g = g_score[current] + cost(current, neighbor)

            if tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                open_set.put(neighbor, f_score[neighbor])
            """,
            "code": {
                "Python": """
import heapq

def astar(grid, start, goal):
    def heuristic(a, b):
        # Manhattan distance heuristic
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    # Priority queue: (f_score, node)
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        # Check all 4 directions
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            neighbor = (current[0]+dx, current[1]+dy)
            rows, cols = len(grid), len(grid[0])

            # Check bounds and walls
            if (0 <= neighbor[0] < rows and
                0 <= neighbor[1] < cols and
                grid[neighbor[0]][neighbor[1]] == 0):

                tentative_g = g_score[current] + 1

                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f, neighbor))

    return None  # No path found

# Example: 0=free, 1=wall
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
path = astar(grid, (0,0), (4,4))
print("Path:", path)
                """,
                "C++": """
#include <iostream>
#include <queue>
#include <vector>
#include <cmath>
using namespace std;

struct Node {
    int x, y, f, g;
    bool operator>(const Node& o) const {
        return f > o.f;
    }
};

int heuristic(int x1, int y1, int x2, int y2) {
    return abs(x1-x2) + abs(y1-y2);
}

void astar(vector<vector<int>>& grid,
           pair<int,int> start, pair<int,int> goal) {
    int rows = grid.size(), cols = grid[0].size();
    priority_queue<Node, vector<Node>, greater<Node>> pq;
    vector<vector<int>> g(rows, vector<int>(cols, INT_MAX));

    pq.push({start.first, start.second, 0, 0});
    g[start.first][start.second] = 0;

    int dx[] = {0,1,0,-1};
    int dy[] = {1,0,-1,0};

    while (!pq.empty()) {
        Node cur = pq.top(); pq.pop();

        if (cur.x==goal.first && cur.y==goal.second) {
            cout << "Path found!" << endl;
            return;
        }

        for (int i = 0; i < 4; i++) {
            int nx = cur.x+dx[i], ny = cur.y+dy[i];
            if (nx>=0 && nx<rows && ny>=0 && ny<cols
                && grid[nx][ny]==0) {
                int ng = cur.g + 1;
                if (ng < g[nx][ny]) {
                    g[nx][ny] = ng;
                    int h = heuristic(nx,ny,goal.first,goal.second);
                    pq.push({nx, ny, ng+h, ng});
                }
            }
        }
    }
}
                """,
                "Java": """
import java.util.*;

public class AStar {
    static int heuristic(int x1,int y1,int x2,int y2) {
        return Math.abs(x1-x2) + Math.abs(y1-y2);
    }

    public static void astar(int[][] grid,
                               int[] start, int[] goal) {
        int rows = grid.length, cols = grid[0].length;
        PriorityQueue<int[]> pq = new PriorityQueue<>(
            (a,b) -> a[4]-b[4]);
        int[][] gScore = new int[rows][cols];
        for (int[] row : gScore) Arrays.fill(row, Integer.MAX_VALUE);

        gScore[start[0]][start[1]] = 0;
        int h0 = heuristic(start[0],start[1],goal[0],goal[1]);
        pq.offer(new int[]{start[0],start[1],0,0,h0});

        int[] dx = {0,1,0,-1}, dy = {1,0,-1,0};

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            if (cur[0]==goal[0] && cur[1]==goal[1]) {
                System.out.println("Path found!");
                return;
            }
            for (int i=0; i<4; i++) {
                int nx=cur[0]+dx[i], ny=cur[1]+dy[i];
                if (nx>=0&&nx<rows&&ny>=0&&ny<cols&&grid[nx][ny]==0) {
                    int ng = cur[2]+1;
                    if (ng < gScore[nx][ny]) {
                        gScore[nx][ny] = ng;
                        int h = heuristic(nx,ny,goal[0],goal[1]);
                        pq.offer(new int[]{nx,ny,ng,ng,ng+h});
                    }
                }
            }
        }
    }
}
                """,
                "JavaScript": """
function astar(grid, start, goal) {
    const heuristic = (a, b) =>
        Math.abs(a[0]-b[0]) + Math.abs(a[1]-b[1]);

    const key = p => p.join(',');
    const openSet = [[0, start]];
    const gScore = new Map([[key(start), 0]]);
    const cameFrom = new Map();

    while (openSet.length > 0) {
        openSet.sort((a,b) => a[0]-b[0]);
        const [, current] = openSet.shift();

        if (current[0]===goal[0] && current[1]===goal[1]) {
            const path = [];
            let cur = current;
            while (cameFrom.has(key(cur))) {
                path.unshift(cur);
                cur = cameFrom.get(key(cur));
            }
            return path;
        }

        for (const [dx,dy] of [[0,1],[1,0],[0,-1],[-1,0]]) {
            const nb = [current[0]+dx, current[1]+dy];
            if (nb[0]>=0 && nb[0]<grid.length &&
                nb[1]>=0 && nb[1]<grid[0].length &&
                grid[nb[0]][nb[1]]===0) {
                const ng = (gScore.get(key(current))||0) + 1;
                if (ng < (gScore.get(key(nb))||Infinity)) {
                    cameFrom.set(key(nb), current);
                    gScore.set(key(nb), ng);
                    openSet.push([ng+heuristic(nb,goal), nb]);
                }
            }
        }
    }
    return null;
}
                """
            },
            "time_complexity": "O(E log V)",
            "space_complexity": "O(V)",
            "best_case": "O(1)",
            "worst_case": "O(E log V)",
            "steps": [
                "Start (0,0): g=0, h=8, f=8. Add to open set",
                "Expand (0,0): check neighbors. Best is (1,0) with f=8",
                "Expand (1,0): wall at (1,1),(1,2),(1,3) — blocked!",
                "Go around wall: (2,0),(2,1),(2,2) — f getting smaller",
                "Continue navigating around walls towards goal",
                "Each step picks node with lowest f score",
                "Reach (4,4) — reconstruct path! ✅"
            ],
            "quiz": [
                {
                    "question": "What does f(n) = g(n) + h(n) represent?",
                    "options": [
                        "f=speed, g=distance, h=height",
                        "f=total estimated cost, g=actual cost, h=heuristic",
                        "f=final node, g=goal, h=hops",
                        "f=frontier, g=graph, h=history"
                    ],
                    "answer": "f=total estimated cost, g=actual cost, h=heuristic"
                },
                {
                    "question": "A* with h=0 becomes which algorithm?",
                    "options": ["BFS", "DFS", "Dijkstra", "Greedy"],
                    "answer": "Dijkstra"
                },
                {
                    "question": "Which heuristic is used for grid movement?",
                    "options": ["Euclidean", "Manhattan", "Chebyshev", "Minkowski"],
                    "answer": "Manhattan"
                },
                {
                    "question": "What property must A* heuristic have?",
                    "options": ["Consistent", "Admissible (never overestimate)", "Monotonic", "Linear"],
                    "answer": "Admissible (never overestimate)"
                }
            ]
        },

        "Dijkstra": {
            "full_name": "Dijkstra's Shortest Path",
            "category": "Search",
            "difficulty": "Medium",
            "description": """
Dijkstra's algorithm finds the shortest path from a source node to all other nodes in a **weighted graph**.

**How it works:**
- Start with distance 0 to source, infinity to all others
- Always pick the unvisited node with minimum distance
- Update distances of its neighbors
- Repeat until all nodes visited

**Key limitation:**
Does NOT work with negative edge weights! Use Bellman-Ford instead.

**Why use a Priority Queue:**
Always processing the closest unvisited node makes it efficient — O(V² without PQ, O(E log V) with PQ)

**Real world uses:**
- Google Maps routing
- Network routing protocols (OSPF)
- Flight path optimization
- Telephone network routing
            """,
            "pseudocode": """
Dijkstra(graph, source):
    dist[source] = 0
    dist[all others] = infinity
    priority_queue = [(0, source)]

    while priority_queue not empty:
        (d, u) = priority_queue.pop_min()

        for each neighbor v of u:
            if dist[u] + weight(u,v) < dist[v]:
                dist[v] = dist[u] + weight(u,v)
                priority_queue.push((dist[v], v))

    return dist
            """,
            "code": {
                "Python": """
import heapq

def dijkstra(graph, source):
    # Initialize distances
    dist = {node: float('inf') for node in graph}
    dist[source] = 0

    # Priority queue: (distance, node)
    pq = [(0, source)]

    while pq:
        d, u = heapq.heappop(pq)

        # Skip if we found a better path already
        if d > dist[u]:
            continue

        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))

    return dist

# Example: {node: [(neighbor, weight), ...]}
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('D', 3), ('C', 1)],
    'C': [('B', 1), ('D', 5)],
    'D': []
}
distances = dijkstra(graph, 'A')
print(distances)
# {'A': 0, 'B': 3, 'C': 2, 'D': 6}
                """,
                "C++": """
#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

vector<int> dijkstra(vector<vector<pair<int,int>>>& graph,
                     int source, int n) {
    vector<int> dist(n, INT_MAX);
    priority_queue<pair<int,int>,
                   vector<pair<int,int>>,
                   greater<>> pq;

    dist[source] = 0;
    pq.push({0, source});

    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();

        if (d > dist[u]) continue;

        for (auto [v, w] : graph[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
    return dist;
}
                """,
                "Java": """
import java.util.*;

public class Dijkstra {
    public static int[] dijkstra(
        List<List<int[]>> graph, int source) {

        int n = graph.size();
        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[source] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>(
            (a,b) -> a[0]-b[0]);
        pq.offer(new int[]{0, source});

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int d = curr[0], u = curr[1];

            if (d > dist[u]) continue;

            for (int[] edge : graph.get(u)) {
                int v = edge[0], w = edge[1];
                if (dist[u]+w < dist[v]) {
                    dist[v] = dist[u]+w;
                    pq.offer(new int[]{dist[v], v});
                }
            }
        }
        return dist;
    }
}
                """,
                "JavaScript": """
function dijkstra(graph, source) {
    const dist = {};
    for (const node in graph) dist[node] = Infinity;
    dist[source] = 0;

    const pq = [[0, source]];

    while (pq.length > 0) {
        pq.sort((a,b) => a[0]-b[0]);
        const [d, u] = pq.shift();

        if (d > dist[u]) continue;

        for (const [v, w] of graph[u]) {
            if (dist[u]+w < dist[v]) {
                dist[v] = dist[u]+w;
                pq.push([dist[v], v]);
            }
        }
    }
    return dist;
}
                """
            },
            "time_complexity": "O(E log V)",
            "space_complexity": "O(V)",
            "best_case": "O(E log V)",
            "worst_case": "O(E log V)",
            "steps": [
                "Init: dist[A]=0, dist[B]=∞, dist[C]=∞, dist[D]=∞",
                "Process A (dist=0): Update B=4, C=2",
                "Process C (dist=2, minimum): Update B=3, D=7",
                "Process B (dist=3): Update D=6",
                "Process D (dist=6): No neighbors to update",
                "Final distances: A=0, B=3, C=2, D=6 ✅"
            ],
            "quiz": [
                {
                    "question": "Dijkstra does NOT work with?",
                    "options": ["Weighted graphs", "Negative weights", "Directed graphs", "Large graphs"],
                    "answer": "Negative weights"
                },
                {
                    "question": "What data structure makes Dijkstra efficient?",
                    "options": ["Stack", "Queue", "Priority Queue", "Array"],
                    "answer": "Priority Queue"
                },
                {
                    "question": "Time complexity with Priority Queue?",
                    "options": ["O(V²)", "O(E log V)", "O(V log V)", "O(E²)"],
                    "answer": "O(E log V)"
                },
                {
                    "question": "Dijkstra finds shortest path from?",
                    "options": ["One source to one destination", "One source to all nodes", "All nodes to all nodes", "Two nodes only"],
                    "answer": "One source to all nodes"
                }
            ]
        },

        "Greedy Best First": {
            "full_name": "Greedy Best First Search",
            "category": "Search",
            "difficulty": "Medium",
            "description": """
Greedy Best First Search always expands the node that appears closest to the goal using a heuristic function. It's called greedy because it always makes the locally optimal choice.

**How it differs from A*:**
- Greedy Best First: f(n) = h(n) only (heuristic only)
- A*: f(n) = g(n) + h(n) (actual + heuristic)
- Greedy is faster but NOT guaranteed to find shortest path!
- A* is slower but ALWAYS finds shortest path

**When to use Greedy:**
- When speed matters more than optimality
- Large search spaces where approximate solution is okay
- Game AI where close enough is good enough

**Real world uses:**
- Game NPC movement
- Approximate pathfinding
- Quick navigation estimates
            """,
            "pseudocode": """
GreedyBestFirst(start, goal, heuristic):
    open_set = PriorityQueue()
    open_set.put(start, heuristic(start, goal))
    visited = {}

    while open_set not empty:
        current = open_set.get_min()

        if current == goal:
            return path

        visited.add(current)

        for neighbor of current:
            if neighbor not in visited:
                h = heuristic(neighbor, goal)
                open_set.put(neighbor, h)
            """,
            "code": {
                "Python": """
import heapq

def greedy_best_first(grid, start, goal):
    def heuristic(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    open_set = [(heuristic(start, goal), start)]
    visited = set()
    came_from = {}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        visited.add(current)

        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            neighbor = (current[0]+dx, current[1]+dy)
            rows, cols = len(grid), len(grid[0])

            if (0 <= neighbor[0] < rows and
                0 <= neighbor[1] < cols and
                grid[neighbor[0]][neighbor[1]] == 0 and
                neighbor not in visited):

                came_from[neighbor] = current
                h = heuristic(neighbor, goal)
                heapq.heappush(open_set, (h, neighbor))

    return None

# Example
grid = [[0]*5 for _ in range(5)]
grid[1][1] = grid[1][2] = grid[1][3] = 1  # wall
path = greedy_best_first(grid, (0,0), (4,4))
print("Path:", path)
                """,
                "C++": """
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int heuristic(int x1,int y1,int x2,int y2) {
    return abs(x1-x2)+abs(y1-y2);
}

void greedyBFS(vector<vector<int>>& grid,
               pair<int,int> start, pair<int,int> goal) {
    int rows=grid.size(), cols=grid[0].size();
    priority_queue<pair<int,pair<int,int>>,
                   vector<pair<int,pair<int,int>>>,
                   greater<>> pq;
    vector<vector<bool>> visited(rows,vector<bool>(cols,false));

    pq.push({heuristic(start.first,start.second,
                       goal.first,goal.second), start});

    while (!pq.empty()) {
        auto [h, cur] = pq.top(); pq.pop();
        auto [x, y] = cur;

        if (x==goal.first && y==goal.second) {
            cout << "Goal reached!" << endl;
            return;
        }

        visited[x][y] = true;
        int dx[]={0,1,0,-1}, dy[]={1,0,-1,0};

        for (int i=0; i<4; i++) {
            int nx=x+dx[i], ny=y+dy[i];
            if (nx>=0&&nx<rows&&ny>=0&&ny<cols&&
                !grid[nx][ny]&&!visited[nx][ny]) {
                pq.push({heuristic(nx,ny,
                    goal.first,goal.second),{nx,ny}});
            }
        }
    }
}
                """,
                "Java": """
import java.util.*;

public class GreedyBFS {
    static int heuristic(int x1,int y1,int x2,int y2){
        return Math.abs(x1-x2)+Math.abs(y1-y2);
    }

    public static void greedyBFS(int[][] grid,
                                   int[] start, int[] goal) {
        int rows=grid.length, cols=grid[0].length;
        PriorityQueue<int[]> pq=new PriorityQueue<>(
            (a,b)->a[2]-b[2]);
        boolean[][] visited=new boolean[rows][cols];

        pq.offer(new int[]{start[0],start[1],
            heuristic(start[0],start[1],goal[0],goal[1])});

        int[] dx={0,1,0,-1}, dy={1,0,-1,0};

        while (!pq.isEmpty()) {
            int[] cur=pq.poll();
            if (cur[0]==goal[0]&&cur[1]==goal[1]) {
                System.out.println("Goal reached!");
                return;
            }
            visited[cur[0]][cur[1]]=true;
            for (int i=0;i<4;i++) {
                int nx=cur[0]+dx[i],ny=cur[1]+dy[i];
                if (nx>=0&&nx<rows&&ny>=0&&ny<cols&&
                    grid[nx][ny]==0&&!visited[nx][ny]) {
                    pq.offer(new int[]{nx,ny,
                        heuristic(nx,ny,goal[0],goal[1])});
                }
            }
        }
    }
}
                """,
                "JavaScript": """
function greedyBFS(grid, start, goal) {
    const h = (a,b) => Math.abs(a[0]-b[0])+Math.abs(a[1]-b[1]);
    const openSet = [[h(start,goal), start]];
    const visited = new Set();
    const cameFrom = new Map();
    const key = p => p.join(',');

    while (openSet.length > 0) {
        openSet.sort((a,b) => a[0]-b[0]);
        const [, current] = openSet.shift();

        if (current[0]===goal[0] && current[1]===goal[1]) {
            const path = [];
            let cur = current;
            while (cameFrom.has(key(cur))) {
                path.unshift(cur);
                cur = cameFrom.get(key(cur));
            }
            return path;
        }

        visited.add(key(current));

        for (const [dx,dy] of [[0,1],[1,0],[0,-1],[-1,0]]) {
            const nb = [current[0]+dx, current[1]+dy];
            if (nb[0]>=0&&nb[0]<grid.length&&
                nb[1]>=0&&nb[1]<grid[0].length&&
                grid[nb[0]][nb[1]]===0&&
                !visited.has(key(nb))) {
                cameFrom.set(key(nb), current);
                openSet.push([h(nb,goal), nb]);
            }
        }
    }
    return null;
}
                """
            },
            "time_complexity": "O(E log V)",
            "space_complexity": "O(V)",
            "best_case": "O(1)",
            "worst_case": "O(E log V)",
            "steps": [
                "Start (0,0): h=8. Add to open set",
                "Expand (0,0): neighbors → pick lowest h",
                "Move towards goal greedily — always pick closest",
                "May go wrong way if wall blocks direct path",
                "NOT guaranteed shortest — just fastest exploration",
                "Reaches goal quickly but path may not be optimal!",
                "Compare: A* finds optimal, Greedy finds fast ✅"
            ],
            "quiz": [
                {
                    "question": "Greedy Best First uses which value to pick next node?",
                    "options": ["g(n) only", "h(n) only", "g(n)+h(n)", "random"],
                    "answer": "h(n) only"
                },
                {
                    "question": "Is Greedy Best First guaranteed to find shortest path?",
                    "options": ["Yes always", "No", "Only in trees", "Only with admissible heuristic"],
                    "answer": "No"
                },
                {
                    "question": "Greedy Best First is faster than A* because?",
                    "options": ["It uses better heuristic", "It ignores actual path cost", "It uses BFS", "It uses DFS"],
                    "answer": "It ignores actual path cost"
                },
                {
                    "question": "When is Greedy Best First preferred over A*?",
                    "options": ["When optimal path is needed", "When speed matters more than optimality", "Always", "Never"],
                    "answer": "When speed matters more than optimality"
                }
            ]
        },
    },

    # ================================
    # SORTING ALGORITHMS
    # ================================
    "Sorting Algorithms": {

        "Bubble Sort": {
            "full_name": "Bubble Sort",
            "category": "Sorting",
            "difficulty": "Easy",
            "description": """
Bubble Sort repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. Larger elements "bubble up" to the end.

**How it works:**
- Compare adjacent pairs
- Swap if out of order
- After each pass, largest unsorted element is at correct position
- Repeat n-1 times

**Optimization:**
If no swaps in a pass — array is sorted! Break early.
This makes best case O(n) for nearly sorted arrays.

**Why learn Bubble Sort:**
- Simplest sorting algorithm to understand
- Good for teaching swap operations
- Useful for nearly sorted small arrays

**Real world uses:**
- Educational purposes
- Detecting nearly sorted data
- Simple embedded systems with small datasets
            """,
            "pseudocode": """
BubbleSort(arr):
    n = length(arr)
    for i = 0 to n-1:
        swapped = false
        for j = 0 to n-i-2:
            if arr[j] > arr[j+1]:
                swap(arr[j], arr[j+1])
                swapped = true
        if not swapped:
            break  // already sorted!
    return arr
            """,
            "code": {
                "Python": """
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # If no swap occurred, array is sorted
        if not swapped:
            break

    return arr

# Example
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))
# Output: [11, 12, 22, 25, 34, 64, 90]
                """,
                "C++": """
#include <iostream>
#include <vector>
using namespace std;

void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n-1; i++) {
        bool swapped = false;
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                swap(arr[j], arr[j+1]);
                swapped = true;
            }
        }
        if (!swapped) break; // already sorted
    }
}
                """,
                "Java": """
public class BubbleSort {
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n-1; i++) {
            boolean swapped = false;
            for (int j = 0; j < n-i-1; j++) {
                if (arr[j] > arr[j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                    swapped = true;
                }
            }
            if (!swapped) break;
        }
    }
}
                """,
                "JavaScript": """
function bubbleSort(arr) {
    const n = arr.length;
    for (let i = 0; i < n-1; i++) {
        let swapped = false;
        for (let j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                [arr[j], arr[j+1]] = [arr[j+1], arr[j]];
                swapped = true;
            }
        }
        if (!swapped) break;
    }
    return arr;
}
                """
            },
            "time_complexity": "O(n²)",
            "space_complexity": "O(1)",
            "best_case": "O(n)",
            "worst_case": "O(n²)",
            "steps": [
                "Array: [64, 34, 25, 12, 22]",
                "Pass 1: Compare 64,34 → swap → [34, 64, 25, 12, 22]",
                "Pass 1: Compare 64,25 → swap → [34, 25, 64, 12, 22]",
                "Pass 1: Compare 64,12 → swap → [34, 25, 12, 64, 22]",
                "Pass 1: Compare 64,22 → swap → [34, 25, 12, 22, 64]",
                "64 is now in correct position!",
                "Repeat for remaining elements → [12, 22, 25, 34, 64] ✅"
            ],
            "quiz": [
                {
                    "question": "Worst case time complexity of Bubble Sort?",
                    "options": ["O(n)", "O(n log n)", "O(n²)", "O(log n)"],
                    "answer": "O(n²)"
                },
                {
                    "question": "Best case of optimized Bubble Sort?",
                    "options": ["O(n²)", "O(n log n)", "O(n)", "O(1)"],
                    "answer": "O(n)"
                },
                {
                    "question": "Space complexity of Bubble Sort?",
                    "options": ["O(n)", "O(n²)", "O(log n)", "O(1)"],
                    "answer": "O(1)"
                },
                {
                    "question": "Is Bubble Sort stable?",
                    "options": ["Yes", "No", "Depends", "Only for integers"],
                    "answer": "Yes"
                }
            ]
        },

        "Selection Sort": {
            "full_name": "Selection Sort",
            "category": "Sorting",
            "difficulty": "Easy",
            "description": """
Selection Sort finds the minimum element from the unsorted portion and places it at the beginning. It divides the array into sorted and unsorted portions.

**How it works:**
- Find minimum in unsorted portion
- Swap it with first unsorted element
- Move sorted boundary one step right
- Repeat until fully sorted

**Comparison with Bubble Sort:**
- Both are O(n²) but Selection Sort does fewer swaps
- Bubble Sort: O(n²) swaps in worst case
- Selection Sort: O(n) swaps always!
- Selection Sort is better when memory writes are costly

**Real world uses:**
- When memory writes are expensive
- Small arrays
- Simple embedded systems
            """,
            "pseudocode": """
SelectionSort(arr):
    n = length(arr)
    for i = 0 to n-1:
        min_idx = i
        for j = i+1 to n:
            if arr[j] < arr[min_idx]:
                min_idx = j
        swap(arr[i], arr[min_idx])
    return arr
            """,
            "code": {
                "Python": """
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Find minimum in unsorted portion
        min_idx = i

        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap minimum with first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

# Example
arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))
# Output: [11, 12, 22, 25, 64]
                """,
                "C++": """
#include <iostream>
#include <vector>
using namespace std;

void selectionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n-1; i++) {
        int min_idx = i;
        for (int j = i+1; j < n; j++) {
            if (arr[j] < arr[min_idx])
                min_idx = j;
        }
        swap(arr[i], arr[min_idx]);
    }
}
                """,
                "Java": """
public class SelectionSort {
    public static void selectionSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n-1; i++) {
            int min_idx = i;
            for (int j = i+1; j < n; j++) {
                if (arr[j] < arr[min_idx])
                    min_idx = j;
            }
            int temp = arr[min_idx];
            arr[min_idx] = arr[i];
            arr[i] = temp;
        }
    }
}
                """,
                "JavaScript": """
function selectionSort(arr) {
    const n = arr.length;
    for (let i = 0; i < n-1; i++) {
        let minIdx = i;
        for (let j = i+1; j < n; j++) {
            if (arr[j] < arr[minIdx]) minIdx = j;
        }
        [arr[i], arr[minIdx]] = [arr[minIdx], arr[i]];
    }
    return arr;
}
                """
            },
            "time_complexity": "O(n²)",
            "space_complexity": "O(1)",
            "best_case": "O(n²)",
            "worst_case": "O(n²)",
            "steps": [
                "Array: [64, 25, 12, 22, 11]",
                "Pass 1: Find min=11 at index 4. Swap with index 0 → [11, 25, 12, 22, 64]",
                "Pass 2: Find min=12 at index 2. Swap with index 1 → [11, 12, 25, 22, 64]",
                "Pass 3: Find min=22 at index 3. Swap with index 2 → [11, 12, 22, 25, 64]",
                "Pass 4: Find min=25 at index 3. Already in place!",
                "Array fully sorted: [11, 12, 22, 25, 64] ✅"
            ],
            "quiz": [
                {
                    "question": "Time complexity of Selection Sort in ALL cases?",
                    "options": ["O(n)", "O(n log n)", "O(n²)", "O(log n)"],
                    "answer": "O(n²)"
                },
                {
                    "question": "Selection Sort advantage over Bubble Sort?",
                    "options": ["Faster", "Fewer swaps (O(n) swaps)", "More stable", "Less memory"],
                    "answer": "Fewer swaps (O(n) swaps)"
                },
                {
                    "question": "Is Selection Sort stable?",
                    "options": ["Yes always", "No", "Depends on implementation", "Only for strings"],
                    "answer": "No"
                },
                {
                    "question": "Selection Sort is best when?",
                    "options": ["Large datasets", "Memory writes are expensive", "Nearly sorted data", "Random data"],
                    "answer": "Memory writes are expensive"
                }
            ]
        },

        "Insertion Sort": {
            "full_name": "Insertion Sort",
            "category": "Sorting",
            "difficulty": "Easy",
            "description": """
Insertion Sort builds the sorted array one element at a time by inserting each element into its correct position — like sorting playing cards in your hand!

**How it works:**
- Start with second element
- Compare with previous elements
- Shift larger elements right
- Insert current element in correct position
- Repeat for all elements

**Why Insertion Sort is special:**
- Excellent for small or nearly sorted arrays!
- Online algorithm — can sort as data arrives
- O(n) for nearly sorted data
- Used in practice for small subarrays (Timsort uses it!)

**Real world uses:**
- Sorting playing cards
- Online sorting (real-time data)
- Small arrays in hybrid algorithms (Timsort)
- Nearly sorted data
            """,
            "pseudocode": """
InsertionSort(arr):
    for i = 1 to n-1:
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]  // shift right
            j = j - 1

        arr[j+1] = key  // insert at correct position
    return arr
            """,
            "code": {
                "Python": """
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # element to insert
        j = i - 1

        # Shift elements larger than key to the right
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        # Insert key at correct position
        arr[j+1] = key

    return arr

# Example
arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr))
# Output: [5, 6, 11, 12, 13]
                """,
                "C++": """
#include <iostream>
#include <vector>
using namespace std;

void insertionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = key;
    }
}
                """,
                "Java": """
public class InsertionSort {
    public static void insertionSort(int[] arr) {
        int n = arr.length;
        for (int i = 1; i < n; i++) {
            int key = arr[i];
            int j = i - 1;

            while (j >= 0 && arr[j] > key) {
                arr[j+1] = arr[j];
                j--;
            }
            arr[j+1] = key;
        }
    }
}
                """,
                "JavaScript": """
function insertionSort(arr) {
    for (let i = 1; i < arr.length; i++) {
        const key = arr[i];
        let j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = key;
    }
    return arr;
}
                """
            },
            "time_complexity": "O(n²)",
            "space_complexity": "O(1)",
            "best_case": "O(n)",
            "worst_case": "O(n²)",
            "steps": [
                "Array: [12, 11, 13, 5, 6]",
                "i=1: key=11. Compare with 12 → shift. Insert 11 → [11, 12, 13, 5, 6]",
                "i=2: key=13. Compare with 12 → no shift. Insert 13 → [11, 12, 13, 5, 6]",
                "i=3: key=5. Shift 13,12,11 right. Insert 5 → [5, 11, 12, 13, 6]",
                "i=4: key=6. Shift 13,12,11 right. Insert 6 → [5, 6, 11, 12, 13]",
                "Array fully sorted! ✅"
            ],
            "quiz": [
                {
                    "question": "Best case time complexity of Insertion Sort?",
                    "options": ["O(n²)", "O(n log n)", "O(n)", "O(1)"],
                    "answer": "O(n)"
                },
                {
                    "question": "Insertion Sort is best for?",
                    "options": ["Large random data", "Nearly sorted small arrays", "Reverse sorted data", "All cases"],
                    "answer": "Nearly sorted small arrays"
                },
                {
                    "question": "Is Insertion Sort an online algorithm?",
                    "options": ["Yes — can sort as data arrives", "No", "Only for numbers", "Depends"],
                    "answer": "Yes — can sort as data arrives"
                },
                {
                    "question": "Which sorting algorithm is Insertion Sort similar to?",
                    "options": ["Sorting cards in hand", "Building a pyramid", "Counting objects", "Dividing groups"],
                    "answer": "Sorting cards in hand"
                }
            ]
        },

        "Merge Sort": {
            "full_name": "Merge Sort",
            "category": "Sorting",
            "difficulty": "Medium",
            "description": """
Merge Sort is a **divide and conquer** algorithm. It divides the array into halves, sorts each half recursively, then merges them.

**The 3 steps:**
1. **Divide** — split array into two halves at midpoint
2. **Conquer** — recursively sort each half
3. **Combine** — merge two sorted halves by comparing elements

**Why Merge Sort is special:**
- Guaranteed O(n log n) in ALL cases — even worst case!
- Stable sort — equal elements maintain original order
- Perfect for linked lists (no random access needed)
- Foundation of external sorting

**Code explanation:**
- `merge_sort()` splits array recursively until size 1
- `merge()` combines two sorted arrays by comparing front elements
- Each merge step takes O(n) time
- log n merge steps → total O(n log n)

**Real world uses:**
- Python's Timsort (based on Merge Sort)
- Java's Arrays.sort() for objects
- Database external sorting
- Counting inversions
            """,
            "pseudocode": """
MergeSort(arr):
    if length(arr) <= 1: return arr

    mid = length(arr) / 2
    left = MergeSort(arr[0..mid])
    right = MergeSort(arr[mid..end])
    return Merge(left, right)

Merge(left, right):
    result = []
    while left and right not empty:
        if left[0] <= right[0]:
            result.append(left.pop_front())
        else:
            result.append(right.pop_front())
    return result + remaining elements
            """,
            "code": {
                "Python": """
def merge_sort(arr):
    # Base case: array of 0 or 1 elements is sorted
    if len(arr) <= 1:
        return arr

    # Divide: find midpoint
    mid = len(arr) // 2

    # Conquer: recursively sort both halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Combine: merge sorted halves
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # Compare elements from both halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result += left[i:]
    result += right[j:]
    return result

# Example
arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))
# Output: [3, 9, 10, 27, 38, 43, 82]
                """,
                "C++": """
#include <iostream>
#include <vector>
using namespace std;

void merge(vector<int>& arr, int l, int m, int r) {
    vector<int> temp;
    int i = l, j = m+1;

    while (i <= m && j <= r) {
        if (arr[i] <= arr[j]) temp.push_back(arr[i++]);
        else temp.push_back(arr[j++]);
    }
    while (i <= m) temp.push_back(arr[i++]);
    while (j <= r) temp.push_back(arr[j++]);

    for (int k = l; k <= r; k++)
        arr[k] = temp[k-l];
}

void mergeSort(vector<int>& arr, int l, int r) {
    if (l >= r) return;
    int m = (l+r)/2;
    mergeSort(arr, l, m);
    mergeSort(arr, m+1, r);
    merge(arr, l, m, r);
}
                """,
                "Java": """
public class MergeSort {
    public static void mergeSort(int[] arr, int l, int r) {
        if (l >= r) return;
        int m = (l+r)/2;
        mergeSort(arr, l, m);
        mergeSort(arr, m+1, r);
        merge(arr, l, m, r);
    }

    static void merge(int[] arr, int l, int m, int r) {
        int[] temp = new int[r-l+1];
        int i=l, j=m+1, k=0;
        while (i<=m && j<=r) {
            if (arr[i]<=arr[j]) temp[k++]=arr[i++];
            else temp[k++]=arr[j++];
        }
        while (i<=m) temp[k++]=arr[i++];
        while (j<=r) temp[k++]=arr[j++];
        for (int p=0; p<temp.length; p++)
            arr[l+p]=temp[p];
    }
}
                """,
                "JavaScript": """
function mergeSort(arr) {
    if (arr.length <= 1) return arr;
    const mid = Math.floor(arr.length/2);
    const left = mergeSort(arr.slice(0, mid));
    const right = mergeSort(arr.slice(mid));
    return merge(left, right);
}

function merge(left, right) {
    const result = [];
    let i=0, j=0;
    while (i<left.length && j<right.length) {
        if (left[i]<=right[j]) result.push(left[i++]);
        else result.push(right[j++]);
    }
    return result.concat(left.slice(i)).concat(right.slice(j));
}
                """
            },
            "time_complexity": "O(n log n)",
            "space_complexity": "O(n)",
            "best_case": "O(n log n)",
            "worst_case": "O(n log n)",
            "steps": [
                "Array: [38, 27, 43, 3, 9, 82, 10]",
                "Split: [38, 27, 43] | [3, 9, 82, 10]",
                "Split: [38] [27,43] | [3,9] [82,10]",
                "Sort [27,43]: compare 27<43 → [27,43]",
                "Merge [38] + [27,43] → [27,38,43]",
                "Merge [3,9] + [10,82] → [3,9,10,82]",
                "Final merge [27,38,43] + [3,9,10,82] → [3,9,10,27,38,43,82] ✅"
            ],
            "quiz": [
                {
                    "question": "Time complexity of Merge Sort in ALL cases?",
                    "options": ["O(n)", "O(n²)", "O(n log n)", "O(log n)"],
                    "answer": "O(n log n)"
                },
                {
                    "question": "Design technique used by Merge Sort?",
                    "options": ["Greedy", "Dynamic Programming", "Divide and Conquer", "Backtracking"],
                    "answer": "Divide and Conquer"
                },
                {
                    "question": "Is Merge Sort stable?",
                    "options": ["Yes", "No", "Depends on implementation", "Only for integers"],
                    "answer": "Yes"
                },
                {
                    "question": "Space complexity of Merge Sort?",
                    "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                    "answer": "O(n)"
                }
            ]
        },

        "Quick Sort": {
            "full_name": "Quick Sort",
            "category": "Sorting",
            "difficulty": "Medium",
            "description": """
Quick Sort picks a **pivot** element and partitions the array so all smaller elements go left, larger go right. Then recursively sorts both sides.

**The partition step is the KEY:**
- Choose pivot (last element, first, random, or median)
- Rearrange: elements < pivot go left, elements > pivot go right
- Pivot is now in its FINAL correct position
- Recursively sort left and right sub-arrays

**Why Quick Sort is popular:**
- Average O(n log n) — very fast in practice!
- In-place — O(log n) extra space only
- Cache friendly — works on contiguous memory
- Default sort in many standard libraries

**Worst case problem:**
If pivot is always min/max (sorted array) → O(n²)
**Fix:** Random pivot or median-of-three pivot selection

**Real world uses:**
- C's qsort() standard library
- Java's Arrays.sort() for primitives
- Most language standard libraries
            """,
            "pseudocode": """
QuickSort(arr, low, high):
    if low < high:
        pivot_idx = Partition(arr, low, high)
        QuickSort(arr, low, pivot_idx-1)
        QuickSort(arr, pivot_idx+1, high)

Partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j = low to high-1:
        if arr[j] <= pivot:
            i++
            swap(arr[i], arr[j])
    swap(arr[i+1], arr[high])
    return i+1
            """,
            "code": {
                "Python": """
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr)-1

    if low < high:
        # Partition and get pivot index
        pivot_idx = partition(arr, low, high)

        # Recursively sort both sides
        quick_sort(arr, low, pivot_idx-1)
        quick_sort(arr, pivot_idx+1, high)

    return arr

def partition(arr, low, high):
    pivot = arr[high]  # choose last as pivot
    i = low - 1        # index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in correct position
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

# Example
arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr)
print(arr)
# Output: [1, 5, 7, 8, 9, 10]
                """,
                "C++": """
#include <iostream>
#include <vector>
using namespace std;

int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = low-1;
    for (int j=low; j<high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i+1], arr[high]);
    return i+1;
}

void quickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi-1);
        quickSort(arr, pi+1, high);
    }
}
                """,
                "Java": """
public class QuickSort {
    static int partition(int[] arr, int low, int high) {
        int pivot=arr[high], i=low-1;
        for (int j=low; j<high; j++) {
            if (arr[j]<=pivot) {
                i++;
                int t=arr[i]; arr[i]=arr[j]; arr[j]=t;
            }
        }
        int t=arr[i+1]; arr[i+1]=arr[high]; arr[high]=t;
        return i+1;
    }

    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pi=partition(arr, low, high);
            quickSort(arr, low, pi-1);
            quickSort(arr, pi+1, high);
        }
    }
}
                """,
                "JavaScript": """
function quickSort(arr, low=0, high=arr.length-1) {
    if (low < high) {
        const pi = partition(arr, low, high);
        quickSort(arr, low, pi-1);
        quickSort(arr, pi+1, high);
    }
    return arr;
}

function partition(arr, low, high) {
    const pivot = arr[high];
    let i = low-1;
    for (let j=low; j<high; j++) {
        if (arr[j] <= pivot) {
            i++;
            [arr[i],arr[j]]=[arr[j],arr[i]];
        }
    }
    [arr[i+1],arr[high]]=[arr[high],arr[i+1]];
    return i+1;
}
                """
            },
            "time_complexity": "O(n log n)",
            "space_complexity": "O(log n)",
            "best_case": "O(n log n)",
            "worst_case": "O(n²)",
            "steps": [
                "Array: [10, 7, 8, 9, 1, 5], pivot=5",
                "Partition: 1 goes left of 5 → [1, 5, 10, 7, 8, 9]",
                "Pivot 5 is now in correct position!",
                "Left [1]: already sorted",
                "Right [10, 7, 8, 9], pivot=9",
                "Partition: [7, 8, 9, 10]",
                "Final: [1, 5, 7, 8, 9, 10] ✅"
            ],
            "quiz": [
                {
                    "question": "Worst case time complexity of Quick Sort?",
                    "options": ["O(n)", "O(n log n)", "O(n²)", "O(log n)"],
                    "answer": "O(n²)"
                },
                {
                    "question": "When does Quick Sort worst case occur?",
                    "options": ["Random data", "Already sorted data with bad pivot", "Reverse sorted", "All same elements"],
                    "answer": "Already sorted data with bad pivot"
                },
                {
                    "question": "Is Quick Sort stable?",
                    "options": ["Yes", "No", "Depends on implementation", "Only for integers"],
                    "answer": "No"
                },
                {
                    "question": "Space complexity of Quick Sort?",
                    "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                    "answer": "O(log n)"
                }
            ]
        },

        "Heap Sort": {
            "full_name": "Heap Sort",
            "category": "Sorting",
            "difficulty": "Medium",
            "description": """
Heap Sort uses a **Binary Heap** data structure to sort elements. It first builds a max-heap, then repeatedly extracts the maximum element.

**Two phases:**
1. **Build Max-Heap** — rearrange array into heap structure
2. **Extract & Sort** — repeatedly extract max, place at end

**What is a Max-Heap:**
- Complete binary tree
- Parent is always larger than children
- Root = maximum element
- Stored as array: parent at i, children at 2i+1 and 2i+2

**Heapify operation:**
Ensures heap property is maintained — O(log n)

**Why Heap Sort:**
- Guaranteed O(n log n) like Merge Sort
- In-place like Quick Sort (O(1) extra space)
- Not stable — equal elements may change order

**Real world uses:**
- Priority queues implementation
- OS job scheduling
- Finding k largest/smallest elements efficiently
            """,
            "pseudocode": """
HeapSort(arr):
    n = length(arr)

    // Phase 1: Build max-heap
    for i = n/2 - 1 down to 0:
        Heapify(arr, n, i)

    // Phase 2: Extract elements
    for i = n-1 down to 1:
        swap(arr[0], arr[i])  // move max to end
        Heapify(arr, i, 0)    // heapify reduced heap

Heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr[i], arr[largest])
        Heapify(arr, n, largest)
            """,
            "code": {
                "Python": """
def heap_sort(arr):
    n = len(arr)

    # Phase 1: Build max-heap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # Phase 2: Extract elements from heap
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # move max to end
        heapify(arr, i, 0)               # restore heap

    return arr

def heapify(arr, n, i):
    largest = i      # root
    left = 2*i + 1   # left child
    right = 2*i + 2  # right child

    # Check if left child is larger
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child is larger
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Swap and continue heapifying if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Example
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print(arr)
# Output: [5, 6, 7, 11, 12, 13]
                """,
                "C++": """
#include <iostream>
#include <vector>
using namespace std;

void heapify(vector<int>& arr, int n, int i) {
    int largest=i, left=2*i+1, right=2*i+2;
    if (left<n && arr[left]>arr[largest]) largest=left;
    if (right<n && arr[right]>arr[largest]) largest=right;
    if (largest!=i) {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

void heapSort(vector<int>& arr) {
    int n=arr.size();
    for (int i=n/2-1; i>=0; i--) heapify(arr, n, i);
    for (int i=n-1; i>0; i--) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}
                """,
                "Java": """
public class HeapSort {
    static void heapify(int[] arr, int n, int i) {
        int largest=i, l=2*i+1, r=2*i+2;
        if (l<n && arr[l]>arr[largest]) largest=l;
        if (r<n && arr[r]>arr[largest]) largest=r;
        if (largest!=i) {
            int t=arr[i]; arr[i]=arr[largest]; arr[largest]=t;
            heapify(arr, n, largest);
        }
    }

    public static void heapSort(int[] arr) {
        int n=arr.length;
        for (int i=n/2-1; i>=0; i--) heapify(arr,n,i);
        for (int i=n-1; i>0; i--) {
            int t=arr[0]; arr[0]=arr[i]; arr[i]=t;
            heapify(arr, i, 0);
        }
    }
}
                """,
                "JavaScript": """
function heapSort(arr) {
    const n = arr.length;
    for (let i=Math.floor(n/2)-1; i>=0; i--)
        heapify(arr, n, i);
    for (let i=n-1; i>0; i--) {
        [arr[0],arr[i]]=[arr[i],arr[0]];
        heapify(arr, i, 0);
    }
    return arr;
}

function heapify(arr, n, i) {
    let largest=i, l=2*i+1, r=2*i+2;
    if (l<n && arr[l]>arr[largest]) largest=l;
    if (r<n && arr[r]>arr[largest]) largest=r;
    if (largest!==i) {
        [arr[i],arr[largest]]=[arr[largest],arr[i]];
        heapify(arr, n, largest);
    }
}
                """
            },
            "time_complexity": "O(n log n)",
            "space_complexity": "O(1)",
            "best_case": "O(n log n)",
            "worst_case": "O(n log n)",
            "steps": [
                "Array: [12, 11, 13, 5, 6, 7]",
                "Build max-heap: [13, 11, 12, 5, 6, 7]",
                "Extract max 13, swap with last → [7, 11, 12, 5, 6, 13]",
                "Heapify: [12, 11, 7, 5, 6] → extract 12",
                "Continue extracting: 11, 7, 6, 5...",
                "Each extraction takes O(log n)",
                "Final sorted array: [5, 6, 7, 11, 12, 13] ✅"
            ],
            "quiz": [
                {
                    "question": "What data structure does Heap Sort use?",
                    "options": ["Stack", "Queue", "Binary Heap", "BST"],
                    "answer": "Binary Heap"
                },
                {
                    "question": "Time complexity of Heap Sort?",
                    "options": ["O(n)", "O(n²)", "O(n log n)", "O(log n)"],
                    "answer": "O(n log n)"
                },
                {
                    "question": "Is Heap Sort in-place?",
                    "options": ["Yes O(1) space", "No needs O(n)", "No needs O(log n)", "Depends"],
                    "answer": "Yes O(1) space"
                },
                {
                    "question": "In max-heap, where is the maximum element?",
                    "options": ["Last position", "Middle", "Root (index 0)", "Random"],
                    "answer": "Root (index 0)"
                }
            ]
        },
    },

    # ================================
    # GRAPH ALGORITHMS
    # ================================
    "Graph Algorithms": {

        "Floyd Warshall": {
            "full_name": "Floyd-Warshall Algorithm",
            "category": "Graph",
            "difficulty": "Medium",
            "description": """
Floyd-Warshall finds the shortest paths between **ALL pairs** of vertices in a weighted graph. It works with negative edges (but not negative cycles).

**How it works:**
- Uses dynamic programming with 3 nested loops
- For each intermediate vertex k, check if going through k gives shorter path
- dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

**Key difference from Dijkstra:**
- Dijkstra: one source to all destinations
- Floyd-Warshall: ALL sources to ALL destinations

**When to use:**
- Small dense graphs (V ≤ 500)
- Need all-pairs shortest paths
- Negative edges present (but no negative cycles)

**Detecting negative cycles:**
If dist[i][i] < 0 after running — negative cycle exists!

**Real world uses:**
- Network routing tables
- Finding transitive closure
- Detecting negative cycles
- City distance matrices
            """,
            "pseudocode": """
FloydWarshall(graph):
    dist = copy of adjacency matrix

    for k = 0 to V-1:
        for i = 0 to V-1:
            for j = 0 to V-1:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist
            """,
            "code": {
                "Python": """
def floyd_warshall(graph):
    V = len(graph)
    # Copy adjacency matrix
    dist = [row[:] for row in graph]

    # Try each vertex as intermediate
    for k in range(V):
        for i in range(V):
            for j in range(V):
                # Can we go i→k→j shorter than i→j?
                if (dist[i][k] != float('inf') and
                    dist[k][j] != float('inf') and
                    dist[i][k] + dist[k][j] < dist[i][j]):
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# Example: INF = no direct edge
INF = float('inf')
graph = [
    [0,   3,   INF, 7  ],
    [8,   0,   2,   INF],
    [5,   INF, 0,   1  ],
    [2,   INF, INF, 0  ]
]

dist = floyd_warshall(graph)
print("Shortest distances:")
for row in dist:
    print(row)
                """,
                "C++": """
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

void floydWarshall(vector<vector<int>>& dist) {
    int V = dist.size();
    for (int k=0; k<V; k++)
        for (int i=0; i<V; i++)
            for (int j=0; j<V; j++)
                if (dist[i][k]!=INT_MAX &&
                    dist[k][j]!=INT_MAX &&
                    dist[i][k]+dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k]+dist[k][j];
}
                """,
                "Java": """
public class FloydWarshall {
    static final int INF = Integer.MAX_VALUE/2;

    public static void floydWarshall(int[][] dist) {
        int V = dist.length;
        for (int k=0; k<V; k++)
            for (int i=0; i<V; i++)
                for (int j=0; j<V; j++)
                    if (dist[i][k]+dist[k][j] < dist[i][j])
                        dist[i][j] = dist[i][k]+dist[k][j];
    }
}
                """,
                "JavaScript": """
function floydWarshall(graph) {
    const V = graph.length;
    const dist = graph.map(row => [...row]);

    for (let k=0; k<V; k++)
        for (let i=0; i<V; i++)
            for (let j=0; j<V; j++)
                if (dist[i][k]+dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k]+dist[k][j];

    return dist;
}
                """
            },
            "time_complexity": "O(V³)",
            "space_complexity": "O(V²)",
            "best_case": "O(V³)",
            "worst_case": "O(V³)",
            "steps": [
                "Initialize dist matrix from adjacency matrix",
                "k=0 (vertex 0 as intermediate): update all i→0→j paths",
                "k=1 (vertex 1 as intermediate): update all i→1→j paths",
                "k=2 (vertex 2 as intermediate): update all i→2→j paths",
                "k=3 (vertex 3 as intermediate): update all i→3→j paths",
                "After all k iterations, dist[i][j] = shortest path i to j",
                "Check diagonal — if dist[i][i] < 0, negative cycle! ✅"
            ],
            "quiz": [
                {
                    "question": "Floyd-Warshall finds shortest paths between?",
                    "options": ["One source to all", "All pairs", "Two specific nodes", "Minimum spanning tree"],
                    "answer": "All pairs"
                },
                {
                    "question": "Time complexity of Floyd-Warshall?",
                    "options": ["O(V²)", "O(V³)", "O(E log V)", "O(VE)"],
                    "answer": "O(V³)"
                },
                {
                    "question": "Floyd-Warshall can handle?",
                    "options": ["Only positive weights", "Negative weights (no negative cycles)", "Negative cycles", "Only integers"],
                    "answer": "Negative weights (no negative cycles)"
                },
                {
                    "question": "How to detect negative cycle with Floyd-Warshall?",
                    "options": ["dist[0][0] < 0", "dist[i][i] < 0 for any i", "dist[V-1][0] < 0", "Total sum < 0"],
                    "answer": "dist[i][i] < 0 for any i"
                }
            ]
        },

        "Topological Sort": {
            "full_name": "Topological Sort",
            "category": "Graph",
            "difficulty": "Medium",
            "description": """
Topological Sort orders vertices of a **Directed Acyclic Graph (DAG)** such that for every edge u→v, u comes before v in the ordering.

**Key requirement:**
Graph must be a DAG (Directed Acyclic Graph) — no cycles!

**Two algorithms:**
1. **Kahn's Algorithm** (BFS-based) — uses in-degree
2. **DFS-based** — uses stack

**How Kahn's works:**
- Calculate in-degree of all vertices
- Start with vertices having in-degree 0
- Remove vertex, reduce neighbors' in-degree
- If any neighbor reaches in-degree 0, add to queue

**Real world uses:**
- Build systems (make, gradle) — compile in order
- Course prerequisites (take CS101 before CS201)
- Task scheduling with dependencies
- Package installation order
            """,
            "pseudocode": """
TopologicalSort(graph):
    // Kahn's Algorithm
    in_degree = count incoming edges for each vertex

    queue = all vertices with in_degree = 0
    result = []

    while queue not empty:
        u = queue.dequeue()
        result.append(u)

        for each neighbor v of u:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.enqueue(v)

    if len(result) != V: // cycle detected!
        return "Graph has cycle"
    return result
            """,
            "code": {
                "Python": """
from collections import deque

def topological_sort(graph, V):
    # Calculate in-degree of each vertex
    in_degree = [0] * V
    for u in range(V):
        for v in graph[u]:
            in_degree[v] += 1

    # Start with vertices with no incoming edges
    queue = deque([u for u in range(V) if in_degree[u] == 0])
    result = []

    while queue:
        u = queue.popleft()
        result.append(u)

        # Reduce in-degree of neighbors
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(result) != V:
        return "Cycle detected — topological sort impossible!"
    return result

# Example: course prerequisites
# 0→1, 0→2, 1→3, 2→3 (0 before 1,2; 1,2 before 3)
graph = [[1,2], [3], [3], []]
print(topological_sort(graph, 4))
# Output: [0, 1, 2, 3]
                """,
                "C++": """
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<int> topoSort(vector<vector<int>>& graph, int V) {
    vector<int> in_degree(V, 0);
    for (int u=0; u<V; u++)
        for (int v : graph[u])
            in_degree[v]++;

    queue<int> q;
    for (int u=0; u<V; u++)
        if (in_degree[u]==0) q.push(u);

    vector<int> result;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        result.push_back(u);
        for (int v : graph[u])
            if (--in_degree[v]==0) q.push(v);
    }
    return result;
}
                """,
                "Java": """
import java.util.*;

public class TopologicalSort {
    public static List<Integer> topoSort(
        List<List<Integer>> graph, int V) {

        int[] inDegree = new int[V];
        for (int u=0; u<V; u++)
            for (int v : graph.get(u))
                inDegree[v]++;

        Queue<Integer> q = new LinkedList<>();
        for (int u=0; u<V; u++)
            if (inDegree[u]==0) q.add(u);

        List<Integer> result = new ArrayList<>();
        while (!q.isEmpty()) {
            int u = q.poll();
            result.add(u);
            for (int v : graph.get(u))
                if (--inDegree[v]==0) q.add(v);
        }
        return result;
    }
}
                """,
                "JavaScript": """
function topologicalSort(graph, V) {
    const inDegree = new Array(V).fill(0);
    for (let u=0; u<V; u++)
        for (const v of graph[u])
            inDegree[v]++;

    const queue = [];
    for (let u=0; u<V; u++)
        if (inDegree[u]===0) queue.push(u);

    const result = [];
    while (queue.length > 0) {
        const u = queue.shift();
        result.push(u);
        for (const v of graph[u])
            if (--inDegree[v]===0) queue.push(v);
    }
    return result.length===V ? result : "Cycle detected!";
}
                """
            },
            "time_complexity": "O(V + E)",
            "space_complexity": "O(V)",
            "best_case": "O(V + E)",
            "worst_case": "O(V + E)",
            "steps": [
                "Graph: 0→1, 0→2, 1→3, 2→3",
                "in-degree: [0:0, 1:1, 2:1, 3:2]",
                "Queue starts with in-degree 0: [0]",
                "Process 0: add to result. Reduce 1,2 in-degree → [1:0, 2:0]",
                "Queue: [1, 2]. Process 1: reduce 3 in-degree → [3:1]",
                "Process 2: reduce 3 in-degree → [3:0]. Add 3 to queue",
                "Process 3: result = [0, 1, 2, 3] ✅"
            ],
            "quiz": [
                {
                    "question": "Topological sort only works on?",
                    "options": ["Undirected graphs", "Directed Acyclic Graphs (DAG)", "Weighted graphs", "Complete graphs"],
                    "answer": "Directed Acyclic Graphs (DAG)"
                },
                {
                    "question": "What does in-degree mean?",
                    "options": ["Number of outgoing edges", "Number of incoming edges", "Total edges", "Degree of vertex"],
                    "answer": "Number of incoming edges"
                },
                {
                    "question": "If result length != V after Kahn's algorithm?",
                    "options": ["Algorithm is wrong", "Graph has a cycle", "Graph is disconnected", "V is incorrect"],
                    "answer": "Graph has a cycle"
                },
                {
                    "question": "Real world use of Topological Sort?",
                    "options": ["Finding shortest path", "Course prerequisites ordering", "Minimum spanning tree", "Network flow"],
                    "answer": "Course prerequisites ordering"
                }
            ]
        },
    },

    # ================================
    # DYNAMIC PROGRAMMING
    # ================================
    "Dynamic Programming": {

        "Fibonacci DP": {
            "full_name": "Fibonacci — Dynamic Programming",
            "category": "Dynamic Programming",
            "difficulty": "Easy",
            "description": """
Fibonacci sequence using Dynamic Programming — the classic introduction to DP!

**The problem:**
Find nth Fibonacci number where F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)

**Why naive recursion is bad:**
F(5) calls F(4) and F(3)
F(4) calls F(3) and F(2)
F(3) is calculated TWICE! This leads to O(2^n) time!

**Two DP approaches:**

**1. Memoization (Top-Down):**
Store results as we calculate them
If already calculated, return stored result

**2. Tabulation (Bottom-Up):**
Build solution from smaller subproblems
Fill table from F(0) to F(n)

**Key DP insight:**
Overlapping subproblems + Optimal substructure = DP!

**Real world uses:**
- Learning DP concepts
- Financial calculations
- Nature patterns (spiral shells, flower petals)
            """,
            "pseudocode": """
// Memoization approach
memo = {}
Fibonacci(n):
    if n in memo: return memo[n]
    if n <= 1: return n
    memo[n] = Fibonacci(n-1) + Fibonacci(n-2)
    return memo[n]

// Tabulation approach
FibTabulation(n):
    dp = array of size n+1
    dp[0] = 0, dp[1] = 1
    for i = 2 to n:
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
            """,
            "code": {
                "Python": """
# Approach 1: Naive Recursion — O(2^n) — BAD!
def fib_naive(n):
    if n <= 1: return n
    return fib_naive(n-1) + fib_naive(n-2)

# Approach 2: Memoization (Top-Down DP) — O(n)
def fib_memo(n, memo={}):
    if n in memo: return memo[n]  # already calculated!
    if n <= 1: return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# Approach 3: Tabulation (Bottom-Up DP) — O(n)
def fib_tabulation(n):
    if n <= 1: return n
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# Approach 4: Space Optimized — O(1) space
def fib_optimized(n):
    if n <= 1: return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a+b
    return b

# Example
print(fib_tabulation(10))  # Output: 55
print(fib_optimized(10))   # Output: 55
                """,
                "C++": """
#include <iostream>
#include <vector>
using namespace std;

// Tabulation approach
int fibonacci(int n) {
    if (n <= 1) return n;
    vector<int> dp(n+1);
    dp[0]=0; dp[1]=1;
    for (int i=2; i<=n; i++)
        dp[i] = dp[i-1]+dp[i-2];
    return dp[n];
}

// Space optimized
int fibOptimized(int n) {
    if (n<=1) return n;
    int a=0, b=1;
    for (int i=2; i<=n; i++) {
        int c=a+b; a=b; b=c;
    }
    return b;
}
                """,
                "Java": """
public class Fibonacci {
    // Memoization
    static int[] memo;

    public static int fib(int n) {
        memo = new int[n+1];
        java.util.Arrays.fill(memo, -1);
        return fibHelper(n);
    }

    static int fibHelper(int n) {
        if (memo[n] != -1) return memo[n];
        if (n <= 1) return memo[n]=n;
        return memo[n]=fibHelper(n-1)+fibHelper(n-2);
    }

    // Tabulation
    public static int fibTab(int n) {
        if (n<=1) return n;
        int[] dp = new int[n+1];
        dp[0]=0; dp[1]=1;
        for (int i=2; i<=n; i++)
            dp[i]=dp[i-1]+dp[i-2];
        return dp[n];
    }
}
                """,
                "JavaScript": """
// Memoization
function fibMemo(n, memo={}) {
    if (n in memo) return memo[n];
    if (n <= 1) return n;
    memo[n] = fibMemo(n-1, memo) + fibMemo(n-2, memo);
    return memo[n];
}

// Tabulation
function fibTab(n) {
    if (n <= 1) return n;
    const dp = new Array(n+1).fill(0);
    dp[1] = 1;
    for (let i=2; i<=n; i++)
        dp[i] = dp[i-1]+dp[i-2];
    return dp[n];
}

console.log(fibTab(10)); // 55
                """
            },
            "time_complexity": "O(n)",
            "space_complexity": "O(n)",
            "best_case": "O(n)",
            "worst_case": "O(n)",
            "steps": [
                "n=6, tabulation approach",
                "dp[0]=0, dp[1]=1 (base cases)",
                "dp[2] = dp[1]+dp[0] = 1+0 = 1",
                "dp[3] = dp[2]+dp[1] = 1+1 = 2",
                "dp[4] = dp[3]+dp[2] = 2+1 = 3",
                "dp[5] = dp[4]+dp[3] = 3+2 = 5",
                "dp[6] = dp[5]+dp[4] = 5+3 = 8 ✅"
            ],
            "quiz": [
                {
                    "question": "Naive recursive Fibonacci time complexity?",
                    "options": ["O(n)", "O(n²)", "O(2^n)", "O(log n)"],
                    "answer": "O(2^n)"
                },
                {
                    "question": "DP Fibonacci time complexity?",
                    "options": ["O(2^n)", "O(n²)", "O(n)", "O(log n)"],
                    "answer": "O(n)"
                },
                {
                    "question": "What DP technique stores results as they're computed?",
                    "options": ["Tabulation", "Memoization", "Greedy", "Backtracking"],
                    "answer": "Memoization"
                },
                {
                    "question": "What is F(10)?",
                    "options": ["34", "55", "89", "21"],
                    "answer": "55"
                }
            ]
        },

        "0/1 Knapsack": {
            "full_name": "0/1 Knapsack Problem",
            "category": "Dynamic Programming",
            "difficulty": "Medium",
            "description": """
The 0/1 Knapsack problem: given items with weights and values, find maximum value you can put in a knapsack of capacity W. Each item can be taken or left (0 or 1 — not fractional).

**Why it's important:**
- Classic DP problem asked in almost every interview!
- Foundation for many resource allocation problems

**The key insight:**
For each item, we have exactly 2 choices:
1. **Include** the item (if it fits)
2. **Exclude** the item

**DP table explanation:**
dp[i][w] = max value using first i items with capacity w
- If item i doesn't fit: dp[i][w] = dp[i-1][w]
- If item i fits: dp[i][w] = max(dp[i-1][w], val[i] + dp[i-1][w-wt[i]])

**Real world uses:**
- Resource allocation
- Portfolio optimization
- Budget planning
- Cargo loading
            """,
            "pseudocode": """
Knapsack(weights, values, W, n):
    dp[n+1][W+1] = 0 (initialize)

    for i = 1 to n:
        for w = 1 to W:
            // Don't take item i
            dp[i][w] = dp[i-1][w]

            // Take item i (if it fits)
            if weights[i] <= w:
                dp[i][w] = max(dp[i][w],
                               values[i] + dp[i-1][w-weights[i]])

    return dp[n][W]
            """,
            "code": {
                "Python": """
def knapsack(weights, values, W):
    n = len(weights)
    # dp[i][w] = max value with first i items, capacity w
    dp = [[0]*(W+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(W+1):
            # Option 1: Don't take item i
            dp[i][w] = dp[i-1][w]

            # Option 2: Take item i (if it fits)
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w],
                               values[i-1] + dp[i-1][w-weights[i-1]])

    return dp[n][W]

# Example
weights = [2, 3, 4, 5]
values  = [3, 4, 5, 6]
W = 5  # knapsack capacity

print(f"Max value: {knapsack(weights, values, W)}")
# Output: Max value: 7 (items with weight 2 and 3)
                """,
                "C++": """
#include <iostream>
#include <vector>
using namespace std;

int knapsack(vector<int>& wt, vector<int>& val,
             int W, int n) {
    vector<vector<int>> dp(n+1, vector<int>(W+1, 0));

    for (int i=1; i<=n; i++) {
        for (int w=0; w<=W; w++) {
            dp[i][w] = dp[i-1][w];
            if (wt[i-1] <= w)
                dp[i][w] = max(dp[i][w],
                    val[i-1]+dp[i-1][w-wt[i-1]]);
        }
    }
    return dp[n][W];
}
                """,
                "Java": """
public class Knapsack {
    public static int knapsack(int[] wt, int[] val,
                                int W, int n) {
        int[][] dp = new int[n+1][W+1];

        for (int i=1; i<=n; i++) {
            for (int w=0; w<=W; w++) {
                dp[i][w] = dp[i-1][w];
                if (wt[i-1]<=w)
                    dp[i][w] = Math.max(dp[i][w],
                        val[i-1]+dp[i-1][w-wt[i-1]]);
            }
        }
        return dp[n][W];
    }
}
                """,
                "JavaScript": """
function knapsack(weights, values, W) {
    const n = weights.length;
    const dp = Array(n+1).fill(null)
                .map(() => Array(W+1).fill(0));

    for (let i=1; i<=n; i++) {
        for (let w=0; w<=W; w++) {
            dp[i][w] = dp[i-1][w];
            if (weights[i-1] <= w)
                dp[i][w] = Math.max(dp[i][w],
                    values[i-1]+dp[i-1][w-weights[i-1]]);
        }
    }
    return dp[n][W];
}
                """
            },
            "time_complexity": "O(n × W)",
            "space_complexity": "O(n × W)",
            "best_case": "O(n × W)",
            "worst_case": "O(n × W)",
            "steps": [
                "Items: weights=[2,3,4,5], values=[3,4,5,6], W=5",
                "Build dp table row by row",
                "i=1 (weight=2, value=3): dp[1][2]=3, dp[1][3]=3, dp[1][4]=3, dp[1][5]=3",
                "i=2 (weight=3, value=4): dp[2][3]=4, dp[2][5]=max(3, 4+3)=7",
                "i=3 (weight=4, value=5): dp[3][5]=max(7, 5+0)=7",
                "i=4 (weight=5, value=6): dp[4][5]=max(7, 6+0)=7",
                "Answer: dp[4][5] = 7 ✅"
            ],
            "quiz": [
                {
                    "question": "Why is it called 0/1 Knapsack?",
                    "options": ["Uses binary numbers", "Each item taken fully or not at all", "Works only with 0 and 1", "Values are 0 or 1"],
                    "answer": "Each item taken fully or not at all"
                },
                {
                    "question": "Time complexity of 0/1 Knapsack DP?",
                    "options": ["O(n)", "O(n²)", "O(n × W)", "O(2^n)"],
                    "answer": "O(n × W)"
                },
                {
                    "question": "dp[i][w] represents?",
                    "options": ["Weight of i items", "Max value with i items and capacity w", "Number of items", "Remaining capacity"],
                    "answer": "Max value with i items and capacity w"
                },
                {
                    "question": "If item weight > current capacity, we?",
                    "options": ["Skip the item", "Take it anyway", "Split the item", "Reduce capacity"],
                    "answer": "Skip the item"
                }
            ]
        },

        "Longest Common Subsequence": {
            "full_name": "Longest Common Subsequence (LCS)",
            "category": "Dynamic Programming",
            "difficulty": "Medium",
            "description": """
LCS finds the longest subsequence common to two strings. A subsequence doesn't need to be contiguous — just in order.

**Example:**
- String 1: "ABCBDAB"
- String 2: "BDCAB"
- LCS: "BCAB" or "BDAB" (length 4)

**Subsequence vs Substring:**
- Subsequence: characters in order but not necessarily adjacent
- Substring: characters must be adjacent (contiguous)

**DP recurrence:**
- If chars match: dp[i][j] = 1 + dp[i-1][j-1]
- If don't match: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

**Real world uses:**
- Git diff (showing changes between files)
- DNA sequence alignment in bioinformatics
- Plagiarism detection
- Version control systems
- Spell checkers
            """,
            "pseudocode": """
LCS(s1, s2):
    m = length(s1), n = length(s2)
    dp[m+1][n+1] = 0

    for i = 1 to m:
        for j = 1 to n:
            if s1[i] == s2[j]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]
            """,
            "code": {
                "Python": """
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    # dp[i][j] = LCS of s1[0..i] and s2[0..j]
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                # Characters match — extend LCS
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                # Don't match — take best without one char
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

def lcs_string(s1, s2):
    # Also return the actual LCS string
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Backtrack to find the actual string
    result = []
    i, j = m, n
    while i>0 and j>0:
        if s1[i-1]==s2[j-1]:
            result.append(s1[i-1])
            i -= 1; j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(result))

s1, s2 = "ABCBDAB", "BDCAB"
print(f"LCS length: {lcs(s1, s2)}")      # 4
print(f"LCS string: {lcs_string(s1, s2)}")  # BCAB or BDAB
                """,
                "C++": """
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int lcs(string s1, string s2) {
    int m=s1.size(), n=s2.size();
    vector<vector<int>> dp(m+1, vector<int>(n+1, 0));

    for (int i=1; i<=m; i++)
        for (int j=1; j<=n; j++)
            if (s1[i-1]==s2[j-1])
                dp[i][j] = 1+dp[i-1][j-1];
            else
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);

    return dp[m][n];
}
                """,
                "Java": """
public class LCS {
    public static int lcs(String s1, String s2) {
        int m=s1.length(), n=s2.length();
        int[][] dp = new int[m+1][n+1];

        for (int i=1; i<=m; i++)
            for (int j=1; j<=n; j++)
                if (s1.charAt(i-1)==s2.charAt(j-1))
                    dp[i][j] = 1+dp[i-1][j-1];
                else
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);

        return dp[m][n];
    }
}
                """,
                "JavaScript": """
function lcs(s1, s2) {
    const m=s1.length, n=s2.length;
    const dp = Array(m+1).fill(null)
                .map(() => Array(n+1).fill(0));

    for (let i=1; i<=m; i++)
        for (let j=1; j<=n; j++)
            if (s1[i-1]===s2[j-1])
                dp[i][j] = 1+dp[i-1][j-1];
            else
                dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);

    return dp[m][n];
}
                """
            },
            "time_complexity": "O(m × n)",
            "space_complexity": "O(m × n)",
            "best_case": "O(m × n)",
            "worst_case": "O(m × n)",
            "steps": [
                "s1='ABCB', s2='BCB'",
                "Build dp table: rows for s1, cols for s2",
                "i=1(A): A≠B→0, A≠C→0, A≠B→0",
                "i=2(B): B=B→1, B≠C→1, B=B→1",
                "i=3(C): C≠B→1, C=C→2, C≠B→2",
                "i=4(B): B=B→2, B≠C→2, B=B→3",
                "LCS length = dp[4][3] = 3 (BCB) ✅"
            ],
            "quiz": [
                {
                    "question": "LCS of 'ABCD' and 'ACBD' is?",
                    "options": ["AB", "ABD", "ACD", "3"],
                    "answer": "ABD"
                },
                {
                    "question": "Time complexity of LCS?",
                    "options": ["O(n)", "O(n²)", "O(m×n)", "O(2^n)"],
                    "answer": "O(m×n)"
                },
                {
                    "question": "When characters match in LCS: dp[i][j] = ?",
                    "options": ["dp[i-1][j-1]", "1+dp[i-1][j-1]", "max(dp[i-1][j], dp[i][j-1])", "0"],
                    "answer": "1+dp[i-1][j-1]"
                },
                {
                    "question": "LCS is used in which real application?",
                    "options": ["Sorting", "Git diff (comparing files)", "Graph traversal", "Memory management"],
                    "answer": "Git diff (comparing files)"
                }
            ]
        },
    },

    # ================================
    # GAME ALGORITHMS
    # ================================
    "Game Algorithms": {

        "MinMax": {
            "full_name": "Minimax Algorithm",
            "category": "Game",
            "difficulty": "Medium",
            "description": """
Minimax is a decision algorithm for two-player games. One player **maximizes** score, the other **minimizes** score.

**How it works:**
- Build a game tree of all possible moves
- At MAX nodes: choose move with highest score
- At MIN nodes: choose move with lowest score
- Leaf nodes: evaluate board position

**Assumption:**
Both players play optimally — MAX tries to win, MIN tries to prevent MAX from winning.

**The recursion:**
- If it's MAX's turn: return max of children
- If it's MIN's turn: return min of children
- Base case: game over → return score

**Limitations:**
- Explores ALL nodes → O(b^d) where b=branching factor, d=depth
- Too slow for complex games like Chess
- Solution: Alpha-Beta pruning (next algorithm!)

**Real world uses:**
- Tic-tac-toe AI
- Chess AI (with improvements)
- Checkers
- Connect Four
- Any two-player zero-sum game
            """,
            "pseudocode": """
Minimax(node, depth, isMaximizing):
    if depth == 0 or game_over(node):
        return evaluate(node)

    if isMaximizing:
        maxVal = -infinity
        for each child of node:
            val = Minimax(child, depth-1, false)
            maxVal = max(maxVal, val)
        return maxVal
    else:
        minVal = +infinity
        for each child of node:
            val = Minimax(child, depth-1, true)
            minVal = min(minVal, val)
        return minVal
            """,
            "code": {
                "Python": """
# Minimax for Tic-Tac-Toe
def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    # Terminal states
    if score == 10: return score - depth  # X wins
    if score == -10: return score + depth  # O wins
    if not moves_left(board): return 0    # draw

    if is_maximizing:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    best = max(best,
                        minimax(board, depth+1, False))
                    board[i][j] = '_'  # undo move
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    best = min(best,
                        minimax(board, depth+1, True))
                    board[i][j] = '_'  # undo move
        return best

def evaluate(board):
    # Check rows, cols, diagonals for winner
    lines = [board[i] for i in range(3)]
    lines += [[board[i][j] for i in range(3)] for j in range(3)]
    lines += [[board[i][i] for i in range(3)]]
    lines += [[board[i][2-i] for i in range(3)]]

    for line in lines:
        if line == ['X','X','X']: return 10
        if line == ['O','O','O']: return -10
    return 0

def moves_left(board):
    return any(board[i][j]=='_' for i in range(3) for j in range(3))

# Example board
board = [
    ['X', 'O', 'X'],
    ['O', 'O', '_'],
    ['_', '_', 'X']
]
print(f"Best score: {minimax(board, 0, True)}")
                """,
                "C++": """
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Simplified minimax for game tree
int minimax(vector<int>& scores, int depth,
            int node, bool isMax,
            int height) {
    // Leaf node
    if (depth == height)
        return scores[node];

    if (isMax) {
        return max(
            minimax(scores, depth+1, 2*node, false, height),
            minimax(scores, depth+1, 2*node+1, false, height)
        );
    } else {
        return min(
            minimax(scores, depth+1, 2*node, true, height),
            minimax(scores, depth+1, 2*node+1, true, height)
        );
    }
}
                """,
                "Java": """
public class Minimax {
    // Minimax on game tree
    public static int minimax(int[] scores, int depth,
                               int node, boolean isMax,
                               int height) {
        if (depth == height) return scores[node];

        if (isMax) {
            return Math.max(
                minimax(scores, depth+1, 2*node, false, height),
                minimax(scores, depth+1, 2*node+1, false, height)
            );
        } else {
            return Math.min(
                minimax(scores, depth+1, 2*node, true, height),
                minimax(scores, depth+1, 2*node+1, true, height)
            );
        }
    }
}
                """,
                "JavaScript": """
function minimax(scores, depth, node, isMax, height) {
    if (depth === height) return scores[node];

    if (isMax) {
        return Math.max(
            minimax(scores, depth+1, 2*node, false, height),
            minimax(scores, depth+1, 2*node+1, false, height)
        );
    } else {
        return Math.min(
            minimax(scores, depth+1, 2*node, true, height),
            minimax(scores, depth+1, 2*node+1, true, height)
        );
    }
}
                """
            },
            "time_complexity": "O(b^d)",
            "space_complexity": "O(d)",
            "best_case": "O(b^d)",
            "worst_case": "O(b^d)",
            "steps": [
                "Game tree: MAX is X, MIN is O",
                "Evaluate all leaf nodes (game outcomes)",
                "MIN level: pick minimum from children",
                "MAX level: pick maximum from children",
                "Propagate values up the tree",
                "Root gives best move for MAX player",
                "Best move chosen with optimal play assumed ✅"
            ],
            "quiz": [
                {
                    "question": "In Minimax, what does MAX player try to do?",
                    "options": ["Minimize score", "Maximize score", "Tie the game", "Random moves"],
                    "answer": "Maximize score"
                },
                {
                    "question": "Time complexity of Minimax?",
                    "options": ["O(n)", "O(b^d)", "O(n²)", "O(log n)"],
                    "answer": "O(b^d)"
                },
                {
                    "question": "What improvement reduces Minimax nodes explored?",
                    "options": ["DFS pruning", "Alpha-Beta pruning", "BFS pruning", "Random pruning"],
                    "answer": "Alpha-Beta pruning"
                },
                {
                    "question": "Minimax assumes both players play?",
                    "options": ["Randomly", "Optimally", "Greedily", "Poorly"],
                    "answer": "Optimally"
                }
            ]
        },

        "Alpha-Beta Pruning": {
            "full_name": "Alpha-Beta Pruning",
            "category": "Game",
            "difficulty": "Hard",
            "description": """
Alpha-Beta Pruning is an optimization of Minimax that **prunes branches** that cannot possibly affect the final decision.

**Two parameters:**
- **Alpha (α)**: Best value MAX can guarantee so far (starts -∞)
- **Beta (β)**: Best value MIN can guarantee so far (starts +∞)

**Pruning conditions:**
- At MAX node: if value ≥ β → prune (MIN won't allow this)
- At MIN node: if value ≤ α → prune (MAX won't choose this)

**Why it's powerful:**
- Reduces nodes from O(b^d) to O(b^(d/2))!
- Same result as Minimax — just faster
- Can search TWICE as deep as Minimax!

**Perfect ordering:**
If moves are perfectly ordered (best first), achieves O(b^(d/2))
Worst case: O(b^d) (same as Minimax)

**Real world uses:**
- Chess engines (Stockfish, DeepBlue)
- Go game AI
- Any game that uses Minimax
            """,
            "pseudocode": """
AlphaBeta(node, depth, alpha, beta, isMax):
    if depth == 0 or game_over:
        return evaluate(node)

    if isMaximizing:
        for each child:
            val = AlphaBeta(child, depth-1, alpha, beta, false)
            alpha = max(alpha, val)
            if beta <= alpha:
                break  // Beta cutoff — PRUNE!
        return alpha
    else:
        for each child:
            val = AlphaBeta(child, depth-1, alpha, beta, true)
            beta = min(beta, val)
            if beta <= alpha:
                break  // Alpha cutoff — PRUNE!
        return beta
            """,
            "code": {
                "Python": """
def alpha_beta(board, depth, alpha, beta, is_maximizing):
    score = evaluate(board)

    # Terminal states
    if abs(score) == 10 or depth == 0:
        return score
    if not moves_left(board):
        return 0

    if is_maximizing:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    val = alpha_beta(board, depth-1,
                                     alpha, beta, False)
                    best = max(best, val)
                    alpha = max(alpha, best)
                    board[i][j] = '_'

                    # Beta cutoff — prune remaining branches!
                    if beta <= alpha:
                        break
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    val = alpha_beta(board, depth-1,
                                     alpha, beta, True)
                    best = min(best, val)
                    beta = min(beta, best)
                    board[i][j] = '_'

                    # Alpha cutoff — prune remaining branches!
                    if beta <= alpha:
                        break
        return best

# Call with initial alpha=-inf, beta=+inf
import math
board = [['_']*3 for _ in range(3)]
result = alpha_beta(board, 9, -math.inf, math.inf, True)
print(f"Best score: {result}")
                """,
                "C++": """
#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;

int alphaBeta(vector<int>& scores, int depth, int node,
              int alpha, int beta, bool isMax, int height) {
    if (depth == height) return scores[node];

    if (isMax) {
        int best = INT_MIN;
        for (int i=0; i<2; i++) {
            int val = alphaBeta(scores, depth+1, 2*node+i,
                                alpha, beta, false, height);
            best = max(best, val);
            alpha = max(alpha, best);
            if (beta <= alpha) break; // beta cutoff
        }
        return best;
    } else {
        int best = INT_MAX;
        for (int i=0; i<2; i++) {
            int val = alphaBeta(scores, depth+1, 2*node+i,
                                alpha, beta, true, height);
            best = min(best, val);
            beta = min(beta, best);
            if (beta <= alpha) break; // alpha cutoff
        }
        return best;
    }
}
                """,
                "Java": """
public class AlphaBeta {
    public static int alphaBeta(int[] scores, int depth,
            int node, int alpha, int beta,
            boolean isMax, int height) {
        if (depth == height) return scores[node];

        if (isMax) {
            int best = Integer.MIN_VALUE;
            for (int i=0; i<2; i++) {
                int val = alphaBeta(scores, depth+1, 2*node+i,
                                    alpha, beta, false, height);
                best = Math.max(best, val);
                alpha = Math.max(alpha, best);
                if (beta <= alpha) break;
            }
            return best;
        } else {
            int best = Integer.MAX_VALUE;
            for (int i=0; i<2; i++) {
                int val = alphaBeta(scores, depth+1, 2*node+i,
                                    alpha, beta, true, height);
                best = Math.min(best, val);
                beta = Math.min(beta, best);
                if (beta <= alpha) break;
            }
            return best;
        }
    }
}
                """,
                "JavaScript": """
function alphaBeta(scores, depth, node, alpha, beta,
                   isMax, height) {
    if (depth === height) return scores[node];

    if (isMax) {
        let best = -Infinity;
        for (let i=0; i<2; i++) {
            const val = alphaBeta(scores, depth+1, 2*node+i,
                                   alpha, beta, false, height);
            best = Math.max(best, val);
            alpha = Math.max(alpha, best);
            if (beta <= alpha) break; // prune!
        }
        return best;
    } else {
        let best = Infinity;
        for (let i=0; i<2; i++) {
            const val = alphaBeta(scores, depth+1, 2*node+i,
                                   alpha, beta, true, height);
            best = Math.min(best, val);
            beta = Math.min(beta, best);
            if (beta <= alpha) break; // prune!
        }
        return best;
    }
}
                """
            },
            "time_complexity": "O(b^(d/2))",
            "space_complexity": "O(d)",
            "best_case": "O(b^(d/2))",
            "worst_case": "O(b^d)",
            "steps": [
                "Start: alpha=-∞, beta=+∞",
                "MAX node explores first child → updates alpha",
                "MIN node: if current value ≤ alpha → PRUNE (alpha cutoff)",
                "MAX node: if current value ≥ beta → PRUNE (beta cutoff)",
                "Pruned branches are never explored!",
                "Same final result as Minimax but much faster",
                "Best case: searches b^(d/2) nodes instead of b^d ✅"
            ],
            "quiz": [
                {
                    "question": "Alpha-Beta pruning gives same result as Minimax?",
                    "options": ["Yes always", "No different result", "Sometimes", "Only in chess"],
                    "answer": "Yes always"
                },
                {
                    "question": "Best case time complexity of Alpha-Beta?",
                    "options": ["O(b^d)", "O(b^(d/2))", "O(d)", "O(b)"],
                    "answer": "O(b^(d/2))"
                },
                {
                    "question": "Beta cutoff occurs when?",
                    "options": ["alpha >= beta at MAX node", "beta <= alpha at MIN node", "depth = 0", "No moves left"],
                    "answer": "beta <= alpha at MIN node"
                },
                {
                    "question": "Alpha represents?",
                    "options": ["Best MIN can do", "Best MAX can guarantee so far", "Current depth", "Number of nodes"],
                    "answer": "Best MAX can guarantee so far"
                }
            ]
        },
    },

    # ================================
    # INTELLIGENT AGENTS
    # ================================
    "Intelligent Agents": {

        "Simple Reflex Agent": {
            "full_name": "Simple Reflex Agent",
            "category": "Intelligent Agents",
            "difficulty": "Easy",
            "description": """
A Simple Reflex Agent selects actions based only on the **current percept** — it ignores history!

**How it works:**
- Receives current percept from environment
- Matches percept to condition-action rules
- Performs corresponding action
- No memory of past — completely reactive

**Structure:**
Percept → Condition-Action Rules → Action

**Condition-Action Rules (IF-THEN rules):**
- IF room is dirty THEN vacuum
- IF obstacle ahead THEN turn right
- IF temperature > 30 THEN turn on AC

**Limitations:**
- Only works in fully observable environments
- Cannot handle partial observability
- No learning capability
- Cannot plan ahead

**Real world examples:**
- Thermostat (if cold → heat, if hot → cool)
- Smoke detector (if smoke → alarm)
- Traffic light controller (if timer → change)
            """,
            "pseudocode": """
SimpleReflexAgent(percept):
    rules = set of condition-action rules

    state = interpret_input(percept)
    rule = match_rule(state, rules)
    action = rule.action

    return action

// Example rules
rules = [
    IF dirty → vacuum,
    IF clean → move_forward,
    IF bump → turn_right
]
            """,
            "code": {
                "Python": """
# Simple Reflex Agent — Vacuum Cleaner World

class SimpleReflexAgent:
    def __init__(self):
        # Condition-Action rules
        self.rules = {
            'dirty': 'vacuum',
            'clean': 'move_forward',
            'bump': 'turn_right'
        }

    def perceive(self, environment):
        # Get current state from environment
        return environment.get_current_percept()

    def act(self, percept):
        # Match percept to rule and return action
        if percept in self.rules:
            return self.rules[percept]
        return 'idle'

    def run(self, environment, steps=10):
        for step in range(steps):
            percept = self.perceive(environment)
            action = self.act(percept)
            print(f"Step {step+1}: Percept={percept}, Action={action}")
            environment.apply_action(action)

# Simulation
class VacuumEnvironment:
    def __init__(self):
        self.rooms = ['dirty', 'clean', 'dirty']
        self.position = 0

    def get_current_percept(self):
        return self.rooms[self.position]

    def apply_action(self, action):
        if action == 'vacuum':
            self.rooms[self.position] = 'clean'
        elif action == 'move_forward':
            self.position = min(self.position+1, len(self.rooms)-1)

env = VacuumEnvironment()
agent = SimpleReflexAgent()
agent.run(env, 5)
                """,
                "C++": """
#include <iostream>
#include <map>
#include <string>
using namespace std;

class SimpleReflexAgent {
    map<string, string> rules;

public:
    SimpleReflexAgent() {
        rules["dirty"] = "vacuum";
        rules["clean"] = "move_forward";
        rules["bump"] = "turn_right";
    }

    string act(string percept) {
        if (rules.count(percept))
            return rules[percept];
        return "idle";
    }
};

int main() {
    SimpleReflexAgent agent;
    vector<string> percepts = {"dirty","clean","dirty","bump"};

    for (auto& p : percepts)
        cout << "Percept: " << p
             << " → Action: " << agent.act(p) << endl;
}
                """,
                "Java": """
import java.util.*;

public class SimpleReflexAgent {
    Map<String, String> rules = new HashMap<>();

    public SimpleReflexAgent() {
        rules.put("dirty", "vacuum");
        rules.put("clean", "move_forward");
        rules.put("bump", "turn_right");
    }

    public String act(String percept) {
        return rules.getOrDefault(percept, "idle");
    }

    public static void main(String[] args) {
        SimpleReflexAgent agent = new SimpleReflexAgent();
        String[] percepts = {"dirty","clean","dirty","bump"};

        for (String p : percepts)
            System.out.println("Percept: " + p +
                " → Action: " + agent.act(p));
    }
}
                """,
                "JavaScript": """
class SimpleReflexAgent {
    constructor() {
        this.rules = {
            'dirty': 'vacuum',
            'clean': 'move_forward',
            'bump': 'turn_right'
        };
    }

    act(percept) {
        return this.rules[percept] || 'idle';
    }

    run(percepts) {
        percepts.forEach((p, i) => {
            console.log(`Step ${i+1}: ${p} → ${this.act(p)}`);
        });
    }
}

const agent = new SimpleReflexAgent();
agent.run(['dirty', 'clean', 'dirty', 'bump']);
                """
            },
            "time_complexity": "O(1) per step",
            "space_complexity": "O(r) rules",
            "best_case": "O(1)",
            "worst_case": "O(r)",
            "steps": [
                "Agent receives percept from environment",
                "Matches percept to condition-action rules",
                "IF room=dirty THEN action=vacuum",
                "IF room=clean THEN action=move_forward",
                "No memory — only current percept matters!",
                "Action sent to environment",
                "Cycle repeats for each new percept ✅"
            ],
            "quiz": [
                {
                    "question": "Simple Reflex Agent decisions are based on?",
                    "options": ["Past history", "Future predictions", "Current percept only", "Random choice"],
                    "answer": "Current percept only"
                },
                {
                    "question": "What type of rules does Simple Reflex Agent use?",
                    "options": ["Neural networks", "Condition-Action (IF-THEN) rules", "Decision trees", "Probability tables"],
                    "answer": "Condition-Action (IF-THEN) rules"
                },
                {
                    "question": "Simple Reflex Agent works best in?",
                    "options": ["Partially observable environments", "Fully observable environments", "Unknown environments", "Complex environments"],
                    "answer": "Fully observable environments"
                },
                {
                    "question": "Which is a real example of Simple Reflex Agent?",
                    "options": ["Self-driving car", "Chess AI", "Thermostat", "Recommendation system"],
                    "answer": "Thermostat"
                }
            ]
        },

        "Model-Based Reflex Agent": {
            "full_name": "Model-Based Reflex Agent",
            "category": "Intelligent Agents",
            "difficulty": "Easy",
            "description": """
A Model-Based Reflex Agent maintains an **internal model** of the world to handle partially observable environments.

**Key difference from Simple Reflex:**
- Simple Reflex: only current percept
- Model-Based: current percept + internal state (history)

**Two key components:**
1. **Transition model**: How world changes over time
2. **Sensor model**: How percepts relate to world state

**Internal state:**
Agent keeps track of parts of world it cannot currently see.

**Example:**
A robot remembers it cleaned room A even when it can't see room A anymore!

**Process:**
1. Update internal state based on percept
2. Match updated state to rules
3. Choose action

**Real world examples:**
- Self-driving car (remembers road seen moments ago)
- Robot vacuum (tracks cleaned areas)
- Smart thermostat (learns usage patterns)
            """,
            "pseudocode": """
ModelBasedReflexAgent(percept):
    state = update_state(state, action, percept)
    rule = match_rule(state, rules)
    action = rule.action
    return action

update_state(state, action, percept):
    // Use transition and sensor models
    // to update internal world model
    state = apply_transition(state, action)
    state = apply_sensor_model(state, percept)
    return state
            """,
            "code": {
                "Python": """
class ModelBasedReflexAgent:
    def __init__(self):
        # Internal model of the world
        self.state = {
            'roomA': 'unknown',
            'roomB': 'unknown',
            'position': 'A',
            'last_action': None
        }

        # Rules based on internal state
        self.rules = [
            (lambda s: s['position']=='A' and s['roomA']=='dirty',
             'vacuum'),
            (lambda s: s['position']=='A' and s['roomA']=='clean',
             'move_to_B'),
            (lambda s: s['position']=='B' and s['roomB']=='dirty',
             'vacuum'),
            (lambda s: s['position']=='B' and s['roomB']=='clean',
             'move_to_A'),
        ]

    def update_state(self, percept, action):
        # Update internal model
        pos = self.state['position']

        # Update cleanliness based on percept
        if pos == 'A':
            self.state['roomA'] = percept
        else:
            self.state['roomB'] = percept

        # Update position based on last action
        if action == 'move_to_B':
            self.state['position'] = 'B'
        elif action == 'move_to_A':
            self.state['position'] = 'A'

        if action == 'vacuum':
            self.state[f'room{pos}'] = 'clean'

    def act(self, percept):
        # Update internal model
        self.update_state(percept, self.state['last_action'])

        # Match state to rules
        for condition, action in self.rules:
            if condition(self.state):
                self.state['last_action'] = action
                return action

        return 'idle'

# Test
agent = ModelBasedReflexAgent()
percepts = ['dirty', 'dirty', 'clean', 'dirty']
for p in percepts:
    action = agent.act(p)
    print(f"Percept: {p}, State: {agent.state['position']}, Action: {action}")
                """,
                "C++": """
#include <iostream>
#include <string>
#include <map>
using namespace std;

class ModelBasedAgent {
    map<string, string> world_model;
    string position;
    string last_action;

public:
    ModelBasedAgent() : position("A"), last_action("") {
        world_model["A"] = "unknown";
        world_model["B"] = "unknown";
    }

    void updateState(string percept) {
        world_model[position] = percept;
        if (last_action == "vacuum")
            world_model[position] = "clean";
        else if (last_action == "move_to_B") position = "B";
        else if (last_action == "move_to_A") position = "A";
    }

    string act(string percept) {
        updateState(percept);
        string action = "idle";

        if (world_model[position] == "dirty") action = "vacuum";
        else action = (position=="A") ? "move_to_B" : "move_to_A";

        last_action = action;
        return action;
    }
};
                """,
                "Java": """
import java.util.*;

public class ModelBasedAgent {
    Map<String, String> worldModel = new HashMap<>();
    String position = "A";
    String lastAction = "";

    public ModelBasedAgent() {
        worldModel.put("A", "unknown");
        worldModel.put("B", "unknown");
    }

    void updateState(String percept) {
        worldModel.put(position, percept);
        if ("vacuum".equals(lastAction))
            worldModel.put(position, "clean");
        else if ("move_to_B".equals(lastAction)) position = "B";
        else if ("move_to_A".equals(lastAction)) position = "A";
    }

    public String act(String percept) {
        updateState(percept);
        String action;
        if ("dirty".equals(worldModel.get(position)))
            action = "vacuum";
        else
            action = position.equals("A") ? "move_to_B" : "move_to_A";
        lastAction = action;
        return action;
    }
}
                """,
                "JavaScript": """
class ModelBasedAgent {
    constructor() {
        this.worldModel = { A: 'unknown', B: 'unknown' };
        this.position = 'A';
        this.lastAction = null;
    }

    updateState(percept) {
        this.worldModel[this.position] = percept;
        if (this.lastAction === 'vacuum')
            this.worldModel[this.position] = 'clean';
        else if (this.lastAction === 'move_to_B') this.position = 'B';
        else if (this.lastAction === 'move_to_A') this.position = 'A';
    }

    act(percept) {
        this.updateState(percept);
        let action;
        if (this.worldModel[this.position] === 'dirty')
            action = 'vacuum';
        else
            action = this.position === 'A' ? 'move_to_B' : 'move_to_A';
        this.lastAction = action;
        return action;
    }
}
                """
            },
            "time_complexity": "O(r) per step",
            "space_complexity": "O(s) state size",
            "best_case": "O(1)",
            "worst_case": "O(r)",
            "steps": [
                "Agent receives new percept",
                "Update internal state using transition model",
                "Apply sensor model to reconcile percept with state",
                "Internal state now reflects world including unseen parts",
                "Match updated state to condition-action rules",
                "Execute chosen action",
                "Remember action for next state update ✅"
            ],
            "quiz": [
                {
                    "question": "What makes Model-Based Agent better than Simple Reflex?",
                    "options": ["Faster", "Maintains internal state (memory)", "Uses neural networks", "Learns from experience"],
                    "answer": "Maintains internal state (memory)"
                },
                {
                    "question": "Model-Based Agent can handle?",
                    "options": ["Only fully observable environments", "Partially observable environments", "Only simple tasks", "Only deterministic worlds"],
                    "answer": "Partially observable environments"
                },
                {
                    "question": "What is a transition model?",
                    "options": ["Rules for actions", "How world changes over time", "Sensor readings", "Goal conditions"],
                    "answer": "How world changes over time"
                },
                {
                    "question": "Real example of Model-Based Agent?",
                    "options": ["Thermostat", "Smoke detector", "Robot vacuum tracking cleaned areas", "Simple calculator"],
                    "answer": "Robot vacuum tracking cleaned areas"
                }
            ]
        },

        "Goal-Based Agent": {
            "full_name": "Goal-Based Agent",
            "category": "Intelligent Agents",
            "difficulty": "Medium",
            "description": """
A Goal-Based Agent has explicit **goals** and chooses actions that help achieve those goals. It plans ahead rather than just reacting.

**Key components:**
1. **World model** — current state of environment
2. **Goals** — desired states to achieve
3. **Search/Planning** — find sequence of actions to reach goal

**How it differs from Reflex Agents:**
- Reflex: IF condition THEN action (no goal)
- Goal-Based: considers future states, plans sequence of actions

**Goal vs No-Goal:**
- Reflex agent at junction: randomly turns
- Goal-Based agent at junction: turns based on destination!

**Advantages:**
- More flexible — can achieve many different goals
- Can handle new situations by planning
- Actions motivated by purpose

**Limitations:**
- Slower (needs planning)
- May not choose most efficient action

**Real world examples:**
- GPS navigation (goal = destination)
- Chess AI planning moves (goal = checkmate)
- Robot arm (goal = pick up object)
            """,
            "pseudocode": """
GoalBasedAgent(percept, goal):
    state = update_state(state, percept)
    plan = search(state, goal)
    action = plan.next_action()
    return action

search(state, goal):
    // Use BFS, DFS, A*, etc.
    // Find sequence of actions from state to goal
    return action_sequence
            """,
            "code": {
                "Python": """
from collections import deque

class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal
        self.plan = []
        self.state = None

    def update_state(self, percept):
        self.state = percept

    def search(self, start, goal, graph):
        # BFS to find path to goal
        queue = deque([(start, [start])])
        visited = {start}

        while queue:
            node, path = queue.popleft()
            if node == goal:
                return path[1:]  # actions to take

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return []

    def act(self, percept, graph):
        self.update_state(percept)

        # Replan if no current plan
        if not self.plan:
            self.plan = self.search(self.state, self.goal, graph)
            print(f"New plan: {self.plan}")

        # Execute next action
        if self.plan:
            return self.plan.pop(0)
        return 'goal_reached'

# Example: navigate from A to D
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}
agent = GoalBasedAgent(goal='D')
percepts = ['A', 'B', 'D']

for p in percepts:
    action = agent.act(p, graph)
    print(f"State: {p}, Action: {action}")
                """,
                "C++": """
#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

class GoalBasedAgent {
    string goal;
    vector<string> plan;

public:
    GoalBasedAgent(string g) : goal(g) {}

    vector<string> search(string start,
            unordered_map<string,vector<string>>& graph) {
        queue<pair<string,vector<string>>> q;
        q.push({start, {start}});

        while (!q.empty()) {
            auto [node, path] = q.front(); q.pop();
            if (node == goal)
                return vector<string>(path.begin()+1, path.end());

            for (auto& nb : graph[node])
                q.push({nb, [&](){
                    auto p=path; p.push_back(nb); return p;}()});
        }
        return {};
    }

    string act(string state,
               unordered_map<string,vector<string>>& graph) {
        if (plan.empty()) plan = search(state, graph);
        if (!plan.empty()) {
            string action = plan.front();
            plan.erase(plan.begin());
            return action;
        }
        return "goal_reached";
    }
};
                """,
                "Java": """
import java.util.*;

public class GoalBasedAgent {
    String goal;
    List<String> plan = new ArrayList<>();

    public GoalBasedAgent(String goal) { this.goal = goal; }

    List<String> search(String start,
            Map<String, List<String>> graph) {
        Queue<List<String>> queue = new LinkedList<>();
        queue.add(Arrays.asList(start));

        while (!queue.isEmpty()) {
            List<String> path = queue.poll();
            String node = path.get(path.size()-1);

            if (node.equals(goal)) {
                return path.subList(1, path.size());
            }

            for (String nb : graph.getOrDefault(node, new ArrayList<>())) {
                List<String> newPath = new ArrayList<>(path);
                newPath.add(nb);
                queue.add(newPath);
            }
        }
        return new ArrayList<>();
    }

    public String act(String state,
                       Map<String, List<String>> graph) {
        if (plan.isEmpty()) plan = search(state, graph);
        if (!plan.isEmpty()) return plan.remove(0);
        return "goal_reached";
    }
}
                """,
                "JavaScript": """
class GoalBasedAgent {
    constructor(goal) {
        this.goal = goal;
        this.plan = [];
    }

    search(start, graph) {
        const queue = [[start]];
        const visited = new Set([start]);

        while (queue.length > 0) {
            const path = queue.shift();
            const node = path[path.length-1];

            if (node === this.goal) return path.slice(1);

            for (const nb of (graph[node] || [])) {
                if (!visited.has(nb)) {
                    visited.add(nb);
                    queue.push([...path, nb]);
                }
            }
        }
        return [];
    }

    act(state, graph) {
        if (this.plan.length === 0)
            this.plan = this.search(state, graph);
        return this.plan.length > 0 ?
               this.plan.shift() : 'goal_reached';
    }
}
                """
            },
            "time_complexity": "O(V + E) for BFS planning",
            "space_complexity": "O(V)",
            "best_case": "O(1)",
            "worst_case": "O(V + E)",
            "steps": [
                "Agent receives percept — knows current state",
                "Has goal: reach destination D",
                "Plans path using BFS: A → B → D",
                "Executes first action: move to B",
                "Next percept: at B. Plan: [D]",
                "Executes: move to D",
                "Goal reached! ✅"
            ],
            "quiz": [
                {
                    "question": "What makes Goal-Based Agent different from Reflex Agent?",
                    "options": ["Speed", "Has explicit goals and plans ahead", "Uses more memory", "Simpler rules"],
                    "answer": "Has explicit goals and plans ahead"
                },
                {
                    "question": "Goal-Based Agent uses what to find actions?",
                    "options": ["Condition-action rules only", "Search/Planning algorithms", "Random selection", "Neural networks"],
                    "answer": "Search/Planning algorithms"
                },
                {
                    "question": "Advantage of Goal-Based over Reflex Agent?",
                    "options": ["Faster", "More flexible — can handle different goals", "Simpler", "Uses less memory"],
                    "answer": "More flexible — can handle different goals"
                },
                {
                    "question": "Real example of Goal-Based Agent?",
                    "options": ["Thermostat", "GPS navigation", "Smoke detector", "Simple timer"],
                    "answer": "GPS navigation"
                }
            ]
        },

        "Utility-Based Agent": {
            "full_name": "Utility-Based Agent",
            "category": "Intelligent Agents",
            "difficulty": "Medium",
            "description": """
A Utility-Based Agent chooses actions that **maximize utility** (happiness/reward). It goes beyond goals by considering HOW WELL goals are achieved.

**Goal vs Utility:**
- Goal-Based: reach destination (yes/no)
- Utility-Based: reach destination FASTEST with LEAST fuel (maximize utility)

**Utility function:**
Maps states to real numbers indicating how "happy" the agent is in that state.

**Decision making:**
Choose action that leads to state with MAXIMUM expected utility.

**Expected Utility:**
When world is uncertain, calculate probability-weighted utility:
EU(action) = Σ P(outcome) × U(outcome)

**Advantages:**
- Handles conflicting goals (speed vs safety)
- Works in uncertain environments
- Can make rational tradeoffs

**Real world examples:**
- Self-driving cars (safety + speed + comfort)
- Stock trading AI (maximize profit, minimize risk)
- Game AI with multiple objectives
- Medical diagnosis AI
            """,
            "pseudocode": """
UtilityBasedAgent(percept):
    state = update_state(state, percept)

    best_action = null
    best_utility = -infinity

    for each possible_action:
        // Calculate expected utility
        eu = expected_utility(possible_action, state)
        if eu > best_utility:
            best_utility = eu
            best_action = possible_action

    return best_action

expected_utility(action, state):
    return sum(P(s'|state,action) * U(s')
               for each possible next state s')
            """,
            "code": {
                "Python": """
class UtilityBasedAgent:
    def __init__(self):
        # Utility values for different states
        self.utility = {
            'goal_fast': 100,     # reached goal quickly
            'goal_slow': 60,      # reached goal slowly
            'safe_path': 80,      # safe but longer path
            'risky_path': 90,     # faster but risky
            'collision': -100,    # crashed!
            'idle': 0
        }

        # Transition probabilities (state, action) → outcomes
        self.transitions = {
            ('start', 'fast_route'): [
                ('goal_fast', 0.7),   # 70% reach fast
                ('collision', 0.3)    # 30% crash
            ],
            ('start', 'safe_route'): [
                ('goal_slow', 0.95),  # 95% reach slowly
                ('idle', 0.05)        # 5% stuck
            ]
        }

    def expected_utility(self, action, state):
        outcomes = self.transitions.get((state, action), [])
        eu = sum(prob * self.utility.get(outcome, 0)
                 for outcome, prob in outcomes)
        return eu

    def act(self, state, actions):
        best_action = None
        best_eu = float('-inf')

        for action in actions:
            eu = self.expected_utility(action, state)
            print(f"Action: {action}, Expected Utility: {eu:.1f}")

            if eu > best_eu:
                best_eu = eu
                best_action = action

        print(f"Best action: {best_action} (EU={best_eu:.1f})")
        return best_action

# Example
agent = UtilityBasedAgent()
actions = ['fast_route', 'safe_route']
agent.act('start', actions)
# Expected utility fast_route = 0.7*100 + 0.3*(-100) = 40
# Expected utility safe_route = 0.95*60 + 0.05*0 = 57
# Best: safe_route!
                """,
                "C++": """
#include <iostream>
#include <map>
#include <vector>
#include <string>
using namespace std;

class UtilityAgent {
    map<string, double> utility;
    map<pair<string,string>, vector<pair<string,double>>> transitions;

public:
    UtilityAgent() {
        utility["goal_fast"] = 100;
        utility["goal_slow"] = 60;
        utility["collision"] = -100;

        transitions[{"start","fast"}] = {{"goal_fast",0.7},{"collision",0.3}};
        transitions[{"start","safe"}] = {{"goal_slow",0.95},{"idle",0.05}};
    }

    double expectedUtility(string state, string action) {
        double eu = 0;
        for (auto& [outcome, prob] : transitions[{state,action}])
            eu += prob * utility[outcome];
        return eu;
    }

    string act(string state, vector<string> actions) {
        string best; double bestEU = -1e9;
        for (auto& a : actions) {
            double eu = expectedUtility(state, a);
            if (eu > bestEU) { bestEU = eu; best = a; }
        }
        return best;
    }
};
                """,
                "Java": """
import java.util.*;

public class UtilityAgent {
    Map<String, Double> utility = new HashMap<>();

    public UtilityAgent() {
        utility.put("goal_fast", 100.0);
        utility.put("goal_slow", 60.0);
        utility.put("collision", -100.0);
        utility.put("idle", 0.0);
    }

    public double expectedUtility(String action) {
        if (action.equals("fast_route"))
            return 0.7*100 + 0.3*(-100); // 40
        else
            return 0.95*60 + 0.05*0;     // 57
    }

    public String act(String[] actions) {
        String best = null;
        double bestEU = Double.NEGATIVE_INFINITY;
        for (String a : actions) {
            double eu = expectedUtility(a);
            if (eu > bestEU) { bestEU = eu; best = a; }
        }
        return best;
    }
}
                """,
                "JavaScript": """
class UtilityAgent {
    constructor() {
        this.utility = {
            goal_fast: 100, goal_slow: 60,
            collision: -100, idle: 0
        };
        this.transitions = {
            fast_route: [['goal_fast',0.7],['collision',0.3]],
            safe_route: [['goal_slow',0.95],['idle',0.05]]
        };
    }

    expectedUtility(action) {
        return (this.transitions[action] || [])
            .reduce((sum, [outcome, prob]) =>
                sum + prob * (this.utility[outcome] || 0), 0);
    }

    act(actions) {
        let best = null, bestEU = -Infinity;
        for (const a of actions) {
            const eu = this.expectedUtility(a);
            console.log(`${a}: EU=${eu}`);
            if (eu > bestEU) { bestEU = eu; best = a; }
        }
        return best;
    }
}

const agent = new UtilityAgent();
console.log('Best:', agent.act(['fast_route', 'safe_route']));
                """
            },
            "time_complexity": "O(a × s) actions × states",
            "space_complexity": "O(s)",
            "best_case": "O(a)",
            "worst_case": "O(a × s)",
            "steps": [
                "Agent perceives current state: 'start'",
                "Available actions: fast_route, safe_route",
                "Calculate EU(fast_route) = 0.7×100 + 0.3×(-100) = 40",
                "Calculate EU(safe_route) = 0.95×60 + 0.05×0 = 57",
                "Compare: 57 > 40 → safe_route wins!",
                "Execute safe_route despite being slower",
                "Rational choice: maximize expected utility ✅"
            ],
            "quiz": [
                {
                    "question": "Utility-Based Agent improves over Goal-Based by?",
                    "options": ["Being faster", "Considering HOW WELL goals are achieved", "Using less memory", "Simpler rules"],
                    "answer": "Considering HOW WELL goals are achieved"
                },
                {
                    "question": "Expected Utility formula uses?",
                    "options": ["Only utility values", "Probability × Utility for all outcomes", "Maximum utility", "Minimum risk"],
                    "answer": "Probability × Utility for all outcomes"
                },
                {
                    "question": "Utility function maps states to?",
                    "options": ["Actions", "Real numbers (happiness score)", "Other states", "Goals"],
                    "answer": "Real numbers (happiness score)"
                },
                {
                    "question": "Real example of Utility-Based Agent?",
                    "options": ["Thermostat", "Smoke detector", "Self-driving car balancing safety and speed", "Simple alarm"],
                    "answer": "Self-driving car balancing safety and speed"
                }
            ]
        },

        "Learning Agent": {
            "full_name": "Learning Agent",
            "category": "Intelligent Agents",
            "difficulty": "Hard",
            "description": """
A Learning Agent **improves its performance** over time through experience. It's the most powerful and flexible type of agent.

**Four key components:**
1. **Learning element** — improves performance based on feedback
2. **Performance element** — selects actions (like other agents)
3. **Critic** — evaluates how well agent is doing
4. **Problem generator** — suggests exploratory actions to learn new things

**Types of learning:**
- **Reinforcement Learning**: learn from rewards/penalties
- **Supervised Learning**: learn from labeled examples
- **Unsupervised Learning**: discover patterns without labels

**Learning vs Fixed Agents:**
- Fixed agent: programmed rules never change
- Learning agent: adapts and improves with experience!

**The exploration vs exploitation dilemma:**
- Exploit: use what you know works
- Explore: try new things to find better strategies
- Need balance of both!

**Real world examples:**
- AlphaGo (learned to beat world champions)
- ChatGPT (learned from human text)
- Recommendation systems (Netflix, YouTube)
- Self-driving cars learning from experience
            """,
            "pseudocode": """
LearningAgent:
    performance_element = initial_agent
    learning_element = learning_algorithm
    critic = performance_standard
    problem_generator = exploration_strategy

    loop:
        percept = get_percept()

        // Critic evaluates performance
        reward = critic.evaluate(percept, last_action)

        // Learning element updates performance element
        learning_element.update(performance_element,
                                reward, percept)

        // Problem generator suggests exploration
        action = problem_generator.suggest_or(
                 performance_element.act(percept))

        perform(action)
            """,
            "code": {
                "Python": """
import random

class LearningAgent:
    def __init__(self, actions, learning_rate=0.1,
                 discount=0.9, epsilon=0.3):
        self.actions = actions
        self.lr = learning_rate      # how fast to learn
        self.gamma = discount         # future reward weight
        self.epsilon = epsilon        # exploration rate

        # Q-table: state → action → value
        self.Q = {}

    def get_q(self, state, action):
        return self.Q.get((state, action), 0.0)

    def act(self, state):
        # Epsilon-greedy: explore or exploit
        if random.random() < self.epsilon:
            return random.choice(self.actions)  # explore
        else:
            # Exploit: choose action with highest Q value
            return max(self.actions,
                      key=lambda a: self.get_q(state, a))

    def learn(self, state, action, reward, next_state):
        # Q-learning update rule
        current_q = self.get_q(state, action)
        max_next_q = max(self.get_q(next_state, a)
                        for a in self.actions)

        # Bellman equation
        new_q = current_q + self.lr * (
            reward + self.gamma * max_next_q - current_q)

        self.Q[(state, action)] = new_q

    def train(self, environment, episodes=100):
        for ep in range(episodes):
            state = environment.reset()
            total_reward = 0

            for step in range(50):
                action = self.act(state)
                next_state, reward, done = environment.step(action)

                self.learn(state, action, reward, next_state)

                state = next_state
                total_reward += reward

                if done: break

            # Reduce exploration over time
            self.epsilon = max(0.01, self.epsilon * 0.995)

            if ep % 10 == 0:
                print(f"Episode {ep}: Total Reward={total_reward:.1f}")

# Simple grid environment
class GridEnv:
    def __init__(self):
        self.state = 0
        self.goal = 5

    def reset(self):
        self.state = 0
        return self.state

    def step(self, action):
        if action == 'right': self.state = min(5, self.state+1)
        elif action == 'left': self.state = max(0, self.state-1)

        reward = 10 if self.state == self.goal else -1
        done = self.state == self.goal
        return self.state, reward, done

# Train agent
env = GridEnv()
agent = LearningAgent(['left', 'right'])
agent.train(env, episodes=50)
                """,
                "C++": """
#include <iostream>
#include <map>
#include <vector>
#include <random>
#include <algorithm>
using namespace std;

class QLearningAgent {
    map<pair<int,string>, double> Q;
    vector<string> actions;
    double lr, gamma, epsilon;
    mt19937 rng;

public:
    QLearningAgent(vector<string> acts,
                   double lr=0.1, double g=0.9, double e=0.3)
        : actions(acts), lr(lr), gamma(g), epsilon(e),
          rng(random_device{}()) {}

    double getQ(int state, string action) {
        auto key = make_pair(state, action);
        return Q.count(key) ? Q[key] : 0.0;
    }

    string act(int state) {
        uniform_real_distribution<> dist(0, 1);
        if (dist(rng) < epsilon) {
            // Explore
            uniform_int_distribution<> idx(0, actions.size()-1);
            return actions[idx(rng)];
        }
        // Exploit: best Q action
        return *max_element(actions.begin(), actions.end(),
            [&](const string& a, const string& b) {
                return getQ(state, a) < getQ(state, b);
            });
    }

    void learn(int s, string a, double r, int ns) {
        double maxQ = *max_element(actions.begin(), actions.end(),
            [&](const string& x, const string& y) {
                return getQ(ns, x) < getQ(ns, y);
            }) == actions[0] ? getQ(ns, actions[0]) : 0;

        Q[{s,a}] += lr * (r + gamma*maxQ - getQ(s,a));
    }
};
                """,
                "Java": """
import java.util.*;

public class QLearningAgent {
    Map<String, Double> Q = new HashMap<>();
    String[] actions;
    double lr, gamma, epsilon;
    Random rng = new Random();

    public QLearningAgent(String[] actions) {
        this.actions = actions;
        this.lr = 0.1; this.gamma = 0.9; this.epsilon = 0.3;
    }

    double getQ(int state, String action) {
        return Q.getOrDefault(state+":"+action, 0.0);
    }

    public String act(int state) {
        if (rng.nextDouble() < epsilon)
            return actions[rng.nextInt(actions.length)];

        String best = actions[0];
        for (String a : actions)
            if (getQ(state, a) > getQ(state, best)) best = a;
        return best;
    }

    public void learn(int s, String a, double r, int ns) {
        double maxQ = Arrays.stream(actions)
            .mapToDouble(x -> getQ(ns, x)).max().orElse(0);
        String key = s+":"+a;
        Q.put(key, getQ(s,a) + lr*(r + gamma*maxQ - getQ(s,a)));
    }
}
                """,
                "JavaScript": """
class QLearningAgent {
    constructor(actions, lr=0.1, gamma=0.9, epsilon=0.3) {
        this.actions = actions;
        this.Q = new Map();
        this.lr = lr; this.gamma = gamma; this.epsilon = epsilon;
    }

    getQ(state, action) {
        return this.Q.get(`${state}:${action}`) || 0;
    }

    act(state) {
        if (Math.random() < this.epsilon)
            return this.actions[Math.floor(Math.random()*this.actions.length)];

        return this.actions.reduce((best, a) =>
            this.getQ(state, a) > this.getQ(state, best) ? a : best);
    }

    learn(state, action, reward, nextState) {
        const maxQ = Math.max(...this.actions.map(a => this.getQ(nextState, a)));
        const key = `${state}:${action}`;
        const newQ = this.getQ(state,action) +
                     this.lr*(reward + this.gamma*maxQ - this.getQ(state,action));
        this.Q.set(key, newQ);
    }
}
                """
            },
            "time_complexity": "O(episodes × steps)",
            "space_complexity": "O(states × actions)",
            "best_case": "O(1) after training",
            "worst_case": "O(episodes × steps)",
            "steps": [
                "Agent starts with no knowledge (Q=0 for all)",
                "Episode 1: takes random actions (high epsilon)",
                "Gets reward: +10 for reaching goal, -1 otherwise",
                "Updates Q-table using Bellman equation",
                "Episode 10: starts learning good actions",
                "Epsilon decreases: less exploration, more exploitation",
                "After 100 episodes: agent knows optimal path! ✅"
            ],
            "quiz": [
                {
                    "question": "What makes Learning Agent unique?",
                    "options": ["Has goals", "Improves performance over time", "Uses utilities", "Has internal state"],
                    "answer": "Improves performance over time"
                },
                {
                    "question": "The exploration vs exploitation dilemma is about?",
                    "options": ["Memory vs speed", "Trying new actions vs using known good actions", "Learning rate vs discount", "Episodes vs steps"],
                    "answer": "Trying new actions vs using known good actions"
                },
                {
                    "question": "Which component evaluates agent performance?",
                    "options": ["Learning element", "Performance element", "Critic", "Problem generator"],
                    "answer": "Critic"
                },
                {
                    "question": "Q-learning is what type of learning?",
                    "options": ["Supervised", "Unsupervised", "Reinforcement", "Transfer"],
                    "answer": "Reinforcement"
                }
            ]
        },
    },
}

# ================================
# Complexity comparison table
# ================================
complexity_data = {
    "Algorithm": [
        "BFS", "DFS", "Binary Search", "A*", "Dijkstra",
        "Bubble Sort", "Selection Sort", "Insertion Sort",
        "Merge Sort", "Quick Sort", "Heap Sort",
        "Floyd Warshall", "Topological Sort",
        "Fibonacci DP", "0/1 Knapsack", "LCS",
        "Minimax", "Alpha-Beta"
    ],
    "Time (Average)": [
        "O(V+E)", "O(V+E)", "O(log n)", "O(E log V)", "O(E log V)",
        "O(n²)", "O(n²)", "O(n²)",
        "O(n log n)", "O(n log n)", "O(n log n)",
        "O(V³)", "O(V+E)",
        "O(n)", "O(n×W)", "O(m×n)",
        "O(b^d)", "O(b^(d/2))"
    ],
    "Space": [
        "O(V)", "O(V)", "O(1)", "O(V)", "O(V)",
        "O(1)", "O(1)", "O(1)",
        "O(n)", "O(log n)", "O(1)",
        "O(V²)", "O(V)",
        "O(n)", "O(n×W)", "O(m×n)",
        "O(d)", "O(d)"
    ],
    "Stable": [
        "Yes", "Yes", "N/A", "Yes", "Yes",
        "Yes", "No", "Yes",
        "Yes", "No", "No",
        "N/A", "N/A",
        "N/A", "N/A", "N/A",
        "N/A", "N/A"
    ],
    "Difficulty": [
        "Easy", "Easy", "Easy", "Hard", "Medium",
        "Easy", "Easy", "Easy",
        "Medium", "Medium", "Medium",
        "Medium", "Medium",
        "Easy", "Medium", "Medium",
        "Medium", "Hard"
    ]
}

# ================================
# Interview questions
# ================================
interview_questions = [
    # ===== EASY =====
    {
        "question": "What is the time complexity of BFS and DFS?",
        "answer": "Both are O(V+E) where V=vertices and E=edges. Space is O(V) for visited set.",
        "difficulty": "Easy"
    },
    {
        "question": "When would you use DFS over BFS?",
        "answer": "DFS for: maze solving, topological sort, cycle detection, path existence. BFS for: shortest path in unweighted graphs, level-order traversal, finding nearest nodes.",
        "difficulty": "Easy"
    },
    {
        "question": "What data structure does BFS use and why?",
        "answer": "Queue (FIFO) — because we process nodes level by level. We visit all neighbors before going deeper, so first-in first-out is perfect.",
        "difficulty": "Easy"
    },
    {
        "question": "What data structure does DFS use?",
        "answer": "Stack (LIFO) for iterative implementation, or call stack for recursive implementation. We go deep before wide.",
        "difficulty": "Easy"
    },
    {
        "question": "What is Binary Search and when can you use it?",
        "answer": "Binary Search finds element in sorted array by halving search space each step — O(log n). Requires: array must be sorted! Each step eliminates half the remaining elements.",
        "difficulty": "Easy"
    },
    {
        "question": "What is the difference between stable and unstable sorting?",
        "answer": "Stable sort preserves relative order of equal elements. Stable: Bubble, Insertion, Merge Sort. Unstable: Quick Sort, Heap Sort, Selection Sort.",
        "difficulty": "Easy"
    },
    {
        "question": "What is the best sorting algorithm for nearly sorted data?",
        "answer": "Insertion Sort! It's O(n) for nearly sorted data because inner while loop rarely executes. Timsort (Python's sort) also uses Insertion Sort for small runs.",
        "difficulty": "Easy"
    },
    {
        "question": "What is a Simple Reflex Agent?",
        "answer": "Agent that acts only on current percept using condition-action (IF-THEN) rules. No memory of past. Works only in fully observable environments. Example: thermostat.",
        "difficulty": "Easy"
    },
    {
        "question": "What is the difference between subsequence and substring?",
        "answer": "Substring: characters must be contiguous (adjacent). Subsequence: characters must be in order but not necessarily adjacent. LCS finds longest common subsequence.",
        "difficulty": "Easy"
    },
    {
        "question": "What is time and space complexity of Bubble Sort?",
        "answer": "Time: O(n²) worst/average, O(n) best (nearly sorted with optimization). Space: O(1) — in-place sorting. Very slow for large data.",
        "difficulty": "Easy"
    },
    {
        "question": "What is recursion and what is its risk?",
        "answer": "Recursion: function calls itself with smaller input until base case. Risk: stack overflow if recursion too deep or base case missing. Each call adds to call stack.",
        "difficulty": "Easy"
    },
    {
        "question": "What is a DAG?",
        "answer": "Directed Acyclic Graph — directed graph with no cycles. Required for topological sort. Examples: course prerequisites, build dependencies, task scheduling.",
        "difficulty": "Easy"
    },

    # ===== MEDIUM =====
    {
        "question": "What is the difference between Dijkstra and A*?",
        "answer": "Dijkstra explores all directions equally using O(E log V). A* uses heuristic f=g+h to guide towards goal — faster in practice! A* with h=0 becomes Dijkstra.",
        "difficulty": "Medium"
    },
    {
        "question": "Why is Merge Sort preferred over Quick Sort sometimes?",
        "answer": "Merge Sort: guaranteed O(n log n) in all cases, stable sort. Quick Sort: O(n²) worst case, not stable. Use Merge Sort for linked lists and when stability needed.",
        "difficulty": "Medium"
    },
    {
        "question": "Explain the 0/1 Knapsack DP recurrence",
        "answer": "dp[i][w] = max value with first i items, capacity w. If item fits: max(dp[i-1][w], val[i]+dp[i-1][w-wt[i]]). If doesn't fit: dp[i-1][w]. O(n×W) time.",
        "difficulty": "Medium"
    },
    {
        "question": "What is the difference between Simple Reflex and Goal-Based agents?",
        "answer": "Simple Reflex: acts only on current percept using IF-THEN rules, no memory. Goal-Based: maintains world model, plans sequence of actions to achieve explicit goals.",
        "difficulty": "Medium"
    },
    {
        "question": "What is dynamic programming and when to use it?",
        "answer": "DP solves problems by breaking into overlapping subproblems and storing results. Use when: optimal substructure AND overlapping subproblems. Two approaches: memoization (top-down) and tabulation (bottom-up).",
        "difficulty": "Medium"
    },
    {
        "question": "What is the difference between memoization and tabulation?",
        "answer": "Memoization (top-down): recursive, stores results as computed, only computes needed subproblems. Tabulation (bottom-up): iterative, fills table from base cases up, computes all subproblems.",
        "difficulty": "Medium"
    },
    {
        "question": "What is topological sort and when is it impossible?",
        "answer": "Topological sort orders vertices of DAG so every edge u→v has u before v. Impossible when graph has a cycle — detect this if result length < V in Kahn's algorithm.",
        "difficulty": "Medium"
    },
    {
        "question": "Why does Heap Sort have O(1) space complexity?",
        "answer": "Heap Sort sorts in-place using the input array itself as the heap. No extra array needed. It builds max-heap in the array, then extracts elements to the back of the same array.",
        "difficulty": "Medium"
    },
    {
        "question": "What is the partition step in Quick Sort?",
        "answer": "Partition places pivot in its final correct position — all elements left < pivot, all elements right > pivot. This is done in O(n) time with O(1) extra space using two pointers.",
        "difficulty": "Medium"
    },
    {
        "question": "What is LCS and what algorithm solves it?",
        "answer": "Longest Common Subsequence — longest sequence present in both strings in order but not necessarily adjacent. Solved by DP in O(m×n) time. Used in Git diff, DNA alignment.",
        "difficulty": "Medium"
    },
    {
        "question": "What is the difference between Dijkstra and Floyd-Warshall?",
        "answer": "Dijkstra: single source to all destinations, O(E log V), no negative edges. Floyd-Warshall: ALL pairs shortest paths, O(V³), handles negative edges (not negative cycles).",
        "difficulty": "Medium"
    },
    {
        "question": "What is Minimax algorithm?",
        "answer": "Decision algorithm for two-player games. MAX player maximizes score, MIN player minimizes it. Both play optimally. Explores complete game tree — O(b^d) where b=branching factor, d=depth.",
        "difficulty": "Medium"
    },
    {
        "question": "What is a Utility-Based Agent?",
        "answer": "Agent that chooses actions maximizing expected utility. Goes beyond goals — considers HOW WELL goals are achieved. Uses EU(action) = Σ P(outcome) × U(outcome). Example: self-driving car balancing speed and safety.",
        "difficulty": "Medium"
    },
    {
        "question": "How do you detect a cycle in a directed graph?",
        "answer": "Use DFS with 3 colors: WHITE (unvisited), GRAY (in current path), BLACK (fully processed). If DFS reaches GRAY node — cycle found! Also: if topological sort result length < V, cycle exists.",
        "difficulty": "Medium"
    },

    # ===== HARD =====
    {
        "question": "Explain Alpha-Beta pruning and its advantage over Minimax",
        "answer": "Alpha-Beta prunes branches that cannot affect final decision. Uses alpha (best MAX can guarantee) and beta (best MIN can guarantee). Cuts O(b^d) to O(b^(d/2)) — can search twice as deep!",
        "difficulty": "Hard"
    },
    {
        "question": "Why does Floyd-Warshall work with negative edges but not negative cycles?",
        "answer": "Floyd-Warshall relaxes all pairs through each intermediate vertex. Negative edges fine. Negative cycles create infinitely decreasing paths — distances become -infinity, algorithm can't terminate.",
        "difficulty": "Hard"
    },
    {
        "question": "Explain the exploration vs exploitation dilemma in Learning Agents",
        "answer": "Exploration: try new actions to discover better strategies (risk). Exploitation: use known good actions to maximize immediate reward. Balance needed — epsilon-greedy: explore with prob ε, exploit otherwise. Decrease ε over time.",
        "difficulty": "Hard"
    },
    {
        "question": "What is the difference between admissible and consistent heuristics in A*?",
        "answer": "Admissible: never overestimates true cost — guarantees optimal path. Consistent (monotonic): h(n) ≤ c(n,n') + h(n') — ensures each node processed once. Consistent implies admissible. Manhattan distance is both!",
        "difficulty": "Hard"
    },
    {
        "question": "Why is Quick Sort O(n²) in worst case and how to avoid it?",
        "answer": "Worst case when pivot is always min/max (already sorted array). Each partition puts only 1 element in correct position — n partitions of decreasing size = O(n²). Fix: random pivot, median-of-three, or use Introsort.",
        "difficulty": "Hard"
    },
    {
        "question": "What is the Bellman-Ford algorithm and when to use it over Dijkstra?",
        "answer": "Bellman-Ford finds shortest paths with negative edges — O(VE). Use instead of Dijkstra when: negative weight edges exist, need to detect negative cycles. Slower but more general than Dijkstra.",
        "difficulty": "Hard"
    },
    {
        "question": "Explain the Knapsack problem variants",
        "answer": "0/1 Knapsack: each item taken once — DP O(nW). Unbounded Knapsack: items can repeat — DP O(nW). Fractional Knapsack: can take fractions — Greedy O(n log n). Only fractional has greedy solution!",
        "difficulty": "Hard"
    },
    {
        "question": "What is Q-Learning and how does it work?",
        "answer": "Q-Learning is reinforcement learning algorithm. Q(s,a) = expected reward from state s taking action a. Update: Q(s,a) += lr*(r + γ*max Q(s',a') - Q(s,a)). Learns optimal policy without environment model.",
        "difficulty": "Hard"
    },
    {
        "question": "What is Monte Carlo Tree Search (MCTS)?",
        "answer": "MCTS builds game tree through random simulations. 4 steps: Selection (pick promising node), Expansion (add child), Simulation (random playout), Backpropagation (update scores). Used in AlphaGo — no need for evaluation function!",
        "difficulty": "Hard"
    },
    {
        "question": "Explain time-space tradeoff with an example",
        "answer": "Use more memory to reduce time (or vice versa). Example: Fibonacci — naive O(2^n) time O(1) space. Memoization: O(n) time O(n) space. Space-optimized DP: O(n) time O(1) space (only keep last 2 values).",
        "difficulty": "Hard"
    },
]