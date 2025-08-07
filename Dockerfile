# TODO: Use a leaner base image, e.g. with uv
FROM registry.gitlab.com/psynetdev/psynet:v12.1.0

# TODO: replace with a repository-level requirements.txt
RUN pip install psynet@git+https://gitlab.com/PsyNetDev/PsyNet@rating-scales#egg=psynet
