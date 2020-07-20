# DROP TABLES

songplay_table_drop = "drop table if exists songplays;"
user_table_drop = "drop table if exists users;"
song_table_drop = "drop table if exists songs;"
artist_table_drop = "drop table if exists artists;"
time_table_drop = "drop table if exists time;"

# CREATE TABLES

songplay_table_create = ("CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL, start_time timestamp, user_id int, level varchar, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent varchar, CONSTRAINT songplay_u UNIQUE(start_time,user_id,song_id,artist_id));")



user_table_create = ("CREATE TABLE IF NOT EXISTS users (user_id int, first_name varchar, last_name varchar, gender varchar, level varchar);")

song_table_create = ("CREATE TABLE IF NOT EXISTS songs (song_id varchar, title varchar, artist_id varchar, year int, duration float8);")

artist_table_create = ("CREATE TABLE IF NOT EXISTS artists (artist_id varchar, name varchar, location varchar, latitude varchar, longitude varchar);")

time_table_create = ("CREATE TABLE IF NOT EXISTS time (start_time timestamp, hour int, day varchar, week varchar, month varchar, year int, weekday varchar);")

# INSERT RECORDS

songplay_table_insert = ("INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT ON CONSTRAINT songplay_u  DO UPDATE SET level=EXCLUDED.level,  session_id = EXCLUDED.session_id, location = EXCLUDED.location, user_agent = EXCLUDED.user_agent")

user_table_insert = ("INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s,%s,%s,%s,%s)")


song_table_insert = ("INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s,%s,%s,%s,%s)")

artist_table_insert = ("INSERT INTO artists (artist_id, name, location, longitude, latitude) VALUES (%s,%s,%s,%s,%s)")


time_table_insert = ("INSERT INTO time (start_time, hour, day, week, month, year, weekday ) VALUES (%s,%s,%s,%s, %s, %s, %s)")

# FIND SONGS

song_select = ("SELECT song_id, songs.artist_id FROM songs,artists WHERE songs.artist_id=artists.artist_id AND songs.title =%s AND artists.name =%s AND songs.duration=%s ;")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]