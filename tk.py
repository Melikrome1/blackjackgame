from tkinter import *

root =Tk()
root.title('Cyn City - Card Deck<3')
root.geometry("900x500")
root.configure(background= "pink")

my_frame = Frame(root, bg="pink")
my_frame.pack(pady=20)

#frames for cards
dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Player", bd=0)
player_frame.grid(row=0, column=1, ipadx=20)

#in the frame
dealer_label = Label(dealer_frame, text ='')
dealer_label.pack(pady=20)

player_label = Label(player_frame, text ='')
player_label.pack(pady=20)
 
#button #shuffles
shuffle_button = Button(root, text="Choose Cards", font=("Lucida Handwriting", 14))
shuffle_button.pack(pady=20)

card_button = Button(root, text="Get Cards", font=("Lucida Handwriting", 14))
card_button.pack(pady=20)

root.mainloop()