g = nx.erdos_renyi_graph(5, 0.5)

print(g.nodes)

print(g.edges)


pos = {0: (-2, 0.5), 1: (0, 0), 2: (-1, 0.3), 3: (2, 0.17), 4: (4, 0.255), 5: (5, 0.03)}


options = {
    "font-size": 36,
    "node-size": 2000,
    "node_color": "black",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
}

nx.draw_networkx(g, pos, options)

ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()

