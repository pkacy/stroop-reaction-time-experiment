# Stroop Reaction Time Experiment

This project simulates and analyzes a classic **Stroop cognitive psychology experiment** 
using Python.

The Stroop effect demonstrates how **conflicting visual input slows reaction time**. 
In this experiment, participants have to identify the **color of a word**, instead of 
the word itself. When the word and its display color conflict (e.g., the word *RED* 
displayed in the color blue), reaction times tend to be slower.

Read more about the Stroop effect *[here](https://www.apa.org/research-practice/conduct-research/stroop-effect)*

### This project includes tools to:

- Generate Stroop trials
- Record participant responses
- Simulate experimental data
- Store results in JSON
- Analyze differences in reaction time between conditions (congruent/incongruent)

---

## Experiment Overview

Each trial presents a **word stimulus** and a **display color**.

The participant must respond with the **display color**, not the word.

### Congruent

**WORD:** RED

**Color:** red


### Incongruent

**WORD:** RED

**Color:** yellow

Reaction times for incongruent trials are typically **longer** due to cognitive interference.

---

## Running/Simulating the Experiment

### In run_experiment.py, you can:

### Run a manual experiment with user input:

```python
run_experiment(50)
```
**Results are saved to:** 'results/manual_entry_stroop_results.json'

### OR

### Run an automated experiment with randomized data:

```python
simulate_experiment(40, 20)
```

**Results are saved to:** 'results/automated_entry_stroop_results.json'

### Example output:

40 participants × 20 trials = 800 trials

Participants are automatically generated:

P01 P02 P03 ... P40

---

## Testing

This project uses **pytest**.

---

## Concepts
This project combines **computer science** and **cognitive psychology** concepts, including:

- Experimental design
- Behavioral data collection
- Reaction time analysis
- Automated testing (pytest)
- JSON data storage
- Simulation of experimental datasets

---

## Improvements

Some possible improvements are:
- **Visual stimulus presented using a GUI or colors**
  - The Stroop effect is based on color interference during each trial. 
  Right now, my code does not show different colors for each trial. My
  code could be improved by adding some sort of color effect so that
  the colors show up correctly during each trial.
- **Reaction time distribution graphs**
  - Another improvement would be presenting the data with graphs.
  Reaction time distributions could be plotted on a bar chart or histogram 
  to show the differences between congruent and incongruent trials and 
  help visualize the experiment results more clearly.

---

### Author

Piper Hanrahan

Psychology Major, Computer Science Minor

Ithaca College

Stroop Reaction Time - GitHub: https://github.com/pkacy/stroop-reaction-time-experiment

GitHub Profile: https://github.com/pkacy

---

*This project is for educational and research purposes.*