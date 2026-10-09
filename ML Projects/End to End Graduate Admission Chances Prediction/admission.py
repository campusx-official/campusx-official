import sklearn
import joblib
import pandas as pd
import streamlit as st
import random
import time

# Add custom background, title, button, and animation styling
st.markdown(
        """
        <style>
        .stApp {
            background-image: linear-gradient(to right, #4B183B, #FF5733); /* Gradient background */
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            color: #FFFFFF;  /* Text color for readability */
            font-family: 'Arial', sans-serif;
        }

        /* Title Section Styling */
        .title-container {
            animation: colorChange 8s infinite alternate, borderGlow 2s infinite alternate;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            border: 3px solid rgba(255, 255, 255, 0.5);
            box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.6);
            transition: transform 0.3s ease-in-out;
        }
        .title-container:hover {
            transform: scale(1.05);
        }

        h2 {
            color: white;
            font-weight: bold;
            font-size: 2.5em;
            text-shadow: 0px 0px 10px rgba(255, 255, 255, 0.8);
            animation: pulseShadow 2s infinite;
        }

        /* Button Styling */
        .btn {
            background-color: #FF5733;
            color: white;
            padding: 15px 30px;
            font-size: 1.2em;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.3s ease;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
        }
        .btn:hover {
            background-color: #D41443;
            box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.6);
        }

        /* Keyframe Animations */
        @keyframes colorChange {
            0% { background-color: #4B183B; }
            25% { background-color: #8A1C4A; }
            50% { background-color: #D41443; }
            75% { background-color: #FF5733; }
            100% { background-color: #FFC300; }
        }

        @keyframes borderGlow {
            0% { box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.5); }
            100% { box-shadow: 0px 0px 40px rgba(255, 255, 255, 1); }
        }

        @keyframes pulseShadow {
            0%, 100% { text-shadow: 0px 0px 10px rgba(255, 255, 255, 0.8); }
            50% { text-shadow: 0px 0px 20px rgba(255, 255, 255, 1); }
        }

        .falling {
            position: absolute;
            font-size: 40px;
            animation: falling 3s ease-in-out infinite;
            opacity: 0;
        }

        /* Keyframe animation for falling effect */
        @keyframes falling {
            0% { transform: translateY(-100px); opacity: 1; }
            100% { transform: translateY(100vh); opacity: 0; }
        }

        </style>
        """, unsafe_allow_html=True
    )

# Title with Animation
st.markdown("""
        <div class="title-container">
            <h2>
                🎓🏫 Graduate Admission Chances Prediction
            </h2>
        </div>
    """, unsafe_allow_html=True)

# Button for interaction (using Streamlit button)
st.write("")
st.write("")
if st.button('Get Started'):
        st.write("Let's get started with the prediction!")
        # Create random falling emoji from different positions
        for i in range(10):  # Loop for 10 falling emojis
        # Random horizontal position (from left to right)
           left_position = random.randint(0, 100)
        # Random delay for each emoji for variation
           delay = random.randint(0, 2)

           st.markdown(f"""
           <div class="falling" style="left: {left_position}%; animation-delay: {delay}s;">
            🎓
           </div>
            """, unsafe_allow_html=True)

           time.sleep(0.5)  # Adjust the delay between each falling emoji


model = joblib.load('admission_model')
p1 = st.number_input("Enter GRE Score")
p2 = st.number_input("Enter TOEFL Score")

