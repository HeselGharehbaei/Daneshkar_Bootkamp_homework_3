from datetime import datetime
import jdatetime


format_of_birthday_date_and_time = '%Y/%m/%d %H:%M:%S'


users_birthdate_and_time_in_the_Gregorian_calendar_format_as_a_string = input(
"Enter your birthday date and time in form Gregorian calendar and by 'yyyy/mm/dd hh:mm:ss' format: "
)
 

users_birthdate_and_time_in_the_Gregorian_calendar_format = datetime.strptime(
users_birthdate_and_time_in_the_Gregorian_calendar_format_as_a_string, format_of_birthday_date_and_time)


current_datetime = datetime.now()


total_number_of_seconds_spent_during_the_lifetime_of_user = (
current_datetime - users_birthdate_and_time_in_the_Gregorian_calendar_format).total_seconds()


print(f"you spent {total_number_of_seconds_spent_during_the_lifetime_of_user} seconds during your lifetime.")


next_user_birthday_date_and_time_in_the_Gregorian_calendar_format =(
users_birthdate_and_time_in_the_Gregorian_calendar_format.
replace(year= current_datetime.year)
) 


if next_user_birthday_date_and_time_in_the_Gregorian_calendar_format < (
current_datetime    
):
    next_user_birthday_date_and_time_in_the_Gregorian_calendar_format =(
users_birthdate_and_time_in_the_Gregorian_calendar_format.
replace(year= current_datetime.year + 1)
) 


datetime_to_next_birthday = (
next_user_birthday_date_and_time_in_the_Gregorian_calendar_format - 
current_datetime
)

days_to_next_birthday = (
datetime_to_next_birthday.days   
)

minutes_to_next_birthday = int(
datetime_to_next_birthday.seconds
) / 60


print(f"Congratulations, after{days_to_next_birthday}days and {minutes_to_next_birthday} minutes be your birthday celebration")


users_birthdate_in_the_solar_hijri_format = jdatetime.datetime.fromgregorian(
year = users_birthdate_and_time_in_the_Gregorian_calendar_format. year,
month = users_birthdate_and_time_in_the_Gregorian_calendar_format. month,
day = users_birthdate_and_time_in_the_Gregorian_calendar_format. day
)
