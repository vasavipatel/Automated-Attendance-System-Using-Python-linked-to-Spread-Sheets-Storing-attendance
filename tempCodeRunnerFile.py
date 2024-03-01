# bg image
        img3=Image.open(r"C:\smartcampusproject\smartcampuspics\vnr logo.jpg")
        img3=img3.resize((1530,710), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200, width=1450, height=600)