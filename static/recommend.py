import mysql.connector

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'adithya',
    'password': '123',
    'database': 'mydatabase'
}

# Fetch the recommendation data
def fetch_recommendation_data(username):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Fetch the user's age and gender from the users table
    cursor.execute("SELECT age, gender FROM users WHERE username = %s", (username,))
    user_data = cursor.fetchone()
    age, gender = user_data

    # Fetch the user's emotion from the current user table corresponding to the date
    cursor.execute(f"SELECT emotion FROM {username} WHERE date = CURDATE()")
    emotion_row = cursor.fetchone()

    cursor.close()
    conn.close()

    
    if emotion_row:
        emotion = emotion_row[0]
    else:
        emotion = None

    cursor.close()
    conn.close()

    return age, gender, emotion



def generate_recommendation(age, gender, emotion):


    
    valid_ages = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,  
                  26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,  
                  37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47,  
                  48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,  
                  59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70] 

    valid_emotions = ["Happy", "Sad", "Neutral", "Fear", "Disgust", "Angry", "Surprise"]

    age_groups = {"Youth": (15, 20), "Young Adult": (21, 35),  
                  "Middle Aged": (36, 60), "Senior": (61, 70)}

    recommendations = {
        (age_groups["Youth"], "male", "Happy"): "Engage in social activities, join clubs or organizations related to your interests, and pursue personal goals with enthusiasm and positivity.",  
        (age_groups["Youth"], "male", "Sad"): "Reach out for emotional support, engage in activities that bring joy, and consider seeking professional help to address underlying causes of sadness.",
        (age_groups["Youth"], "male", "Neutral"): "Explore various interests, expand your knowledge through learning opportunities, and consider volunteering to find a sense of purpose.",
        (age_groups["Youth"], "male", "Angry"): "Find healthy ways to manage anger, such as engaging in physical exercise, practicing relaxation techniques, and seeking guidance to resolve underlying issues.", 
        (age_groups["Youth"], "male", "Disgust"): "Channel your emotions into advocacy for social causes, support ethical initiatives, and engage in community-building activities.",
        (age_groups["Youth"], "male", "Surprise"): "Embrace new experiences, step out of your comfort zone, and cultivate a sense of wonder through exploration and discovery.",
        (age_groups["Youth"], "male", "Fear"): "Set ambitious goals, challenge yourself to take risks, and actively pursue opportunities that bring fulfillment and excitement.",

        (age_groups["Youth"], "female", "Happy"): "Connect with supportive friends, participate in creative endeavors, and seek opportunities for personal growth and self-expression.", 
        (age_groups["Youth"], "female", "Sad"): "Seek support from loved ones, practice self-care, and explore therapeutic outlets such as counseling or expressive arts.",
        (age_groups["Youth"], "female", "Neutral"): "Focus on self-reflection, engage in mindfulness practices, and pursue activities that nurture your well-being and personal growth.",
        (age_groups["Youth"], "female", "Angry"): "Explore anger management strategies, practice effective communication skills, and prioritize self-care activities that promote emotional balance.",    
        (age_groups["Youth"], "female", "Disgust"): "Educate yourself on environmental and social issues, make sustainable choices, and promote positive change through activism or volunteering.",
        (age_groups["Youth"], "female", "Surprise"): "Embrace spontaneity, seek adventure, and pursue opportunities that bring unexpected joy and excitement into your life.",
        (age_groups["Youth"], "female", "Fear"): "Embrace your passions, engage in activities that spark joy, and surround yourself with people who inspire and motivate you.",
        

        (age_groups["Young Adult"], "male", "Happy"): "Maintain a healthy work-life balance, nurture relationships, and continue pursuing personal and professional growth.",
        (age_groups["Young Adult"], "male", "Sad"): "Seek support from loved ones, consider therapy or counseling, and focus on self-care activities.",  
        (age_groups["Young Adult"], "male", "Neutral"): "Rediscover interests and hobbies, seek personal and professional development opportunities, and foster a sense of purpose.",
        (age_groups["Young Adult"], "male", "Angry"): "Practice anger management techniques, seek counseling, and explore healthy outlets like exercise or creative expression.", 
        (age_groups["Young Adult"], "male", "Disgust"): "Engage in advocacy and community initiatives, support causes that align with your values, and contribute to positive change.",
        (age_groups["Young Adult"], "male", "Surprise"): "Embrace new opportunities, challenge yourself to try new things, and cultivate a sense of adventure and curiosity.", 
        (age_groups["Young Adult"], "male", "Fear"): "Pursue exciting endeavors, take calculated risks, and find ways to infuse passion and enthusiasm into your personal and professional life.",

        (age_groups["Young Adult"], "female", "Happy"): "Focus on self-care, invest in relationships, and explore new avenues for personal growth and happiness.",
        (age_groups["Young Adult"], "female", "Sad"): "Prioritize self-care, seek professional help if needed, and find solace in activities that nurture emotional well-being.",
        (age_groups["Young Adult"], "female", "Neutral"): "Reflect on personal values and goals, nurture personal growth, and find balance in life.",
        (age_groups["Young Adult"], "female", "Angry"): "Develop healthy coping mechanisms, engage in stress-reducing activities, and focus on building positive relationships.", 
        (age_groups["Young Adult"], "female", "Disgust"): "Promote sustainability, support eco-friendly practices, and contribute to organizations working towards positive change.",
        (age_groups["Young Adult"], "female", "Surprise"): "Seek novelty in experiences, explore diverse interests, and prioritize self-discovery and personal growth.",
        (age_groups["Young Adult"], "female", "Fear"): "Embrace opportunities that ignite your passion, nurture a sense of adventure, and cultivate an enthusiastic outlook on life.",

        (age_groups["Middle Aged"], "male", "Happy"): "Cultivate gratitude, maintain social connections, and pursue joyful and fulfilling activities.",
        (age_groups["Middle Aged"], "male", "Sad"): "Seek emotional support, practice self-compassion, and engage in healing activities.", 
        (age_groups["Middle Aged"], "male", "Neutral"): "Rediscover passions, pursue hobbies, and engage in purposeful activities.",
        (age_groups["Middle Aged"], "male", "Angry"): "Seek outlets for anger, practice stress management, and build healthy relationships.",
        (age_groups["Middle Aged"], "male", "Disgust"): "Engage in advocacy, support causes you value, and contribute to positive change.",
        (age_groups["Middle Aged"], "male", "Surprise"): "Embrace new experiences and challenges, embark on travel adventures, and continue pursuing personal growth and learning.",
        (age_groups["Middle Aged"], "male", "Fear"): "Find excitement in new ventures or projects, engage in social activities, and maintain an optimistic outlook.",

        (age_groups["Middle Aged"], "female", "Happy"): "Prioritize self-care, nurture meaningful relationships, and pursue activities that bring you joy and fulfillment.",
        (age_groups["Middle Aged"], "female", "Sad"): "Seek emotional support from loved ones, consider therapy or counseling, and focus on activities that promote healing and well-being.",
        (age_groups["Middle Aged"], "female", "Neutral"): "Maintain a healthy work-life balance, explore personal interests, and engage in activities that nurture your overall well-being.",
        (age_groups["Middle Aged"], "female", "Angry"): "Practice effective communication, explore anger management strategies, and prioritize self-care activities that promote emotional balance.", 
        (age_groups["Middle Aged"], "female", "Disgust"): "Support causes aligned with your values, engage in advocacy, and contribute to positive change in your community.",
        (age_groups["Middle Aged"], "female", "Surprise"): "Embrace new experiences and challenges, foster personal growth and learning, and pursue adventures that ignite your passion.",
        (age_groups["Middle Aged"], "female", "Fear"): "Face your fears with courage, seek support from loved ones, and engage in activities that promote self-confidence and security.",


        (age_groups["Senior"], "male", "Happy"): "Celebrate your achievements, stay socially connected, and engage in activities that bring you joy and fulfillment.",
        (age_groups["Senior"], "male", "Sad"): "Seek support from loved ones, explore therapy or counseling options, and focus on self-care activities that promote emotional well-being.",
        (age_groups["Senior"], "male", "Neutral"): "Stay curious and engaged, pursue lifelong learning opportunities, and maintain a positive outlook on life.",
        (age_groups["Senior"], "male", "Angry"): "Practice patience and forgiveness, seek healthy outlets for anger, and focus on maintaining harmonious relationships.",
        (age_groups["Senior"], "male", "Disgust"): "Advocate for causes you believe in, support organizations promoting positive change, and find purpose in making a difference.",
        (age_groups["Senior"], "male", "Surprise"): "Embrace new experiences, challenge yourself to try new things, and cultivate a sense of wonder and curiosity.",
        (age_groups["Senior"], "male", "Fear"): "Seek support when facing fears or uncertainties, pursue activities that bring comfort and security, and maintain a positive mindset.",

        (age_groups["Senior"], "female", "Happy"): "Nurture your well-being through self-care, maintain social connections, and pursue activities that bring you happiness and fulfillment.",
        (age_groups["Senior"], "female", "Sad"): "Reach out for emotional support, prioritize self-compassion, and engage in activities that promote healing and self-discovery.",
        (age_groups["Senior"], "female", "Neutral"): "Focus on self-reflection, explore new interests, and engage in activities that contribute to your personal growth and well-being.",
        (age_groups["Senior"], "female", "Angry"): "Practice emotional regulation, seek peaceful resolutions, and prioritize self-care activities that promote emotional balance.", 
        (age_groups["Senior"], "female", "Disgust"): "Advocate for causes you care about, support initiatives promoting positive change, and find fulfillment in contributing to a better world.",
        (age_groups["Senior"], "female", "Surprise"): "Embrace the unexpected, seek new adventures, and maintain a sense of curiosity and enthusiasm for life.",
        (age_groups["Senior"], "female", "Fear"): "Face fears with courage, seek support from loved ones, and engage in activities that provide a sense of security and peace."
    }


    recommendation = "No specific recommendation found."

    for key in recommendations:
        age_range, gender_key, emotion_key = key
        if age in range(age_range[0], age_range[1]):
            if gender == gender_key and emotion == emotion_key:
                recommendation = recommendations[key]
                break

    return recommendation

if __name__ == '__main__':
    import sys
    username = sys.argv[1] if len(sys.argv) > 1 else None  # Get the username from command-line arguments
    if username:
        age, gender, emotion = fetch_recommendation_data(username)
        recommendation = generate_recommendation(age, gender, emotion)
        print(recommendation)
    else:
        print('Username not provided.')