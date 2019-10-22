# Physiobank

Not sure what this folder should be called, or what it will encompass. Likely part of Amit project to make a physiological signal database. First will start by organizing ECG data at minimum.

# File Structure

## What type of files are within the folder?

There are multiple folders in the original Amit Research Drive, named _Ischemic and Genetic Mechanisms_.

- Datasets for analysis = MIMS and MIPS data
- Digitized ECG = Twins and Biobank and MIMS and MIPS ECG data / images
- HRV = empty folder
- MIMS2 research export = huge folder of HEA, SIG, and QRS file extensions, unclear which patient population
- Outcomes = MIMS and MIPS SAS data
- VU AMS data = appears to be range of data sets, powerpoints, etc on VUDAMS data

## Approach to explore the file trees

Likely will use bash scripting to help extract and organize the file system. Its a large file tree that is quite inconsistent.

# File Organization

## VU AMS

### Relevant Data Files

Patient_demographics.xls = self-explanatory
Notes.docx = guide on data extraction for a specific analysis type
PAT_data.xlsx = organized data points for all patients over all 3 visits
Empatica_data/ = folder involving all PAT data from all visits that were obtained
2000/ = folders patterned as 20**/, containing subfolders of 3 visits, containing a number of files inside
	Extension 5FS is the raw VUDAMS file
	The largest 5FS file is the "correct" patient file, raw VUDAMS data
	ECG data is organized as well, in some type of multicolumn format

### Directory File Tree
.
├── 2001
│   ├── 2001\ v1
│   ├── 2001\ v2
│   └── 2001\ v3
├── 2002
│   ├── 2002\ v1
│   ├── 2002\ v2
│   └── 2002\ v3
├── 2003
│   ├── 2003\ V1
│   └── 2003\ v2a
├── 2004
├── 2005
│   ├── 2005\ v1
│   ├── 2005\ v2
│   └── 2005\ v3
├── 2006
│   ├── 2006\ v1
│   ├── 2006\ v2
│   └── 2006\ v3
│       └── 2006v3_2
├── 2007
│   ├── 2007\ v1
│   ├── 2007\ v2
│   ├── 2007\ v3
│   └── 2007v1
├── 2008
│   ├── 2008\ v1
│   ├── 2008\ v2
│   └── 2008\ v3
├── 2009
│   ├── 2009\ v1
│   │   └── deleteoutliers
│   ├── 2009\ v2
│   └── 2009\ v3
├── 2010
│   ├── 2010\ v1
│   ├── 2010\ v2
│   └── 2010\ v3
├── 2011
│   ├── 2011\ v1
│   └── 2011\ v2
├── 2012
│   ├── 2012\ v1
│   ├── 2012\ v2
│   └── 2012\ v3
├── 2013
│   ├── 2013\ v1
│   ├── 2013\ v2
│   └── 2013\ v3
├── 2015
│   ├── 2015\ v1
│   ├── 2015\ v2
│   └── 2015\ v3
├── 2016
│   ├── 2016\ v1
│   ├── 2016\ v2
│   └── 2016\ v3
├── 2017
│   ├── 2017\ V1
│   ├── 2017\ v2
│   └── 2017\ v3
├── 2018
│   ├── 2018\ v1
│   │   └── ecgbeat
│   ├── 2018\ v2
│   └── 2018\ v3
├── 2020
│   ├── 2020\ v1
│   ├── 2020\ v2
│   └── 2020\ v3
├── 2021
│   ├── 2021\ v1
│   ├── 2021\ v2
│   └── 2021\ v3
├── 2022
│   ├── 2022\ v1
│   ├── 2022\ v2
│   └── 2022\ v3
├── 2023
│   ├── 2023\ Error\ Files
│   ├── 2023\ v2
│   └── 2023\ v3
├── 2024
│   ├── 2024\ v1
│   ├── 2024\ v2
│   └── 2024\ v3
├── 2025
│   ├── 2025\ v1
│   ├── 2025\ v2
│   └── 2025\ v3
├── 2026
│   ├── 2026\ v1
│   │   ├── 2026v1_2
│   │   └── Empatica_209976
│   ├── 2026\ v2
│   └── 2026\ v3
├── 2027
│   ├── 2027\ v1
│   ├── 2027\ v2
│   └── 2027\ v3
├── CAD_Papers
├── Data2
├── Draft
│   ├── IMAGES
│   └── New\ folder
├── Empatica
├── Empatica_data
│   ├── 2002v2
│   ├── 2002v3
│   ├── 2005v3
│   ├── 2006v3
│   ├── 2007
│   ├── 2007v1
│   ├── 2007v2
│   ├── 2007v3
│   ├── 2008v1
│   ├── 2008v2
│   ├── 2008v3
│   ├── 2009v1
│   ├── 2009v2
│   ├── 2009v3
│   ├── 2010v1
│   ├── 2010v2
│   ├── 2010v3
│   ├── 2011v2
│   ├── 2012v2
│   ├── 2013v3
│   ├── 2015v2
│   ├── 2015v3
│   ├── 2016v2
│   ├── 2017v2
│   ├── 2018v1
│   ├── 2018v2
│   ├── 2018v3
│   ├── 2020v2
│   ├── 2020v3
│   ├── 2021v1
│   ├── 2021v2
│   ├── 2022v2
│   ├── 2023v2
│   ├── 2025v1
│   ├── 2026v1
│   ├── 2027v1
│   └── PAT_data
├── Features_H25
├── ROC
├── Wilcoxon_ttest
├── all_data
├── effectsize
├── healthy_CAD_combine
├── healthy_CAD_scatters
│   └── tight_subplots
├── output_weka
└── paired_ttest

155 directories


