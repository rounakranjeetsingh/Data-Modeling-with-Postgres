To run the Python scripts in the Project:
1. Open TERMINAL from launcher
2. Execute: python /home/workspace/create_tables.py
3. Execute: python /home/workspace/etl.py

root@aca465327b12:/home/workspace# python /home/workspace/create_tables.py
root@aca465327b12:/home/workspace# python /home/workspace/etl.py
75 files found in data/song_data
1/75 files processed.
2/75 files processed.
3/75 files processed.
4/75 files processed.
5/75 files processed.
6/75 files processed.
7/75 files processed.
8/75 files processed.
9/75 files processed.
10/75 files processed.
11/75 files processed.
12/75 files processed.
13/75 files processed.
14/75 files processed.
15/75 files processed.
16/75 files processed.
17/75 files processed.
18/75 files processed.
19/75 files processed.
20/75 files processed.
21/75 files processed.
22/75 files processed.
23/75 files processed.
24/75 files processed.
25/75 files processed.
26/75 files processed.
27/75 files processed.
28/75 files processed.
29/75 files processed.
30/75 files processed.
31/75 files processed.
32/75 files processed.
33/75 files processed.
34/75 files processed.
35/75 files processed.
36/75 files processed.
37/75 files processed.
38/75 files processed.
39/75 files processed.
40/75 files processed.
41/75 files processed.
42/75 files processed.
43/75 files processed.
44/75 files processed.
45/75 files processed.
46/75 files processed.
47/75 files processed.
48/75 files processed.
49/75 files processed.
50/75 files processed.
51/75 files processed.
52/75 files processed.
53/75 files processed.
54/75 files processed.
55/75 files processed.
56/75 files processed.
57/75 files processed.
58/75 files processed.
59/75 files processed.
60/75 files processed.
61/75 files processed.
62/75 files processed.
63/75 files processed.
64/75 files processed.
65/75 files processed.
66/75 files processed.
67/75 files processed.
68/75 files processed.
69/75 files processed.
70/75 files processed.
71/75 files processed.
72/75 files processed.
73/75 files processed.
74/75 files processed.
75/75 files processed.
30 files found in data/log_data
1/30 files processed.
2/30 files processed.
3/30 files processed.
4/30 files processed.
5/30 files processed.
6/30 files processed.
7/30 files processed.
8/30 files processed.
9/30 files processed.
10/30 files processed.
11/30 files processed.
12/30 files processed.
13/30 files processed.
14/30 files processed.
15/30 files processed.
16/30 files processed.
17/30 files processed.
18/30 files processed.
19/30 files processed.
20/30 files processed.
21/30 files processed.
22/30 files processed.
23/30 files processed.
24/30 files processed.
25/30 files processed.
26/30 files processed.
27/30 files processed.
28/30 files processed.
29/30 files processed.
30/30 files processed.
root@aca465327b12:/home/workspace# 


Summary of the project: 
The purpose of the project is to do a song play analysis for a startup called Sparkify by users who have free or paid subscriptions. The data that is being sourced for this analysis is song related metadata and user activity logs from Sparkify's music streaming app. The song play analysis can have metrics across highly active users, number of sessions per user, locations with the most users, Most common device platforms of app usage,  etc.

Database schema design:
1. The database sparkifydb contains a star schema optimized for queries on song play analysis.
2. The star schema consists of the fact table "songplays" which records in log data associated with songs that were played i.e. records with page NextSong. 
3. The dimension table "users" contains information pertaining to identification of the user who is playing the song on the app and the level of subscription (free/paid) to play the songs.
4. The dimension table "songs" contains information pertaining to song metadata.
5. The dimension table "artists" contains information pertaining to artist metadata.
6. The dimension table "time" is capturing the timestamps of records in songplays broken down into specific units.

ETL Pipeline:
1. Extract the songs data and load into 'songs' table -  Total number of rows - 75.
2. Extract the artists data and load into the 'artists' table - Total number of rows - 75.
3. Extract user log data and filter by "Next Song" action.
4. Convert the timestamp in the column 'ts' in user log to datetime and extract timestamp, hour, day, week of year, month, year, and weekday.
5. Load the 'time' table with the extracted values -  Total number of rows - 6820.
6. Load the user table with data from the user log -  Total number of rows - 6820.
7. Load the fact table 'songplays' -  Total number of rows - 6820.

[Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.]

Explanation of the files in the repository: 
1. Folder "data": The repository contains a data folder containg the Song and Log Data sets that serve as teh souce of Data to analyze.
2. sql_queries.py :  A python script containing CREATE, INSERT, DROP & SELECT Statement varibles used in create_tables.py & etl.py to perform the ETL process.
3. create_tables.py: A python script that creates the database "sparkifydb" and the fact and dimension tables.
4. etl.ipynb: A notebook that develops the ETL processes in each table.
5. etl.py : A python script containing the the ETL pipeline that extracts the files from the data folder, transforms the data and load teh dimension and fact tables.
6. test.ipynb : A notebook that confirms the creation of the tables with the correct columns and checks the count of records in each table. 
7. README.md

Rubrics Criteria ETL : Validation Queries
1. The solution dataset will only have 1 row with values for value containing ID for both songid and artistid in the fact table : 
    Query - SELECT * from SONGPLAYS where artist_id !='None';
songplay_id	start_time	user_id	level	song_id	artist_id	session_id	location	user_agent
3225	2018-11-21 21:56:47.796000	15	paid	SOZCTXZ12AB0182364	AR5KOSW1187FB35FF4	5	Chicago-Naperville-Elgin, IL-IN-WI	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/36.0.1985.125 Chrome/36.0.1985.125 Safari/537.36"


    Query - SELECT * from SONGPLAYS where song_id !='None';
songplay_id	start_time	user_id	level	song_id	artist_id	session_id	location	user_agent
3225	2018-11-21 21:56:47.796000	15	paid	SOZCTXZ12AB0182364	AR5KOSW1187FB35FF4	5	Chicago-Naperville-Elgin, IL-IN-WI	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/36.0.1985.125 Chrome/36.0.1985.125 Safari/537.36"

Example queries and results for song play analysis (queries written in test.ipynb):

1.  Count of 'paid' users for a given location:
    Query : select location, count(user_id) as cnt from songplays where level='paid' group by location order by cnt desc;
    
location	cnt
San Francisco-Oakland-Hayward, CA	650
Portland-South Portland, ME	648
Lansing-East Lansing, MI	557
Chicago-Naperville-Elgin, IL-IN-WI	462
Atlanta-Sandy Springs-Roswell, GA	428
Waterloo-Cedar Falls, IA	397
Lake Havasu City-Kingman, AZ	321
Tampa-St. Petersburg-Clearwater, FL	289
Sacramento--Roseville--Arden-Arcade, CA	241
Janesville-Beloit, WI	241
Winston-Salem, NC	213
Birmingham-Hoover, AL	208
Red Bluff, CA	178
San Jose-Sunnyvale-Santa Clara, CA	178
Marinette, WI-MI	169
New York-Newark-Jersey City, NY-NJ-PA	149
Augusta-Richmond County, GA-SC	140
Detroit-Warren-Dearborn, MI	72
San Antonio-New Braunfels, TX	33
Longview, TX	17


2. Count of 'free' users for a given location
    Query : select location, count(user_id) as cnt from songplays where level='free' group by location order by cnt desc;

