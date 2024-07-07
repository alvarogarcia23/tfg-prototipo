#
# NOTE: THIS DOCKERFILE IS GENERATED VIA "make update"! PLEASE DO NOT EDIT IT DIRECTLY.
#

FROM postgres:16-bullseye AS postgis-16

LABEL maintainer="PostGIS Project - https://postgis.net" \
      org.opencontainers.image.description="PostGIS 3.4.2+dfsg-1.pgdg110+1 spatial database extension with PostgreSQL 16 bullseye" \
      org.opencontainers.image.source="https://github.com/postgis/docker-postgis"

ENV POSTGIS_MAJOR 3
ENV POSTGIS_VERSION 3.4.2+dfsg-1.pgdg110+1

RUN --mount=type=cache,id=postgis-apt-cache,target=/var/cache/apt,sharing=locked --mount=type=cache,id=postgis-apt-lib,target=/var/lib/apt,sharing=locked apt-get update \
      && apt-cache showpkg postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR \
      && apt-get install -y --no-install-recommends \
           # ca-certificates: for accessing remote raster files;
           #   fix: https://github.com/postgis/docker-postgis/issues/307
           ca-certificates \
           \
           postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR=$POSTGIS_VERSION \
           postgresql-$PG_MAJOR-postgis-$POSTGIS_MAJOR-scripts

RUN mkdir -p /docker-entrypoint-initdb.d
COPY ./initdb-postgis.sh /docker-entrypoint-initdb.d/10_postgis.sh
COPY ./update-postgis.sh /usr/local/bin

# Multistage build
# 1. Stage: Base image
FROM postgis-16 as final
ARG SERIAL=1
EXPOSE 80/tcp
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Madrid
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_USER=root
ENV PGDATA=/postgresql-data/db
WORKDIR /

RUN mkdir /postgresql-data

# Install updates
RUN --mount=type=cache,id=postgis-apt-cache,target=/var/cache/apt,sharing=locked --mount=type=cache,id=postgis-apt-lib,target=/var/lib/apt,sharing=locked apt-get update \
    && apt-get dist-upgrade -y \
    #Unbrick upgrades.
    && apt-get -y install \
        locales

RUN locale-gen en_US.UTF-8 \
    && update-locale LANG=en_US.UTF-8

WORKDIR /
