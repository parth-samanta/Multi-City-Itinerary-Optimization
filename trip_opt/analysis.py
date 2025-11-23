from .data import ItineraryData
from .solver import ItinerarySolution

def print_solution(data: ItineraryData, sol: ItinerarySolution) -> None:
    if sol.status not in ("optimal", "optimal_inaccurate"):
        print(f"Solver status: {sol.status}")
        print("No feasible itinerary found.")
        return

    print("==== Optimised Holiday Itinerary ====")
    print(f"Solver status      : {sol.status}")
    print(f"Objective (utility): {sol.objective_value:.2f}")
    print(f"Total trip time    : {sol.total_time:.2f} days")
    print(f"Total trip cost    : {sol.total_cost:.2f}")
    print(f"  - Stay cost      : {sol.stay_cost:.2f}")
    print(f"  - Travel cost    : {sol.travel_cost:.2f}")
    print()

    # Route
    names = data.city_names
    if sol.route_indices:
        route_names = " → ".join(names[i] for i in sol.route_indices)
        print("Route:")
        print("  ", route_names)
        print()

    # City-wise details
    print("City-wise stay plan:")
    print(f"{'City':15s} {'Selected':>8s} {'Stay (days)':>12s}")
    print("-" * 40)
    for i, name in enumerate(names):
        selected = "Yes" if i in sol.selected_indices or i == 0 else "No"
        if sol.stay_days is None:
            stay = 0
        else:
            # Round, clip tiny negatives
            stay = int(round(sol.stay_days[i]))
            if stay < 0:
                stay = 0
        print(f"{name:15s} {selected:>8s} {stay:12d}")

