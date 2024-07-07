#! /bin/bash
#set -x
FILE_CONFIG='/mapcache/config-seeder.xml'
LOG_DIR='/mapcache/logs'
EXTENTS_SPAIN='-1200000,4000000,550000,5600000'
EXTENTS_CYL='-840000,4840000,-130000,5400000'
EXTENTS_VALLADOLID_FULL='-561000,5076000,-500000,5150000'
EXTENTS_VALLADOLID_URBAN='-545000,5100000,-518000,5124000'
old_size='-1'
new_size='0'

for map in pnoa osm
do
	for format in JPEG PNG
	do
		while [[ "$old_size" != "$new_size" ]]
		do
			if [ -f "/mapcache/cache/sqlite/sqlitetiles_${format}.db" ]
			then
				old_size=$( stat -c %s "/mapcache/cache/sqlite/sqlitetiles_${format}.db" )
			fi
			
			echo "START seed $(echo $map | tr [:lower:] [:upper:]) $format (zoom 0-6, metatile 15x15, threads 16)"
			mapcache_seed -c "$FILE_CONFIG" -g MapGrid -t "${map}_$format" -n 16 -L "${LOG_DIR}/failed_${map}_${format}_0_6.log" -P 100 \
				-b -z 0,6 -M 15,15 -i scanline
			
			echo "START seed $(echo $map | tr [:lower:] [:upper:]) $format (zoom 7-10, metatile 15x15, threads 16, extents continental Spain)"
			mapcache_seed -c "$FILE_CONFIG" -g MapGrid -t "${map}_$format" -n 16 -L "${LOG_DIR}/failed_${map}_${format}_7_10.log" -P 100 \
				-b -z 7,10 -M 15,15 -i scanline -e "$EXTENTS_SPAIN"
			
			echo "START seed $(echo $map | tr [:lower:] [:upper:]) $format (zoom 11-13, metatile 15x15, threads 16, extents Castilla y Leon)"
			mapcache_seed -c "$FILE_CONFIG" -g MapGrid -t "${map}_$format" -n 16 -L "${LOG_DIR}/failed_${map}_${format}_11_13.log" -P 100 \
				-b -z 11,13 -M 15,15 -i scanline -e "$EXTENTS_CYL"
			
			echo "START seed $(echo $map | tr [:lower:] [:upper:]) $format (zoom 14-16, metatile 15x15, threads 16, extents Valladolid --with enclaves--)"
			mapcache_seed -c "$FILE_CONFIG" -g MapGrid -t "${map}_$format" -n 16 -L "${LOG_DIR}/failed_${map}_${format}_14_16.log" -P 100 \
				-b -z 14,16 -M 15,15 -i scanline -e "$EXTENTS_VALLADOLID_FULL"
				
			echo "START seed $(echo $map | tr [:lower:] [:upper:]) $format (zoom 17-18, metatile 15x15, threads 16, extents urban Valladolid --up to VA-30 + airport--)"
			mapcache_seed -c "$FILE_CONFIG" -g MapGrid -t "${map}_$format" -n 16 -L "${LOG_DIR}/failed_${map}_${format}_17_18.log" -P 100 \
				-b -z 17,18 -M 15,15 -i scanline -e "$EXTENTS_VALLADOLID_URBAN"
				
			sync
			new_size=$( stat -c %s "/mapcache/cache/sqlite/sqlitetiles_${format}.db" )
		done
		
		new_size='0'
		
#		for metatiling in 8,8 4,4 1,1
#		do
#			while [[ "$old_size" != "$new_size" ]]
#			do
#				if [ -f "/mapcache/cache/sqlite/sqlitetiles_${format}.db" ]
#				then
#					old_size=$( stat -c %s "/mapcache/cache/sqlite/sqlitetiles_${format}.db" )
#				fi
				
#				echo "START seed $(echo $map | tr [:lower:] [:upper:]) $format (zoom 0-6, metatile $( echo $metatiling | tr ',' 'x' ), threads 16)"
#				mapcache_seed -c "$FILE_CONFIG" -g MapGrid -t "${map}_$format" -n 16 -L "${LOG_DIR}/failed_${map}_${format}_0_6.log" -P 100 \
#					-b -z 0,6 -M $metatiling
#				
#				echo "START seed $(echo $map | tr [:lower:] [:upper:]) $format (zoom 7-10, metatile $( echo $metatiling | tr ',' 'x' ), threads 16, extents continental Spain)"
#				mapcache_seed -c "$FILE_CONFIG" -g MapGrid -t "${map}_$format" -n 16 -L "${LOG_DIR}/failed_${map}_${format}_7_10.log" -P 100 \
#					-b -z 7,10 -M $metatiling -e "$EXTENTS_SPAIN"
#				
#				echo "START seed $(echo $map | tr [:lower:] [:upper:]) $format (zoom 11-13, metatile $( echo $metatiling | tr ',' 'x' ), threads 16, extents Castilla y Leon)"
#				mapcache_seed -c "$FILE_CONFIG" -g MapGrid -t "${map}_$format" -n 16 -L "${LOG_DIR}/failed_${map}_${format}_11_13.log" -P 100 \
#					-b -z 11,13 -M $metatiling -e "$EXTENTS_CYL"
#				
#				echo "START seed $(echo $map | tr [:lower:] [:upper:]) $format (zoom 14-16, metatile $( echo $metatiling | tr ',' 'x' ), threads 16, extents Valladolid --with enclaves--)"
#				mapcache_seed -c "$FILE_CONFIG" -g MapGrid -t "${map}_$format" -n 16 -L "${LOG_DIR}/failed_${map}_${format}_14_16.log" -P 100 \
#					-b -z 14,16 -M $metatiling -e "$EXTENTS_VALLADOLID_FULL"
#					
#				echo "START seed $(echo $map | tr [:lower:] [:upper:]) $format (zoom 17-18, metatile $( echo $metatiling | tr ',' 'x' ), threads 16, extents urban Valladolid --up to VA-30 + airport--)"
#				mapcache_seed -c "$FILE_CONFIG" -g MapGrid -t "${map}_$format" -n 16 -L "${LOG_DIR}/failed_${map}_${format}_11_13.log" -P 100 \
#					-b -z 17,18 -M $metatiling -e "$EXTENTS_VALLADOLID_URBAN"
#					
#				sync
#				new_size=$( stat -c %s "/mapcache/cache/sqlite/sqlitetiles_${format}.db" )
#			done
#			
#			new_size='0'
#		done
	done
done

chown www-data:www-data /mapcache/cache/sqlite/*.db
