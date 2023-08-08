# import torch
# # from memory_profiler import profile
# # import gc
# # import matplotlib.pyplot as plt
# from PIL import Image
# import cv2
# import torch.hub
# import time

# # @profile()

# # You might need to define the 'classes' list based on the classes used in your model
# classes = ['1000 Pillar Temple Moodabidri', 'Aaliyar Dam Park', 'Academy of Fine Arts Kolkata', 'Achalgarh Fort', 'Achut Bibis Mosque', 'Adalaj Stepwell', 'Adam Fountain', 'Adhanur temple', 'Adhi Ratneswarar Temple', 'Adina Mosque', 'Adinath Temple', 'Adiyogi Shiva statue', 'Afghan Church', 'Aga Khan Palace', 'Agra Fort', 'Agrasen Ki Baoli', 'Ahinsa Sthal', 'Aina Mahal', 'Airavateswarar Temple', 'Ajanta Caves', 'Akal Takht Amritsar', 'Akbar Tomb', 'Akshardham temple', 'Alamgir Masjid', 'Albert Hall Museum', 'Alipore Zoological Gardens', 'All Saints, Cathedral', 'Allahabad Fort', 'Allahabad Public Library', 'Alwar Qila', 'Amarnath Temple', 'Ambalappuzha Sri Krishna Temple', 'Ambedkar Park', 'Amber fort', 'Amer Fort', 'Amruteshwar Temple', 'Ananta Basudeba Temple', 'Ananta Vasudev Temple', 'Ananthapura Lake Temple', 'Anna Memorial', 'Antillia', 'Armenian Church', 'Arthanareeswarar Temple', 'Arulmigu Arunachaleswarar Temple', 'Ashtalakshmi Temple', 'Asirgarh Fort', 'Athirappilly Falls', 'Bada Bagh', 'Bada Gumbad', 'Bada Imambara', 'Badami Cave Temples', 'Badrinath Temple', 'Balaji Temple Ketkawale', 'Bandel Church', 'Bandra Fort', 'Bandra Worli Sea Link', 'Baneshwar Mandir', 'Bangalore Fort', 'Bangalore Palace', 'Bangalore Town Hall', 'Bankey Bihari Temple', 'Bara Kaman', 'Baramotichi Vihir', 'Baroda Art Museum', 'Baroli Temple Complex', 'Basilica of Bom Jesus', 'Basilica of Our Lady of Dolours', 'Basilica of Our Lady of Graces', 'Basilica of Our Lady of Ransom, Vallarpadam', 'Basilica of Our Lady of Snows, Pallippuram', 'Basilica of Our Lady of the Assumption, Secunderabad', 'Bateshwar Group of Temples', 'Begumpuri Masjid', 'Bekal Fort', 'Belur Math', 'Bhadra Fort', 'Bhairavakona', 'Bhakti Dham Mangarh', 'Bhandasar Jain Temple', 'Bharathi Park', 'Bhavanisagar Dam', 'Bhimas-Ratha', 'Bhimakali Temple', 'Bhimashankar', 'Bhimeshvara Temple Nilagunda', 'Bhoganandishwara Temple', 'Bhojeshwar Temple', 'Bhor Rajwada', 'Bhoramdev Temple', 'Bhuleshwar Temple', 'Bhutanatha group of temples', 'Bidar Fort', 'Biodiversity Park', 'Bir Singh Deo Palace', 'Bir-kangra', 'Birla House Gandhi Smriti', 'Birla Mandir, Hyderabad', 'Birla Mandir, Jaipur', 'Birla Mandir, Kolkata', 'Birla Planetarium', 'Bisaldeo Temple', 'Bnaganga Tank', 'Bogatha Waterfalls', 'Bojjannakonda', 'Bolgatty Palace', 'Bombay Stock Exchane', 'Brahma Temple, Pushkar', 'Brahmesvara Temple', 'Brahmeswara Temple', 'Brihadeeswara Temple', 'Buddha International Circuit', 'Buddha Park of Ravangla', 'Buddha Smriti Park', 'Bull Temple', 'Central Bureau of Investigation', 'Char Minar', 'Chhatrapati Shivaji Terminus', 'City Palace', 'Dagdusheth Halwai Ganpati Temple', 'Dakshineshwar Kali Temple', 'Dakshineswar Kali Temple', 'Dansborg Fort', 'Dargah Aala Hazrat', 'Daria Daulat Bagh', 'Das Mahavidya temple', 'Dashashwamedh Ghat', 'Dassam Falls', 'Dastgeer Sahib', 'Daulatabad, Maharashtra', 'David Sassoon Library', 'Deekshabhoomi', 'Delhi Gate', 'Delhi Town Hall', 'Descent of the Ganges', 'Devanahalli Fort', 'Devi Jagdambi Temple Khajuraho', 'Dhamekh Stupa', 'Dharmaraja Ratha', 'Dharmaraya Swamy Temple', 'Dhom Dam', 'Dhrasanvel Temple, Magderu', 'Dhuandhar Falls', 'Diu Fort', 'Do Drul Chorten', 'Dr MGR Memorial', 'Dras War', 'Dubdi Gompa', 'Dudhsagar Falls', 'DulhaDeo Temple Khajuraho', 'Durga Mandir in Bhelupur', 'Durga Temple, Aihole', 'Dwarkadhish Temple', 'Elephanta Caves', 'Ellora caves', 'Enchey Monastery', 'Eros Cinema', 'Erumbeeswarar Temple', 'Ethipothala Falls', 'Ettumanoor Temple', 'Fatehpur sikri', 'Feroz shah kotla', 'Fort Unchagaon', 'Gateway of India', 'Gobal Vipassana Pagoda', 'Gol Gumbaz', 'Golconda fort', 'Golden Temple', 'Gurudwara Bangla Sahib', 'Gurudwara Sahib, Pushkar', 'Haji ali dargha', 'Hawa Mahal', 'High Court of Karnatka', 'Howrah Bridge', 'Humayu Tomb', 'India gate', 'Jal Mahal', 'Jallianwala Bagh', 'Jama Mashjid', 'Jamia Masjid or Begumpet Mosque', 'Jantar Mantar, Jaipur', 'Jantar Mantar', 'Khajuraho Temple', 'Konark Sun Temple', 'Laxmi Narayan Mandir', 'Lotus Temple', 'Mecca Masjid Hyderabad', 'Mehrangarh Fort', 'Mysore Palace', 'Parliament of India', 'Qutub Minar', 'Rashtrapati Bhavan', 'Red Fort', 'Sajjangarh Monsoon Palace', 'Samudra Narayan Temple', 'Sanchi Stupa', 'Shiv Niwas Palace', 'Shore Temple', 'Shree Banashankari Amma Temple', 'Sidhi Vinayak', 'Supreme Court', 'Taj Mahal', 'The Imperial Tower', 'The Taj Mahal palace hotels', 'Umaid Bhawan Palace', 'Vasai Fort Or Bassien Fort', 'Victoria Memorial', 'Vidhana Soudha']

