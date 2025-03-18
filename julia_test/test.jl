using QuantumWalk
using LightGraphs
using SparseArrays  # Ensure sparse matrix operations

# Define a 4-node cycle graph
n = 4
graph = SimpleGraph(n)
for i in 1:n
    add_edge!(graph, i, mod(i, n) + 1)
end

# Compute the degree vector
deg = degree(graph)

# Construct the row-normalized stochastic matrix
A = adjacency_matrix(graph)  # Get adjacency matrix
P = spzeros(Float64, n, n)  # Create a sparse stochastic matrix

for i in 1:n
    if deg[i] > 0
        P[i, :] = A[i, :] ./ deg[i]  # Normalize by degree
    end
end

# Define Szegedy Quantum Walk
szegedy = Szegedy(graph, P)

# Initial state
initial_state = zeros(Complex{Float64}, n^2)
initial_state[1] = 1.0 + 0.0im  # Start at node 1

# Quantum walk evolution
evolution_operator = QWEvolution(szegedy)
final_state = evolve(evolution_operator, initial_state)
# final_state = evolution_operator * initial_state

# Compute probability distribution
probabilities = [sum(abs2, final_state[(i-1)*n+1:i*n]) for i in 1:n]

# Print the final probability distribution
println("Final probabilities: ", probabilities)
