## File Description
- synthnet.py : Contains functions for generation of synthetic networks
- gui/guimaker.py : Contains classes and functions for creating GUI quickly
- simulation.py : Contains functions for simulation of cluster evolution
- example.ipynb : A toy simulation with all functions in place
- main.py : Contains functions to build the gui using guimaker and to call functions in synthnet.py to initialize and build the synthetic network

## Usage
```python
from usagsp import *

n = 100
G = get_empty_graph(100)
af(G)
av(G)

threshold = 0.8

make_init_connections(G, threshold)

aa(G)

H = G.copy()

H = simulate_one_time_step(H, threshold, 1) # Run this as many times as you want

# Summary of commonness between different clusters
ppanalyse(analyse(H, get_clusters(H)), np.mean) # Gives mean commonness between clusters
```