location	cnt
San Jose-Sunnyvale-Santa Clara, CA	114
New York-Newark-Jersey City, NY-NJ-PA	113
Houston-The Woodlands-Sugar Land, TX	66
New Orleans-Metairie, LA	55
New Haven-Milford, CT	48
La Crosse-Onalaska, WI-MN	45
San Francisco-Oakland-Hayward, CA	41
Harrisburg-Carlisle, PA	37
Salinas, CA	37
Philadelphia-Camden-Wilmington, PA-NJ-DE-MD	35
Washington-Arlington-Alexandria, DC-VA-MD-WV	34
Sacramento--Roseville--Arden-Arcade, CA	29
Atlanta-Sandy Springs-Roswell, GA	28
Yuba City, CA	27
Phoenix-Mesa-Scottsdale, AZ	27
Palestine, TX	27
Lubbock, TX	27
Nashville-Davidson--Murfreesboro--Franklin, TN	25
Columbia, SC	25
Red Bluff, CA	23
Dallas-Fort Worth-Arlington, TX	21
Klamath Falls, OR	20
Eugene, OR	20
Santa Rosa, CA	20
San Antonio-New Braunfels, TX	19
Tampa-St. Petersburg-Clearwater, FL	18
Portland-South Portland, ME	17
St. Louis, MO-IL	16
Eureka-Arcata-Fortuna, CA	16
Birmingham-Hoover, AL	15
Minneapolis-St. Paul-Bloomington, MN-WI	15
Seattle-Tacoma-Bellevue, WA	14
Indianapolis-Carmel-Anderson, IN	14
Chicago-Naperville-Elgin, IL-IN-WI	13
Richmond, VA	13
Cedar Rapids, IA	10
Plymouth, IN	10
Milwaukee-Waukesha-West Allis, WI	9
Youngstown-Warren-Boardman, OH-PA	8
Oxnard-Thousand Oaks-Ventura, CA	7
Portland-Vancouver-Hillsboro, OR-WA	7
Janesville-Beloit, WI	7
Ogden-Clearfield, UT	7
Los Angeles-Long Beach-Anaheim, CA	6
Las Cruces, NM	6
Parkersburg-Vienna, WV	5
London, KY	5
San Diego-Carlsbad, CA	5
Raleigh, NC	4
Detroit-Warren-Dearborn, MI	4
Salt Lake City, UT	4
Pensacola-Ferry Pass-Brent, FL	3
Saginaw, MI	3
Elkhart-Goshen, IN	2
Miami-Fort Lauderdale-West Palm Beach, FL	2
Myrtle Beach-Conway-North Myrtle Beach, SC-NC	1


3. The total number of free and paid sessions of a user of the app:
    Query: select songplays.user_id, users.first_name, users.last_name, users.gender, users.level,  count(session_id) cnt from songplays, users where songplays.user_id=users.user_id  group by songplays.user_id, users.first_name, users.last_name, users.gender, users.level order by songplays.user_id;

