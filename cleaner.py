import json
from datetime import datetime
from pytz import timezone

def delete_format_waste_content():
    month_counter = 0
    month = None
    current_month = None

    with open('message.json') as file:
        data = json.load(file)
        print("Loaded json data as dictionary")
        messages = data['messages']
        print("Cleaning content...")
        for message in messages[:]:
            if message['type'] == "Generic":
                try:
                    test = message['photos']
                    messages.remove(message)
                    continue
                except Exception:
                    pass
                try:
                    test = message['sticker']
                    messages.remove(message)
                    continue
                except Exception:
                    pass
                try:
                    test = message['gifs']
                    messages.remove(message)
                    continue
                except Exception:
                    pass
                try:
                    test = message['audio_files']
                    messages.remove(message)
                    continue
                except Exception:
                    pass
                try:
                    test = message['videos']
                    messages.remove(message)
                    continue
                except Exception:
                    pass
                try:
                    test = message['files']
                    messages.remove(message)
                    continue
                except Exception:
                    pass

                del message['type']

                date_obj = convert_time(message['timestamp_ms']/1000)

                message['timestamp_ms'] = date_obj.strftime("%d %b %Y %I:%M %p")

                current_month = date_obj.month
                if current_month == month:
                    month_counter += 1
                else:
                    month = current_month
                    month_counter = 0

                if month_counter >= 14:
                    try:
                        messages.remove(message)
                    except Exception:
                        pass


            else:
                messages.remove(message)

        out = open('message-refined.json','w')
        out.write(json.dumps(messages,sort_keys=True,indent=4,separators=(',',':')))
        print("Content cleaned!!!\n\n")
        return messages[::-1]

def convert_time(time):
    eastern = timezone('Cuba')
    return eastern.localize(datetime.utcfromtimestamp(time))

