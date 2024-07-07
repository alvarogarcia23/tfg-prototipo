ARG SERIAL=1

# Multistage build
# 1. Stage: Base image
#FROM ubuntu:22.04 as base
FROM debian:bookworm as base
#FROM php:apache-bookworm as base
EXPOSE 80/tcp
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Madrid
ENV PROJ_LIB=/usr/share/proj/
ENV MAPSERVER_CONFIG_FILE=/maps/mapserver.conf
WORKDIR /

# Install updates
RUN --mount=type=cache,id=mapserver-apt-cache,target=/var/cache/apt,sharing=locked --mount=type=cache,id=mapserver-apt-lib,target=/var/lib/apt,sharing=locked apt-get update \
    && apt-get dist-upgrade -y \
    #Unbrick upgrades.
    && apt-get -y install \
        locales

RUN locale-gen en_US.UTF-8 \
    && update-locale en_US.UTF-8

# Use apt caching to accelerate build and avoid needing to apt-get clean and/or remove files
RUN --mount=type=cache,id=mapserver-apt-cache,target=/var/cache/apt,sharing=locked --mount=type=cache,id=mapserver-apt-lib,target=/var/lib/apt,sharing=locked apt-get install -y \
		apache2 \
		libapache2-mod-fcgid \
		mapserver-bin \
		cgi-mapserver \
		acl \
		mapcache-cgi \
		mapcache-tools

# Create volumes mountpoints
RUN mkdir /maps

RUN chown www-data:www-data /var/www/html -R

#HEALTHCHECK CMD curl -f http://127.0.0.1 || exit 1
CMD apache2ctl -D FOREGROUND


# 3rd Stage: Development environment.
# Choose via dockerfile -> services.mapserver.build.target
FROM base as devel

RUN --mount=type=cache,id=mapserver-apt-cache,target=/var/cache/apt,sharing=locked --mount=type=cache,id=mapserver-apt-lib,target=/var/lib/apt,sharing=locked apt-get dist-upgrade -y \
	&& apt-get install -y \
		time

#RUN usermod --shell /bin/bash www-data
#RUN rm -rf /etc/apt/apt.conf.d/docker-clean
#RUN --mount=type=cache,target=/var/cache/apt,sharing=locked --mount=type=cache,target=/var/lib/apt,sharing=locked apt-get update \
#	&& apt-get install -y \
#		byobu \
#		nano \
#		bash-completion \
#		command-not-found \
#		curl \
#		wget \
#		htop \
#		xxd \
#		gdal-bin \
#		postgresql-client
#		python2 \
#		unzip \
#		python3-pip \
#		osmctools

CMD apache2ctl -D FOREGROUND
