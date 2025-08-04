# Demo: Tapping Experiment for Beat Synchronisation

This experiment investigates rhythmic tapping abilities through two main tasks:

1. **Isochronous Tapping**: Participants tap along with regular metronome beats at different intervals (600ms and 800ms)
2. **Musical Beat Synchronisation**: Participants tap along with musical excerpts, guided by an initial metronome that gradually fades out

## Features

- Volume calibration to ensure optimal audio levels
- Recording quality checks for accurate data collection
- Tapping calibration to ensure precise measurements
- Data collection using the REPP framework for precise audio analysis

## Technical Implementation

- This experiment is implemented using the [PsyNet framework](https://www.psynet.dev/) 
- The tapping technology is implemented using [REPP](https://gitlab.com/computational-audition/repp), a Python package for measuring sensorimotor synchronisation in laboratory and online settings.

Both frameworks are essential components of this experiment. REPP provides precise timing measurements for sensorimotor synchronisation tasks, whilst PsyNet enables robust online data collection and experiment deployment.


## Documentation

- For more information about PsyNet, see the [documentation website](https://psynetdev.gitlab.io/PsyNet/).
- For more information about REPP, see the [documentation website](https://computational-audition.gitlab.io/repp/).


## Citation

If you use this experiment in your research, please cite the following papers:

1. **REPP Framework** (Rhythm Evaluation and Perception Platform)
   ```bibtex
   @article{anglada2022repp,
     title={REPP: A robust cross-platform solution for online sensorimotor synchronization experiments},
     author={Anglada-Tort, Manuel and Harrison, Peter M. C. and Jacoby, Nori},
     journal={Behavior Research Methods},
     year={2022},
     doi={10.3758/s13428-021-01722-2}
   }
   ```

2. **PsyNet Framework** (Online Experimentation Platform)
   ```bibtex
   @article{harrison2020gibbs,
     title={Gibbs Sampling with People},
     author={Harrison, Peter M. C. and Marjieh, Romi and Adolfi, Federico and van Rijn, Paul and Anglada-Tort, Manuel and Tchernichovski, Ofer and Larrouy-Maestri, Pauline and Jacoby, Nori},
     journal={Advances in Neural Information Processing Systems},
     volume={33},
     pages={10659--10671},
     year={2020}
   }
   ```