# def fun():
#     model = torch.hub.load('ultralytics/yolov5', 'custom', path='./AWS_Rek_Use_Monuments_Logos/monument_1.pt')
#     video_path = 'test.mp4'
#     cap = cv2.VideoCapture(video_path)

#     frame_rate = cap.get(cv2.CAP_PROP_FPS)
#     frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

#     second_results = []

#     for second in range(int(frame_count / frame_rate)):
#         start_frame = int(second * frame_rate)
#         end_frame = int((second + 1) * frame_rate) - 1

#         total_confidence = 0
#         monument_names = set()

#         for frame_idx in range(start_frame, end_frame + 1):
#             ret, frame = cap.read()
#             if not ret:
#                 break

#             # Convert the frame to PIL Image
#             image = Image.fromarray(frame)

#             # Perform detection on the frame
#             results = model(image)

#             for nested_result_list in results.xywhn:
#                 for result_tensor in nested_result_list:
#                     class_index = int(result_tensor[-1])
#                     class_probability = float(result_tensor[-2])
#                     monument_name = classes[class_index]
                    
#                     total_confidence += class_probability
#                     monument_names.add(monument_name)

#         avg_confidence = total_confidence / frame_rate
#         timestamp = time.strftime("%H:%M:%S", time.gmtime(second))
#         monument_names_str = ', '.join(monument_names)

#         second_results.append({
#             'timestamp': timestamp,
#             'monument_names': monument_names_str,
#             'confidence': avg_confidence
#         })
    
#     cap.release()

#     return second_results


