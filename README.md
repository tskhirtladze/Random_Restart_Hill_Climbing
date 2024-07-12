# Travelling Salesperson Problem Solver

This Python script solves the Travelling Salesperson Problem (TSP) using a randomized hill climbing algorithm with random restarts. It calculates the shortest possible tour that visits all given destinations and returns to the starting point.

## Description
The script includes the following functionalities:

Distance Calculation: Uses the Haversine formula to compute the distance between pairs of destinations based on their latitude and longitude coordinates.

Random Tour Generation: Generates a random tour (permutation of destinations).

Tour Length Calculation: Calculates the total distance of a given tour based on the precomputed distance matrix.

Random Restart Hill Climbing: Optimizes the tour using a randomized hill climbing approach:

Starts with a random tour.
Iteratively swaps elements to find shorter tours.
Uses random restarts to avoid local minima.

Output: Prints the best tour found and its length in kilometers.

Dependencies
This script requires Python 3.x with standard libraries math, itertools, and random.

## Usage
To execute the script, simply run it in a Python environment:
python rrhc.py

## Example Output
The script outputs the distance matrix and the best tour found along with its length:

Distance Matrix:
Dam Square to Rijksmuseum: 1.43 km
Dam Square to Anne Frank House: 0.61 km
Dam Square to Van Gogh Museum: 1.60 km
Dam Square to Vondelpark: 1.91 km
Dam Square to Red Light District: 0.61 km
Rijksmuseum to Anne Frank House: 1.67 km
Rijksmuseum to Van Gogh Museum: 0.77 km
Rijksmuseum to Vondelpark: 1.55 km
Rijksmuseum to Red Light District: 1.30 km
Anne Frank House to Van Gogh Museum: 1.74 km
Anne Frank House to Vondelpark: 1.90 km
Anne Frank House to Red Light District: 1.42 km
Van Gogh Museum to Vondelpark: 1.21 km
Van Gogh Museum to Red Light District: 1.09 km
Vondelpark to Red Light District: 1.28 km

Best tour: ['Anne Frank House', 'Rijksmuseum', 'Van Gogh Museum', 'Dam Square', 'Red Light District', 'Vondelpark']
Length of the tour: 6.73 km

## Notes
Ensure that the latitude and longitude coordinates in the destinations dictionary are accurate for correct distance calculations.
Adjust the num_restarts parameter in random_restart_hill_climbing function for potentially better results at the cost of computation time.

## Author
This script was written by Tornike Skhirtladze.
