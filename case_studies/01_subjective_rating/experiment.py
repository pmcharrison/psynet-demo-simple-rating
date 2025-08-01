from pathlib import Path
import random
import psynet.experiment
from psynet.asset import asset  # noqa
from psynet.modular_page import (
    AudioPrompt,
    ModularPage,
    SurveyJSControl,
)
from psynet.page import InfoPage
from psynet.timeline import Event, Timeline
from psynet.trial.static import StaticNode, StaticTrial, StaticTrialMaker

# TODO: Basic data preview -- make a good default from PsyNet?
# TODO: Fix linter errors


# TODO: Wrap in Python classes
RATING_SCALES= [
    {
        "name": "brightness",
        "min": 0,
        "max": 5,
        "min_description": "Dark",
        "max_description": "Bright",
    },
    {
        "name": "roughness",
        "min": 0,
        "max": 5,
        "min_description": "Smooth",
        "max_description": "Rough",
    },
]

# TODO: Good way to avoid hardcoding?
N_TRIALS_PER_PARTICIPANT = 6  # <- set to correspond to the number of stimuli

def list_stimuli():
    stimulus_dir = Path(__file__).parent.parent / "resources" / "instrument_sounds"
    return [
        {
            "name": path.stem,
            "path": path,
        }
        for path in list(stimulus_dir.glob("*.mp3"))
    ]

# Run `python3 experiment.py` to list the stimuli.
if __name__ == "__main__":
    stimuli = list_stimuli()
    print(f"Found {len(stimuli)} stimuli:")
    for stimulus in stimuli:
        print(f"- {stimulus['name']}")


def get_nodes():
    return [
        StaticNode(
            definition={
                "stimulus_name": stimulus["name"]
            },
            assets={
                "stimulus_audio": asset(
                    stimulus["path"],
                    extension=".mp3",
                    cache=True,  # reuse the uploaded file between deployments
                )
            },
        )
        for stimulus in list_stimuli()
    ]


class CustomTrial(StaticTrial):
    time_estimate = 10

    def show_trial(self, experiment, participant):
        return ModularPage(
            "ratings",
            AudioPrompt(
                self.assets["stimulus_audio"],
                "Please rate the sound. You can replay it as many times as you like.",
                controls={"Play from start": "Replay"}
            ),
            SurveyJSControl(
                # See https://surveyjs.io/create-free-survey
                {
                    "elements": [
                        {
                            "type": "rating",
                            "name": scale["name"],
                            "title": scale["name"].capitalize(),
                            "isRequired": True,
                            "minRateDescription": scale["min_description"],
                            "maxRateDescription": scale["max_description"],
                            "rateMin": scale["min"],
                            "rateMax": scale["max"],
                        }
                        for scale in RATING_SCALES
                    ]
                },
                bot_response={
                    scale["name"]: random.choice(range(scale["min"], scale["max"] + 1))
                    for scale in RATING_SCALES
                },
            ),
            events={
                "submitEnable": Event(is_triggered_by="promptEnd"),
            },
            time_estimate=10,
        )

class Exp(psynet.experiment.Experiment):
    label = "Subjective rating"

    timeline = Timeline(
        # VolumeCalibration(),
        InfoPage(
            """
            In this experiment you will hear some sounds. Your task will be to rate
            them on a scale of 1 to 5 on several scales.
            """,
            time_estimate=5,
        ),
        StaticTrialMaker(
            id_="ratings",
            trial_class=CustomTrial,
            nodes=get_nodes,
            expected_trials_per_participant=N_TRIALS_PER_PARTICIPANT,
        ),
        InfoPage(
            """
            Thank you for your participation!
            """,
            time_estimate=5,
        ),
    )
