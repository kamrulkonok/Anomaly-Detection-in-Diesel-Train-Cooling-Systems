README: 
** Overview **
The Cool Train project is part of the INFOH423 Data Mining Project for 2023/24, sponsored by the rolling stock team at the National Railway Company of Belgium (SNCB). This initiative focuses on analyzing and improving the cooling systems of SNCB's diesel trains, specifically the Belgian Railways Class 41. The main objective is to detect anomalies in the cooling systems that could indicate potential failures in engine or transmission operations, and thereby help in avoiding train delays and ensuring operational efficiency.

**Problem Statement**
Diesel trains, particularly the two-vehicle AR41, are equipped with intricate cooling systems necessary for the proper functioning of the engine and transmission. Anomalies in these systems can lead to significant operational disruptions. Our project aims to develop methods to effectively detect and categorize these anomalies, distinguishing between sensor noise, deviations in individual cooling systems, and systemic issues affecting overall engine performance.

**Dataset**
The project utilizes a 2GB CSV file containing time-series data from January to September 2023, capturing various operational parameters of the diesel trains. The data includes:

	-Temperatures and pressures from dual cooling systems
	-Engine RPMs
	-GPS locations
	-Key variables include air and water temperatures, oil pressures, and more, with timestamps for 	real-time tracking.
**Methods and Technologies Used**
	#Data Preprocessing
 		• Removal of null values, filtering based on time intervals, and cleansing of anomalous 		geolocation data.
		• Conversion of timestamps for time-series analysis.
  	#Exploratory Data Analysis (EDA)
   		• Statistical and visual techniques to investigate temporal patterns in temperature and 		pressure anomalies.
	#Data Enrichment
 		• Integration of weather data from nearby stations, considering various weather 			conditions like temperature, humidity, snowfall, and rain, to analyze their impact on 			cooling system performance.
   	#Anomaly Detection 
    		• Development of a real-time dashboard for anomaly visualization, aiding the rolling 			stock team in data-driven decision-making.

**Presentation**
- overleaf link: https://www.overleaf.com/2726483457sfsvcpcstxjw#4c1890

```

 ______   ________   _________  ________       ___ __ __    ________  ___   __     ________  ___   __    _______     
/_____/\ /_______/\ /________/\/_______/\     /__//_//_/\  /_______/\/__/\ /__/\  /_______/\/__/\ /__/\ /______/\    
\:::_ \ \\::: _  \ \\__.::.__\/\::: _  \ \    \::\| \| \ \ \__.::._\/\::\_\\  \ \ \__.::._\/\::\_\\  \ \\::::__\/__  
 \:\ \ \ \\::(_)  \ \  \::\ \   \::(_)  \ \    \:.      \ \   \::\ \  \:. `-\  \ \   \::\ \  \:. `-\  \ \\:\ /____/\ 
  \:\ \ \ \\:: __  \ \  \::\ \   \:: __  \ \    \:.\-/\  \ \  _\::\ \__\:. _    \ \  _\::\ \__\:. _    \ \\:\\_  _\/ 
   \:\/.:| |\:.\ \  \ \  \::\ \   \:.\ \  \ \    \. \  \  \ \/__\::\__/\\. \`-\  \ \/__\::\__/\\. \`-\  \ \\:\_\ \ \ 
    \____/_/ \__\/\__\/   \__\/    \__\/\__\/     \__\/ \__\/\________\/ \__\/ \__\/\________\/ \__\/ \__\/ \_____\/ 

```

```
___________   _______________________________________^__
 ___   ___ |||  ___   ___   ___    ___ ___  |   __  ,----\                     Simon Coessens
|   | |   |||| |   | |   | |   |  |   |   | |  |  | |_____\                      Pepe Jose Carlos
|___| |___|||| |___| |___| |___|  | O | O | |  |  |        \                       MD Kamrul Islam
           |||                    |___|___| |  |__|         )                        Narmina Mahmudova
___________|||______________________________|______________/
           |||                                        /--------
-----------'''---------------------------------------'
```

