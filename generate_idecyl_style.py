#!/usr/bin/env python

import argparse

layer_suffixes = {
   0:0,
   1:1,
   2:2,
   3:3,
   4:4,
   5:5,
   6:6,
   7:7,
   8:8,
   9:9,
   10:10,
   11:11,
   12:12,
   13:13,
   14:14,
   15:15,
   16:16,
   17:17,
   18:18
}

maxscales = {
   0:99999999999,
   1:332808204,
   2:166404102,
   3:83202051,
   4:41601025,
   5:20800512,
   6:10400256,
   7:5200128,
   8:2600064,
   9:1300032,
   10:650016,
   11:325008,
   12:162504,
   13:81252,
   14:40626,
   15:20313,
   16:10156,
   17:5078,
   18:2539
}
minscales = {
   0:332808204,
   1:166404102,
   2:83202051,
   3:41601025,
   4:20800512,
   5:10400256,
   6:5200128,
   7:2600064,
   8:1300032,
   9:650016,
   10:325008,
   11:162504,
   12:81252,
   13:40626,
   14:20313,
   15:10156,
   16:5078,
   17:2539,
   18:0
}

style = {
   'layer_suffix':layer_suffixes,
   'maxscale':maxscales,
   'minscale':minscales,

   'land_clr': '"#E8E6E1"',
   'land_data': {
      0:'"data/land_polygons"',
      9:'"data/land_polygons"'
   },
   'land_epsg': {
      0:'"init=epsg:3857"',
   },


   ##### water #####
   'waterarea_data': {
      0: '"geometry from (select geometry,osm_id ,OSM_NAME_COLUMN as name,type from OSM_PREFIX_waterareas_gen0) as foo using unique osm_id using srid=OSM_SRID"',
      9: '"geometry from (select geometry,osm_id ,OSM_NAME_COLUMN as name,type from OSM_PREFIX_waterareas_gen1) as foo using unique osm_id using srid=OSM_SRID"',
      12: '"geometry from (select geometry,osm_id ,OSM_NAME_COLUMN as name,type from OSM_PREFIX_waterareas) as foo using unique osm_id using srid=OSM_SRID"'
   },
   'display_waterarea_lbl' : {0:0, 11:1},
   'display_waterarea_outline': {0:0, 14:1},
   'waterarea_clr': '"#B3C6D4"',
   'waterarea_ol_clr': '"#B3C6D4"',
   'waterarea_ol_width': 0,
   'waterarea_font': "sc",
   'waterarea_lbl_size': 8,
   'waterarea_lbl_clr': '"#6B94B0"',
   'waterarea_lbl_ol_clr': "255 255 255",
   'waterarea_lbl_ol_width': 2,
   'ocean_clr': '"#B3C6D4"',

   'display_waterways': {
      0:0,
      6:1
   },
   'waterways_data': {
      0:'"geometry from (select geometry, osm_id, type, OSM_NAME_COLUMN as name from OSM_PREFIX_waterways_gen0 where type=\'river\') as foo using unique osm_id using srid=OSM_SRID"',
      9:'"geometry from (select geometry, osm_id, type, OSM_NAME_COLUMN as name from OSM_PREFIX_waterways_gen1 where type=\'river\') as foo using unique osm_id using srid=OSM_SRID"',
      12:'"geometry from (select geometry, osm_id, type, OSM_NAME_COLUMN as name from OSM_PREFIX_waterways) as foo using unique osm_id using srid=OSM_SRID"'
   },

   'canal_width': {
      0:0,
      10:0.5,
      12:1,
      14:2,
      15:4,
      16:8,
      17:16,
      18:30
   },
   'display_canal_lbl' : {0:0, 10:1},
   'canal_clr': '"#B3C6D4"',
   'canal_font': "sc",
   'canal_lbl_size': 8,
   'canal_lbl_clr': '"#6B94B0"',
   'canal_lbl_ol_clr': "255 255 255",
   'canal_lbl_ol_width': 2,

   'stream_width': {
      0:0,
      10:0.5,
      12:1,
      14:2
   },
   'display_stream_lbl' : {0:0, 12:1},
   'stream_clr': '"#B3C6D4"',
   'stream_font': "sc",
   'stream_lbl_size': 8,
   'stream_lbl_clr': '"#6B94B0"',
   'stream_lbl_ol_clr': "255 255 255",
   'stream_lbl_ol_width': 2,

   'river_width': {
      0:0,
      6:0.15,
      7:0.25,
      8:0.5,
      9:1,
      11:2,
      13:3,
      15:4,
      16:5,
      17:6,
      18:7
   },
   'display_river_lbl' : {0:0, 11:1},
   'river_clr': '"#B3C6D4"',
   'river_font': "sc",
   'river_lbl_size': {0:8,15:9,17:10},
   'river_lbl_clr': '"#6B94B0"',
   'river_lbl_ol_clr': "255 255 255",
   'river_lbl_ol_width': 2,


   ##### landusage ######
   'display_landusage': {
      0:0,
      4:1
   },

   'landusage_data': {
      0:'"geometry from (select geometry ,osm_id, type, OSM_NAME_COLUMN as name from OSM_PREFIX_landusages_gen00)\
            as foo using unique osm_id using srid=OSM_SRID"',
      6:'"geometry from (select geometry ,osm_id, type, OSM_NAME_COLUMN as name from OSM_PREFIX_landusages_gen0)\
            as foo using unique osm_id using srid=OSM_SRID"',
      9:'"geometry from (select geometry ,osm_id, type, OSM_NAME_COLUMN as name from OSM_PREFIX_landusages_gen1 \
      where type in (\'forest\',\'wood\',\'industrial\',\'commercial\',\'residential\')) as foo using unique osm_id using srid=OSM_SRID"',
      10:'"geometry from (select geometry ,osm_id, type, OSM_NAME_COLUMN as name from OSM_PREFIX_landusages_gen1 \
      where type in (\'forest\',\'wood\',\'pedestrian\',\'cemetery\',\'industrial\',\'commercial\',\
      \'brownfield\',\'residential\',\'school\',\'college\',\'university\',\
      \'military\',\'park\',\'golf_course\',\'hospital\',\'parking\',\'stadium\',\'sports_center\',\
      \'pitch\') order by area desc) as foo using unique osm_id using srid=OSM_SRID"',
      12:'"geometry from (select geometry ,osm_id, type, OSM_NAME_COLUMN as name from OSM_PREFIX_landusages \
      where type in (\'forest\',\'wood\',\'pedestrian\',\'cemetery\',\'industrial\',\'commercial\',\
      \'brownfield\',\'residential\',\'school\',\'college\',\'university\',\
      \'military\',\'park\',\'golf_course\',\'hospital\',\'parking\',\'stadium\',\'sports_center\',\
      \'pitch\') order by area desc) as foo using unique osm_id using srid=OSM_SRID"'
   },

   'display_industrial': {0:0, 11:1},
   'industrial_clr': '"#d1d1d1"',
   'industrial_ol_clr': '"#d1d1d1"',
   'industrial_ol_width': 0,
   'display_industrial_lbl' : {0:0, 11:1},
   'industrial_font': "sc",
   'industrial_lbl_size': 8,
   'industrial_lbl_clr': '0 0 0',
   'industrial_lbl_ol_clr': "255 255 255",
   'industrial_lbl_ol_width': 2,

   'display_residential': {0:0, 11:1},
   'residential_clr': '"#E3DED4"',
   'residential_ol_clr': '"#E3DED4"',
   'residential_ol_width': 0,
   'display_residential_lbl' : {0:0, 12:1},
   'residential_font': "sc",
   'residential_lbl_size': 8,
   'residential_lbl_clr': '0 0 0',
   'residential_lbl_ol_clr': "255 255 255",
   'residential_lbl_ol_width': 2,

   'display_park': {0:0, 5:1},
   'park_clr': '"#d6edb9"',
   'display_park_lbl' : {0:0, 11:1},
   'park_font': "sc",
   'park_lbl_size': 8,
   'park_lbl_clr': '0 0 0',
   'park_lbl_ol_clr': "255 255 255",
   'park_lbl_ol_width': 2,

   'display_hospital': {0:0, 11:1},
   'hospital_clr': '"#E6C8C3"',
   'display_hospital_lbl' : {0:0, 12:1},
   'hospital_font': "sc",
   'hospital_lbl_size': 8,
   'hospital_lbl_clr': '0 0 0',
   'hospital_lbl_ol_clr': "255 255 255",
   'hospital_lbl_ol_width': 2,

   'display_education': {0:0, 11:1},
   'education_clr': '"#DED1AB"',
   'display_education_lbl' : {0:0, 12:1},
   'education_font': "sc",
   'education_lbl_size': 8,
   'education_lbl_clr': '0 0 0',
   'education_lbl_ol_clr': "255 255 255",
   'education_lbl_ol_width': 2,

   'display_sports': {0:0, 11:1},
   'sports_clr': '"#DED1AB"',
   'display_sports_lbl' : {0:0, 12:1},
   'sports_font': "sc",
   'sports_lbl_size': 8,
   'sports_lbl_clr': '0 0 0',
   'sports_lbl_ol_clr': "255 255 255",
   'sports_lbl_ol_width': 2,

   'display_cemetery': {0:0, 11:1},
   'cemetery_clr': '"#d1d1d1"',
   'display_cemetery_lbl' : {0:0, 12:1},
   'cemetery_font': "sc",
   'cemetery_lbl_size': 8,
   'cemetery_lbl_clr': '0 0 0',
   'cemetery_lbl_ol_clr': "255 255 255",
   'cemetery_lbl_ol_width': 2,

   'display_forest': {0:0, 5:1},
   'forest_clr': '"#C2D1B2"',
   'display_forest_lbl' : {0:0, 12:1},
   'forest_font': "sc",
   'forest_lbl_size': 8,
   'forest_lbl_clr': '0 0 0',
   'forest_lbl_ol_clr': "255 255 255",
   'forest_lbl_ol_width': 2,

   'display_transport_areas' : {0:0,11:1},
   'transport_clr': '200 200 200',
   'display_transport_lbl' : {0:0, 12:1},
   'transport_font': "sc",
   'transport_lbl_size': 8,
   'transport_lbl_clr': '0 0 0',
   'transport_lbl_ol_clr': "255 255 255",
   'transport_lbl_ol_width': 2,

   ###### highways #######

   'roads_data': {
      0:'"geometry from (select osm_id,geometry,OSM_NAME_COLUMN as name,ref,type from OSM_PREFIX_roads_gen0 where type in (\'trunk\',\'motorway\') order by z_order asc) as foo using unique osm_id using srid=OSM_SRID"',
      8:'"geometry from (select osm_id,geometry,OSM_NAME_COLUMN as name,ref,type from OSM_PREFIX_roads_gen1 where type in (\'trunk\',\'motorway\',\'primary\') order by z_order asc) as foo using unique osm_id using srid=OSM_SRID"',
      9:'"geometry from (select osm_id,geometry,OSM_NAME_COLUMN as name,ref,type from OSM_PREFIX_roads_gen1 where type in (\'secondary\',\'trunk\',\'motorway\',\'primary\') order by z_order asc) as foo using unique osm_id using srid=OSM_SRID"',
      10:'"geometry from (select osm_id,geometry,OSM_NAME_COLUMN as name,ref,type from OSM_PREFIX_roads_gen1 ) as foo using unique osm_id using srid=OSM_SRID"',
      11:'"geometry from (select osm_id,geometry,OSM_NAME_COLUMN as name,ref,type from OSM_PREFIX_roads order by z_order asc) as foo using unique osm_id using srid=OSM_SRID"',
      14:'"geometry from (select osm_id,geometry,OSM_NAME_COLUMN as name,ref,type||bridge||tunnel as type from OSM_PREFIX_roads order by z_order asc, st_length(geometry) asc) as foo using unique osm_id using srid=OSM_SRID"',
   },

   'tunnel_opacity': 40,

   'display_bridges': {  #also activates tunnels
      0:0,
      14:1
   },
   'motorway_bridge_clr':"136 136 136",
   'motorway_bridge_width':{0:0.5,14:1},
   'trunk_bridge_clr':"136 136 136",
   'trunk_bridge_width':{0:0.5,14:1},
   'primary_bridge_clr':"136 136 136",
   'primary_bridge_width':{0:0.5,14:1},
   'secondary_bridge_clr':"136 136 136",
   'secondary_bridge_width':{0:0.5,14:1},
   'tertiary_bridge_clr':"136 136 136",
   'tertiary_bridge_width':{0:0.5,14:1},
   'other_bridge_clr':"136 136 136",
   'other_bridge_width':{0:0.5,14:1},
   'pedestrian_bridge_clr':"136 136 136",
   'pedestrian_bridge_width':{0:0.5,14:1},

   'display_highways': {
      0:0,
      5:1
   },

   'display_motorways': {
      0:0,
      5:1
   },
   'display_motorway_links': {
      0:0,
      9:1
   },
   'display_motorway_outline': 0,
   'motorway_clr': '255 255 255',
   'motorway_width': {
      0:0.5,
      8:1,
      9:2,
      11:3,
      12:4,
      14:5,
      15:6,
      16:8,
      17:9,
      18:10
   },
   'label_motorways': {
      0:0,
      10:1
   },
   'motorway_font': "scb",
   'motorway_lbl_size': {
      0:8,
      14:9
   },
   'motorway_lbl_clr': '"#555555"',
   'motorway_ol_width': {
      0:0.5,
      10:1
   },
   'motorway_ol_clr': "100 100 100",

   'display_trunks': {
      0:0,
      5:1
   },
   'display_trunk_links': {
      0:0,
      9:1
   },
   'display_trunk_outline': 0,
   'trunk_clr': '255 255 255',
   'trunk_width': {
      0:0.5,
      8:1,
      9:2,
      11:3,
      12:4,
      14:5,
      15:6,
      16:8,
      17:9,
      18:10
   },
   'label_trunks': {
      0:0,
      10:1
   },
   'trunk_font': "scb",
   'trunk_lbl_size': {
      0:8,
      14:9
   },
   'trunk_lbl_clr': '"#555555"',
   'trunk_ol_width': {
      0:0.5,
      10:1
   },
   'trunk_ol_clr': "100 100 100",

   'display_primaries': {
      0:0,
      8:1
   },
   'display_primary_outline': 0,
   'primary_clr': {
      0:'"#aaaaaa"',
      9:'"#ffffff"'
   },
   'primary_width': {
      0:0.5,
      9:0.75,
      10:1,
      11:1.5,

      12:2,
      13:2.5,
      14:3,
      15:4,
      16:7,
      17:8,
      18:9
   },
   'label_primaries': {
      0:0,
      13:1
   },
   'primary_font': "sc",
   'primary_lbl_size': {
      0:0,
      13:8,
      15:9
   },
   'primary_lbl_clr': {
      0:'"#333333"'
   },
   'primary_lbl_ol_clr': {
      0:'255 255 255'
   },
   'primary_lbl_ol_width': 2,
   'primary_ol_width': 1,
   'primary_ol_clr': "0 0 0",

   'display_secondaries': {
      0:0,
      9:1
   },
   'display_secondary_outline': 0,
   'secondary_clr': {
      0:'"#aaaaaa"',
      10:'"#ffffff"'
   },
   'secondary_width': {
      0:0,
      9:0.5,
      10:0.75,
      11:1,
      12:1.5,
      13:2,
      14:2.5,
      15:3.5,
      16:6,
      17:7,
      18:8
   },
   'label_secondaries': {
      0:0,
      13:1
   },
   'secondary_font': "sc",
   'secondary_lbl_size': {
      0:0,
      13:8,
      15:9
   },
   'secondary_lbl_clr': '"#333333"',
   'secondary_lbl_ol_clr': '255 255 255',
   'secondary_lbl_ol_width': 2,
   'secondary_ol_width': 1,
   'secondary_ol_clr': "0 0 0",

   'display_tertiaries': {
      0:0,
      10:1
   },
   'display_tertiary_outline': 0,
   'tertiary_clr': {
      0:'"#aaaaaa"',
      13:'"#ffffff"'
   },
   'tertiary_width': {
      0:0,
      10:0.5,
      11:0.75,
      12:1,
      13:1.5,
      14:2,
      15:2.5,
      16:5,
      17:6,
      18:7
   },
   'label_tertiaries': {
      0:0,
      15:1
   },
   'tertiary_font': "sc",
   'tertiary_lbl_size': {
      0:0,
      15:8,
   },
   'tertiary_lbl_clr': '"#333333"',
   'tertiary_lbl_ol_clr': '255 255 255',
   'tertiary_lbl_ol_width': 2,
   'tertiary_ol_width': 1,
   'tertiary_ol_clr': "0 0 0",

   'display_other_roads': {
      0:0,
      11:1
   },
   'display_other_outline': 0,
   'other_clr': {
      0:'"#aaaaaa"',
      15:'"#ffffff"'
   },
   'other_width': {
      0:0,
      11:0.5,
      12:0.75,
      13:1,
      14:1.5,
      15:2,
      16:4,
      17:5,
      18:6,
   },
   'label_other_roads': {
      0:0,
      15:1
   },
   'other_font': "sc",
   'other_lbl_size': {
      0:0,
      15:8,
   },
   'other_lbl_clr': '"#333333"',
   'other_lbl_ol_clr': '255 255 255',
   'other_lbl_ol_width': 2,
   'other_ol_width': 1,
   'other_ol_clr': "0 0 0",

   'display_pedestrian': {
      0:0,
      12:1
   },
   'display_pedestrian_outline': 0,
   'pedestrian_clr': '"#f2f2ed"',
   'pedestrian_width': {
      0:0,
      11:0.5,
      12:0.75,
      13:1,
      14:1.5,
      15:2,
      16:2.5,
      17:3,
      18:3.5,
   },
   'label_pedestrian': {
      0:0,
      15:1
   },
   'display_pedestrian_lbl' : {0:0, 12:1},
   'pedestrian_font': "sc",
   'pedestrian_lbl_size': {
      0:0,
      15:8,
   },
   'pedestrian_lbl_clr': '"#333333"',
   'pedestrian_lbl_ol_clr': '255 255 255',
   'pedestrian_lbl_ol_width': 2,
   'pedestrian_ol_width': 1,
   'pedestrian_ol_clr': "0 0 0",

   'display_tracks': {
      0:0,
      12:1
   },
   'display_track_outline': 0,
   'track_clr': {
      0:'"#aaaaaa"',
      15:'"#ffffff"',
   },
   'track_width': {
      0:0,
      11:0.5,
      12:0.75,
      15:1,
   },
   'track_pattern': {
      0: '2 2',
      15: '2 3'
   },
   'label_track': {
      0:0,
      15:1
   },
   'track_font': "sc",
   'track_lbl_size': {
      0:0,
      15:8,
   },
   'track_lbl_clr': '"#333333"',
   'track_lbl_ol_clr': '255 255 255',
   'track_lbl_ol_width': 2,
   'track_ol_width': 1,
   'track_ol_clr': "0 0 0",
   # cycleways
   'display_cycleways': {
      0:0,
      15:1
   },
   'display_cycleway_outline': 0,
   'cycleway_clr': {
      0:'"#aaaaaa"',
      15:'"#ffffff"',
   },
   'cycleway_width': {
      0:0,
      15:2,
   },
   'cycleway_pattern': '2 4',
   'cycleway_ol_width': 1,
   'cycleway_ol_clr': "0 0 0",
   'display_footways': {
      0:0,
      15:1
   },
   'display_footway_outline': 0,
   'footway_clr': {
      0:'"#aaaaaa"',
      15:'"#ffffff"',
   },
   'footway_width': {
      0:0,
      15:1,
   },
   'footway_pattern': '2 3',
   'footway_ol_width': 1,
   'footway_ol_clr': "0 0 0",
   'display_piers': {
      0:0,
      15:1
   },
   'display_pier_outline': 0,
   'pier_clr': {
      0:'"#aaaaaa"',
      15:'"#ffffff"',
   },
   'pier_width': {
      0:0,
      15:4,
   },
   'pier_ol_width': 1,
   'pier_ol_clr': "0 0 0",

   ###### railways ########
   'display_railways': {
      0:0,
      8:1
   },
   'railway_clr': '"#777777"',
   'railway_width': {
      0:0.5,
      10:1
   },
   'railway_ol_clr': '"#777777"',
   'railway_ol_width': 0,
   'railway_pattern': '2 2',
   'railway_tunnel_opacity': 40,
   'railways_data': {
      0:'"geometry from (select geometry, osm_id, tunnel from OSM_PREFIX_railways_gen0 where type=\'rail\') as foo using unique osm_id using srid=OSM_SRID"',
      6:'"geometry from (select geometry, osm_id, tunnel from OSM_PREFIX_railways_gen1 where type=\'rail\') as foo using unique osm_id using srid=OSM_SRID"',
      12:'"geometry from (select geometry, osm_id, tunnel from OSM_PREFIX_railways where type=\'rail\') as foo using unique osm_id using srid=OSM_SRID"'
   },


   ##### borders ######
   'border_data': '"data/boundaries.shp"',
   'border_epsg': {
      0: '"init=epsg:4326"'
   },

   'display_border_2': {
      0:1
   },
   'display_border_2_outer': {
      0:0,
      6:1
   },
   'border_2_clr': {
      0:'"#4a4a4a"'
   },
   'border_2_width': {
      0:'6'
   },
   'border_2_inner_clr': {
      0:'"#000000"',
      4:'"#000000"'
   },
   'border_2_inner_width': {
      0:'1',
      7:'2'
   },
   'border_2_pattern': {
      0:''
   },
   'display_border_4': {
      0:0,
      6:1
   },
   'display_border_4_outer': {
      0:0,
      7:1
   },
   'border_4_clr': {
      0:'"#4a4a4a"'
   },
   'border_4_width': {
      0:'6',
      8:'7'
   },
   'border_4_inner_clr': {
      0:'"#000000"'
   },
   'border_4_inner_width': {
      0:'1',
      7:'2'
   },
   'border_4_pattern': {
      0:'',
      7:'PATTERN 2 2 END'
   },
   'display_border_6': {
      0:0,
      7:1
   },
   'display_border_6_outer': {
      0:0,
      9:1
   },
   'border_6_clr': {
      0:'"#4a4a4a"'
   },
   'border_6_width': {
      0:'6',
      13:'7'
   },
   'border_6_inner_clr': {
      0:'"#000000"'
   },
   'border_6_inner_width': {
      0:'1',
      9:2
   },
   'border_6_pattern': {
      0:'',
      9:'PATTERN 2 2 END'
   },
   'display_border_8': {
      0:0,
      11:1
   },
   'display_border_8_outer': {
      0:0,
      13:1
   },
   'border_8_clr': {
      0:'"#4a4a4a"'
   },
   'border_8_width': {
      0:'6'
   },
   'border_8_inner_clr': {
      0:'"#000000"'
   },
   'border_8_inner_width': {
      0:'1',
      14:'2'
   },
   'border_8_pattern': {
      0:'',
      13:'PATTERN 2 2 END'
   },


   ###### buildings ######
   'display_buildings': {
      0: 0,
      15:1
   },
   'building_clr': '"#bbbbbb"',
   'building_ol_clr': '"#333333"',
   'building_ol_width': {
      0:0,
      16:0.1,
      17:0.5
   },
   'building_font': "sc",
   'building_lbl_clr': "0 0 0",
   'building_lbl_size': 8,
   'building_lbl_ol_clr': "255 255 255",
   'building_lbl_ol_width': 2,
   'label_buildings': {
      0: 0,
      15: 1
   },


   ####### aeroways #######
   'display_aeroways': {
      0:0,
      10:1
   },
   'runway_clr': "180 180 180",
   'runway_width': {
      0:1,
      11:2,
      12:3,
      13:5,
      14:7,
      15:11,
      16:15,
      17:19,
      18:23
   },
   'runway_center_clr': '80 80 80',
   'runway_center_width': {
      0:0,
      15:1
   },
   'runway_center_pattern' : '2 2',
   'taxiway_width': {
      0:0,
      10:0.2,
      13:1,
      14:1.5,
      15:2,
      16:3,
      17:4,
      18:5
   },
   'taxiway_clr': "180 180 180",

   ###### places ######
   'places_data': {
      0: '"geometry from (select * from OSM_PREFIX_places where type in (\'country\',\'continent\') and OSM_NAME_COLUMN is not NULL order by population asc nulls first) as foo using unique osm_id using srid=OSM_SRID"',
      3: '"geometry from (select * from OSM_PREFIX_places where type in (\'country\',\'continent\',\'city\') and OSM_NAME_COLUMN is not NULL order by population asc nulls first) as foo using unique osm_id using srid=OSM_SRID"',
      8: '"geometry from (select * from OSM_PREFIX_places where type in (\'city\',\'town\') and OSM_NAME_COLUMN is not NULL order by population asc nulls first) as foo using unique osm_id using srid=OSM_SRID"',
      11: '"geometry from (select * from OSM_PREFIX_places where type in (\'city\',\'town\',\'village\') and OSM_NAME_COLUMN is not NULL order by population asc nulls first) as foo using unique osm_id using srid=OSM_SRID"',
      13: '"geometry from (select * from OSM_PREFIX_places where OSM_NAME_COLUMN is not NULL order by population asc nulls first) as foo using unique osm_id using srid=OSM_SRID"',
   },
   'display_capitals': 0,
   'display_capital_symbol': {
      0:1,
      10:0
   },
   'capital_lbl_size': {
      0:0,
      3:8,
      8:9,
      10:10,
      13:11,
      15:12

   },
   'capital_size': 6,
   'capital_fg_size': 2,
   'capital_ol_clr': "0 0 0",
   'capital_fg_clr': "0 0 0",
   'capital_clr': "255 0 0",
   'capital_font': "sc",
   'capital_lbl_clr': "0 0 0",
   'capital_lbl_ol_clr': "255 255 255",
   'capital_lbl_ol_width':2,

   'display_continents': {
      0:0
   },
   'continent_lbl_size': 8,
   'continent_lbl_clr': "100 100 100",
   'continent_lbl_ol_width': "1",
   'continent_lbl_ol_clr': "-1 -1 -1",
   'continent_font': "scb",

   'display_countries': {
      0:0
   },
   'country_lbl_size': 8,
   'country_lbl_clr': "100 100 100",
   'country_lbl_ol_width': 2,
   'country_lbl_ol_clr': "-1 -1 -1",
   'country_font': "scb",

   'display_cities': {
      0:0,
      3:1,
      16:0
   },
   'display_city_symbol': {
      0:1,
      10:0
   },
   'city_lbl_size': {
      0:0,
      3:8,
      8:9,
      10:10,
      11:11,
      13:12,
      15:13
   },
   'city_size': {
      0:5,
      8:6
   },
   'city_ol_clr': "0 0 0",
   'city_clr': {
      0:"200 200 200",
      8:"255 255 255"
   },
   'city_font': "sc",
   'city_lbl_clr': {
      0:"68 68 68",
      8:'0 0 0'
   },
   'city_lbl_ol_clr': "255 255 255",
   'city_lbl_ol_width': {
      0:2,
      10:3
   },

   'display_towns': {
      0:0,
      8:1
   },
   'display_town_symbol': {
      0:1,
      12:0
   },
   'town_font': "sc",
   'town_lbl_clr': {
      0:'"#666666"',
      11:'0 0 0'
   },
   'town_lbl_ol_clr': "255 255 255",
   'town_lbl_ol_width':2,
   'town_lbl_size': {
      0:0,
      8:8,
      10:9,
      12:10,
      15:11
   },
   'town_size': {
      0:0,
      8:3,
      10:5
   },
   'town_ol_clr': "0 0 0",
   'town_clr': "200 200 200",

   'display_suburbs': {
      0:0,
      13:1
   },
   'suburb_font': "sc",
   'suburb_lbl_clr': {
      0:'"#444444"',
      15:'0 0 0'
   },
   'suburb_lbl_ol_clr': "255 255 255",
   'suburb_lbl_ol_width': 2,
   'display_suburb_symbol': 0,
   'suburb_lbl_size': {
      0:0,
      13:8,
      15:9,
   },
   'suburb_size': 5,
   'suburb_ol_clr': "0 0 0",
   'suburb_clr': "200 200 200",

   'display_villages': {
      0:0,
      11:1
   },
   'display_village_symbol': {
      0:1,
      14:0
   },
   'village_lbl_size': {
      0:0,
      10:8,
      13:9,
      15:10
   },
   'village_size': {
      0:0,
      11:3,
      13:4
   },
   'village_ol_clr': "0 0 0",
   'village_clr': "200 200 200",
   'village_font': "sc",
   'village_lbl_clr': {
      0:'"#444444"',
      13:'0 0 0'
   },
   'village_lbl_ol_clr': "255 255 255",
   'village_lbl_ol_width': 2,

   'display_hamlets': {
      0:0,
      13:0
   },
   'hamlet_font': "sc",
   'hamlet_lbl_clr': {
      0:'"#444444"',
      15:'0 0 0'
   },
   'hamlet_lbl_ol_clr': "255 255 255",
   'hamlet_lbl_ol_width': 2,
   'display_hamlet_symbol': 0,
   'hamlet_lbl_size': {
      0:0,
      13:8,
      15:9,
   },
   'hamlet_size': 5,
   'hamlet_ol_clr': "0 0 0",
   'hamlet_clr': "200 200 200",

   'display_localities': {
      0:0,
      13:0
   },
   'locality_font': "sc",
   'locality_lbl_clr': {
      0:'"#444444"',
      15:'0 0 0'
   },
   'locality_lbl_ol_clr': "255 255 255",
   'locality_lbl_ol_width': 2,
   'display_locality_symbol': 0,
   'locality_lbl_size': {
      0:0,
      13:8,
      15:9,
   },
   'locality_size': 5,
   'locality_ol_clr': "0 0 0",
   'locality_clr': "200 200 200",

   ##### innerborders ######
   'innerborder_data': '"data/idecyl/comu_spa_recintos/comu_spa_recintos.shp"',
   'innerborder_epsg': { 0: '"init=epsg:25830"' },
   'display_innerborder_2': { 0:0, 5:1, 7:0 },
   'display_innerborder_2_outer': { 0:0, 5:1, 7:0 },
   'innerborder_2_clr': { 0:'"#e3e3e3"' },
   'innerborder_2_width': { 0:'2'  },
   'innerborder_2_inner_clr': { 0:'"#4a4a4a"', },
   'innerborder_2_inner_width': { 0:'3' },
   'innerborder_2_pattern': { 0:'PATTERN 2 10 END' },
   'display_innerborder_4': { 0:0, 7:1, 9:0 },
   'display_innerborder_4_outer': { 0:0, 7:1, 9:0 },
   'innerborder_4_clr': { 0:'"#e3e3e3"' },
   'innerborder_4_width': { 0:'3', },
   'innerborder_4_inner_clr': { 0:'"#4a4a4a"' },
   'innerborder_4_inner_width': { 0:'3', },
   'innerborder_4_pattern': { 0:'PATTERN 2 10 END' },
   'display_innerborder_6': { 0:0, 9:1, 11:0 },
   'display_innerborder_6_outer': { 0:0, 9:1, 11:0 },
   'innerborder_6_clr': { 0:'"#e3e3e3"' },
   'innerborder_6_width': { 0:'3' },
   'innerborder_6_inner_clr': { 0:'"#4a4a4a"' },
   'innerborder_6_inner_width': { 0:'3' },
   'innerborder_6_pattern': { 0:'PATTERN 2 10 END' },
   'display_innerborder_8': { 0:0, 11:1 },
   'display_innerborder_8_outer': { 0:0, 11:1 },
   'innerborder_8_clr': { 0:'"#e3e3e3"' },
   'innerborder_8_width': { 0:'3' },
   'innerborder_8_inner_clr': { 0:'"#4a4a4a"' },
   'innerborder_8_inner_width': { 0:'3' },
   'innerborder_8_pattern': { 0:'PATTERN 2 10 END' },
   'innerborder_extent': '-14130 3892589 1126924 4859517',

   ###### idecyl_aparcamiento ######
   'idecyl_aparcamiento_data': { 0: '"data/idecyl/sigren_aparcamiento/aparcamientoPoint.shp"' },
   'display_idecyl_aparcamiento': { 0:0, 10:1 },
   'display_idecyl_aparcamiento_symbol': { 0:0, 10:1 },
   'display_idecyl_aparcamiento_label': { 0:0, 15:1 },
   'idecyl_aparcamiento_font': "sc",
   'idecyl_aparcamiento_lbl_ol_clr': "255 255 255",
   'idecyl_aparcamiento_lbl_ol_width': 2,
   'idecyl_aparcamiento_lbl_size': {
      0:0,
      8:10
   },
   'idecyl_aparcamiento_size': 20,
   'idecyl_aparcamiento_ol_clr': "0 0 0",
   'idecyl_aparcamiento_clr': "0 0 0",
   'idecyl_aparcamiento_lbl_clr': "0 0 0",
   'idecyl_aparcamiento_ol_width': 10,
   'idecyl_aparcamiento_priority': 8,

   ###### idecyl_arbol ######
   'idecyl_arbol_data': { 0: '"data/idecyl/sigren_arbol/arbolPoint.shp"' },
   'display_idecyl_arbol': { 0:0, 10:1 },
   'display_idecyl_arbol_symbol': { 0:0, 10:1 },
   'display_idecyl_arbol_label': { 0:0, 16:1 },
   'idecyl_arbol_font': "sc",
   'idecyl_arbol_lbl_ol_clr': "255 255 255",
   'idecyl_arbol_lbl_ol_width': 2,
   'idecyl_arbol_lbl_size': {
      0:0,
      8:10 },
   'idecyl_arbol_size': 23,
   'idecyl_arbol_ol_clr': "0 0 0",
   'idecyl_arbol_clr': "0 0 0",
   'idecyl_arbol_lbl_clr': "0 0 0",
   'idecyl_arbol_ol_width': 2,
   'idecyl_arbol_priority': 2,

   ###### idecyl_campamento ######
   'idecyl_campamento_data': { 0: '"data/idecyl/sigren_campamento/campamentoPoint.shp"' },
   'display_idecyl_campamento': { 0:0, 10:1 },
   'display_idecyl_campamento_symbol': { 0:0, 10:1 },
   'display_idecyl_campamento_label': { 0:0, 15:1 },
   'idecyl_campamento_font': "sc",
   'idecyl_campamento_lbl_ol_clr': "255 255 255",
   'idecyl_campamento_lbl_ol_width': 2,
   'idecyl_campamento_lbl_size': {
      0:0,
      8:10 },
   'idecyl_campamento_size': 20,
   'idecyl_campamento_ol_clr': "0 0 0",
   'idecyl_campamento_clr': "0 0 0",
   'idecyl_campamento_lbl_clr': "0 0 0",
   'idecyl_campamento_ol_width': 2,
   'idecyl_campamento_priority': 6,

   ###### idecyl_casa_parque ######
   'idecyl_casa_parque_data': { 0: '"data/idecyl/sigren_casa_parque/casa_parquePoint.shp"' },
   'display_idecyl_casa_parque': { 0:0, 8:1 },
   'display_idecyl_casa_parque_symbol': { 0:0, 8:1 },
   'display_idecyl_casa_parque_label': { 0:0 },
   'idecyl_casa_parque_font': "sc",
   'idecyl_casa_parque_lbl_ol_clr': "255 255 255",
   'idecyl_casa_parque_lbl_ol_width': 2,
   'idecyl_casa_parque_lbl_size': { 0:0 },
   'idecyl_casa_parque_size': 25,
   'idecyl_casa_parque_ol_clr': "0 0 0",
   'idecyl_casa_parque_clr': "0 0 0",
   'idecyl_casa_parque_lbl_clr': "0 0 0",
   'idecyl_casa_parque_ol_width': 2,
   'idecyl_casa_parque_priority': 10,

   ###### idecyl_centro_visitantes ######
   'idecyl_centro_visitantes_data': { 0: '"data/idecyl/sigren_centro_visitantes/centro_visitantesPoint.shp"' },
   'display_idecyl_centro_visitantes': { 0:0, 8:1 },
   'display_idecyl_centro_visitantes_symbol': { 0:0, 8:1 },
   'display_idecyl_centro_visitantes_label': { 0:0 },
   'idecyl_centro_visitantes_font': "sc",
   'idecyl_centro_visitantes_lbl_ol_clr': "255 255 255",
   'idecyl_centro_visitantes_lbl_ol_width': 2,
   'idecyl_centro_visitantes_lbl_size': { 0:0 },
   'idecyl_centro_visitantes_size': 20,
   'idecyl_centro_visitantes_ol_clr': "0 0 0",
   'idecyl_centro_visitantes_clr': "0 0 0",
   'idecyl_centro_visitantes_lbl_clr': "0 0 0",
   'idecyl_centro_visitantes_ol_width': 2,
   'idecyl_centro_visitantes_priority': 9,

   ###### idecyl_instalacion_deportiva ######
   'idecyl_instalacion_deportiva_data': { 0: '"data/idecyl/sigren_instalacion_deportiva/instalacion_deportivaPoint.shp"' },
   'display_idecyl_instalacion_deportiva': { 0:0, 12:1 },
   'display_idecyl_instalacion_deportiva_symbol': { 0:0, 10:1 },
   'display_idecyl_instalacion_deportiva_label': { 0:0, 16:1 },
   'idecyl_instalacion_deportiva_font': "sc",
   'idecyl_instalacion_deportiva_lbl_ol_clr': "255 255 255",
   'idecyl_instalacion_deportiva_lbl_ol_width': 2,
   'idecyl_instalacion_deportiva_lbl_size': {
      0:0,
      8:10
   },
   'idecyl_instalacion_deportiva_size': 20,
   'idecyl_instalacion_deportiva_ol_clr': "0 0 0",
   'idecyl_instalacion_deportiva_clr': "0 0 0",
   'idecyl_instalacion_deportiva_lbl_clr': "0 0 0",
   'idecyl_instalacion_deportiva_ol_width': 2,
   'idecyl_instalacion_deportiva_priority': 3,

   ###### idecyl_kiosco ######
   'idecyl_kiosco_data': { 0: '"data/idecyl/sigren_kiosco/kioscoPoint.shp"' },
   'display_idecyl_kiosco': { 0:0, 8:1 },
   'display_idecyl_kiosco_symbol': { 0:0, 10:1 },
   'display_idecyl_kiosco_label': { 0:0, 10:1 },
   'idecyl_kiosco_font': "sc",
   'idecyl_kiosco_lbl_ol_clr': "255 255 255",
   'idecyl_kiosco_lbl_ol_width': 2,
   'idecyl_kiosco_lbl_size': { 0:0, 8:10 },
   'idecyl_kiosco_size': 20,
   'idecyl_kiosco_ol_clr': "0 0 0",
   'idecyl_kiosco_clr': "0 0 0",
   'idecyl_kiosco_lbl_clr': "0 0 0",
   'idecyl_kiosco_ol_width': 8,
   'idecyl_kiosco_priority': 7,

   ###### idecyl_mirador ######
   'idecyl_mirador_data': { 0: '"data/idecyl/sigren_mirador/miradorPoint.shp"' },
   'display_idecyl_mirador': { 0:0, 10:1 },
   'display_idecyl_mirador_symbol': { 0:0, 10:1 },
   'display_idecyl_mirador_label': { 0:0, 11:1 },
   'idecyl_mirador_font': "sc",
   'idecyl_mirador_lbl_ol_clr': "255 255 255",
   'idecyl_mirador_lbl_ol_width': 2,
   'idecyl_mirador_lbl_size': {
      0:0,
      8:10
   },
   'idecyl_mirador_size': 20,
   'idecyl_mirador_ol_clr': "0 0 0",
   'idecyl_mirador_clr': "0 0 0",
   'idecyl_mirador_lbl_clr': "0 0 0",
   'idecyl_mirador_ol_width': 6,
   'idecyl_mirador_priority': 4,

   ###### idecyl_observatorio ######
   'idecyl_observatorio_data': { 0: '"data/idecyl/sigren_observatorio/observatorioPoint.shp"' },
   'display_idecyl_observatorio': { 0:0, 10:1 },
   'display_idecyl_observatorio_symbol': { 0:0, 10:1 },
   'display_idecyl_observatorio_label': { 0:0, 11:1 },
   'idecyl_observatorio_font': "sc",
   'idecyl_observatorio_lbl_ol_clr': "255 255 255",
   'idecyl_observatorio_lbl_ol_width': 2,
   'idecyl_observatorio_lbl_size': {
      0:0,
      8:10
   },
   'idecyl_observatorio_size': 20,
   'idecyl_observatorio_ol_clr': "0 0 0",
   'idecyl_observatorio_clr': "0 0 0",
   'idecyl_observatorio_lbl_clr': "0 0 0",
   'idecyl_observatorio_ol_width': 6,
   'idecyl_observatorio_priority': 4,

   ###### idecyl_otro_punto_interes ######
   'idecyl_otro_punto_interes_data': { 0: '"data/idecyl/sigren_otro_punto_interes/otro_punto_interesPoint.shp"' },
   'display_idecyl_otro_punto_interes': { 0:0, 12:1 },
   'display_idecyl_otro_punto_interes_symbol': { 0:0, 10:1 },
   'display_idecyl_otro_punto_interes_label': { 0:0, 15:1 },
   'idecyl_otro_punto_interes_font': "sc",
   'idecyl_otro_punto_interes_lbl_ol_clr': "255 255 255",
   'idecyl_otro_punto_interes_lbl_ol_width': 2,
   'idecyl_otro_punto_interes_lbl_size': {
      0:0,
      8:10
   },
   'idecyl_otro_punto_interes_size': 20,
   'idecyl_otro_punto_interes_ol_clr': "0 0 0",
   'idecyl_otro_punto_interes_clr': "0 0 0",
   'idecyl_otro_punto_interes_lbl_clr': "0 0 0",
   'idecyl_otro_punto_interes_ol_width': 3,
   'idecyl_otro_punto_interes_priority': 2,

   ###### idecyl_pto_peligroso ######
   'idecyl_pto_peligroso_data': { 0: '"data/idecyl/sigren_pto_peligroso/pto_peligrosoPoint.shp"' },
   'display_idecyl_pto_peligroso': { 0:0, 10:1 },
   'display_idecyl_pto_peligroso_symbol': { 0:0, 10:1 },
   'display_idecyl_pto_peligroso_label': { 0:0, 15:1 },
   'idecyl_pto_peligroso_font': "sc",
   'idecyl_pto_peligroso_lbl_ol_clr': "255 255 255",
   'idecyl_pto_peligroso_lbl_ol_width': 2,
   'idecyl_pto_peligroso_lbl_size': {
      0:0,
      8:10
   },
   'idecyl_pto_peligroso_size': 20,
   'idecyl_pto_peligroso_ol_clr': "0 0 0",
   'idecyl_pto_peligroso_clr': "0 0 0",
   'idecyl_pto_peligroso_lbl_clr': "0 0 0",
   'idecyl_pto_peligroso_ol_width': 5,
   'idecyl_pto_peligroso_priority': 3,

   ###### idecyl_refugio ######
   'idecyl_refugio_data': { 0: '"data/idecyl/sigren_refugio/refugioPoint.shp"' },
   'display_idecyl_refugio': { 0:0, 10:1 },
   'display_idecyl_refugio_symbol': { 0:0, 10:1 },
   'display_idecyl_refugio_label': { 0:0, 16:1 },
   'idecyl_refugio_font': "sc",
   'idecyl_refugio_lbl_ol_clr': "255 255 255",
   'idecyl_refugio_lbl_ol_width': 2,
   'idecyl_refugio_lbl_size': {
      0:0,
      8:10
   },
   'idecyl_refugio_size': 20,
   'idecyl_refugio_ol_clr': "0 0 0",
   'idecyl_refugio_clr': "0 0 0",
   'idecyl_refugio_lbl_clr': "0 0 0",
   'idecyl_refugio_ol_width': 7,
   'idecyl_refugio_priority': 5,

   ###### idecyl_senal ######
   'idecyl_senal_data': { 0: '"data/idecyl/sigren_senal/senalPoint.shp"' },
   'display_idecyl_senal': { 0:0, 12:1 },
   'display_idecyl_senal_symbol': { 0:0, 10:1 },
   'display_idecyl_senal_label': { 0:0, 16:1 },
   'idecyl_senal_font': "sc",
   'idecyl_senal_lbl_ol_clr': "255 255 255",
   'idecyl_senal_lbl_ol_width': 2,
   'idecyl_senal_lbl_size': { 0:0, 16:10 },
   'idecyl_senal_size': 20,
   'idecyl_senal_ol_clr': "0 0 0",
   'idecyl_senal_clr': "0 0 0",
   'idecyl_senal_lbl_clr': "0 0 0",
   'idecyl_senal_ol_width': 2,
   'idecyl_senal_priority': 1,

   ###### idecyl_zona_acamp ######
   'idecyl_zona_acamp_data': { 0: '"data/idecyl/sigren_zona_acamp/zona_acampPoint.shp"' },
   'display_idecyl_zona_acamp': { 0:0, 10:1 },
   'display_idecyl_zona_acamp_symbol': { 0:0, 10:1 },
   'display_idecyl_zona_acamp_label': { 0:0, 16:1 },
   'idecyl_zona_acamp_font': "sc",
   'idecyl_zona_acamp_lbl_ol_clr': "255 255 255",
   'idecyl_zona_acamp_lbl_ol_width': 5,
   'idecyl_zona_acamp_lbl_size': {
      0:0,
      8:10
   },
   'idecyl_zona_acamp_size': 20,
   'idecyl_zona_acamp_ol_clr': "0 0 0",
   'idecyl_zona_acamp_clr': "0 0 0",
   'idecyl_zona_acamp_lbl_clr': "0 0 0",
   'idecyl_zona_acamp_ol_width': 2,
   'idecyl_zona_acamp_priority': 6,

   ###### idecyl_zona_rec ######
   'idecyl_zona_rec_data': { 0: '"data/idecyl/sigren_zona_rec/zona_recPoint.shp"' },
   'display_idecyl_zona_rec': { 0:0, 12:1 },
   'display_idecyl_zona_rec_symbol': { 0:0, 10:1 },
   'display_idecyl_zona_rec_label': { 0:0, 16:1 },
   'idecyl_zona_rec_font': "sc",
   'idecyl_zona_rec_lbl_ol_clr': "255 255 255",
   'idecyl_zona_rec_lbl_ol_width': 2,
   'idecyl_zona_rec_lbl_size': {
      0:0,
      8:10
   },
   'idecyl_zona_rec_size': 25,
   'idecyl_zona_rec_ol_clr': "255 255 255",
   'idecyl_zona_rec_clr': "0 0 0",
   'idecyl_zona_rec_lbl_clr': "0 0 0",
   'idecyl_zona_rec_ol_width': 2,
   'idecyl_zona_rec_priority': 3,
   
   ###### idecyl_ren ######
   'idecyl_ren_data': { 0: '"data/idecyl/sigren_ren_cyl/ren_cyl.shp"' },
   'display_idecyl_ren': {0:0, 5:1},
   'idecyl_ren_clr': '"#95c7a2"',
   'display_idecyl_ren_lbl' : {0:0, 8:1},
   'idecyl_ren_font': "sc",
   'idecyl_ren_lbl_size': 8,
   'idecyl_ren_lbl_clr': '0 0 0',
   'idecyl_ren_lbl_ol_clr': "255 255 255",
   'idecyl_ren_lbl_ol_width': 2,
}

