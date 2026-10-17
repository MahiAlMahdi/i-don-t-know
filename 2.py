import time
import random
import streamlit as st

# পেজ কনফিগারেশন
st.set_page_config(
    page_title="Interactive Fun Quiz", page_icon="🎲", layout="centered"
)

# স্টাইলিং (Custom CSS)
st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        color: #FF4B4B;
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .custom-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .result-text {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        color: #1E88E5;
    }
    .slogan-box {
        background-color: #E8F5E9;
        border-left: 5px solid #2E7D32;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        color: #1B5E20;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# শিরোনাম
st.markdown(
    '<div class="main-title">🎉 Fun Interactive Quiz & Dice Game 🎲</div>',
    unsafe_allow_html=True,
)

# ১. নিকনেম ইনপুট
st.markdown("### 👤 Step 1: Tell us about yourself")
nickname = st.text_input(
    "What's your name? (Only nickname)", placeholder="Type your nickname..."
)

if nickname:
  # ২. বয়স ইনপুট
  age = st.number_input(
      "Enter your age:", min_value=1, max_value=100, value=20, step=1
  )

  st.markdown("---")
  # ৩. সিঙ্গেল স্ট্যাটাস
  st.markdown("### 💖 Step 2: Relationship Status")
  is_single = st.selectbox("Are you single?", ["Select", "Yes", "No"])

  if is_single != "Select":
    # ৪. বিয়ের ইচ্ছে
    want_to_marry = st.selectbox(
        "Do you want to marry?", ["Select", "Yes", "No"]
    )

    if want_to_marry == "No":
      gender = st.selectbox("Select your gender:", ["Select", "Male", "Female"])

      if gender == "Male":
        st.error(f"🏳️‍🌈 **{nickname}**, why are you gay? 🤔")
        st.snow()  # অ্যানিমেশন
      elif gender == "Female":
        st.success(f"🏳️‍🌈 **{nickname}**, congratulations dear lesbian! 🌈")
        st.balloons()  # অ্যানিমেশন

    elif want_to_marry == "Yes":
      st.markdown("---")
      # ৫. বয়স সীমা (Age Range)
      st.markdown("### 💍 Step 3: Match Preference")
      age_range = st.selectbox(
          "Choose your preferable age range",
          ["Select", "18-25", "26-35", "36-45", "46-55"],
      )

      if age_range != "Select":
        range_mappings = {
            "18-25": list(range(18, 28)),
            "26-35": list(range(26, 36)),
            "36-45": list(range(36, 46)),
            "46-55": list(range(46, 56)),
        }

        exact_age = st.selectbox(
            "Choose your exact preferable age",
            ["Select"] + range_mappings[age_range],
        )

        if exact_age != "Select":
          st.markdown("---")
          # ৬. ডাইস রোল ইন্টারফেস
          st.markdown("### 🎲 Step 4: Predict Your Future!")

          if st.button("🎲 Roll the Dice!", use_container_width=True):
            # রোলিং অ্যানিমেশন
            with st.spinner("Rolling the dice for you... 🎲"):
              time.sleep(1.2)  # ইন্টারেক্টিভ লোডিং অনুভূতি

            # কন্ডিশন: মান সবসময় ৩ থেকে ৬
            dice_result = random.randint(3, 6)
            st.session_state["dice_result"] = dice_result

          # ৭. ডাইস ফলাফলের ইন্টারফেস
          if "dice_result" in st.session_state:
            dice_val = st.session_state["dice_result"]

            st.balloons()  # বেলুন অ্যানিমেশন
            st.markdown(
                f"""
                        <div class="custom-card">
                            <div class="result-text">🎲 You rolled a {dice_val}!</div>
                            <br>
                            <h2 style="text-align: center; color: #2E7D32;">
                                🎉 Congratulations {nickname}, you will have {dice_val} kids! 👶
                            </h2>
                        </div>
                        """,
                unsafe_allow_html=True,
            )

            st.markdown("<br>", unsafe_allow_html=True)
            # ৮. স্লোগান
            st.markdown(
                """
                        <div class="slogan-box">
                            🇧🇩 "দুটি সন্তানের বেশি নয়, একটি হলে ভালো হয়"
                        </div>
                        """,
                unsafe_allow_html=True,
            )