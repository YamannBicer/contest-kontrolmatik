import os
import importlib
import pandas as pd

print("test_chsnge")





input_folder = "inputs"
result_file = "results.csv"
contenders_folder = "contenders"


def evaluate_algorithms(input_folder, results_csv, contenders_folder):
    results = []

    # read input
    input_file = os.path.join(input_folder, "input0.csv")
    df = pd.read_csv(input_file)
    price_list = df['electricity_price'].tolist()

    # evaulate each algorithm
    for file in os.listdir(contenders_folder):
        if file.endswith(".py"):
            contender_name = file[:-3]
            contender_module = importlib.import_module(f"{contenders_folder}.{contender_name}")

            # run contenders algorithm
            balance = contender_module.algorithm(price_list)

            # save result
            results.append((contender_name, balance))

    # sort contenders by profit
    results.sort(key=lambda x: x[1], reverse=True)

    # write results to csv
    df = pd.DataFrame(results, columns=["Participant", "Profit"])
    df.to_csv(results_csv, index=False)
    print("results saved to csv")


if __name__ == "__main__":
    evaluate_algorithms(input_folder, result_file, contenders_folder)
