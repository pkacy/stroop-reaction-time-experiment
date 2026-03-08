from stroop_experiments import generate_trial, record_trial_result, save_results_to_json

manual_entry_result_file = "results/manual_entry_stroop_results.json"
automated_entry_result_file = "results/automated_entry_stroop_results.json"

def run_experiment(num_trials):
    import time, random, json

    participant = input("Enter participant ID: ")
    try:
        with open(manual_entry_result_file, "r") as f:
            results = json.load(f)
    except FileNotFoundError:
        results = []

    print("\nType the color of the word shown.\n")

    for trial_num in range(num_trials):
        trial = generate_trial()

        word = trial["word"]
        color = trial["color"]
        condition = trial["condition"]

        print("Trial " + str(trial_num + 1) + ":")
        print("Word: " + word.upper())

        start = time.time()

        response = input("Color: ").strip()
        response.lower()

        reaction_time = round(time.time() - start, 2)

        trial_result = record_trial_result(participant, word, color, condition, response, reaction_time)

        results.append(trial_result)

    save_results_to_json(results, manual_entry_result_file)

    print("\nExperiment complete.")
    print("Results saved to " + manual_entry_result_file)


def simulate_experiment(num_participants, trials_per_participant):

    import json, random

    try:
        with open(automated_entry_result_file, "r") as f:
            results = json.load(f)
    except FileNotFoundError:
        results = []

    for i in range(num_participants):
        num = i + 1

        if num < 10:
            participant = "P0" + str(num)
        else:
            participant = "P" + str(num)

        for trial_num in range(trials_per_participant):
            trial = generate_trial()

            word = trial["word"]
            color = trial["color"]
            condition = trial["condition"]

            if condition == "congruent":
                reaction_time = round(0.45 + random.random() * 0.15, 2)
            else:
                reaction_time = round(0.65 + random.random() * 0.25, 2)

            response = color

            trial_result = record_trial_result(participant, word, color, condition, response, reaction_time)

            results.append(trial_result)

    save_results_to_json(results, automated_entry_result_file)

    print("\nSimulation complete.")
    print("Total trials:", len(results))


if __name__ == "__main__":
    # run_experiment(50)     # manual data entry
    # simulate_experiment(40, 20)     # automated dataset
