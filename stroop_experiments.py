import random, json
experiment_words = ["red", "blue", "green", "yellow"]

def determine_condition(word, color):
    """
    Determines whether a Stroop Trial is congruent or incongruent.

    A trial is congruent when the meaning of the word matches the display
    color (e.g. "red" as red). Otherwise, it's considered incongruent.

    :param word: Text stimulus presented, as a string.
    :param color: Display color of word, as a string.
    :return: "congruent" or "incongruent", as strings.
    :raises: Type error if either param is not a string.
    """

    if type(word) != str or type(color) != str:
        raise TypeError("Arguments must be strings")

    return "congruent" if word == color else "incongruent"


def is_correct_response(response, color):
    """
    Determines whether a participant responded with the correct color.

    :param response: Participant's typed response, as a str.
    :param color: Correct display of color, as a str.
    :return: bool True/False
    :raises: TypeError if either param isn't a str.
    """

    if type(response) != str or type(color) != str:
        raise TypeError("Arguments must be strings")

    return response == color


def generate_trial():
    """
    Generates random Stroop Trial stimulus.

    Trials consist of randomly selected word & display color.
    Trial condition is determined based on determine_condition(word, color).

    :return: dict containing trial stimulus with keys word (str), color (str), and condition (str).
    """

    word_index = random.randrange(len(experiment_words))
    color_index = random.randrange(len(experiment_words))

    word = experiment_words[word_index]
    color = experiment_words[color_index]

    condition = determine_condition(word, color)

    return {"word": word, "color": color, "condition": condition}

    raise NotImplementedError("Not yet implemented")


def record_trial_result(participant, word, color, condition, response, reaction_time):
    """
    Records the results of completed Stroop Trial.

    :param participant: participant ID, as a str.
    :param word: Stimulus shown, as str.
    :param color: Display color, as str.
    :param condition: "congruent"/"incongruent", as str.
    :param response: Participant's typed response, as str.
    :param reaction_time: Time taken to respond in seconds, as a float.
    :return: dict representing the full trial result
    """

    correct = is_correct_response(response, color)

    return {"participant": participant, "word": word, "color": color,
            "condition": condition, "response": response, "correct": correct,
            "reaction_time": reaction_time}

    raise NotImplementedError("Not yet implemented")


def calculate_average_reaction_times(results):
    """
    Computes average reaction times for congruent & incongruent trials.

    :param results: list of dicts containing keys "condition" and "reaction_time"
    :return: dict containing average reaction times as floats
    :raises: ValueError if list is empty OR if dict in list is empty
    """

    if len(results) < 1:
        raise ValueError("Results cannot be empty")

    congruent = []
    incongruent = []

    for trial in results:
        if len(trial) < 1:
            raise ValueError("Trial dict cannot be empty")

        if trial["condition"] == "congruent":
            congruent.append(trial["reaction_time"])
        else:
            incongruent.append(trial["reaction_time"])

    return {"congruent": sum(congruent)/len(congruent),
            "incongruent": sum(incongruent)/len(incongruent)}

    raise NotImplementedError("Not yet implemented")


def save_results_to_json(results, filepath):
    """
    Saves experiment results to JSON file.
    :param results: list of dicts containing trial results
    :param filepath: where to write JSON file
`    """
    raise NotImplementedError("Not yet implemented")