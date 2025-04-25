import random
import numpy as np
import matplotlib.pyplot as plt

def random_walk_cgraph(graph_size ,steps):
    x_pos = 0
    probabilities = [-1, 1]
    x_li = [x_pos]

    for i in range(steps):
        x_pos += random.choice(probabilities)
        x_li.append(x_pos % graph_size)

    return x_li

# Test
# print(random_walk_cgraph(5, 10))

def plot_prob(graph_size, steps):
    visit_counts = np.zeros(graph_size)

    node_visits = random_walk_cgraph(graph_size, steps)
    # print(node_visits)
    for node in node_visits:
        visit_counts[node] += 1

    node_prob = visit_counts/steps

    plt.bar(range(graph_size), node_prob, color='b', alpha=0.7)
    plt.xlabel("Node")
    plt.ylabel("Probability")
    plt.title(f"Probability Distribution After {steps} Steps")
    plt.xticks(range(graph_size))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

plot_prob(5, 1000)



# old test stuff
# newlist = {i : [(i, (i-1)%5),(i, (i+1)%5)] for i in range(5)}

# newlist = {i : [] for i in range(5)}

# for i in range(5):
#     newlist[i].append((i, (i-1)%5))
#     newlist[i].append((i, (i+1)%5))

# print(newlist)

# def gen_cycle_graph(n):
#     # graph with node(key):list of edges(value)
#     graph = {i : [] for i in range(n)}
    
#     for i in range(n):
#         graph[i].append((i, (i-1)%n))
#         graph[i].append((i, (i+1)%n))
#     return graph