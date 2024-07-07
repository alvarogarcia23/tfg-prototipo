#!/bin/bash

#set -exuo pipefail

TMP_DIR=$(mktemp -d)

#URL_OSM_LAND_POLY_COMPLETE='https://osmdata.openstreetmap.de/download/land-polygons-complete-3857.zip'
URL_OSM_LAND_POLY_SPLIT='https://osmdata.openstreetmap.de/download/land-polygons-split-3857.zip'
URL_OSM_LAND_POLY_SIMPLIFIED='https://osmdata.openstreetmap.de/download/simplified-land-polygons-complete-3857.zip'
URL_OSM_LAND_POLY_PROCESSED_STORAGE='https://github.com/datadesk/osm-la-streets/raw/master/la-streets/layers/processed_p/'
URL_IMPOSM3='https://github.com/omniscale/imposm3/releases/download/v0.11.1/imposm-0.11.1-linux-x86-64.tar.gz'
URL_OSM_SPAIN='https://download.geofabrik.de/europe/spain-latest.osm.pbf'
URL_OSM_PORTUGAL='https://download.geofabrik.de/europe/portugal-latest.osm.pbf'
URL_OSM_CASTILLA_Y_LEON='https://download.geofabrik.de/europe/spain/castilla-y-leon-latest.osm.pbf'

#FILENAME_OSM_LAND_POLY_COMPLETE="$(basename ${URL_OSM_LAND_POLY_COMPLETE})"
FILENAME_OSM_LAND_POLY_SPLIT="$(basename ${URL_OSM_LAND_POLY_SPLIT})"
FILENAME_OSM_LAND_POLY_SIMPLIFIED="$(basename ${URL_OSM_LAND_POLY_SIMPLIFIED})"
FILENAME_IMPOSM3="$(basename ${URL_IMPOSM3})"

#FOLDER_TMP_OSM_LAND_POLY_COMPLETE="${TMP_DIR}/land_poly/$(basename ${FILENAME_OSM_LAND_POLY_COMPLETE} .zip)"
FOLDER_TMP_OSM_LAND_POLY_SPLIT="${TMP_DIR}/land_poly/$(basename ${FILENAME_OSM_LAND_POLY_SPLIT} .zip)"
FOLDER_TMP_OSM_LAND_POLY_SIMPLIFIED="${TMP_DIR}/land_poly/$(basename ${FILENAME_OSM_LAND_POLY_SIMPLIFIED} .zip)"



# Fetch imposm3
if [[ ! -f "./imposm3/releases/$FILENAME_IMPOSM3" ]]
then
	echo "Fetching missing imposm3"
	mkdir ${TMP_DIR}/imposm
	wget -q --show-progress -N -nd -nH --no-cache -O "${TMP_DIR}/imposm/${FILENAME_IMPOSM3}" "$URL_IMPOSM3"
	mkdir -p ./imposm3/releases
	tar -xzvf "${TMP_DIR}/imposm/${FILENAME_IMPOSM3}" -C ${TMP_DIR}/imposm/
	mv ${TMP_DIR}/imposm/* ./imposm3/releases/
fi



# Create temp folder to manage downloads at
mkdir ${TMP_DIR}/land_poly

## Fetch OSM's land polygons (complete) ONLY if newer version exists
## Commented out as unneeded, and would both: introduce filename collisions with, and use more memory if used in prod than, the split polygon set (below).
##
#printf '\n\nFetching (updated) world landmasses - (base)maps requirement\n'
#date_old=0
#date_new=$(wget --server-response --spider "$URL_OSM_LAND_POLY_COMPLETE" 2>&1 | grep -i 'Last-Modified' | cut -d ':' -f 2- | sed 's/^[[:space:]]*//g')
#
#if [[ -f ./mapserver/bind-mounts/maps/data/land_polygons.cpg ]] && \
#   [[ -f ./mapserver/bind-mounts/maps/data/land_polygons.dbf ]] && \
#   [[ -f ./mapserver/bind-mounts/maps/data/land_polygons.prj ]] && \
#   [[ -f ./mapserver/bind-mounts/maps/data/land_polygons.shp ]] && \
#   [[ -f ./mapserver/bind-mounts/maps/data/land_polygons.shx ]]
#then
#	date_old=$( date -r "./mapserver/bind-mounts/maps/data/${FILENAME_OSM_LAND_POLY_COMPLETE}" +"%s" 2>/dev/null )
#fi
#
#if [[ "$date_new" == '' ]] || [[ $( date -d "$date_new" +"%s" ) > $date_old ]]
#then
#	wget -q --show-progress -N -nd -nH --no-cache -O "${TMP_DIR}/land_poly/${FILENAME_OSM_LAND_POLY_COMPLETE}" "$URL_OSM_LAND_POLY_COMPLETE"
#	unzip -n -d "${TMP_DIR}/land_poly" "${TMP_DIR}/land_poly/${FILENAME_OSM_LAND_POLY_COMPLETE}"
#	
#	# Commit/Move files for prod use
#	mv -f -t ./mapserver/bind-mounts/maps/data/ "${TMP_DIR}/land_poly/${FILENAME_OSM_LAND_POLY_COMPLETE}"
#	mv -f -t ./mapserver/bind-mounts/maps/data/ ${FOLDER_TMP_OSM_LAND_POLY_COMPLETE}/land_*
#fi



