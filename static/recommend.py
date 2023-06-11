# Define the recommendation data structure
recommendations = {
    ("15-29", "male", "Happy"): "Engage in social activities, join clubs or organizations related to your interests, and pursue personal goals with enthusiasm and positivity.",
    ("15-29", "male", "Sad"): "Reach out for emotional support, engage in activities that bring joy, and consider seeking professional help to address underlying causes of sadness.",
    ("15-29", "male", "Neutral"): "Explore various interests, expand your knowledge through learning opportunities, and consider volunteering to find a sense of purpose.",
    ("15-29", "male", "Angry"): "Find healthy ways to manage anger, such as engaging in physical exercise, practicing relaxation techniques, and seeking guidance to resolve underlying issues.",
    ("15-29", "male", "Disgust"): "Channel your emotions into advocacy for social causes, support ethical initiatives, and engage in community-building activities.",
    ("15-29", "male", "Surprise"): "Embrace new experiences, step out of your comfort zone, and cultivate a sense of wonder through exploration and discovery.",
    ("15-29", "male", "Fear"): "Set ambitious goals, challenge yourself to take risks, and actively pursue opportunities that bring fulfillment and excitement.",

    ("15-29", "female", "Happy"): "Connect with supportive friends, participate in creative endeavors, and seek opportunities for personal growth and self-expression.",
    ("15-29", "female", "Sad"): "Seek support from loved ones, practice self-care, and explore therapeutic outlets such as counseling or expressive arts.",
    ("15-29", "female", "Neutral"): "Focus on self-reflection, engage in mindfulness practices, and pursue activities that nurture your well-being and personal growth.",
    ("15-29", "female", "Angry"): "Explore anger management strategies, practice effective communication skills, and prioritize self-care activities that promote emotional balance.",
    ("15-29", "female", "Disgust"): "Educate yourself on environmental and social issues, make sustainable choices, and promote positive change through activism or volunteering.",
    ("15-29", "female", "Surprise"): "Embrace spontaneity, seek adventure, and pursue opportunities that bring unexpected joy and excitement into your life.",
    ("15-29", "female", "Fear"): "Embrace your passions, engage in activities that spark joy, and surround yourself with people who inspire and motivate you.",
    
    # Add more recommendations for other combinations of age, gender, and emotion
    
    # Repeat the recommendations for the remaining age groups
    ("30-44", "male", "Happy"): "Maintain a healthy work-life balance, nurture relationships, and continue pursuing personal and professional growth to sustain happiness.",
    ("30-44", "male", "Sad"): "Seek support from loved ones, consider therapy or counseling, and focus on self-care activities to address underlying causes of sadness.",
    ("30-44", "male", "Neutral"): "Rediscover interests and hobbies, seek personal and professional development opportunities, and foster a sense of purpose and fulfillment.",
    ("30-44", "male", "Angry"): "Practice anger management techniques, seek therapy or counseling, and explore healthy outlets for emotions such as physical exercise or creative expression.",
    ("30-44", "male", "Disgust"): "Engage in advocacy and community initiatives, support causes that align with your values, and contribute to positive change.",
    ("30-44", "male", "Surprise"): "Embrace new opportunities, challenge yourself to try new things, and cultivate a sense of adventure and curiosity in your daily life.",
    ("30-44", "male", "Fear"): "Pursue exciting endeavors, take calculated risks, and find ways to infuse passion and enthusiasm into your personal and professional life.",

    ("30-44", "female", "Happy"): "Focus on self-care, invest in relationships, and explore new avenues for personal growth and happiness.",
    ("30-44", "female", "Sad"): "Prioritize self-care, seek professional help if needed, and find solace in activities that nurture emotional well-being.",
    ("30-44", "female", "Neutral"): "Reflect on personal values and goals, nurture personal growth, and find balance in various aspects of life.",
    ("30-44", "female", "Angry"): "Develop healthy coping mechanisms, engage in stress-reducing activities, and focus on building positive relationships and communication skills.",
    ("30-44", "female", "Disgust"): "Promote sustainability in daily life, support eco-friendly practices, and contribute to organizations working towards positive change.",
    ("30-44", "female", "Surprise"): "Seek novelty in experiences, explore diverse interests, and prioritize self-discovery and personal growth.",
    ("30-44", "female", "Fear"): "Embrace opportunities that ignite your passion, nurture a sense of adventure, and cultivate an enthusiastic outlook on life.",
    
    # Repeat the recommendations for the remaining age groups
    ("45-59", "male", "Happy"): "Cultivate gratitude, maintain social connections, and pursue activities that bring joy and fulfillment in this phase of life.",
    ("45-59", "male", "Sad"): "Seek emotional support, practice self-compassion, and engage in activities that promote healing and well-being.",
    ("45-59", "male", "Neutral"): "Rediscover passions, pursue hobbies, and engage in activities that bring a sense of purpose and fulfillment.",
    ("45-59", "male", "Angry"): "Seek outlets for anger, practice stress management techniques, and focus on building healthy relationships and communication skills.",
    ("45-59", "male", "Disgust"): "Engage in advocacy and community initiatives, support causes that align with your values, and contribute to positive change.",
    ("45-59", "male", "Surprise"): "Embrace new experiences and challenges, embark on travel adventures, and continue pursuing personal growth and learning.",
    ("45-59", "male", "Fear"): "Find excitement in new ventures or projects, engage in social activities, and maintain an optimistic outlook on life.",

    ("45-59", "female", "Happy"): "Focus on self-care, seek personal fulfillment, and explore new avenues for happiness and personal growth.",
    ("45-59", "female", "Sad"): "Seek support from loved ones, engage in activities that promote emotional well-being, and consider therapy or counseling if needed.",
    ("45-59", "female", "Neutral"): "Reflect on personal values and goals, nurture personal growth, and find balance in various aspects of life.",
    ("45-59", "female", "Angry"): "Develop strategies for anger management, prioritize self-care, and explore mindfulness practices to foster emotional well-being.",
    ("45-59", "female", "Disgust"): "Support environmental causes, promote sustainability, and contribute to positive change through personal choices and advocacy.",
    ("45-59", "female", "Surprise"): "Embrace spontaneity, explore new hobbies or interests, and find joy in discovering new aspects of life in this phase.",
    ("45-59", "female", "Fear"): "Embrace your passions, seek new opportunities for growth and fulfillment, and maintain a zest for life.",
    
    # Repeat the recommendations for the remaining age groups
    ("60-70", "male", "Happy"): "Enjoy retirement, engage in activities that bring joy and fulfillment, and foster connections with loved ones and the community.",
    ("60-70", "male", "Sad"): "Seek support from loved ones, engage in activities that promote emotional well-being, and consider joining support groups or therapy.",
    ("60-70", "male", "Neutral"): "Explore new hobbies or interests, invest time in self-reflection and personal growth, and enjoy the freedom of this phase of life.",
    ("60-70", "male", "Angry"): "Find healthy outlets for anger, engage in relaxation techniques or meditation, and seek support to navigate through this phase of life.",
    ("60-70", "male", "Disgust"): "Dedicate time to causes you care about, engage in community service, and embrace opportunities to leave a positive impact.",
    ("60-70", "male", "Surprise"): "Embrace new experiences and challenges, embark on travel adventures, and continue pursuing personal growth and learning.",
    ("60-70", "male", "Fear"): "Find excitement in new ventures or projects, engage in social activities, and maintain an optimistic outlook on life.",

    ("60-70", "female", "Happy"): "Cultivate meaningful relationships, pursue hobbies and interests, and embrace opportunities for personal growth and happiness.",
    ("60-70", "female", "Sad"): "Prioritize self-care, practice self-compassion, and engage in activities that bring solace and a sense of peace.",
    ("60-70", "female", "Neutral"): "Focus on self-discovery, engage in activities that bring fulfillment and joy, and prioritize well-being and self-care.",
    ("60-70", "female", "Angry"): "Develop coping mechanisms for anger, prioritize self-care, and explore therapeutic options to manage emotions effectively.",
    ("60-70", "female", "Disgust"): "Advocate for environmental sustainability, support ethical initiatives, and contribute to organizations working towards positive change.",
    ("60-70", "female", "Surprise"): "Embrace spontaneity, explore new hobbies or interests, and find joy in discovering new aspects of life in this phase.",
    ("60-70", "female", "Fear"): "Embrace your passions, seek new opportunities for growth and fulfillment, and maintain a zest for life.",
}

# Function to get recommendation based on input
def get_recommendation(age, gender, emotion):
    key = (age, gender.lower(), emotion.lower())
    if key in recommendations:
        return recommendations[key]
    else:
        return "No recommendation found for the given input."

# Main program
while True:
    age = input("Enter age (15-29, 30-44, 45-59, 60-70): ")
    age_class = ""

    if age in ["15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29"]:
        age_class = "15-29"
    elif age in ["30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44"]:
        age_class = "30-44"
    elif age in ["45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59"]:
        age_class = "45-59"
    elif age in ["60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70"]:
        age_class = "60-70"
    else:
        print("Invalid age. Please enter a valid age.")
        continue 

    gender = input("Enter gender (male, female): ")
    emotion = input("Enter emotion (Happy, Sad, Neutral, Angry, Disgust, Surprise, Fear ): ")

    recommendation = get_recommendation(age_class, gender, emotion)
    print("Recommendation:", recommendation)

    
