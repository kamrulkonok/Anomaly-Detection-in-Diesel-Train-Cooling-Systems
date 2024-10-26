# Anomaly Detection in Diesel Train Cooling Systems

## Overview
The Cool Train project is part of the INFOH423 Data Mining Project for 2023/24, sponsored by the rolling stock team at the National Railway Company of Belgium (SNCB). This initiative focuses on analyzing and improving the cooling systems of SNCB's diesel trains, specifically the Belgian Railways Class 41. The main objective is to detect anomalies in the cooling systems that could indicate potential failures in engine or transmission operations, and thereby help in avoiding train delays and ensuring operational efficiency.

## Problem Statement
Diesel trains, particularly the two-vehicle AR41, are equipped with intricate cooling systems necessary for the proper functioning of the engine and transmission. Anomalies in these systems can lead to significant operational disruptions. Our project aims to develop methods to effectively detect and categorize these anomalies, distinguishing between sensor noise, deviations in individual cooling systems, and systemic issues affecting overall engine performance.

## Dataset
The project utilizes a 2GB CSV file containing time-series data from January to September 2023, capturing various operational parameters of the diesel trains. The data includes:
- Temperatures and pressures from dual cooling systems
- Engine RPMs
- GPS locations
- Key variables include air and water temperatures, oil pressures, and more, with timestamps for real-time tracking.

## Methods and Technologies Used
### Data Preprocessing
- Removal of null values, filtering based on time intervals, and cleansing of anomalous geolocation data.
- Conversion of timestamps for time-series analysis.

### Exploratory Data Analysis (EDA)
- Statistical and visual techniques to investigate temporal patterns in temperature and pressure anomalies.

### Data Enrichment
- Integration of weather data from nearby stations, considering various weather conditions like temperature, humidity, snowfall, and rain, to analyze their impact on cooling system performance.

### Anomaly Detection
- Implementation of K-means clustering and Isolation Forest algorithms to differentiate between noise and genuine deviations in cooling systems.
- Development of a real-time dashboard for anomaly visualization, aiding the rolling stock team in data-driven decision-making.

## File Structure
```
/cool-train-project
│
├── pdf_files/ # Documentation and PDF reports
│ ├── Data Mining Presentation.pdf
│ ├── R1.pdf
│ ├── R10.1.pdf
│ ├── R10.2.pdf
│ ├── R11.pdf
│ ├── R12.pdf
│ ├── R2.pdf
│ ├── R8.pdf
│ ├── R9.pdf
│ ├── cover.pdf
│ ├── dashboard.pdf
│ └── r4-r5.pdf
│
├── src/ # Source code for analysis and processing
│ ├── 1. Data Preprocessing/
│ ├── 2. Data Exploration/
│ ├── 3. Data Enrichment/
│ ├── 4. Research Questions/
│ ├── 5. Anomaly Detection Methods/
│ ├── 6. Dashboard Development/
│ ├── 7. Streaming Data Analysis/
│ └── Old Files/
│
├── Data Mining Project.pdf # Project description and requirements
└── README.md
```
## Presentation
- Access our detailed presentation on Overleaf: [View Presentation](https://www.overleaf.com/2726483457sfsvcpcstxjw)


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
