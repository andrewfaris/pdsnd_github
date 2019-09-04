import time
import pandas as pd
import numpy as np

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
        cities = ('chicago', 'new york city', 'washington')
        city = input('Enter the city you would like to explore (chicago, new york city, washington): ')
        city = city.lower()
        if city not in cities:
            print('Please enter a valid city name.')
            continue
        else:
             break


    # get user input for month (all, january, february, march, april , june)
    while True:
        months = ('january', 'february', 'march', 'april', 'may', 'june', 'all')
        month = input('Enter the month you would like to explore (january, february, march, april, may, june) or type All to explore all months: ')
        month = month.lower()
        if month not in months:
            print('Please enter a valid city name.')
            continue
        else:
             break


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        dows = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all')
        day = input('Enter the day of the week you would like to explore or type All to explore all days of the week: ')
        day = day.lower()
        if day not in dows:
            print('Please enter a valid day of the week.')
            continue
        else:
             break


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('Most common month: ', df['month'].mode()[0])


    # display the most common day of week
    print('Most common day of week: ', df['day_of_week'].mode()[0])


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('Most common hour: ', df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most common start station: ', df['Start Station'].mode()[0])


    # display most commonly used end station
    print('Most common end station: ', df['End Station'].mode()[0])


    # display most frequent combination of start station and end station trip
    df['start and stop combo'] = 'Start: ' + df['Start Station']+', End: ' + df['End Station']
    print('Most frequent combination of start station and end station: ', df['start and stop combo'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total Travel Time: ', df['Trip Duration'].sum())


    # display mean travel time
    print('Mean Travel Time: ', df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts of user types: ', df['User Type'].value_counts())


    if 'Gender' in df.columns:
        # Display counts of gender
        print('Counts of gender: ', df['Gender'].value_counts())
    else:
        print('No gender data available.')

    if 'Birth Year' in df.columns:
        # Display earliest, most recent, and most common year of birth
        print('Earliest Birth Year: ', df['Birth Year'].min())
        print('Most Recent Birth Year: ', df['Birth Year'].max())
        print('Most Common Birth Year: ', df['Birth Year'].mode()[0])
    else:
        print('No birth year data available.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter exactly yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
