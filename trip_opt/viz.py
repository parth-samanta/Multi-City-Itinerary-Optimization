import matplotlib.pyplot as plt
import numpy as np
from .data import ItineraryData
from .solver import ItinerarySolution


def plot_stay_durations(data: ItineraryData, sol: ItinerarySolution) -> None:
    if sol.stay_days is None:
        print("No stay information to plot.")
        return

    # Only plot cities where we actually stay
    city_indices = [i for i in range(data.n_cities) if sol.stay_days[i] > 1e-3]
    if not city_indices:
        print("No stays to plot.")
        return

    city_names = [data.city_names[i] for i in city_indices]
    stays = [sol.stay_days[i] for i in city_indices]

    x = np.arange(len(city_names))
    plt.figure()
    plt.bar(x, stays)
    plt.xticks(x, city_names, rotation=45, ha="right")
    plt.ylabel("Stay duration (days)")
    plt.title("Optimised Stay Duration per City")
    plt.tight_layout()
    plt.show()


def plot_budget_allocation(data: ItineraryData, sol: ItinerarySolution) -> None:
    #Plot of budget allocation between stay cost, travel cost,
    #and unused budget.

    if sol.stay_cost is None or sol.travel_cost is None or sol.total_cost is None:
        print("No cost information to plot.")
        return

    stay_cost = sol.stay_cost
    travel_cost = sol.travel_cost
    total_cost = sol.total_cost
    budget = data.budget

    unused = max(budget - total_cost, 0.0)

    labels = ["Stay", "Travel", "Unused budget"]
    values = [stay_cost, travel_cost, unused]

    plt.figure()
    x = np.arange(len(labels))
    plt.bar(x, values)
    plt.xticks(x, labels, rotation=15)
    plt.ylabel("Amount (currency units)")
    plt.title("Budget Allocation")
    plt.tight_layout()
    plt.show()

def plot_budget_sensitivity(budgets, objectives) -> None:
    #Plot how the optimal objective changes as the budget varies.

    import numpy as np
    import matplotlib.pyplot as plt

    budgets = np.array(budgets, dtype=float)
    objectives = np.array(objectives, dtype=float)

    plt.figure()
    plt.plot(budgets, objectives, marker="o")
    plt.xlabel("Budget")
    plt.ylabel("Optimal Objective Value")
    plt.title("Budget Sensitivity Analysis")
    plt.grid(True)
    plt.tight_layout()
    plt.show()



