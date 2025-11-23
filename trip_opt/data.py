from dataclasses import dataclass
import numpy as np

@dataclass
class ItineraryData:
    city_names: list
    stay_cost_per_day: np.ndarray  # shape (n,)
    enjoyment_per_day: np.ndarray  # shape (n,)
    min_stay: np.ndarray           # shape (n,)
    max_stay: np.ndarray           # shape (n,)
    travel_time: np.ndarray        # shape (n, n)
    travel_cost: np.ndarray        # shape (n, n)
    total_trip_days: float
    budget: float
    travel_time_penalty: float = 0.1  # weight in objective for travel burden

    @property
    def n_cities(self):
        return len(self.city_names)


def generate_synthetic_data(seed: int = 42) -> ItineraryData:

    #City 0 is the 'home' city (no stay).
    
    rng = np.random.default_rng(seed)

    city_names = ["Home", "Paris", "Rome", "Berlin", "Barcelona", "Prague"]
    n = len(city_names)

    # Home has zero stay cost and enjoyment.
    stay_cost_per_day = np.array([0, 120, 100, 90, 110, 80], dtype=float)
    enjoyment_per_day = np.array([0, 9, 8, 7.5, 8.5, 7], dtype=float)

    # Minimum and maximum stays (days)
    min_stay = np.array([0, 1, 1, 1, 1, 1], dtype=float)
    max_stay = np.array([0, 4, 4, 4, 4, 4], dtype=float)

    # Travel time (days) and travel cost (one-way) between cities
    # Using random symmetric matrices with zeros on diagonal.
    base_times = rng.uniform(0.3, 1.2, size=(n, n))
    travel_time = (base_times + base_times.T) / 2.0
    np.fill_diagonal(travel_time, 0.0)

    base_costs = rng.uniform(80, 300, size=(n, n))
    travel_cost = (base_costs + base_costs.T) / 2.0
    np.fill_diagonal(travel_cost, 0.0)

    total_trip_days = 16.0   # Max vacation days (travel + stay)
    budget = 2500.0          # Total budget

    return ItineraryData(
        city_names=city_names,
        stay_cost_per_day=stay_cost_per_day,
        enjoyment_per_day=enjoyment_per_day,
        min_stay=min_stay,
        max_stay=max_stay,
        travel_time=travel_time,
        travel_cost=travel_cost,
        total_trip_days=total_trip_days,
        budget=budget,
        travel_time_penalty=0.1,
    )
