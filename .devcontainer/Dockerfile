FROM mcr.microsoft.com/devcontainers/base:resolute

RUN apt-get update && apt-get install -y \
    bash \
    curl \
    git \
    wget \
    graphviz \
    texlive-latex-recommended \
    texlive-fonts-recommended \
    texlive-science

# Node.js via nvm.
ENV NVM_DIR=/root/.nvm
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.5/install.sh | bash

# Each RUN is a fresh shell, so nvm has to be re-sourced here rather than
# relying on a previous RUN's environment. Symlinking into /usr/local/bin
# makes node/npm/npx available in login and non-interactive shells too,
# not just interactive bash (the only shell that sources nvm via ~/.bashrc).
RUN bash -c '. "$NVM_DIR/nvm.sh" && nvm install 24 && \
    ln -sf "$NVM_DIR/versions/node/$(nvm version 24)/bin/"* /usr/local/bin/'

# Chrome and chromedriver for puppeteer. Both pinned to the same channel to
# keep their versions in sync.
RUN bash -c '. "$NVM_DIR/nvm.sh" && nvm use 24 && npx @puppeteer/browsers install chrome@stable'
RUN bash -c '. "$NVM_DIR/nvm.sh" && nvm use 24 && npx @puppeteer/browsers install chromedriver@stable'

# Pandoc.
RUN wget https://github.com/jgm/pandoc/releases/download/3.10/pandoc-3.10-1-amd64.deb \
    && apt install -y ./pandoc-3.10-1-amd64.deb \
    && rm pandoc-3.10-1-amd64.deb
