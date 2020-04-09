#!/usr/bin/env python
# coding: utf-8
#Import necessary packages
import time
import pandas as pd
import numpy as np

#Set download URLs data
chi_link = "https://raw.githubusercontent.com/igorstojanovic91/udacity-bikeshare-project/master/chicago.csv"
nyc_link = "https://raw.githubusercontent.com/igorstojanovic91/udacity-bikeshare-project/master/new_york_city.csv"
was_data = "https://raw.githubusercontent.com/igorstojanovic91/udacity-bikeshare-project/master/washington.csv"

city_data = {'chicago': chi_link,
             'new york city': nyc_link,
             'washington': was_link}

cities = ["chicago", "washington", "new york city"]
months = ["january", "february", "march", "april", "may", "june"]
wdays = ["monday", "tuesday", "wednesday", "thursday", "firady", "saturday", "sunday"]

def get_filters():
    print("-" * 40)
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Do you want to explore Chicago, New York City or Washington \n").lower()
        if city in cities:
            print("We are going to explore {}.".format(city))
            break
        else:
            print("Invalid input, {} is not in the city list, try again.".format(city))

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month from January to June do you want to explore? \n If all months type All \n").lower()
        if month in months or month == "all":
            print("We are going to explore {}.".format(month))
            break
        else:
            print("Invalid input, {} is not in the month list, try again.".format(month))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        wday = input("Which week day do you want to explore? \n If all months type All \n").lower()
        if wday in wdays or wday == "all":
            print("We are going to explore {}.".format(wday))
            break
        else:
            print("Invalid input, {} is not in the week day list, try again.".format(month))

    print('-'*40)
    return city, month, wday

def load_data(city, month, wday):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print("Downloading data for {}".format(city))
    df = pd.read_csv(city_data[city], index_col=0)
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    df["Month"] = df["Start Time"].dt.month_name()
    df["Weekday"] = df["Start Time"].dt.day_name()
    df["Hour"] = df["Start Time"].dt.hour

    if month != "all":
        df = df[df['Month'] == month.title()]

    if wday != "all":
        df = df[df['Weekday'] == wday.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    com_month = df["Month"].mode()[0]
    print("Month with most rides is {}.".format(com_month))

    # TO DO: display the most common day of week
    com_wday = df["Weekday"].mode()[0]
    print("Weekday with most rides is {}.".format(com_wday))

    # TO DO: display the most common start hour
    com_hour = df["Hour"].mode()[0]
    print("Hour with most rides is {}.".format(com_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mc_start_station = df["Start Station"].mode()[0]
    print("Start station with most rides is {}.".format(mc_start_station))

    # TO DO: display most commonly used end station
    mc_end_station = df["End Station"].mode()[0]
    print("End station with most rides is {}.".format(mc_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    mc_combinatiton = (df["Start Station"] + " - " + df["End Station"]).mode()[0]
    print("Trip with most rides is {}.".format(mc_combinatiton))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_tavel_time = df["Trip Duration"].sum()/60/60
    print("Total travel time is {} hours.".format(total_tavel_time))

    # TO DO: display mean travel time
    mean_tavel_time = df["Trip Duration"].mean()/60
    print("Mean travel time is {} minutes.".format(mean_tavel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    ut_count = df.groupby("User Type")["Start Time"].count()
    print(ut_count)
    print("\n")

    # TO DO: Display counts of gender
    try:
      gender_count = df['Gender'].value_counts()
      print(gender_count)
    except KeyError:
      print("Gender stats: No data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      min_year = df["Birth Year"].min()
      print("\nEarliest birth year is {}".format(min_year))
    except KeyError:
      print("Min year: No data available for this month.")

    try:
      max_year = df["Birth Year"].max()
      print("\nLatest birth year is {}".format(max_year))
    except KeyError:
      print("Max year: No data available for this month.")

    try:
      mc_year = df["Birth Year"].mode()[0]
      print("\nMost common birth year is {}".format(mc_year))
    except KeyError:
      print("Most common year: No data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """
    Asks user if they want to see 5 lines of raw data.
    Returns the 5 lines of raw data if user inputs `yes`. Iterate until user response with a `no`
    """

    data = 0

    while True:
        answer = input("Would you like to see 5 lines of raw data? Enter yes or no: ")
        if answer.lower() == "yes":
            print(df.iloc[data:data+5,:])
            data += 5
        else:
            break

def main():
    while True:
        city, month, wday = get_filters()
        df = load_data(city, month, wday)

        print(city, month, wday)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
