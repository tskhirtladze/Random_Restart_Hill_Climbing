import math
import itertools
import random


# Define the destinations and their coordinates (latitude, longitude)
destinations = {
    'Dam Square': (52.3731, 4.8922),
    'Rijksmuseum': (52.3600, 4.8852),
    'Anne Frank House': (52.3752, 4.8817),
    'Van Gogh Museum': (52.3584, 4.8816),
    'Vondelpark': (52.3582, 4.8687),
    'Red Light District': (52.3722, 4.8969)
}

# Function to calculate distance between two points using Haversine formula
def calculate_distance(dest1, dest2):
    lat1, lon1 = dest1
    lat2, lon2 = dest2
    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Earth's radius in kilometers
    R = 6371.0

    # Haversine formula
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance

# Precompute distances between all pairs of destinations
distance_matrix = {}
for dest1, dest2 in itertools.combinations(destinations.keys(), 2):
    dist = calculate_distance(destinations[dest1], destinations[dest2])
    distance_matrix[(dest1, dest2)] = dist
    distance_matrix[(dest2, dest1)] = dist

# Print the distance matrix (optional)
print("Distance Matrix:")
for (dest1, dest2), dist in distance_matrix.items():
    print(f"{dest1} to {dest2}: {dist:.2f} km")


def generate_random_tour(destinations):
    tour = list(destinations.keys())
    random.shuffle(tour)
    return tour

def calculate_tour_length(tour, distance_matrix):
    total_distance = 0
    num_destinations = len(tour)
    for i in range(num_destinations):
        total_distance += distance_matrix[(tour[i], tour[(i + 1) % num_destinations])]
    return total_distance

def random_restart_hill_climbing(destinations, distance_matrix, num_restarts=1000):
    best_tour = None
    best_tour_length = float('inf')

    for _ in range(num_restarts):
        current_tour = generate_random_tour(destinations)
        current_length = calculate_tour_length(current_tour, distance_matrix)

        improved = True
        while improved:
            improved = False
            for i in range(len(current_tour)):
                for j in range(i + 1, len(current_tour)):
                    new_tour = current_tour[:]
                    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                    new_length = calculate_tour_length(new_tour, distance_matrix)

                    if new_length < current_length:
                        current_tour = new_tour
                        current_length = new_length
                        improved = True

        if current_length < best_tour_length:
            best_tour = current_tour
            best_tour_length = current_length

    return best_tour, best_tour_length

# Run the algorithm
best_tour, best_length = random_restart_hill_climbing(destinations, distance_matrix)

# Output the best tour found
print("Best tour:", best_tour)
print(f"Length of the tour: {best_length:.2f} km")
