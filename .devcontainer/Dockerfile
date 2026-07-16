FROM mcr.microsoft.com/devcontainers/base:resolute

RUN apt-get update && apt-get install -y \
    bash \
    curl \
    git \
    wget \
    graphviz \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-fonts-recommended \
    texlive-science \
    libnss3 \
    libnspr4 \
    libatk1.0-0t64 \
    libatk-bridge2.0-0t64 \
    libasound2t64 \
    libxdamage1 \
    libatspi2.0-0t64

# Pandoc.
RUN wget https://github.com/jgm/pandoc/releases/download/3.10/pandoc-3.10-1-amd64.deb \
    && apt install -y ./pandoc-3.10-1-amd64.deb \
    && rm pandoc-3.10-1-amd64.deb

# This base image's embedded devcontainer metadata defaults remoteUser to
# "vscode", so everything from here on installs as that user (into its own
# home directory) rather than root, where it would be unreachable at runtime.
USER vscode
WORKDIR /home/vscode

# Node.js via nvm.
ENV NVM_DIR=/home/vscode/.nvm
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.5/install.sh | bash

# Each RUN is a fresh shell, so nvm has to be re-sourced here rather than
# relying on a previous RUN's environment. Symlinking into /usr/local/bin
# (via passwordless sudo, available for vscode in this base image) makes
# node/npm/npx available in login and non-interactive shells too, not just
# interactive bash (the only shell that sources nvm via ~/.bashrc).
RUN bash -c '. "$NVM_DIR/nvm.sh" && nvm install 24 && \
    sudo ln -sf "$NVM_DIR/versions/node/$(nvm version 24)/bin/"* /usr/local/bin/'

# Chrome and chromedriver for puppeteer. Both pinned to the same channel to
# keep their versions in sync.
RUN bash -c '. "$NVM_DIR/nvm.sh" && nvm use 24 && npx @puppeteer/browsers install chrome@stable'
RUN bash -c '. "$NVM_DIR/nvm.sh" && nvm use 24 && npx @puppeteer/browsers install chromedriver@stable'

# uv (Python package/project manager). Symlinked into /usr/local/bin for the
# same reason as the node binaries above: available in every shell context,
# not just ones that source the installer's rc-file additions.
RUN curl -LsSf https://astral.sh/uv/install.sh | sh \
    && sudo ln -sf /home/vscode/.local/bin/uv /home/vscode/.local/bin/uvx /usr/local/bin/