# if __name__ == '__main__':
#     second_results = fun()
#     for result in second_results:
#         print(f"Timestamp: {result['timestamp']}, Monuments: {result['monument_names']}, Confidence: {result['confidence']:.4f}")

import torch
# from memory_profiler import profile
# import gc
# import matplotlib.pyplot as plt
from PIL import Image
import cv2
import torch.hub
import time

# @profile()

# You might need to define the 'classes' list based on the classes used in your model
classes = ['1000 Pillar Temple Moodabidri', 'Aaliyar Dam Park', 'Academy of Fine Arts Kolkata', 'Achalgarh Fort', 'Achut Bibis Mosque', 'Adalaj Stepwell', 'Adam Fountain', 'Adhanur temple', 'Adhi Ratneswarar Temple', 'Adina Mosque', 'Adinath Temple', 'Adiyogi Shiva statue', 'Afghan Church', 'Aga Khan Palace', 'Agra Fort', 'Agrasen Ki Baoli', 'Ahinsa Sthal', 'Aina Mahal', 'Airavateswarar Temple', 'Ajanta Caves', 'Akal Takht Amritsar', 'Akbar Tomb', 'Akshardham temple', 'Alamgir Masjid', 'Albert Hall Museum', 'Alipore Zoological Gardens', 'All Saints, Cathedral', 'Allahabad Fort', 'Allahabad Public Library', 'Alwar Qila', 'Amarnath Temple', 'Ambalappuzha Sri Krishna Temple', 'Ambedkar Park', 'Amber fort', 'Amer Fort', 'Amruteshwar Temple', 'Ananta Basudeba Temple', 'Ananta Vasudev Temple', 'Ananthapura Lake Temple', 'Anna Memorial', 'Antillia', 'Armenian Church', 'Arthanareeswarar Temple', 'Arulmigu Arunachaleswarar Temple', 'Ashtalakshmi Temple', 'Asirgarh Fort', 'Athirappilly Falls', 'Bada Bagh', 'Bada Gumbad', 'Bada Imambara', 'Badami Cave Temples', 'Badrinath Temple', 'Balaji Temple Ketkawale', 'Bandel Church', 'Bandra Fort', 'Bandra Worli Sea Link', 'Baneshwar Mandir', 'Bangalore Fort', 'Bangalore Palace', 'Bangalore Town Hall', 'Bankey Bihari Temple', 'Bara Kaman', 'Baramotichi Vihir', 'Baroda Art Museum', 'Baroli Temple Complex', 'Basilica of Bom Jesus', 'Basilica of Our Lady of Dolours', 'Basilica of Our Lady of Graces', 'Basilica of Our Lady of Ransom, Vallarpadam', 'Basilica of Our Lady of Snows, Pallippuram', 'Basilica of Our Lady of the Assumption, Secunderabad', 'Bateshwar Group of Temples', 'Begumpuri Masjid', 'Bekal Fort', 'Belur Math', 'Bhadra Fort', 'Bhairavakona', 'Bhakti Dham Mangarh', 'Bhandasar Jain Temple', 'Bharathi Park', 'Bhavanisagar Dam', 'Bhimas-Ratha', 'Bhimakali Temple', 'Bhimashankar', 'Bhimeshvara Temple Nilagunda', 'Bhoganandishwara Temple', 'Bhojeshwar Temple', 'Bhor Rajwada', 'Bhoramdev Temple', 'Bhuleshwar Temple', 'Bhutanatha group of temples', 'Bidar Fort', 'Biodiversity Park', 'Bir Singh Deo Palace', 'Bir-kangra', 'Birla House Gandhi Smriti', 'Birla Mandir, Hyderabad', 'Birla Mandir, Jaipur', 'Birla Mandir, Kolkata', 'Birla Planetarium', 'Bisaldeo Temple', 'Bnaganga Tank', 'Bogatha Waterfalls', 'Bojjannakonda', 'Bolgatty Palace', 'Bombay Stock Exchane', 'Brahma Temple, Pushkar', 'Brahmesvara Temple', 'Brahmeswara Temple', 'Brihadeeswara Temple', 'Buddha International Circuit', 'Buddha Park of Ravangla', 'Buddha Smriti Park', 'Bull Temple', 'Central Bureau of Investigation', 'Char Minar', 'Chhatrapati Shivaji Terminus', 'City Palace', 'Dagdusheth Halwai Ganpati Temple', 'Dakshineshwar Kali Temple', 'Dakshineswar Kali Temple', 'Dansborg Fort', 'Dargah Aala Hazrat', 'Daria Daulat Bagh', 'Das Mahavidya temple', 'Dashashwamedh Ghat', 'Dassam Falls', 'Dastgeer Sahib', 'Daulatabad, Maharashtra', 'David Sassoon Library', 'Deekshabhoomi', 'Delhi Gate', 'Delhi Town Hall', 'Descent of the Ganges', 'Devanahalli Fort', 'Devi Jagdambi Temple Khajuraho', 'Dhamekh Stupa', 'Dharmaraja Ratha', 'Dharmaraya Swamy Temple', 'Dhom Dam', 'Dhrasanvel Temple, Magderu', 'Dhuandhar Falls', 'Diu Fort', 'Do Drul Chorten', 'Dr MGR Memorial', 'Dras War', 'Dubdi Gompa', 'Dudhsagar Falls', 'DulhaDeo Temple Khajuraho', 'Durga Mandir in Bhelupur', 'Durga Temple, Aihole', 'Dwarkadhish Temple', 'Elephanta Caves', 'Ellora caves', 'Enchey Monastery', 'Eros Cinema', 'Erumbeeswarar Temple', 'Ethipothala Falls', 'Ettumanoor Temple', 'Fatehpur sikri', 'Feroz shah kotla', 'Fort Unchagaon', 'Gateway of India', 'Gobal Vipassana Pagoda', 'Gol Gumbaz', 'Golconda fort', 'Golden Temple', 'Gurudwara Bangla Sahib', 'Gurudwara Sahib, Pushkar', 'Haji ali dargha', 'Hawa Mahal', 'High Court of Karnatka', 'Howrah Bridge', 'Humayu Tomb', 'India gate', 'Jal Mahal', 'Jallianwala Bagh', 'Jama Mashjid', 'Jamia Masjid or Begumpet Mosque', 'Jantar Mantar, Jaipur', 'Jantar Mantar', 'Khajuraho Temple', 'Konark Sun Temple', 'Laxmi Narayan Mandir', 'Lotus Temple', 'Mecca Masjid Hyderabad', 'Mehrangarh Fort', 'Mysore Palace', 'Parliament of India', 'Qutub Minar', 'Rashtrapati Bhavan', 'Red Fort', 'Sajjangarh Monsoon Palace', 'Samudra Narayan Temple', 'Sanchi Stupa', 'Shiv Niwas Palace', 'Shore Temple', 'Shree Banashankari Amma Temple', 'Sidhi Vinayak', 'Supreme Court', 'Taj Mahal', 'The Imperial Tower', 'The Taj Mahal palace hotels', 'Umaid Bhawan Palace', 'Vasai Fort Or Bassien Fort', 'Victoria Memorial', 'Vidhana Soudha']

