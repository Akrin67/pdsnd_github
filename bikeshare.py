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
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input('Please select the city you want to explore: Chicago, New York City or Washington.\n').lower()
        if city not in CITY_DATA:
            print('This city is not part of the data set, please choose Chicago, New York City or Washington.\n')
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)

    months = ['all','january','february','march','april','may','june']

    while True:
        month = input('Please select the month you want to explore: January, February, March, April, May, June or all.\n').lower()
        if month not in months:
            print('This month is not part of the data set, please choose January, February, March, April, May, June or all.\n')
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']

    while True:
        day = input('Please select the month you want to explore: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all.\n').lower()
        if day not in days:
            print('This day is not part of the data set, please choose Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all.\n')
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
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable

    if month != 'all':
        # use the index of the months list to get the corresponding int

        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe

        df = df[df['month'] == month]

    # filter by day of week if applicable

    if day != 'all':
        # filter by day of week to create the new dataframe

        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    c_month = df['month'].mode()[0]
    print('The most common month is: ' + months[c_month].title())

    # TO DO: display the most common day of week

    c_day = df['day_of_week'].mode()[0]
    print('The most common day is: ' + c_day)


    # TO DO: display the most common start hour

    c_start_hour = df['hour'].mode()[0]
    print('The most common start hour is: ' + str(c_start_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    c_start_station = df['Start Station'].mode()[0]
    print('The most common start station is: ' + c_start_station)

    # TO DO: display most commonly used end station

    c_end_station = df['End Station'].mode()[0]
    print('The most common end station is: ' + c_end_station)

    # TO DO: display most frequent combination of start station and end station trip

    start_end = (df['Start Station'] + ' / ' + df['End Station']).mode()[0]
    print('The most frequent combination of start station and end station is: ' + start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    sum_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: ' + str(sum_travel_time) + ' seconds')

    # TO DO: display mean travel time

    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is: ' + str(mean_travel_time) + ' seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    count_types = df['User Type'].value_counts()
    print('The count of user types is: \n' + str(count_types))

    # TO DO: Display counts of gender

    if 'Gender' in df:
        count_gender = df['Gender'].value_counts()
        print('\nThe count of gender is: \n' + str(count_gender))
    else:
        print('\nThere is no gender information in the data set of this city.')

    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df:
        min_birth = df['Birth Year'].min()
        print('\nThe earliest year of birth is: ' + str(min_birth))
        max_birth = df['Birth Year'].max()
        print('The most recent year of birth is: ' + str(max_birth))
        c_birth = df['Birth Year'].mode()[0]
        print('The most common year of birth is: ' + str(c_birth))
    else:
        print('\nThere is no year of birth information in the data set of this city.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_raw_data(df):

    data_count = 0
    answers = ['yes','no']
    answer = ''

    while answer not in answers:
        answer = input('Do you want to see some of the raw data (5 data records)? Answer with yes or no.\n').lower()
        if answer in answers:
            if answer == 'yes':
                data = df.iloc[data_count:data_count + 10]
                print(data)
            break
        elif answer not in answers:
            print('Please enter yes or no')
            continue
        else:
            break

    while answer == 'yes':
        answer = input('Do you want to see 10 extra data records? Answer with yes or no.\n').lower()
        if answer not in answers:
            print('Please anwer with yes or no\n')
            answer = 'yes'
            continue
        elif answer in answers:
            if answer == 'yes':
                data_count += 10
                data = df.iloc[data_count:data_count + 10]
                print(data)

        else:
             break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)



        trip_duration_stats(df)
        time_stats(df)
        station_stats(df)
        user_stats(df)
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
