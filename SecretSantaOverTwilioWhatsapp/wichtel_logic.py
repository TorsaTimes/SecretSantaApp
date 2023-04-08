import random
import time
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

nr_list = ['WHATSAPPNUMBER', 'WHATSAPPNUMBER', 'WHATSAPPNUMBER', 'WHATSAPPNUMBER']

name_list = ['NAME', 'NAME', 'NAME', 'NAME']
# final list
final_nr_tuple_list = []
# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
# Your Account SID from twilio.com/console
account_sid = os.getenv('ACCOUNT_SID')
# Your Auth Token from twilio.com/console
auth_token  = os.getenv('AUTH_TOKEN')
from_whatsapp_number = os.getenv('TWILIO_SANDBOX_TESTING_NUMBER')
# timer for loop    


def get_wichtel_tuple_list():

    tuple_list = []
    timeout = time.time() + 5  # 5 minutes from now
    # santa list
    nums = [1, 2, 3, 4]
    # who got which santa from list nums
    nums_sec = [1, 2, 3, 4]

    while 1:
        # select santa 1

        if time.time() > timeout:
            # reset all while timeout
            print("reset all")
            nums = [1, 2, 3, 4]
            nums_sec = [1, 2, 3, 4]
            tuple_list = []
            timeout = time.time() + 5 

        if len(nums_sec) == 0 and len(nums_sec) == 0:
            if len(tuple_list) == 4:
                break
            else: 
                # reset all while tuple list
                print("reset all")
                nums = [1, 2, 3, 4]
                nums_sec = [1, 2, 3, 4]
                tuple_list = []
                timeout = time.time() + 5 

        nums_rIndex = random.randrange(len(nums))
            
        nums_sec_rIndex = random.randrange(len(nums_sec))
        if nums_sec[nums_sec_rIndex] != nums[nums_rIndex]:
            # add tuple to list
            tuple_list.append((nums_sec[nums_sec_rIndex]-1, nums[nums_rIndex]-1))
            print(nums_sec[nums_sec_rIndex], " AND " ,nums[nums_rIndex])

            print("removed numbers: ", nums_sec[nums_sec_rIndex], " and ", nums[nums_rIndex])
            # remove numbers
            nums_sec.remove(nums_sec[nums_sec_rIndex])
            nums.remove(nums[nums_rIndex])
        nr_list
    return tuple_list
    
def set_wichtel_tuple_list(tuple_list):
    
    print(len(nr_list), " ", nr_list[3])
    for tuple in tuple_list:
        print("Diese Nummer: ", tuple[0], " hat die nummer gezogen: ", tuple[1])
        final_nr_tuple_list.append((nr_list[tuple[0]],name_list[tuple[1]]))
    for tuple in final_nr_tuple_list:
        print("Diese Nummer: ", tuple[0], " hat die nummer gezogen: ", tuple[1])


def send_wichtel_msg():

    client = Client(account_sid, auth_token)

    for tuple in final_nr_tuple_list:

        print('die nummer', tuple[0], ' hat ', tuple[1], ' gezogen')

        client.messages.create(body= "\U0001F385" + ' Hohoho du hast ' + tuple[1] + ' gezogen',
                        from_=from_whatsapp_number,
                        to=tuple[0])
