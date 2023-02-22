import streamlit as st


st.set_page_config(page_title="Portfolio", page_icon=":smirk_cat:", layout="wide")

st.header("A Student Trying Her Best In This World")

st.write("---")
st.subheader("A Brief Introduction to this 'passion project'")


#sidebar thingss
with st.container():
 with st.sidebar:
   menu = ["About Me","About Project"]
   choice = st.sidebar.selectbox("Additional Info!",menu)
   if choice == "About Project":
     st.subheader("What I used")
     st.write("I used Streamlit and coded using Visual Studio Code. I had Pycharm and Anaconda installed but I felt that VSC was the easiest platform to use as someone with zero experience at all")
     st.subheader("These are the resources I used as learning material")
     st.write("[The Streamlit Tutorials itself](https://docs.streamlit.io/)")
     st.write("[This life saving youtube channel](https://www.youtube.com/@CodingIsFun/featured)")
     st.write("Reddit forums")
     st.write("[This forum too](https://www.freecodecamp.org/news/python-code-examples-sample-script-coding-tutorial-for-beginners/)")
     st.write("[Stack Overflow](https://stackoverflow.com/)")
     st.subheader("What I learnt")
     """The basic terminology of certain things such as "file path", "root directory" etc. I have learnt the basics of coding and can now code a simple blog on my own from scratch
     without guidance! More importantly, I realised that I actually **enjoyed** coding despite the warnings given to me by my peers :smirk_cat:"""
     st.subheader("What I hope to improve on")
     """My goal by the end of this month (February) is to be able to create a simple finance calculator and maybe expand into other languages, i.e HTML and C++"""
    
   else:
    st.header("About me")
   
    """My name is Jaimie, some call me James for short. I'm a fresh junior college graduate. Unsurprisingly, I enjoy
    watching shows and spending time with people, like many others do. However, that's not all I do with my spare time. On quiet days, I can and will spend my days cooped up in my room
    watching documentaries about anything and everything that comes to mind. As an extremely curious person who values knowledge as power, I value the art of questioning and exploring.
    """
    st.subheader("Random facts about me (why not)")
    """
   - 13 years of dance experience
   - Completed 4 grades of abacus
   - **LOVE** music (I cannot emphasize this enough)
   - Types at 130wpm 
   - Massive Eater
   - Wants a dog and cat
    """


st.write("##")
text_column, image_column = st.columns ((2, 1))
with text_column:

  st.write(
    """Its not often that I get the opportunity to explore my interests, with the heavy workloads and expectations to keep up, it wasn't easy to set aside time to think of what 
I was truly passionate about. There was a moment in time where I was determined to pursue medicine, then astrophysics. Slowly after, I was introduced to the latest craze of 
computing which really expanded my perspective of the world. So I realised that it was time to act on my feelings, which is what this passion project is about. I apologise if this 
website appears to be lackluster - it is my first time doing a hands on coding project with the help of youtube tutorials, online forums and hours of troubleshooting by exploring 
every function!""")


st.write("---")

st.header("My Other Projects!")
st.subheader("Figma App Design")
st.write("This was a design project that I undertook to try my hand at visualising an application that I have **yet** have the ability to actually create.")
st.write("To see the whole design in action, you can click [here](https://www.figma.com/proto/howzl49kutxqNl7auywbI5/Project1?node-id=1%3A2&starting-point-node-id=1%3A2) to view")
st.write("_You might require an account to veiw it unfortunately_ :cry:")

st.subheader("My little coffee opinion generator (Had a little coding fun :smiley:)")
st.write("[Please take everything in this little survey as a joke](https://coffeemachine.streamlit.app/)")

st.subheader("Portfolio/summary")
st.write("[Portfolio document](https://docs.google.com/document/d/12zTsrW1emw6DRS4-2sx6G9qtgmDf4f1Ql2L1AMyftOs/edit?usp=sharing)")
"""This was supposed to be the initial webpage, however I encountered an issue with deploying it. I'm guessing it's because of the images uploaded. This webpage was supposed
to be an attempt in salvaging my previously "failed" website. Not to be mistaken, I have not given up on trying to resolve the issue, but this would be a back up to showcase
my efforts. :confused:"""

st.write("**To give a small description to my issue**")
txt = st.text_area
st.write("The terminal stated")
st.code("syntaxerror: Invalid syntax")
st.write("However the program ran perfectly locally. So I deployed it, which eventually prompted me an issue with my image files. ")
contact_form ="""<form action="https://formsubmit.co/d4pper.i0@gmail.com" method="POST">
     <input type="text" name="name" placeholder= "Your name" required>
     <input type="email" name="email" placeholder= "Your real/fake email" required>
     <textarea name="message" placeholder="Advise, Opinions, Messages welcomed"></textarea>
     <button type="submit">Send</button>
     </form>"""

st.markdown(contact_form, unsafe_allow_html=True)

st.container()
st.empty()
st.text("I tried styling it, but I'm still figuring that out.")

st.write("Thats all for this website, I'll be creating more (better) projects along the way. I hope you consider my application :heart:")