How to import weather data: 
  - Assign weather data from the closest weather station.
        - Is weather data always pulled from the closest weather station?
        - Would it be more accurate to assign a temperature based on trip partitions?
  - Choose a time interval and update weather data only after every time interval



TODO: 2 November
  - Narmina: Anomaly detection techniques ✅
  - Kamrul: Data Cleaning ✅, Anomaly detection techniques ✅
  - Pepe: Weather data ✅
  - Simon: Visualizations ✅, Separate journeys ✅

**NEXT MEETING**: thursday 9 november 10:00 

TODO: 9 November:
  - Simon: MobilityDB setup ✅
  - Narmina: Anomaly detection techniques ✅
  - Kamrul: Local notebook (jupyter) ✅
  - Pepe: other work ✅

for  everyone: 
  - Refresh on Data Mining concepts ✅
  - How to build Data Mining workflows? ✅
  - ![image](https://github.com/simoncoessens/DataMining/assets/129620441/c3b7423b-24a5-4186-ad73-a1e03bacf0ac)



WEATHER DATA: 
What weather data are we going to incorporate in the analysis? 
- ``Temperature``
- ```Humidity```
- ````Snowfall````
- ```Rain```

**NEXT MEETING**: thursday 16 november 10:00 


NEXT STEPS: 

Feature extraction: 
- Labeling the anomalies


 1. Data cleaning ( output: .csv)
	2.	Database creation
	3.	Add features to the DB
	4.	Feature extraction
	5.	Data mining algorithms

TASKS: 
- Connect Kaggle to local postgres (Simon) ✅
- Adding extra features to the DB (Pepe) ✅
- Correlation, heat map, feature extraction (Konok) ✅
- preprocessing (Narmina) ✅


**NEXT MEETING**: Sunday 19 november 10:00 


**NEXT MEETING:** Thursday 23, November (after going to the Data Mining lab)

Classification will be important for the stream outlier detection part of the project

Feature extraction:
- Difference between two sensors
- Temperature categorization

Type portability:
- Numerical to categorical (temperature values)

Descriptive Analytics:
- Narmina has performed sampling rate (it varies)
- Simon has looked into segment speed
- Pepe has looked into the bounding box (values not contained in the Belgium geom)

Noisy entries:
- Kamrul mentioned binning to clean the noisy entries

Distance:
- Distance to weather pull sensors can be included in the outlier detection analysis

Clustering:
- Could be useful to clean data (if a data point doesn't end up in a cluster it could be considered an outlier)

Topics to be investigated:
- Narmina: Classification and model validation data preparation
- Kamrul: Clustering
- Simon: Frequent patterns and association rule mining
- Pepe: Outlier mining


**Basic research questions:**
1. Absolute number of times the temperatures are outside the boundaries for each vehicle_id (maybe there are more for one -> problem with a veh_id).\
	SIMON: ✅ Look at R1.ipynb in exports

2.  Locations of the places where the temperatures are outside of the boundaries.\
	SIMON: ✅ R2

3.  Look at the rpm values for when the temperatures are outside the boundaries\
   	NARMINA: ✅ R3

4. Are there specific times of day, days of the week, or months where temperature anomalies are more frequent?\
   	KAMRUL: ✅ Look at R4_R5.ipynb in exports

8. Look at the speed and find anomalies\
   	SIMON: ✅ R8

9. Look at the internal temperature sensor values that exceed certain differences with the ambient temperature\
	PEPE: 🔄 working on it

10. Look at the differences between the pairs of sensors. Look at other attributes when they deviate from each other \
	PEPE: 🔄 working on it


**Ideas on things for the stream bonus task**
- Algorithm that checks incoming locations if the speed is within boundaries, it flags incorrect location
- Algorithm that checks incoming temperatures and checks the duration of occurrences when the temperature is outside of boundaries and then reports
