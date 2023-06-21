import streamlit as st

# Create a title for the quiz
st.title(" Fitness tips for beginners")

import streamlit as st

# Create a title for the program
st.title("* Basic Gym Rules")

# Create a section for the rules
st.write("Here are some basic gym rules that you should follow:")

# List the rules
st.markdown("""
* Be respectful of other gym users.
* Wipe down equipment after use.
* Don't hog equipment.
* Don't leave your belongings unattended.
* Don't use your phone while on the equipment.
* Don't drink alcohol or eat food in the gym.
* Shower before and after your workout.
* Be mindful of your noise level.
* If you are injured, consult with a doctor or physical therapist before working out.
""")


# Define the fitness tips
fitness_tips = [
  {
    "tip": "1. Set realistic goals.",
    "description": "Don't try to do too much too soon. Start with small goals that you can easily achieve, and then gradually increase the difficulty and intensity of your workouts as you get fitter.",
  },
  {
    "tip": "2. Find an activity you enjoy.",
    "description": "If you don't enjoy your workouts, you're less likely to stick with them. Find an activity that you find fun and challenging, and you'll be more likely to make fitness a part of your lifestyle.",
  },
  {
    "tip": "3. Make fitness a priority.",
    "description": "Schedule time for workouts in your day just like you would any other important appointment. And don't be afraid to say no to other commitments if it means you can get your workout in.",
  },
  {
    "tip": "4. Listen to your body.",
    "description": "Don't push yourself too hard. If you're feeling pain, take a break. It's better to rest and recover than to injure yourself.",
  },
  {
    "tip": "5. Celebrate your successes.",
    "description": "When you reach a fitness goal, take some time to celebrate your success. This will help you stay motivated and keep working towards your goals.",
  },
]

# Create a fitness tips page
st.title("* 5 Fitness Tips")

for tip in fitness_tips:
  st.subheader(tip["tip"])
  st.write(tip["description"])


# Create a question
st.title("* Tips & tricks for build muscle/lose fats?")

# Create a radio button group to allow users to select their goal
options = ["Lose weight", "Build muscle", "Get in shape", "Improve my overall health"]
choice = st.radio("", options)

# Create a conditional statement to display different text based on the user's choice
if choice == "Lose weight":
  st.markdown("Here are some tips for losing weight at the gym:")
  st.markdown("* Set realistic goals.")
  st.markdown("* Find a workout routine that you enjoy and that fits your schedule.")
  st.markdown("* Eat a healthy diet.")
  st.markdown("* Get enough sleep.")
  st.markdown("* Daily workout & keep running.")
  

elif choice == "Build muscle":
  st.markdown("Here are some tips for building muscle at the gym:")
  st.markdown("* Lift weights that are challenging but that you can still control.")
  st.markdown("* Focus on compound exercises that work multiple muscle groups.")
  st.markdown("* Eat a healthy diet that is high in protein.")
  st.markdown("* Get enough sleep.")

elif choice == "Get in shape":
  st.markdown("Here are some tips for getting in shape at the gym:")
  st.markdown("* Start with a basic workout routine and gradually increase the intensity and duration of your workouts over time.")
  st.markdown("* Focus on exercises that improve your cardiovascular health, such as running, swimming, and biking.")
  st.markdown("* Eat a healthy diet.")
  st.markdown("* Get enough sleep.")

elif choice == "Improve my overall health":
  st.markdown("Here are some tips for improving your overall health at the gym:")
  st.markdown("* Exercise regularly.")
  st.markdown("* Eat a healthy diet.")
  st.markdown("* Get enough sleep.")
  st.markdown("* Manage stress.")
  st.markdown("* Get regular medical checkups.")



import streamlit as st
import pandas as pd

#create a title 
st.title("* workout schedule")

#create a heading
st.markdown("schedule for you")

#create a radio button to group bodyparts
bodyParts = ["Delt","Back","Leg","Chest","Arms","Hamstring"]
choice = st.radio("",bodyParts)

if choice =="Delt":
    myworkout = pd.DataFrame({
        'workout':   ["standing lateral rise","Rear peckdeck fly","Rop face pully","Dumbell press","sruggs Back&front"],
        'no of sets':["15*4","15*4","12*4","12*4","12*5"],
    })
    st.experimental_show(myworkout)

elif choice =="Back":
    myworkout = pd.DataFrame({
        'workout':  ["dumbell rowing","T bar rowing","lat pully front","Rop rowing"],
        'no of sets' :["12*4","12*4","12*4","15*4"],
    })
    st.experimental_show(myworkout)

elif choice =="Leg":
    myworkout = pd.DataFrame({
        'workout': ["front extension","leg curl","front dumbell squat","Leg press","Dumbell sumo squat",],
        'no of sets' : ["15*4","15*5","12*4","12*5","12*4"],
    })
    st.experimental_show(myworkout)   

elif choice =="Chest":
    myworkout = pd.DataFrame({
        'workout': ["peck dec fly","cabel crossover down","falt dumbell press","cabel crossover upp","Upper dumbell press"],
        'no of sets':["15*4","15*4","12*4","12*4","12*5"],
    })
    st.experimental_show(myworkout)

elif choice =="Arms":
    myworkout = pd.DataFrame({
        'workout' : ["precher curl","Barbell curl","Hammer curl","Rop push down","Dumbell ower head","shot bar push down"],
        'no of sets':["15*4","15*4","12*4","12*4","12*5","15*4"],
    })
    st.experimental_show(myworkout)

elif choice =="Hamstring":
    myworkout = pd.DataFrame({
        'workout' : ["Walking lunges","Back curl","smith squat","Front extrnsion","Leg press","Dumbell sumo squat"],
                'no of sets':["15*4","15*4","12*4","12*4","12*5","15*4"],
    })
    st.experimental_show(myworkout)
    
# Create a title for the program        
st.title("* Simple diet plan")  
  
# Create a section for the rules
st.write("Here are some basic gym diet that you should follow:")

# List the rules
st.markdown("""Meal 1

3 whole eggs_
4 slices of toast_
2 cups oatmeal_
Protein powder_ 

Meal 2

2 large baked potatoes_
12 oz. beef steak_
8 oz. fibrous vegetables_

Meal 3

1 cup of almonds_
Protein powder_
1 pint of ice cream_

Meal 4

2 large baked potatoes_
12 oz. chicken off-the-bone_
8 oz. fibrous vegetables_

Meal 5

2 servings of fruit_
12 oz. turkey off-the-bone_
8 oz. fibrous vegetables_
1 pint of ice cream""")
