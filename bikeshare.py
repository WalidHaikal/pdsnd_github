# -*- coding: utf-8 -*-

import time
import pandas as pd
import numpy as np

months = ['january', 'february', 'march', 'april', 'may', 'june']

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input ('Please, Enter any city from this list chicago, new york city, washington: ').lower ()
        if city in CITY_DATA:
            break
        else:
            print ('Invalid input, Because the name of city is not correct, try again')
                        
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input ('Please, Enter any month from january, february, march, april, may, june, or all: ').lower ()
        if month in ['january', 'february','march', 'april', 'may', 'june', 'all']:
            break
        else:
            print ('Invalid input, Because the name of month is not correct')


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input ('Please, Enter the name of day or type all to display all days: ').lower ()
        if day in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']:
            break
        else:
            print ('Invalid input, Because the name of day is not right')    


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv (CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime (df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name ()
    df ['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        
        month = months.index(month) +1
    
        # filter by month to create the new dataframe
        df = df [df ['month'] == month ]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df [df ['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = months [df['month'].mode()[0] - 1 ].title()
    print ('The most common month is: ', common_month, '\n')

    # display the most common day of week
    common_day = df ['day_of_week'].mode()[0]
    print ('the most common day is: ', common_day, '\n')

    # display the most common start hour
    common_s_hour = df ['hour'].mode () [0]
    print ('the most common start hour is: ', common_s_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df ['Start Station'].mode () [0]
    print ('the most commonly used start station is: ', start_station, '\n')

    # display most commonly used end station
    end_station = df ['End Station'].mode () [0]
    print ('the most commonly used end station is: ',end_station , '\n')

    # display most frequent combination of start station and end station trip
    df ['combination'] = df ['Start Station'] + '-' + df ['End Station']
    compination = df ['combination'].mode () [0]
    print ('the most frequent combination of start station and end station trip is: ', compination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df ['Trip Duration'].sum ()
    print ('The total travel time is: ',total_time/3600, 'hours',  '\n')

    # display mean travel time
    mean_time = df ['Trip Duration'].mean ()
    print ('The mean travel time is: ', mean_time/3600, 'hours')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    if city != 'washington':
      user_type = df['User Type'].value_counts()
      print ('Counts of user types is: ', user_type)

    # Display counts of gender
    if 'Gender' in df.columns:
        print ('Counts of gender is: ', df['Gender'].value_counts ())
    else:
        print ('May be not gender in this city you choose')

    # Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        print ('Earliest birth year is: ', df ['Birth_Year'].min())
        print ('Most recent birth year is: ', df ['Birth_Year'].max())
        print ('Most common year of birth is: ', df ['Birth_Year'].mode()[0])
    else:
        print ('No birth year here')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def raw_data (df):
    x = 0
    answer = input ('\nIf you would like to see some raws data, Try to enter yes or press no to cancel that.\n').lower()
    pd.set_option ('display.max_columns', None)
    while True:
        if answer == 'no':
            break
        print(df[x:x+5])
        answer = input ('\nIf you would like to see next 5 raws data, enter yes or no.\n').lower()
        x = x+5
        
            
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data (df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()