# Fetch OSM's land polygons (split) ONLY if newer version exists
date_old=0
date_new=$(wget --server-response --spider "$URL_OSM_LAND_POLY_SPLIT" 2>&1 | grep -i 'Last-Modified' | cut -d ':' -f 2- | sed 's/^[[:space:]]*//g')

if [[ -f ./mapserver/bind-mounts/maps/data/land_polygons.cpg ]] && 
   [[ -f ./mapserver/bind-mounts/maps/data/land_polygons.dbf ]] && 
   [[ -f ./mapserver/bind-mounts/maps/data/land_polygons.prj ]] && 
   [[ -f ./mapserver/bind-mounts/maps/data/land_polygons.shp ]] && 
   [[ -f ./mapserver/bind-mounts/maps/data/land_polygons.shx ]]
then
	date_old=$( date -r "./mapserver/bind-mounts/maps/data/${FILENAME_OSM_LAND_POLY_SPLIT}" +"%s" 2>/dev/null )
fi

if [[ "$date_new" == '' ]] || [[ $( date -d "$date_new" +"%s" ) > $date_old ]]
then
	wget -q --show-progress -N -nd -nH --no-cache -O "${TMP_DIR}/land_poly/${FILENAME_OSM_LAND_POLY_SPLIT}" "$URL_OSM_LAND_POLY_SPLIT"
	unzip -n -d "${TMP_DIR}/land_poly" "${TMP_DIR}/land_poly/${FILENAME_OSM_LAND_POLY_SPLIT}"
	
	# Commit/Move files for prod use
	mv -f -t ./mapserver/bind-mounts/maps/data/ ${TMP_DIR}/land_poly/${FILENAME_OSM_LAND_POLY_SPLIT}
	mv -f -t ./mapserver/bind-mounts/maps/data/ ${FOLDER_TMP_OSM_LAND_POLY_SPLIT}/land_*
fi



# Fetch OSM's land polygons (simplified) ONLY if newer version exists
date_old=0
date_new=$(wget --server-response --spider "$URL_OSM_LAND_POLY_SIMPLIFIED" 2>&1 | grep -i 'Last-Modified' | cut -d ':' -f 2- | sed 's/^[[:space:]]*//g')

if [[ -f ./mapserver/bind-mounts/maps/data/simplified_land_polygons.cpg ]] && 
   [[ -f ./mapserver/bind-mounts/maps/data/simplified_land_polygons.dbf ]] && 
   [[ -f ./mapserver/bind-mounts/maps/data/simplified_land_polygons.prj ]] && 
   [[ -f ./mapserver/bind-mounts/maps/data/simplified_land_polygons.shp ]] && 
   [[ -f ./mapserver/bind-mounts/maps/data/simplified_land_polygons.shx ]]
then
	date_old=$( date -r "./mapserver/bind-mounts/maps/data/${FILENAME_OSM_LAND_POLY_SIMPLIFIED}" +"%s" 2>/dev/null )
fi