def fun():
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='./AWS_Rek_Use_Monuments_Logos/monument_1.pt')
    video_path = 'test.mp4'
    cap = cv2.VideoCapture(video_path)

    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    second_results = []

    for second in range(int(frame_count / frame_rate)):
        start_frame = int(second * frame_rate)
        end_frame = int((second + 1) * frame_rate) - 1

        total_confidence = 0
        monument_names = set()

        for frame_idx in range(start_frame, end_frame + 1):
            ret, frame = cap.read()
            if not ret:
                break

            # Convert the frame to PIL Image
            image = Image.fromarray(frame)

            # Perform detection on the frame
            results = model(image)

            for nested_result_list in results.xywhn:
                for result_tensor in nested_result_list:
                    class_index = int(result_tensor[-1])
                    class_probability = float(result_tensor[-2])
                    monument_name = classes[class_index]
                    
                    total_confidence += class_probability
                    monument_names.add(monument_name)

        avg_confidence = total_confidence / frame_rate
        timestamp = time.strftime("%H:%M:%S", time.gmtime(second))
        monument_names_str = ', '.join(monument_names)

        if monument_names:
            second_results.append({
                'timestamp': timestamp,
                'monument_names': monument_names_str,
                'confidence': avg_confidence
            })
    
    cap.release()

    return second_results


if __name__ == '__main__':
    second_results = fun()
    for result in second_results:
        print(f"Timestamp: {result['timestamp']}, Monuments: {result['monument_names']}, Confidence: {result['confidence']:.4f}")
