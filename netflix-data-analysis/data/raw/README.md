# Raw Data

This folder is intended to store raw, unprocessed datasets.

Raw data files are not included in this repository to keep it lightweight and clean.

To use this project:

- [Download the dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows?resource=download) separately
- Place it in this folder before running the scripts

No modifications should be made to files in this directory.

# WIP LIST

## Issues Found
	- Large missing values in 'director' (~30%), 'cast' (~9%), and 'country' (~9%)
	- Negligible missing values in 'date_added' (10ct), 'rating' (4ct), duration (3ct)
	- Inconsistent data in 'rating' column (some entries contain movie duration instead)
	- Multiple values stored in single fields (e.g., multiple countries per entry)

## Possible Analyses
	- Content breakdown by genre (identifies viewer interest by proxy of Netflix development focus)
	- content breakdown by rating (identifies target audience)
	- Content growth over time
	- What countries produces the most content?
	- Basic movie/show stats (longest, shortest, average, most common genre)
	- How often does Netflix wait to add a movie or show on average (average difference between release year and date added)
	- Trend discovery (Has Netflix been adding more/less of a specific genre as time goes on)

## Cleaning Needed
	- Fill missing directors and casts with "Unknown".
	- Handle missing "country" values.
	- Ignore minor missing values as they do not have a realized impact on analysis outcomes.
	- Handle duration values in rating column
	- convert date added to be in a standardized and usable format for arithmetic.
	- Add 'grace_period' column to determine how long a show/movie was released before being added to the Netflix catalog.
