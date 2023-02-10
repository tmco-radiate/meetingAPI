import streamlit as st
from multiapp import MultiApp
from apps import users, rooms, bookings # import your app modules here

app= MultiApp()

app.add_app("bookings", bookings.app)
app.add_app("users", users.app)
app.add_app("rooms", rooms.app)

app.run()