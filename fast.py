from deepface import DeepFace
from textblob import TextBlob

condition = input("Enter 'I' for image to emotion  and  any key for text to emotion : ")

if condition != 'I' :
    sentence = input("Enter your sentence : ")

    positive_feedbacks = []
    negative_feedbacks = []
    neutral_feedbacks = []


    feedback_polarity = TextBlob(sentence).sentiment.polarity
    if feedback_polarity>0.05:
        positive_feedbacks.append(sentence)
    elif feedback_polarity<-0.05:
        negative_feedbacks.append(sentence)
    else :
        neutral_feedbacks.append(sentence)
    
    if len(positive_feedbacks)==1 :
        print('Positive')
    elif len(negative_feedbacks)==1 :
        print('Negative')
    else :
        print('Neutral')
        
        
else :
    #model =DeepFace.build_model(model_name="DeepFace")
    # face_analysis = DeepFace.verify(img1_path=r"E:\hack\th.jpeg",img2_path=r"E:\hack\th.jpeg",model_name="DeepFace")
    face_analysis = DeepFace.analyze("D:\Arya Hackathon\th.jpeg")
    
    print(face_analysis)
    print(face_analysis[0]["emotion"])
    print(face_analysis[0]["dominant_emotion"])