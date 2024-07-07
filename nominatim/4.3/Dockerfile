ARG NOMINATIM_VERSION=4.3.2
ARG USER_AGENT=mediagis/nominatim-docker:${NOMINATIM_VERSION}

FROM ubuntu:jammy AS build

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8

WORKDIR /app

    # Do not start daemons after installation.
RUN echo '#!/bin/sh\nexit 101' > /usr/sbin/policy-rc.d \
    && chmod +x /usr/sbin/policy-rc.d
    
RUN useradd -m nominatim -d /nominatim

# Install updates
RUN --mount=type=cache,id=nominatim-apt-cache,target=/var/cache/apt,sharing=locked --mount=type=cache,id=nominatim-apt-lib,target=/var/lib/apt,sharing=locked apt-get update \
    && apt-get dist-upgrade -y \
    #Unbrick upgrades.
    && apt-get -y install \
        locales \
        ca-certificates \
        wget \
        gpg

RUN install -m 0755 -d /etc/apt/keyrings

ADD https://www.postgresql.org/media/keys/ACCC4CF8.asc /etc/apt/keyrings/ACCC4CF8.asc
RUN gpg --dearmor /etc/apt/keyrings/ACCC4CF8.asc \
	&& mv /etc/apt/keyrings/ACCC4CF8.asc.gpg /etc/apt/keyrings/pgdg.gpg \
	&& chmod a+r /etc/apt/keyrings/pgdg.gpg \
	&& echo "deb [signed-by=/etc/apt/keyrings/pgdg.gpg] https://apt.postgresql.org/pub/repos/apt jammy-pgdg main" > /etc/apt/sources.list.d/pgdg.list
	
RUN --mount=type=cache,id=nominatim-apt-cache,target=/var/cache/apt,sharing=locked --mount=type=cache,id=nominatim-apt-lib,target=/var/lib/apt,sharing=locked apt-get update \
    && apt-get dist-upgrade -y

RUN locale-gen en_US.UTF-8 \
    && update-locale LANG=en_US.UTF-8

RUN --mount=type=cache,id=nominatim-apt-cache,target=/var/cache/apt,sharing=locked --mount=type=cache,id=nominatim-apt-lib,target=/var/lib/apt,sharing=locked apt-get -y install \
    # Install all required packages.
        -o APT::Install-Recommends="false" \
        -o APT::Install-Suggests="false" \
        # Build tools from sources.
        build-essential \
        g++ \
        cmake \
        libpq-dev \
        zlib1g-dev \
        libbz2-dev \
        libproj-dev \
        libexpat1-dev \
        libboost-dev \
        libboost-system-dev \
        libboost-filesystem-dev \
	liblua5.4-0 \
        liblua5.4-dev \
        nlohmann-json3-dev \
        # PostgreSQL.
        postgresql-server-dev-14 \
        postgresql-client-14 \
        # PHP and Apache 2.
        php \
        php-intl \
        php-pgsql \
        php-cgi \
        apache2 \
        libapache2-mod-php \
        # Python 3.
        python3-dev \
        python3-pip \
        python3-tidylib \
        python3-psycopg2 \
        python3-setuptools \
        python3-dotenv \
        python3-psutil \
        python3-jinja2 \
        python3-sqlalchemy \
        python3-asyncpg \
        python3-datrie \
        python3-icu \
        python3-argparse-manpage \
        # Misc.
        git \
        curl \
        sudo \
        sshpass \
        openssh-client

# Osmium install to run continuous updates.
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade pyyaml
RUN pip3 install osmium 

# Nominatim install.
ARG NOMINATIM_VERSION
ARG USER_AGENT

RUN true \
    && curl -A $USER_AGENT https://nominatim.org/release/Nominatim-$NOMINATIM_VERSION.tar.bz2 -o nominatim.tar.bz2 \
    && tar xf nominatim.tar.bz2 \
    && mkdir build \
    && cd build \
    && cmake ../Nominatim-$NOMINATIM_VERSION \
    && make -j`nproc` \
    && make install

RUN --mount=type=cache,id=nominatim-apt-cache,target=/var/cache/apt,sharing=locked --mount=type=cache,id=nominatim-apt-lib,target=/var/lib/apt,sharing=locked apt-get -y remove --purge \
    # Remove development and unused packages.
        cpp-9 \
        gcc-9* \
        g++ \
        git \
        make \
        cmake* \
        llvm-10* \
        libc6-dev \
        linux-libc-dev \
        libclang-*-dev \
        build-essential \
#        liblua*-dev \
        postgresql-server-dev-14 \
        postgresql-server-dev-16 \
        nlohmann-json3-dev \
    && apt-get autoremove -y
    
RUN --mount=type=cache,id=nominatim-apt-cache,target=/var/cache/apt,sharing=locked --mount=type=cache,id=nominatim-apt-lib,target=/var/lib/apt,sharing=locked apt-get -y install \
    # Install all required packages.
        -o APT::Install-Recommends="false" \
        -o APT::Install-Suggests="false" \
	osm2pgsql

    # Clear temporary files and directories.
RUN rm -rf \
        /tmp/* \
        /var/tmp/* \
        /root/.cache \
        /app/src/.git \
        /var/lib/apt/lists/* \
    # Remove nominatim source and build directories
    && rm /app/*.tar.bz2 \
    && rm -rf /app/build \
    && rm -rf /app/Nominatim-$NOMINATIM_VERSION

# Apache configuration
COPY conf.d/apache.conf /etc/apache2/sites-enabled/000-default.conf

COPY config.sh /app/config.sh
COPY init.sh /app/init.sh
COPY start.sh /app/start.sh
COPY startapache.sh /app/startapache.sh

# Collapse image to single layer.
FROM scratch

COPY --from=build / /

# Please override this
ENV NOMINATIM_PASSWORD=qaIACxO6wMR3

ENV PROJECT_DIR=/nominatim

ARG USER_AGENT
ENV USER_AGENT=${USER_AGENT}

WORKDIR /app

EXPOSE 5432
EXPOSE 8080

COPY conf.d/env $PROJECT_DIR/.env
RUN chmod 755 /nominatim -R

CMD ["/app/start.sh"]
