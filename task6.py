FRIENDS = {
    "Aisha": ["Ben", "Carla"],
    "Ben":   ["Aisha", "Dev"],
    "Carla": ["Aisha", "Dev"],
    "Dev":   ["Ben", "Carla", "Eli"],
    "Eli":   ["Dev"],
}

def add_person(graph, name):
    if name not in graph:
        graph[name] = []

def add_friendship(graph, a, b):
    add_person(graph, a)
    add_person(graph, b)
    if b not in graph[a]:
        graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)

def print_friends(graph):
    print("\nFriends List:")
    print("-" * 30)
    for person, friends in graph.items():
        print(f"  {person} → {friends}")

def friends_count(graph, name):
    """Return the number of friends for a person."""
    if name in graph:
        return len(graph[name])
    return 0

def are_friends(graph, a, b):
    """Check if two people are friends."""
    if a in graph and b in graph[a]:
        return True
    return False

def most_friends(graph):
    """Find the person with the most friends."""
    most_popular = None
    max_friends = -1
    
    for person, friends in graph.items():
        if len(friends) > max_friends:
            max_friends = len(friends)
            most_popular = person
    
    return most_popular, max_friends

# Test
print_friends(FRIENDS)

print("\nAisha's friend count:", friends_count(FRIENDS, "Aisha"))

print("are Aisha and Ben friends?", are_friends(FRIENDS, "Aisha", "Ben"))

person, count = most_friends(FRIENDS)
print("Person with most friends:", person)
print("No. of Friends:", count)