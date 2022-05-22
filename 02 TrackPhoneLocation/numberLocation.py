import json

import iso3166 as iso3166
import phonenumbers
import pycountry

from tkinter import Tk, Label, Button, Entry
from phonenumbers import carrier
from phonenumbers import geocoder
#len (pycountry.countries)
#from phone-iso3166-3.country


class Track:
    def __init__(self, App):
        self.window = App
        self.window.title("Phone Number Tracker")
        self.window.geometry("500x400")
        self.window.configure(bg="#2f2212")
        self.window.resizable(False, False)

        #__________Application Menu__________
        Label(App, text="TRACK PHONE NUMBER", fg="white", font=("Times", 20), bg="#3f5edb").place(x=150, y=30)
        self.mobile_number = Entry(App, width=20, font=("Arial", 15), relief="flat")
        self.trackingbutton = Button(App, text="S E A R C H", bg="#22c6c3", relief="sunken")
        self.countryname = Label(App, fg="white", font=("Times", 20), bg="#3f5efb")
        self.countryname2 = Label(App, fg="white", font=("Times", 20), bg="#3f5efb")

        # ________Place Widgets on the Window__________
        self.mobile_number.place(x=150, y=120)
        self.trackingbutton.place(x=200, y=200)
        self.countryname.place(x=100, y=280)

        #_________Lining Button with Countries_________
        self.countryname2.place(x=300, y=280)
        self.trackingbutton.bind("<Button-1>", self.Track_THE_location)

    def Track_THE_location(self, event):
        phone_number = self.mobile_number.get()
        country = "Country is Unknown"
        if phone_number:
            tracked = phonenumbers.parse(phone_number, "RO")
            tracked2 = phonenumbers.parse(phone_number, "CH")
        self.countryname.configure(text=carrier.name_for_number(tracked, "en"))
        self.countryname2.configure(text=geocoder.description_for_number(tracked2, "en"))


PhoneTracking = Tk()
MyApp = Track(PhoneTracking)

PhoneTracking.mainloop()
