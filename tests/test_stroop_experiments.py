from stroop_experiments import *
import pytest, json

def test_determine_condition():
    """
    determine_condition(word, color) should return:
        - "congruent" if the word meaning matches the displayed color
        - "incongruent" if the word meaning differs from the display color
    """
    assert determine_condition("red", "red") == "congruent"
    assert determine_condition("blue", "blue") == "congruent"

    with pytest.raises(TypeError):
        determine_condition(1, "red")
    with pytest.raises(TypeError):
        determine_condition("blue", 1)


def test_is_correct_response():
    """
    is_correct_response(response, color) should return:
        - True if the participant's response matches the displayed color
        - else: False
    """

    assert is_correct_response("red", "red") == True
    assert is_correct_response("red", "blue") == False

    with pytest.raises(TypeError):
        is_correct_response(1, "red")

def test_generate_trial():
    """
    generate_trial() should return a dict representing a trial stimulus

    keys:
        - word: the text shown to participant
        - color: display color
        - condition: "congruent" or "incongruent"
    """

    trial = generate_trial()

    assert type(trial) == dict
    assert "word" in trial
    assert "color" in trial
    assert "condition" in trial

    assert trial["condition"] in ["congruent", "incongruent"]


def test_record_trial_result():
    """
    record_trial_result() should create a trial result containing:
        - participant ID
        - word stimulus
        - color stimulus
        - condition (congruent/incongruent)
        - participant response
        - correctness (True/False)
        - reaction_time in seconds
    :return: result as a dict
    """

    result = record_trial_result("P01", "red", "blue", "incongruent", "blue", 0.75)

    assert result["participant"] == "P01"
    assert result["word"] == "red"
    assert result["color"] == "blue"
    assert result["condition"] == "incongruent"
    assert result["response"] == "blue"
    assert result["reaction_time"] == 0.75


def test_calculate_average_reaction_times():
    """
    calculate_average_reaction_times(results) computes average reaction time for both congruent & incongruent trials
    :return: dict containing both averages
    """

    data = [{"condition": "congruent", "reaction_time": 0.5}, {"condition": "congruent", "reaction_time": 0.9},
            {"condition": "incongruent", "reaction_time": 1.2}, {"condition": "incongruent", "reaction_time": 1.7}]

    result = calculate_average_reaction_times(data)

    assert result["congruent"] == 0.7
    assert result["incongruent"] == 1.45

    with pytest.raises(ValueError):
        calculate_average_reaction_times([])
    with pytest.raises(ValueError):
        calculate_average_reaction_times([{}])


def test_save_results_to_json():
    """
    save_results_to_json(results, filepath) should write experiment results to JSON file at given filepath

    saved file should contain list of trial result dicts
    """

    results = [{"word": "red"}]

    filepath = "test/test_saved_json_file.json"

    save_results_to_json(results, filepath)

    with open(filepath) as f:
        data = json.load(f)

    assert data == results
