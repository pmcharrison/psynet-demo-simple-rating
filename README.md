# Subjective rating experiment

## Overview

This is a demo of a 'subjective rating experiment' using the PsyNet framework.
The subjective rating experiment is one of the simplest kinds of perceptual experiments.
We present participants with a series of stimuli, one at a time, and ask them to rate the stimulus on one or more numeric scales.

In this demo, the stimuli are instrument sounds, which we store within the `data/instrument_sounds` directory. We have participants rate these sounds for
brightness and roughness.

## Running the experiment

### GitHub Codespaces

The simplest way to work with this experiment is to run it in GitHub Codespaces.
To do so, navigate to the repository page in GitHub (you might be looking at it already),
and click the green "Code" button, click "Codespaces", and then click "Create codespace on main". The codespace will take a while to start up, because it needs to install the
dependencies, but don't worry, this is a one-time process. Once the codespace is ready, you
can then launch the experiment in debug mode by running the following command in the terminal:

```bash
psynet debug local
```

Wait a moment, and then a browser window should open containing a link to the dashboard.
Click it, then enter 'admin' as both username and password, then press OK.
You'll now see the experiment dashboard.
Click 'Development', then 'New participant', to create a link to try the experiment
as a participant.

### Devcontainer in VSCode/Cursor

It is possible to spin up a similar development locally if you are using an IDE
with Devcontainers support (e.g. VSCode, Cursor).

1. Download the repository to your local machine using `git clone`.
2. Open the repository in your IDE.
3. Accept the prompt that asks whether you want to open the repository in Devcontainers.

### Locally in a virtual environment

If you don't want to use Docker, then you can instead run this demo locally in a virtual environment.
This is more involved as you have to install several related dependencies like Redis and PostgreSQL.
To do so, navigate to the [PsyNet website](https://psynet.dev) and follow the 'virtual environment'
installation instructions. We recommend using Python 3.12.10 for this (or double-check the recommended
version of Python specified in the `pyproject.toml` file in the PsyNet source directory).
