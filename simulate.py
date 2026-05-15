import numpy as np
import pandas as pd


np.random.seed(42)

print("\nSimulation Started...\n")


# GINI FUNCTION

def gini(array):

    array = np.sort(array)

    n = len(array)

    cumulative = np.cumsum(array)

    return (
        n + 1
        - 2 * np.sum(cumulative) / cumulative[-1]
    ) / n

# LORENZ CURVE FUNCTION

def lorenz_curve(wealth):

    sorted_wealth = np.sort(wealth)

    cumulative_wealth = np.cumsum(
        sorted_wealth
    )

    cumulative_wealth = (
        cumulative_wealth
        / cumulative_wealth[-1]
    )

    cumulative_population = np.arange(
        1,
        len(sorted_wealth) + 1
    ) / len(sorted_wealth)

    return (
        cumulative_population,
        cumulative_wealth
    )

# MAIN SIMULATION FUNCTION

def run_simulation(
    system_name,
    tax_threshold=None,
    tax_rate=0,
    welfare_threshold=None,
    redistribution_frequency=1000,
    rounds=100000
):

    print(f"\nStarting {system_name}...\n")

    wealth = np.full(1000, 1000.0)

    checkpoints = [
        1000,
        2000,
        5000,
        10000,
        20000,
        50000,
        100000
    ]

    results = {
        'Rounds': [],
        'Median Wealth': [],
        'Top 10% Wealth Share': [],
        'Gini Coefficient': [],
        'Poverty Percentage': []
    }


    # MAIN LOOP

    for round_num in range(1, rounds + 1):

      
        # PROGRESS LOG

        if round_num % 5000 == 0:

            print(
                f"{system_name} running..."
                f" Round {round_num}/{rounds}"
            )

        # TRANSACTIONS

        for _ in range(100):

            a, b = np.random.choice(
                1000,
                2,
                replace=False
            )

            if wealth[a] <= 0 or wealth[b] <= 0:
                continue

            poorer_wealth = min(
                wealth[a],
                wealth[b]
            )

            stake = 0.05 * poorer_wealth

            if stake < 1:
                continue

            wealth[a] -= stake
            wealth[b] -= stake

            winner = np.random.choice([a, b])

            wealth[winner] += 2 * stake

        # REDISTRIBUTION

        if (
            tax_rate > 0 and
            round_num % redistribution_frequency == 0
        ):

            rich_agents = wealth > tax_threshold

            taxable_surplus = (
                wealth[rich_agents]
                - tax_threshold
            )

            taxes = taxable_surplus * tax_rate

            wealth[rich_agents] -= taxes

            tax_pool = taxes.sum()

            poor_agents = wealth < welfare_threshold

            num_poor = poor_agents.sum()

            if num_poor > 0:

                redistribution = (
                    tax_pool / num_poor
                )

                wealth[poor_agents] += redistribution

        # CHECKPOINT METRICS

        if round_num in checkpoints:

            print(
                f"{system_name}: "
                f"Analyzing Round {round_num}"
            )

            sorted_wealth = np.sort(
                wealth
            )[::-1]

            total_wealth = sorted_wealth.sum()

            median_wealth = np.median(
                sorted_wealth
            )

            top_10_share = (
                sorted_wealth[:100].sum()
                / total_wealth
            ) * 100

            gini_coeff = gini(
                sorted_wealth
            )

            poverty_percent = (
                np.sum(wealth < 200)
                / 1000
            ) * 100

            results['Rounds'].append(
                round_num
            )

            results['Median Wealth'].append(
                round(median_wealth, 2)
            )

            results['Top 10% Wealth Share'].append(
                round(top_10_share, 2)
            )

            results['Gini Coefficient'].append(
                round(gini_coeff, 4)
            )

            results['Poverty Percentage'].append(
                round(poverty_percent, 2)
            )

    print(f"\n{system_name} Completed.\n")

    df = pd.DataFrame(results)

    return df, wealth

# SIMULATIONS

free_market_df, free_final = run_simulation(
    system_name='Free Market'
)

welfare_df, welfare_final = run_simulation(
    system_name='Welfare Society',
    tax_threshold=1500,
    tax_rate=0.15,
    welfare_threshold=500,
    redistribution_frequency=1000
)

egalitarian_df, egalitarian_final = run_simulation(
    system_name='Egalitarian Utopia',
    tax_threshold=1200,
    tax_rate=0.45,
    welfare_threshold=700,
    redistribution_frequency=500
)

# COMPARISON TABLE

comparison_df = pd.DataFrame({

    'Rounds':
        free_market_df['Rounds'],

    'Free Median':
        free_market_df['Median Wealth'],

    'Welfare Median':
        welfare_df['Median Wealth'],

    'Egalitarian Median':
        egalitarian_df['Median Wealth'],

    'Free Top10':
        free_market_df['Top 10% Wealth Share'],

    'Welfare Top10':
        welfare_df['Top 10% Wealth Share'],

    'Egalitarian Top10':
        egalitarian_df['Top 10% Wealth Share'],

    'Free Gini':
        free_market_df['Gini Coefficient'],

    'Welfare Gini':
        welfare_df['Gini Coefficient'],

    'Egalitarian Gini':
        egalitarian_df['Gini Coefficient'],

    'Free Poverty':
        free_market_df['Poverty Percentage'],

    'Welfare Poverty':
        welfare_df['Poverty Percentage'],

    'Egalitarian Poverty':
        egalitarian_df['Poverty Percentage']
})

# LORENZ CURVE DATA

free_x, free_y = lorenz_curve(
    free_final
)

welfare_x, welfare_y = lorenz_curve(
    welfare_final
)

egalitarian_x, egalitarian_y = lorenz_curve(
    egalitarian_final
)

lorenz_df = pd.DataFrame({

    'Population Share':
        free_x,

    'Free Market':
        free_y,

    'Welfare Society':
        welfare_y,

    'Egalitarian Utopia':
        egalitarian_y
})

# CSV FILES

print("\nSaving CSV Files...\n")

free_market_df.to_csv(
    'free_market.csv',
    index=False
)

welfare_df.to_csv(
    'welfare_society.csv',
    index=False
)

egalitarian_df.to_csv(
    'egalitarian_utopia.csv',
    index=False
)

comparison_df.to_csv(
    'comparison.csv',
    index=False
)

lorenz_df.to_csv(
    'lorenz.csv',
    index=False
)

print("\nAll CSV Files Generated Successfully.\n")