# Add custom CSS styling for a small width box with a bouncing and color-changing effect
st.markdown(
        """
        <style>
        @keyframes bounce {
            0% { transform: translateY(0); }
            30% { transform: translateY(-10px); }
            50% { transform: translateY(0); }
            70% { transform: translateY(-5px); }
            100% { transform: translateY(0); }
        }

        @keyframes color-change {
        0% { background-color: #909497; }  /* Grey */
        100% { background-color: #17202a; } /* Black */
        }

        .bounce-box {
            color: white;                /* Text color */
            padding: 10px 5px;           /* Padding for height but very small width */
            border-radius: 5px;          /* Rounded corners */
            font-size: 1.2em;            /* Font size */
            text-align: center;          /* Centered text */
            width: auto;                 /* Automatic width */
            min-width: 50px;             /* Minimum width */
            max-width: 100px;            /* Maximum width for the box */
            animation: bounce 1s ease infinite, color-change 3s ease infinite; /* Bounce and color change effect */
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.4);  /* Small shadow */
            display: inline-block;       /* Inline-block for small width */
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Slider for University Rating
p3 = st.slider('Select University Rating🏫⭐', 1, 5)

    # Display selected value inside a small, bouncing box with changing colors
st.markdown(f'<div class="bounce-box">You selected: {p3}</div>', unsafe_allow_html=True)


    # Using the select_slider
p4 = st.number_input('Enter SOP')
p5 = st.number_input('Enter LOR')
p6 = st.number_input('Enter CGPA')
p7 = st.selectbox('Select Research',(0,1))

    # Display a summary of inputs
input_data = pd.DataFrame({
        'GRE Score': [p1],
        'TOEFL Score': [p2],
        'University Rating': [p3],
        'SOP': [p4],
        'LOR': [p5],
        'CGPA': [p6],
        'Research': [p7],
    })

    # Generate HTML for table with styling
table_html = input_data.to_html(index=False, classes='styled-table')

    # CSS to style the black box and table
st.markdown(
        """
        <style>
        .black-box {
            background-color: #000000;        /* Black background for box */
            color: white;                     /* White text color */
            padding: 10px;                    /* Padding around the table */
            border-radius: 10px;              /* Rounded corners */
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.6); /* Shadow for depth */
            max-width: 90%;                   /* Maximum width of box */
            margin: auto;                     /* Center-align the box */
        }

        /* Table styling within the black box */
        .styled-table {
            width: 100%;
            color: white;
            border-collapse: collapse;
        }

        .styled-table th, .styled-table td {
            border: 1px solid #444444;        /* Border color for cells */
            padding: 8px;                     /* Padding inside cells */
            text-align: center;               /* Center-align text */
        }

        .styled-table th {
            background-color: #333333;        /* Dark background for header */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display table inside black box
st.markdown("### Customer Data Summary", unsafe_allow_html=True)
st.markdown(table_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


if st.button('Predict'):
        pred = model.predict(
            [[p1, p2, p3, p4, p5, p6, p7]])

        # Display the result
        if pred[0] == 1:
            st.balloons()
            st.toast("Prediction completed!")
            st.success("🎉 High Chance of getting admission 🎉")
        else:
            st.error("⚠️ High risk of not getting admission ⚠️")

    # html_temp = """
    #        <div style="
    #            animation: borderGlow 2s infinite alternate;
    #            padding: 20px;
    #            border-radius: 10px;
    #            text-align: center;
    #            border: 3px solid rgba(255,255,255,0.5);
    #            box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.6);
    #        ">
    #            <h2 style="color: white; font-family: Arial, sans-serif; font-weight: bold;
    #                       text-shadow: 0px 0px 10px rgba(255,255,255,0.8);
    #                       animation: pulseShadow 2s infinite;">
    #                Thank you for using Graduate Admission Chances Prediction tool! 🎓🏫
    #            </h2>
    #        </div>
    #
    #        <style>
    #            /* Keyframes for border glow effect */
    #            @keyframes borderGlow {
    #                0% { box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.5); }
    #                100% { box-shadow: 0px 0px 40px rgba(255, 255, 255, 1); }
    #            }
    #
    #            /* Keyframes for text shadow pulsing effect */
    #            @keyframes pulseShadow {
    #                0%, 100% { text-shadow: 0px 0px 10px rgba(255, 255, 255, 0.8); }
    #                50% { text-shadow: 0px 0px 20px rgba(255, 255, 255, 1); }
    #            }
    #        </style>
    #    """
    # st.write("")
    # st.markdown(html_temp, unsafe_allow_html=True)


html_temp = """
               <div style="
                   animation: borderGlow 2s infinite alternate;
                   padding: 20px;
                   border-radius: 10px;
                   text-align: center;
                   border: 3px solid rgba(255,255,255,0.5);
                   background-color: black;          /* Black background */
                   box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.6);
               ">
                   <h2 style="color: white; font-family: Arial, sans-serif; font-weight: bold; 
                              text-shadow: 0px 0px 10px rgba(255,255,255,0.8); 
                              animation: pulseShadow 2s infinite;">
                       Thank you for using Graduate Admission Chances Prediction tool! 🎓🏫
                   </h2>
               </div>

               <style>
                   /* Keyframes for border glow effect */
                   @keyframes borderGlow {
                       0% { box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.5); }
                       100% { box-shadow: 0px 0px 40px rgba(255, 255, 255, 1); }
                   }

                   /* Keyframes for text shadow pulsing effect */
                   @keyframes pulseShadow {
                       0%, 100% { text-shadow: 0px 0px 10px rgba(255, 255, 255, 0.8); }
                       50% { text-shadow: 0px 0px 20px rgba(255, 255, 255, 1); }
                   }
               </style>
           """
st.write("")
st.markdown(html_temp, unsafe_allow_html=True)

