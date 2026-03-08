import stroop_experiments
import pytest

def test_determine_condition():
    '''
    determine_codition(word, color) should return:
        - "congruent" if the word meaning matches the displayed color
        - "incongruent" if the word meaning differs from the display color
    '''
    pass

def test_is_correct_response():
    '''
    is_correct_response(response, color) should return:
        - True if the participant's response matches the displayed color
        - else: False
    '''
    pass

def test_generate_trial():
    '''
    generate_trial() should return a dict representing a trial stimulus

    keys:
        - word: the text shown to participant
        - color: display color
        - condition: "congruent" or "incongruent"
    '''
    pass

def test_record_trial_result():
    '''
    record_trial_result() should create a trial result containing:
        - participant ID
        - word stimulus
        - color stimulus
        - condition (congruent/incongruent)
        - participant response
        - correctness (True/False)
        - reaction_time in seconds
    :return: result as a dict
    '''
    pass

def test_save_results_to_json():
    '''
    save_results_to_json(results, filepath) should write experiment results to JSON file at given filepath

    saved file should contain list of trial result dicts
    '''
    pass

def test_calculate_average_reaction_times():
    '''
    calculate_average_reaction_times(results) computes average reaction time for both congruent & incongruent trials
    :return: dict containing both averages
    '''
    pass