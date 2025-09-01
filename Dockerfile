# This Dockerfile is used both to specify a functional development environment 
# (e.g. on GitHub Codespaces) and a deployment image.

FROM ghcr.io/astral-sh/uv:python3.12-bookworm

# Heroku CLI is currently needed to run `psynet test local`, this should change soon
RUN curl https://cli-assets.heroku.com/install.sh | sh

RUN mkdir /experiment
WORKDIR /experiment

COPY requirements.txt requirements.txt
COPY *constraints.txt constraints.txt

ENV SKIP_DEPENDENCY_CHECK=""
ENV DALLINGER_NO_EGG_BUILD=1

# Note: SKIP_CHECK_PSYNET_VERSION_REQUIREMENT=1 below will soon become unnecessary as we are removing
# verify_psynet_requirement() from check_constraints. For now, though it is still necessary,
# because the Docker image being used for this step lags behind the latest version of PsyNet.

# # Have commented out this check because it's awkward for users to respond to this when it happens
# # during the devcontainers build process.
# # If you see an error here, you probably need to run `bash docker/generate-constraints` and then try again.
# RUN SKIP_CHECK_PSYNET_VERSION_REQUIREMENT=1 psynet check-constraints

RUN if [ -f constraints.txt ]; then \
        uv pip install -r constraints.txt --system; \
    else \
        uv pip install -r requirements.txt --system; \
    fi

COPY *prepare_docker_image.sh prepare_docker_image.sh
RUN if test -f prepare_docker_image.sh ; then bash prepare_docker_image.sh ; fi

COPY . /experiment

ENV PORT=5000

CMD dallinger_heroku_web