namedstyles = {
   'default': {},
   'outlined':{
      'display_motorway_outline': {
         0:0,
         7:1
      },
      'motorway_ol_width': {
         0:0.5,
         10:1
      },
      'motorway_ol_clr': '0 0 0',
      'display_trunk_outline': {
         0:0,
         7:1,
      },
      'trunk_ol_width': {
         0:0.5,
         10:1
      },
      'trunk_ol_clr': '0 0 0',
      'display_primary_outline': {
         0:0,
         9:1
      },
      'primary_ol_width': {
         0:0.5,
         11:1
      },
      'primary_ol_clr': '0 0 0',
      'display_secondary_outline': {
         0:0,
         10:1
      },
      'secondary_ol_width': {
         0:0.5,
         13:1
      },
      'secondary_ol_clr': '0 0 0',
      'display_tertiary_outline': {
         0:0,
         12:1
      },
      'tertiary_ol_width': {
         0:0.5,
         15:1
      },
      'tertiary_ol_clr': '0 0 0',
      'display_other_outline': {
         0:0,
         14:1
      },
      'other_width': {
         0:0,
         11:0.5,
         14:2.5,
         15:4,
         16:6,
      },
      'other_ol_width': {
         0:0.5,
         17:1
      },
      'other_ol_clr': '0 0 0',
      'display_pedestrian_outline': {
         0:0,
         13:1
      },
      'pedestrian_ol_width': {
         0:0.5,
         17:1
      },
      'pedestrian_ol_clr': '0 0 0',
      'display_pier_outline': {0:0, 11:1},
      'pier_ol_width': {
         0:0.5,
         17:1
      },
   },
   'centerlined': {
      'display_motorway_centerline' : {
         0:0,
         10:1
      },
      'motorway_centerline_clr': {
         0: '255 253 139'
      },
      'motorway_centerline_width': {
         0:1,
         12:1.5,
         14:2
      },
      'display_trunk_centerline' : {
         0:0,
         10:1
      },
      'trunk_centerline_clr': {
         0: '255 255 255'
      },
      'trunk_centerline_width': {
         0:1,
         12:1.5,
         14:2
      }
   },
   'google':{
      'motorway_clr': "253 146 58",
      'trunk_clr': "255 195 69",
      'primary_clr': {
         0:'193 181 157',
         9:"255 253 139"
      },
      'secondary_clr': {
         0:'193 181 157',
         10:"255 253 139"
      },
      'tertiary_clr': {
         0:'193 181 157',
         12:"255 253 139"
      },
      'other_clr': {
         0:'193 181 157',
         14:"255 255 255"
      },
      'pedestrian_clr': '250 250 245',
      'forest_clr': "203 216 195",
      'industrial_clr': "209 208 205",
      'education_clr': "222 210 172",
      'hospital_clr': "229 198 195",
      'residential_clr': "242 239 233",
      'land_clr': "242 239 233",
      'park_clr': '181 210 156',
      'ocean_clr': '153 179 204',
      'waterarea_clr': '153 179 204',
      'river_clr': '153 179 204',
      'stream_clr': '153 179 204',
      'canal_clr': '153 179 204',

      'motorway_ol_clr': '186 110 39',
      'trunk_ol_clr': '221 159 17',
      'primary_ol_clr': '193 181 157',
      'secondary_ol_clr': '193 181 157',
      'tertiary_ol_clr': '193 181 157',
      'other_ol_clr': '193 181 157',
      'pedestrian_ol_clr': '193 181 157',
      'pier_ol_clr': '193 181 157',
      'display_buildings':{0:0, 11:1}
   },
   'michelin':{
      'motorway_clr': '228 24 24',
      'trunk_clr': '228 24 24',
      'primary_clr': {
         0:'"#aaaaaa"',
         9:'228 24 24'
      },
      'secondary_clr': {
         0:'"#aaaaaa"',
         10:'252 241 20'
      },
      'tertiary_clr': {
         0:'"#aaaaaa"',
         12:'252 241 20'
      },
      'other_clr': {
         0:'"#aaaaaa"',
         13:'"#ffffff"'
      },
      'display_primary_outline': {
         0:0,
         11:1
      },
      'display_secondary_outline': {
         0:0,
         12:1
      },
      'display_tertiary_outline': {
         0:0,
         13:1
      },
      'display_other_outline': {
         0:0,
         14:1
      },

      'motorway_ol_width': 0.5,
      'trunk_ol_width': 0.5,
      'primary_ol_width': 0.2,
      'secondary_ol_width': 0.2,
      'tertiary_ol_width': 0.2,
      'other_ol_width': 0.2,
      'pier_ol_width': 0.2,

      'pedestrian_clr': '"#fafaf5"',
      'forest_clr': '188 220 180',
      'industrial_clr': '"#ebe5d9"',
      'education_clr': '"#ded1ab"',
      'hospital_clr': '"#e6c8c3"',
      'residential_clr': '255 234 206',
      'land_clr': '"#ffffff"',
      'park_clr': '"#d6edb9"',
      'ocean_clr': '172 220 244',
      'waterarea_clr': '172 220 244',
      'river_clr': '172 220 244',
      'stream_clr': '172 220 244',
      'canal_clr': '172 220 244',

      'motorway_ol_clr': '0 0 0',
      'trunk_ol_clr': '0 0 0',
      'primary_ol_clr': '0 0 0',
      'secondary_ol_clr': '0 0 0',
      'tertiary_ol_clr': '0 0 0',
      'other_ol_clr': '0 0 0',
      'pedestrian_ol_clr': '0 0 0',
      'pier_ol_clr': '0 0 0',
      'footway_clr': '"#7f7f7f"'
   },
   'bing':{
      'motorway_clr': '"#BAC3A8"',
      'trunk_clr': '"#F2935D"',
      'primary_clr': {
         0:'"#aaaaaa"',
         9:'"#FEF483"'
      },
      'secondary_clr': {
         0:'"#aaaaaa"',
         10:'"#FCFCCC"'
      },
      'tertiary_clr': {
         0:'"#aaaaaa"',
         12:'"#ffffff"'
      },
      'other_clr': {
         0:'"#aaaaaa"',
         13:'"#ffffff"'
      },
      'pedestrian_clr': '"#fafaf5"',
      'forest_clr': '"#d6edb9"',
      'industrial_clr': '"#ebe5d9"',
      'education_clr': '"#ded1ab"',
      'hospital_clr': '"#e6c8c3"',
      'residential_clr': '"#f6f1e6"',
      'land_clr': '"#f6f1e6"',
      'park_clr': '"#d6edb9"',
      'ocean_clr': '"#b3c6d4"',
      'waterarea_clr': '"#b3c6d4"',
      'river_clr': '"#b3c6d4"',
      'stream_clr': '"#b3c6d4"',
      'canal_clr': '"#b3c6d4"',

      'motorway_ol_clr': '"#39780f"',
      'trunk_ol_clr': '"#bf6219"',
      'primary_ol_clr': '"#d17f40"',
      'secondary_ol_clr': '"#bbb8b4"',
      'tertiary_ol_clr': '"#b7ac9a"',
      'other_ol_clr': '"#b7ac9a"',
      'pedestrian_ol_clr': '193 181 157',
      'pier_ol_clr': '193 181 157',
      'footway_clr': '"#7f7f7f"'
   },
   'osm2pgsql': {
      'waterarea_data': {
         0: '"way from (select way,osm_id , OSM_NAME_COLUMN as name, waterway as type from OSM_PREFIX_polygon where \\\"natural\\\"=\'water\' or landuse=\'basin\' or landuse=\'reservoir\' or waterway=\'riverbank\') as foo using unique osm_id using srid=OSM_SRID"'
      },
      'waterways_data': {
         0: '"way from (select way,waterway as type,osm_id, OSM_NAME_COLUMN as name from OSM_PREFIX_line where waterway IN (\'river\', \'stream\', \'canal\')) as foo using unique osm_id using srid=OSM_SRID"'
      },
      'places_data': {
         0: '"way from (select osm_id, way, OSM_NAME_COLUMN as name, place as type from OSM_PREFIX_point where place in (\'country\',\'continent\') and OSM_NAME_COLUMN is not NULL ) as foo using unique osm_id using srid=OSM_SRID"',
         3: '"way from (select osm_id, way, OSM_NAME_COLUMN as name, place as type from OSM_PREFIX_point where place in (\'country\',\'continent\',\'city\') and OSM_NAME_COLUMN is not NULL ) as foo using unique osm_id using srid=OSM_SRID"',
         8: '"way from (select osm_id, way, OSM_NAME_COLUMN as name, place as type from OSM_PREFIX_point where place in (\'city\',\'town\') and OSM_NAME_COLUMN is not NULL ) as foo using unique osm_id using srid=OSM_SRID"',
         11: '"way from (select osm_id, way, OSM_NAME_COLUMN as name, place as type from OSM_PREFIX_point where place in (\'city\',\'town\',\'village\') and OSM_NAME_COLUMN is not NULL ) as foo using unique osm_id using srid=OSM_SRID"',
         13: '"way from (select osm_id, way, OSM_NAME_COLUMN as name, place as type from OSM_PREFIX_point where place is not NULL and OSM_NAME_COLUMN is not NULL ) as foo using unique osm_id using srid=OSM_SRID"',
      },
      'railways_data': {
         0:'"way from (select way, osm_id, tunnel, railway as type from OSM_PREFIX_line where railway=\'rail\') as foo using unique osm_id using srid=OSM_SRID"'
      },
      'landusage_data': {
         0:'"way from (select way, osm_id, name, type from (select way, st_area(way) as area, osm_id, (case when landuse is not null then landuse else (case when \\\"natural\\\" is not null then \\\"natural\\\" else (case when leisure is not null then leisure else amenity end) end) end) as type, OSM_NAME_COLUMN as name from OSM_PREFIX_polygon) as osm2 \
         where type in (\'forest\',\'wood\',\'residential\')\
         order by area desc) as foo using unique osm_id using srid=OSM_SRID"',
         6:'"way from (select way, osm_id, name, type from (select way , st_area(way) as area ,osm_id, (case when landuse is not null then landuse else (case when \\\"natural\\\" is not null then \\\"natural\\\" else (case when leisure is not null then leisure else amenity end) end) end) as type, OSM_NAME_COLUMN as name from OSM_PREFIX_polygon) as osm2 \
         where type in (\'forest\',\'wood\',\'industrial\',\'commercial\',\'residential\')\
         order by area desc) as foo using unique osm_id using srid=OSM_SRID"',
         9:'"way from (select way, osm_id, name, type from (select way, st_area(way) as area ,osm_id, (case when landuse is not null then landuse else (case when \\\"natural\\\" is not null then \\\"natural\\\" else (case when leisure is not null then leisure else amenity end) end) end) as type, OSM_NAME_COLUMN as name from OSM_PREFIX_polygon) as osm2 \
         where type in (\'forest\',\'wood\',\'pedestrian\',\'cemetery\',\'industrial\',\'commercial\',\
         \'brownfield\',\'residential\',\'school\',\'college\',\'university\',\
         \'military\',\'park\',\'golf_course\',\'hospital\',\'parking\',\'stadium\',\'sports_center\',\
         \'pitch\') order by area desc) as foo using unique osm_id using srid=OSM_SRID"',
         12:'"way from (select way, osm_id, name, type from (select way , st_area(way) as area ,osm_id, (case when landuse is not null then landuse else (case when \\\"natural\\\" is not null then \\\"natural\\\" else (case when leisure is not null then leisure else amenity end) end) end) as type, OSM_NAME_COLUMN as name from OSM_PREFIX_polygon) as osm2 \
         where type in (\'forest\',\'wood\',\'pedestrian\',\'cemetery\',\'industrial\',\'commercial\',\
         \'brownfield\',\'residential\',\'school\',\'college\',\'university\',\
         \'military\',\'park\',\'golf_course\',\'hospital\',\'parking\',\'stadium\',\'sports_center\',\
         \'pitch\') order by area desc) as foo using unique osm_id using srid=OSM_SRID"'
      },
      'roads_data': {
         0: '"way from (select osm_id,way,OSM_NAME_COLUMN as name,ref,highway as type, 0 as tunnel, 0 as bridge from OSM_PREFIX_line where highway in (\'motorway\',\'trunk\') order by z_order asc, st_length(way) asc) as foo using unique osm_id using srid=OSM_SRID"',
         8: '"way from (select osm_id,way,OSM_NAME_COLUMN as name,ref,highway as type, 0 as tunnel, 0 as bridge from OSM_PREFIX_line where highway in (\'motorway\',\'trunk\',\'primary\') order by z_order asc, st_length(way) asc) as foo using unique osm_id using srid=OSM_SRID"',
         9: '"way from (select osm_id,way,OSM_NAME_COLUMN as name,ref,highway as type, 0 as tunnel, 0 as bridge from OSM_PREFIX_line where highway in (\'motorway\',\'trunk\',\'primary\',\'secondary\',\'motorway_link\',\'trunk_link\',\'primary_link\')order by z_order asc, st_length(way) asc) as foo using unique osm_id using srid=OSM_SRID"',
         10:'"way from (select osm_id,way,OSM_NAME_COLUMN as name,ref,highway as type, 0 as tunnel, 0 as bridge from OSM_PREFIX_line where highway in (\'motorway\',\'trunk\',\'primary\',\'secondary\',\'tertiary\',\'motorway_link\',\'trunk_link\',\'primary_link\',\'secondary_link\',\'tertiary_link\') order by z_order asc, st_length(way) asc) as foo using unique osm_id using srid=OSM_SRID"',
         11:'"way from (select osm_id,way,OSM_NAME_COLUMN as name,ref,highway as type, 0 as tunnel, 0 as bridge from OSM_PREFIX_line where highway is not null order by z_order asc, st_length(way) asc) as foo using unique osm_id using srid=OSM_SRID"',
         14:'"way from (select osm_id,way,OSM_NAME_COLUMN as name,ref,highway||(case when bridge=\'yes\' then 1 else 0 end)||(case when tunnel=\'yes\' then 1 else 0 end) as type from OSM_PREFIX_line where highway is not null order by z_order asc, st_length(way) asc) as foo using unique osm_id using srid=OSM_SRID"',
      },

   },
   'bw':{
        'park_clr': "0 0 0",
        'residential_clr': "0 0 0",
        'town_ol_clr': "0 0 0",
        'other_clr': "0 0 0",
        'motorway_ol_clr': "0 0 0",
        'city_ol_clr': "0 0 0",
        'suburb_ol_clr': "0 0 0",
        'forest_clr': "0 0 0",
        'tertiary_clr': "0 0 0",
        'river_clr': "0 0 0",
        'building_clr': "0 0 0",
        'secondary_ol_clr': "0 0 0",
        'pedestrian_ol_clr': "0 0 0",
        'cemetery_clr': "0 0 0",
        'hamlet_ol_clr': "0 0 0",
        'land_clr': "0 0 0",
        'capital_fg_clr': "0 0 0",
        'town_clr': "0 0 0",
        'border_2_inner_clr': "0 0 0",
        'pedestrian_clr': "0 0 0",
        'taxiway_clr': "0 0 0",
        'cycleway_ol_clr': "0 0 0",
        'footway_ol_clr': "0 0 0",
        'canal_clr': "0 0 0",
        'stream_clr': "0 0 0",
        'village_clr': "0 0 0",
        'track_clr': "0 0 0",
        'hospital_clr': "0 0 0",
        'motorway_clr': "0 0 0",
        'trunk_clr': "0 0 0",
        'ocean_clr': "0 0 0",
        'building_ol_clr': "0 0 0",
        'runway_center_clr': "0 0 0",
        'border_2_clr': "0 0 0",
        'village_ol_clr': "0 0 0",
        'railway_ol_clr': "0 0 0",
        'primary_clr': "0 0 0",
        'industrial_clr': "0 0 0",
        'primary_bridge_clr': "0 0 0",
        'track_ol_clr': "0 0 0",
        'other_ol_clr': "0 0 0",
        'other_bridge_clr': "0 0 0",
        'railway_clr': "0 0 0",
        'education_clr': "0 0 0",
        'hamlet_clr': "0 0 0",
        'footway_clr': "0 0 0",
        'waterarea_clr': "0 0 0",
        'locality_ol_clr': "0 0 0",
        'secondary_bridge_clr': "0 0 0",
        'motorway_bridge_clr': "0 0 0",
        'locality_clr': "0 0 0",
        'runway_clr': "0 0 0",
        'waterarea_ol_clr': "0 0 0",
        'capital_ol_clr': "0 0 0",
        'cycleway_clr': "0 0 0",
        'capital_clr': "0 0 0",
        'primary_ol_clr': "0 0 0",
        'tertiary_ol_clr': "0 0 0",
        'residential_ol_clr': "0 0 0",
        'trunk_bridge_clr': "0 0 0",
        'city_clr': "0 0 0",
        'secondary_clr': "0 0 0",
        'suburb_clr': "0 0 0",
        'industrial_ol_clr': "0 0 0",
        'sports_clr': "0 0 0",
        'tertiary_bridge_clr': "0 0 0",
        'trunk_ol_clr': "0 0 0",
        'pedestrian_bridge_clr': "0 0 0",
        'transport_clr': "0 0 0",

       'waterarea_lbl_clr': '"#000000"',
       'waterarea_clr': '"#000000"',
       'waterarea_ol_clr': '"#000000"',
       'ocean_clr': '"#000000"',
       'canal_clr': '"#000000"',
       'stream_clr': '"#000000"',
       'river_clr': '"#000000"',
       'river_clr': '"#000000"',
       'canal_lbl_clr': '"#000000"',
       'stream_lbl_clr': '"#000000"',
       'river_lbl_clr': '"#000000"',


       'motorway_bridge_clr':"255 255 255",
       'trunk_bridge_clr':"255 255 255",
       'primary_bridge_clr':"255 255 255",
       'secondary_bridge_clr':"255 255 255",
       'tertiary_bridge_clr':"255 255 255",
       'other_bridge_clr':"255 255 255",
       'pedestrian_bridge_clr':"255 255 255",
       'motorway_centerline_clr': '255 255 255',

      'motorway_clr': '"#000000"',
      'trunk_clr': '"#000000"',
      'primary_clr': {
         0:'"#FFFFFF"',
         9:'"#000000"'
      },
      'secondary_clr': {
         0:'"#FFFFFF"',
         10:'"#000000"'
      },
      'tertiary_clr': {
         0:'"#FFFFFF"',
         12:'"#ffffff"'
      },
      'other_clr': {
         0:'"#FFFFFF"',
         13:'"#ffffff"'
      },
      'pedestrian_clr': '"#ffffff"',
      'forest_clr': '"#ffffff"',
      'industrial_clr': '"#ffffff"',
      'education_clr': '"#ffffff"',
      'hospital_clr': '"#ffffff"',
      'residential_clr': '"#ffffff"',
      'land_clr': '"#ffffff"',
      'park_clr': '"#ffffff"',
      'ocean_clr': '"#ffffff"',
      'waterarea_clr': '"#ffffff"',
      'river_clr': '"#ffffff"',
      'stream_clr': '"#ffffff"',
      'canal_clr': '"#ffffff"',

      'motorway_ol_clr': '"#FFFFFF"',
      'trunk_ol_clr': '"#ffffff"',
      'primary_ol_clr': '"#FFFFFF"',
      'secondary_ol_clr': '"#FFFFFF"',
      'tertiary_ol_clr': '"#FFFFFF"',
      'other_ol_clr': '"#000000"',
      'pedestrian_ol_clr': '255 255 255',
      'pier_ol_clr': '0 0 0',
      'footway_clr': '"#000000"'
   },
}

