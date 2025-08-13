# Subjective rating experiment

## Overview

This is a demo of a 'subjective rating experiment' using the PsyNet framework.
The subjective rating experiment is one of the simplest kinds of perceptual experiments.
We present participants with a series of stimuli, one at a time, and ask them to rate the stimulus on one or more numeric scales.

In this demo, the stimuli are instrument sounds, which we store within the `data/instrument_sounds` directory. We have participants rate these sounds for 
brightness and roughness.

## Running the experiment

The simplest way to work with this experiment is to run it in GitHub Codespaces.
To do so, navigate to the repository page in GitHub (you might be looking at it already),
and click the green "Code" button, click "Codespaces", and then click "Create codespace on main". The codespace will take a while to start up, because it needs to install the 
dependencies, but don't worry, this is a one-time process. Once the codespace is ready, you 
can then launch the experiment in debug mode by running the following command in the terminal:

```bash
psynet debug local
```

Wait a moment, and then a browser window should open containing a link to the dashboard.
Click it, then enter 'admin' as the username as password, then press OK.
You'll now see the experiment dashboard.
Click 'Development', then 'New participant', to create a link to try the experiment 
as a participant.

