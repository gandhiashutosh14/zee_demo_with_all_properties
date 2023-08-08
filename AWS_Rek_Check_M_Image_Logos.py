import torch
# from memory_profiler import profile
# import gc
# import matplotlib.pyplot as plt
from PIL import Image

# @profile()

classes = ['ACKO', 'Adidas', 'Amazon', 'Amul', 'Aramco', 'BCCI', 'Booking.com', 'Byjus', 'CRED', 'Ceat', 'Chennai Super kings', 'Deccan Chargers', 'Delhi Capitals'
    , 'Domino-s'
    , 'Dream11'
    , 'EBIX Cash'
    , 'Emirates'
    , 'Fbb'
    , 'Go Daddy'
    , 'Gujarat Titans'
    , 'Gujarat lions'
    , 'Gulf'
    , 'Hotstar'
    , 'IPL'
    , 'JK lakshmi cement'
    , 'Jio'
    , 'Kochi Tuskers'
    , 'Kolkata Knigth Riders'
    , 'Lucknow Super Giants'
    , 'MPL'
    , 'MRF'
    , 'Mountain Dew'
    , 'Mumbai Indians'
    , 'Myntra'
    , 'Oppo'
    , 'Paytm'
    , 'Pepsi'
    , 'Postpe'
    , 'Pune Warriors'
    , 'Punjab Kings'
    , 'Rajasthan Royals'
    , 'Rising Pune Supergiants'
    , 'Royal Challengers Bangalore'
    , 'Rupay'
    , 'Slice IPL'
    , 'Star Sports'
    , 'Sunrisers Hyderabad'
    , 'Swiggy'
    , 'TATA Safari'
    , 'TATA'
    , 'TVS Eurogrip'
    , 'Unacademy'
    , 'Unicef'
    , 'Upstox'
    , 'Vivo'
    , 'safari']
def fun():
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='./AWS_Rek_Use_Monuments_Logos/logo_best.pt')
    # gc.collect()
    img = './logoss/MicrosoftTeams-image.png'
    image = Image.open(img)
    # gc.collect()
    # print(type(model))
    dict = {}
    results = model(image)
    for nested_result_list in results.xywhn:
        class_dict = {}
        for result_tensor in nested_result_list:
            class_index = int(result_tensor[-1])
            class_probability = float(result_tensor[-2])
            print('________')
            class_dict[classes[class_index]] = class_probability
            # dicMicrosoftTeams-imaget.append(class_dict)
    print(class_dict)



if __name__ == '__main__':
    fun()