# these are the preconfigured styles that can be called when creating the final mapfile,
# e.g. with `make STYLE=google`. This will create an osm-google.map mapfile
style_aliases = {

   # map with no road casing and few colors, suited for using as a basemap when overlaying
   # other layers without risk of confusion between layers.
   "default":"default",

   # a style resembling the google-maps theme
   "google":"default,outlined,google",

   # same style as above, but using data coming from an osm2pgsql schema rather than imposm
   "googleosm2pgsql":"default,outlined,google,osm2pgsql",
   "bing":"default,outlined,bing",
   "michelin":"default,outlined,centerlined,michelin",

   "bw":"default,outlined,centerlined,bw"
}


parser = argparse.ArgumentParser()
parser.add_argument("-l", "--level", dest="level", type=int, action="store", default=-1,
                  help="generate file for level n")
parser.add_argument("-g", "--global", dest="full", action="store_true", default=False,
                  help="generate global include file")
parser.add_argument("-s", "--style", action="store", dest="style", default="default",
                  help="comma separated list of styles to apply (order is important)")

args = parser.parse_args()

for namedstyle in style_aliases[args.style].split(','):
   style.update(namedstyles[namedstyle].items())

if args.full:
   print("###### level 0 ######")
   for k, v in style.items():
      if isinstance(v, dict):
         print("#define _{0}0 {1}".format(k, v[0]))
      else:
         print("#define _{0}0 {1}".format(k, v))


   for i in range(1, 19):
      print('')
      print("###### level {0} ######".format(i))
      for k, v in style.items():
         if isinstance(v, dict):
            if not i in v:
               print("#define _{0}{1} _{0}{2}".format(k, i, i-1))
            else:
               print("#define _{0}{1} {2}".format(k, i, v[i]))
         else:
            print("#define _{0}{1} {2}".format(k, i, v))

if args.level != -1:
   level = args.level
   for k, v in style.items():
      print("#undef _{0}".format(k))

   for k, v in style.items():
      print("#define _{0} _{0}{1}".format(k, level))
