from datetime import timedelta

def runtime_format(calculation_time: timedelta, print_precision: int = 3) -> str:
    #This function formats the time result to units that make sense - seconds if time > 1000 ms, otherwise miliseconds.

    calculation_time_miliseconds = calculation_time.microseconds/1000 + calculation_time.seconds*1000
    formatted_time_result = f"{(calculation_time.microseconds/1000 + calculation_time.seconds*1000):.{print_precision}f} miliseconds."

    if (calculation_time_miliseconds >= 1000): #display time in seconds
        formatted_time_result = f"{(calculation_time_miliseconds/1000):.{print_precision}f} seconds."

    return formatted_time_result