import requests
import time
import winsound  # Used to play alert sounds on Windows

def get_available_appointments(date):
    """
    Pass in a valid date string, e.g. '2025-04-15'.
    Returns the appointment information for that date.
    """
    url = "https://www48.muenchen.de/buergeransicht/api/backend/available-appointments"
    
    # Request parameters: make sure to replace 'date' with a valid date.
    params = {
        "date": date,
        "officeId": "10187259",
        "serviceId": "10339027",
        "serviceCount": "1"
    }
    
    # Request headers copied from the curl command to mimic a browser.
    headers = {
        "Accept": "*/*",
        "Accept-Language": "de,zh-CN;q=0.9,zh;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Origin": "https://stadt.muenchen.de",
        "Referer": "https://stadt.muenchen.de/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"'
    }
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()  # Raise an exception if the status code is not 200
        return response.json()  # Return the response in JSON format
    except Exception as e:
        print(f"Request exception: {e}")
        return None

def play_alert():
    """
    Play a simple alert sound (1000Hz for 500ms)
    """
    winsound.Beep(1000, 500)

def check_appointments_for_date(date):
    """
    Checks the appointment availability for the specified date.
    If the returned data contains appointment info, trigger an alert.
    """
    print(f"Checking appointment availability for {date}...")
    data = get_available_appointments(date)
    
    print("Returned data:", data)  # Print the data for debugging purposes.
    
    # Process the returned data structure. If the date is invalid or no appointment exists,
    # the API might return an error message.
    if isinstance(data, dict):
        # If the dictionary contains error information (e.g. errorCode, errorMessage), check it.
        if "errorCode" in data:
            print(f"Error code: {data['errorCode']} -- {data.get('errorMessage', '')}")
            return False
        else:
            # If there is no error information, assume the data contains appointment details.
            # You can modify this logic based on the actual data structure.
            print("Appointment data detected:", data)
            play_alert()
            return True
    # If the returned data format is unexpected, consider it as no valid appointment.
    print("Unexpected data format or no appointment available")
    return False

def main_loop():
    # Set the date you want to monitor; this can be a fixed date or an iteration over multiple dates.
    # In this example, we use a fixed valid date.
    appointment_date = "2025-04-15"  # Replace with the valid date you want to check.
    
    while True:
        if check_appointments_for_date(appointment_date):
            print("Appointment available! Stopping monitor.")
            break
        else:
            print("No appointment available. Checking again in 10 seconds...\n")
        time.sleep(10)

if __name__ == "__main__":
    main_loop()
