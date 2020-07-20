import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *

def process_song_file(cur, filepath):
    """
    - Function reads the song dataset source file in the 'filepath' location and loads the tables songs and artists
    """    
    
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data = df[['song_id', 'title', 'artist_id','year', 'duration']].values.tolist()[0] 
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = df[['artist_id', 'artist_name', 'artist_location','artist_latitude', 'artist_longitude']].values.tolist()[0]
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    - Function reads the log dataset source file in the 'filepath' location, filters by 'NextSong' action and loads the tables time, users and songplays 
    """  
    
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[(df.page == 'NextSong')] 

    # convert timestamp column to datetime
    Date_Time = pd.to_datetime(df.ts, unit='ms')
    timestamp = Date_Time
    hour = Date_Time.dt.hour
    day = Date_Time.dt.day
    week = Date_Time.dt.week
    month = Date_Time.dt.month
    year = Date_Time.dt.year
    weekday = Date_Time.dt.weekday

    df['timestamp'] = timestamp
    df['hour'] = hour
    df['day'] = day
    df['week'] = week
    df['month'] = month
    df['year'] = year
    df['weekday'] = weekday
    
    t=df[['timestamp', 'hour', 'day', 'week','month', 'year', 'weekday']]
    
    # insert time data records
    time_data = list (t.values)
    column_labels =list(t)
    time_df = pd.DataFrame(time_data, columns = column_labels) 

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender','level'] ]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    songplay_data_list =[]
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (row.timestamp, row.userId, row.level, str(songid), str(artistid), row.itemInSession, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)

def process_data(cur, conn, filepath, func):
   
    """
    - Function reads the source files one at a time in the 'filepath' location and calls the 'process_song_file' and 'process_log_file' functions
    - 'process_song_file' and 'process_log_file' functions are called by passing the cursor and absolute path of a source file 
    """  

    
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    
    """
    - Main Function connects to sparkifydb and calls 'process_data' function to load song data set and log dataset in sequence
    """  
    
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()
    

if __name__ == "__main__":
    main()