if [[ "$date_new" == '' ]] || [[ $( date -d "$date_new" +"%s" ) > $date_old ]]
then
	wget -q --show-progress -N -nd -nH --no-cache -O "${TMP_DIR}/land_poly/${FILENAME_OSM_LAND_POLY_SIMPLIFIED}" "$URL_OSM_LAND_POLY_SIMPLIFIED"
	unzip -n -d "${TMP_DIR}/land_poly" "${TMP_DIR}/land_poly/${FILENAME_OSM_LAND_POLY_SIMPLIFIED}"
	
	# Commit/Move files for prod use
	mv -f -t ./mapserver/bind-mounts/maps/data/ ${TMP_DIR}/land_poly/${FILENAME_OSM_LAND_POLY_SIMPLIFIED}
	mv -f -t ./mapserver/bind-mounts/maps/data/ ${FOLDER_TMP_OSM_LAND_POLY_SIMPLIFIED}/simplified_*
fi



## Fetch OSM land polygons (processed). Timestamping not enabled serverside :(
## Disabled as the relevant files have been embedded into the repository. Left commented for its potential usefulness.
#
#for i in 'processed_p.dbf' 'processed_p.dbf' 'processed_p.prj' 'processed_p.shp' 'processed_p.shx'
#do
#	if [[ ! -f "./mapserver/bind-mounts/maps/data/$i" ]]
#	then
#		wget -q --show-progress -N -nd -nH --no-cache -O "${TMP_DIR}/land_poly/$i" "${URL_OSM_LAND_POLY_PROCESSED_STORAGE}/$i"
#		# Commit/move files for prod use
#		mv -f -t ./mapserver/bind-mounts/maps/data/ ${TMP_DIR}/land_poly/$i
#	fi
#done

# Cleanup now unneeded tmp folders/files
rm -rf ${TMP_DIR}/land_poly



# Fetch detailed geodata for required regions
printf '\n\nFetching (updated) OSM data into ./osm/ as needed\n'
for i in "$URL_OSM_SPAIN" "${URL_OSM_SPAIN}.md5" "$URL_OSM_PORTUGAL" "${URL_OSM_PORTUGAL}.md5" "$URL_OSM_CASTILLA_Y_LEON" "${URL_OSM_CASTILLA_Y_LEON}.md5"
do
	cp -a "./shared/osm/$(basename $i)" ${TMP_DIR}/
	pushd "$TMP_DIR" > /dev/null
	wget -q --show-progress -N -nd -nH --no-cache "$i"
	chmod 644 "./$(basename $i)"
	popd > /dev/null
	cp -a -u "${TMP_DIR}/$(basename $i)" ./shared/osm/
	rm "${TMP_DIR}/$(basename $i)"
done



# Verify downloaded & verifiable OSM data
printf '\n\nChecking MD5 hashes of OSM data collected...\n\n'
pushd ./shared/osm/ > /dev/null
cat ./*.md5 > MD5SUMS
md5sum -c MD5SUMS
popd > /dev/null



#Fix file/folder permissions for prod use
find ./mapserver/bind-mounts/maps/	-type f ! -name '.git*' ! -name 'Makefile'	-exec chmod 644 {} \;
find ./mapserver/bind-mounts/maps/	-type d						-exec chmod 755 {} \;
find ./mapserver/bind-mounts/mapcache/	-type d						-exec chmod 777 {} \;
find ./mapserver/bind-mounts/mapcache/	-type f ! -name '.git*'				-exec chmod 644 {} \;
find ./mapserver/bind-mounts/mapcache/cache/	-type f ! -name '.git*'			-exec chmod 640 {} \;
find ./mapserver/bind-mounts/mapcache/locker/	-type f ! -name '.git*'			-exec chmod 640 {} \;
find ./mapserver/bind-mounts/logs/	-type d						-exec chmod 777 {} \;
find ./mapserver/bind-mounts/logs/	-type f ! -name '.git*'				-exec chmod 666 {} \;
find ./mapserver/bind-mounts/		-type f -name '*.conf'				-exec chmod 644 {} \;
find ./mapserver/bind-mounts/		-type f -name '*.sh'				-exec chmod 775 {} \;
find ./shared/osm/			-name '*.pbf' -type f				-exec chmod 644 {} \;

chmod 777 ./postgis/storage


docker compose build mapserver postgis postgis-alpine nominatim webapp valhalla
docker compose up mapserver -d

for i in ./mapserver/bind-mounts/maps/data/*.shp
do
	docker exec -it mapserver shptree "/maps/data/$(basename $i)" 8
done
