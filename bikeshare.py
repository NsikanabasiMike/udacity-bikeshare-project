import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }
MONTHS = ('All','January', 'February', 'March', 'April', 'May', 'June')
DAYS_OF_WEEK = ('All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    cities = 'Chicago', 'New York City', 'Washington'
    print('Available cities: ',cities)
    while True:
        city = input('Enter city name: ').title()
    
        if city in cities:
            break
    print('List of available months: ',MONTHS)

    while True:
        month = input('Enter month name: ').title()
        if month in MONTHS:
            break
    print('Available days of the week:',DAYS_OF_WEEK)
    while True:
        day = input('Enter day of the week: ').title()
        if day in DAYS_OF_WEEK:
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month.apply(lambda x: MONTHS[x])
    df['Day'] = df['Start Time'].dt.day_name()
    df['Hour'] = df['Start Time'].dt.hour
    df['Start_and_End_Stations'] = df['Start Station'] +' and '+ df['End Station']
    if day != 'All':
        df = df[df['Day'] == day]

    if month != 'All':
        df = df[df['Month'] == month]

    return df
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print('favourite month of travel: \n', df['Month'].value_counts().idxmax())
    print('favourite day of travel: \n', df['Day'].value_counts().idxmax())

    print('most common start hour: \n', df['Hour'].value_counts().idxmax())

    print("\nThis took %s second." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print('most commonly used start station: \n', df['Start Station'].value_counts().idxmax())        

    print('most commonly used end station: \n', df['End Station'].value_counts().idxmax())

    print('most frequent combination of start station and end station trip:\n', df['Start_and_End_Stations'].value_counts().idxmax())

    print("\nThis took %s second." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print('total travel time is approximately %d days: \n'% int(df['Trip Duration'].sum()/ 24))
    print()
    print('mean travel time is approximately %d days: \n'% int(df['Trip Duration'].mean()/ 24))
    print()
    print("\nThis took %s second." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    if ('Gender') and ('Birth Year') in df:
        print('\nCalculating User Stats...\n')
        start_time = time.time()
        
        print('counts of user types: ', df['User Type'].count())
        print()
    # ratio of User Type
        print('ratio of unique user type:\n', df.groupby(df['User Type'])['User Type'].count())
        print()
    
        print('counts of gender: ',df['Gender'].count())
    # ratio of Gender
        print('Ratio of Male to Female:\n' , df.groupby(df['Gender'])['Gender'].count())
    # earliest birth year
        print('earliest birthday:', int(df['Birth Year'].min()))
    
    # most recent birth year
        print('most recent birth year :\n', int(df['Birth Year'].max()))
    
    # most common birth year
        print('most common birth year: \n', int(df['Birth Year'].value_counts().idxmax()))
    
        print("\nThis took %s second." % (time.time() - start_time))
        print('-'*40)
    else:
        print('sorry, Gender and Birth Year are not in dataframe')
        
def raw_data(df):
    
    """
    Display 5 lines of raw data if a user requests.
    Display next 5 lines of raw data if user's input is 'yes'. If 'no', break.
    """
    counter = 0 
    while True:
        
        response = input('\nWould you like to see 5 lines of raw data? Enter Yes or No:\n')
        if response.title() == 'Yes':
            print('five lines of raw data:\n', df.iloc[counter:counter+5, :])
            counter += 5     
        else:
            break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

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