user_id	first_name	last_name	gender	level	cnt
2	Jizelle	Benjamin	F	free	100
3	Isaac	Valdez	M	free	9
4	Alivia	Terrell	F	free	25
5	Elijah	Davis	M	free	16
6	Cecilia	Owens	F	free	529
7	Adelyn	Jordan	F	free	25
8	Kaylee	Summers	F	free	729
9	Wyatt	Scott	M	free	256
10	Sylvie	Cruz	F	free	784
11	Christian	Porter	F	free	4
12	Austin	Rosales	M	free	144
13	Ava	Robinson	F	free	25
14	Theodore	Harris	M	free	484
15	Lily	Koch	F	free	463
15	Lily	Koch	F	paid	213906
16	Rylan	George	M	free	3345
16	Rylan	George	M	paid	46384
17	Makinley	Jones	F	free	49
18	Jacob	Rogers	M	free	25
19	Zachary	Thomas	M	free	81
20	Aiden	Ramirez	M	paid	81
22	Sean	Wilson	F	free	4
23	Morris	Gilmore	M	free	16
24	Layla	Griffin	F	paid	103041
25	Jayden	Graves	M	paid	28561
26	Ryan	Smith	M	free	12996
27	Carlos	Carter	M	free	4
28	Brantley	West	M	free	49
29	Jacqueline	Lynch	F	free	1730
29	Jacqueline	Lynch	F	paid	117986
30	Avery	Watkins	F	paid	31684
32	Lily	Burns	F	free	3136
33	Bronson	Harris	M	free	400
34	Evelin	Ayala	F	free	81
35	Molly	Taylor	F	free	256
36	Matthew	Jones	M	free	1736
36	Matthew	Jones	M	paid	59768
37	Jordan	Hicks	F	free	1156
38	Gianna	Jones	F	free	9
39	Walter	Frye	M	free	4
40	Tucker	Garrison	M	free	49
41	Brayden	Clark	M	free	81
42	Harper	Barrett	M	paid	19600
43	Jahiem	Miles	M	free	121
44	Aleena	Kirby	F	paid	157609
45	Dominick	Norris	M	free	1
47	Kimber	Norris	F	free	9
48	Marina	Sutton	F	free	9
49	Chloe	Cuevas	F	free	26871
49	Chloe	Cuevas	F	paid	447850
50	Ava	Robinson	F	free	2304
51	Maia	Burke	F	free	225
52	Theodore	Smith	M	free	289
53	Celeste	Williams	F	free	400
54	Kaleb	Cook	M	free	729
55	Martin	Johnson	M	free	225
56	Cienna	Freeman	F	free	4
57	Katherine	Gay	F	free	64
58	Emily	Benson	F	paid	19600
59	Lily	Cooper	F	free	4
60	Devin	Larson	M	free	324
61	Samuel	Gonzalez	M	free	576
62	Connar	Moreno	M	free	100
63	Ayla	Johnson	F	free	400
64	Hannah	Calhoun	F	free	4
65	Amiya	Davidson	F	paid	289
66	Kevin	Arellano	M	free	1369
67	Colm	Santana	M	free	625
68	Jordan	Rodriguez	F	free	9
69	Anabelle	Simpson	F	free	841
70	Jaleah	Hayes	F	paid	1089
71	Ayleen	Wise	F	free	25
72	Hayden	Brock	F	paid	5184
73	Jacob	Klein	M	paid	83521
74	Braden	Parker	M	free	64
75	Joseph	Gutierrez	M	free	324
76	Jayden	Duffy	F	free	196
77	Magdalene	Herman	F	free	100
78	Chloe	Roth	F	free	196
79	James	Martin	M	free	4
80	Tegan	Levine	F	free	11305
80	Tegan	Levine	F	paid	430920
81	Sienna	Colon	F	free	36
82	Avery	Martinez	F	paid	7569
83	Stefany	White	F	free	729
84	Shakira	Hunt	F	free	36
85	Kinsley	Young	F	free	179
85	Kinsley	Young	F	paid	31862
86	Aiden	Hess	M	free	2025
87	Dustin	Lee	M	free	1
88	Mohammad	Rodriguez	M	free	7830
88	Mohammad	Rodriguez	M	paid	65070
89	Kynnedi	Sanchez	F	free	100
90	Andrea	Butler	F	free	9
91	Jayden	Bell	M	free	81
92	Ryann	Smith	F	free	729
94	Noah	Chavez	M	free	49
95	Sara	Johnson	F	paid	45369
96	Cierra	Finley	F	free	169
97	Kate	Harrell	F	paid	310249
98	Jordyn	Powell	F	free	16
99	Ann	Banks	F	free	16
100	Adler	Barrera	M	free	361
101	Jayden	Fox	M	free	30


4. Most common device platforms of app usage
    Query: %sql select user_agent, count(session_id) as cnt from songplays group by user_agent order by cnt desc;

user_agent	cnt
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36"	971
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/7.0.6 Safari/537.78.2"	708
Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0	696
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/36.0.1985.125 Chrome/36.0.1985.125 Safari/537.36"	577
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 Safari/537.36"	573
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:31.0) Gecko/20100101 Firefox/31.0	443
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36"	427
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"	419
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/7.0.5 Safari/537.77.4"	319
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0	310
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36"	259
"Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53"	228
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36"	179
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"	148
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"	111
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 Safari/537.36"	87
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:30.0) Gecko/20100101 Firefox/30.0	72
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 Safari/537.36"	45
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0	30
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36"	27
Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0	26
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.103 Safari/537.36"	20
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14"	18
Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko	16
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.102 Safari/537.36"	15
"Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D201 Safari/9537.53"	11
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36"	10
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"	10
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/538.46 (KHTML, like Gecko) Version/8.0 Safari/538.46"	10
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36"	9
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)	9
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:31.0) Gecko/20100101 Firefox/31.0	9
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10"	8
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36"	5
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14"	5
Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0	3
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)	2
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"	2
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 Safari/537.36"	2
Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko	1
