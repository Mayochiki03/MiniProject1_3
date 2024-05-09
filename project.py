from tkinter import*  
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk

window = Tk ()
window.attributes('-fullscreen', True)
window.title("โปรแกรมอธิบายการทำงาน")

#ประกาศตัวแปรรูปภาพ
Insertion_image = PhotoImage(file="D:/New folder1/Insertion_image.png")
sorting_image = PhotoImage(file="D:/New folder1/mormor.png")
index_image = PhotoImage(file="D:/New folder1/mormor.png")
Insertion_image_page2_pic1 = PhotoImage(file="D:/New folder1/Insertion (1).png")
Insertion_image_page2_pic2 = PhotoImage(file="D:/New folder1/Insertion (2).png")
Insertion_image_page2_pic3 = PhotoImage(file="D:/New folder1/Insertion (3).png")
Insertion_image_page3_pic1 = PhotoImage(file="D:/New folder1/Insertion (4).png")
Insertion_image_page3_pic2 = PhotoImage(file="D:/New folder1/Insertion (5).png")
Insertion_image_page3_pic3 = PhotoImage(file="D:/New folder1/Insertion (6).png")
Insertion_image_page4_pic2 = PhotoImage(file="D:/New folder1/Insertion (8).png")
Insertion_image_page4_pic3 = PhotoImage(file="D:/New folder1/Insertion (9).png")
selectio_image_page1= PhotoImage(file="D:/New folder1/selectio  (1).png")
selectio_image_page2= PhotoImage(file="D:/New folder1/selectio  (2).png")
selectio_image_page3= PhotoImage(file="D:/New folder1/selectio  (3).png")
selectio_image_page4= PhotoImage(file="D:/New folder1/selectio  (4).png")
selectio_image_page5= PhotoImage(file="D:/New folder1/selectio  (5).png")
selectio_image_page6= PhotoImage(file="D:/New folder1/selectio  (6).png")
merge_image1 = PhotoImage(file="D:/New folder1/merge1.png")
merge_image2 = PhotoImage(file="D:/New folder1/merge2.png")
merge_image3 = PhotoImage(file="D:/New folder1/merge3.png")
merge_image4 = PhotoImage(file="D:/New folder1/merge4.png")
bubble_image1 = PhotoImage(file="D:/New folder1/bubblepage1.png")
bubble_image2 = PhotoImage(file="D:/New folder1/bubblepage2.png")
bubble_image3 = PhotoImage(file="D:/New folder1/bubblepage3.png")
bubble_image4 = PhotoImage(file="D:/New folder1/bubblepage4.png")
bubble_image5 = PhotoImage(file="D:/New folder1/bubblepage5.png")
searching_seq1 = PhotoImage(file="D:/New folder1/searching-seq1.png")
searching_seq2 = PhotoImage(file="D:/New folder1/searching-seq2.png")
searching_seq3 = PhotoImage(file="D:/New folder1/searching-seq3.png")
searching_seq4 = PhotoImage(file="D:/New folder1/searching-seq4.png")
Binary_page1 = PhotoImage(file="D:/New folder1/Binary (1).png")
Binary_page2 = PhotoImage(file="D:/New folder1/Binary (2).png")
Binary_page3 = PhotoImage(file="D:/New folder1/Binary (3).png")
developer = PhotoImage(file="D:/New folder1/Developer.png")
index_label = Label(window, image=index_image)
index_label.place(relwidth=1.0, relheight=1.0)

button_style = ttk.Style()
button_style.configure("Custom.TButton", font=('Angsana New', 18, 'bold'), width = '60')
button_style.map("Custom.TButton",foreground=[('active', 'gray'), ('!active', 'black')])
def menuExit():
    window.destroy()

def Sorting():
    windowst = Toplevel()
    windowst.title("sorting")
    windowst.geometry("650x650+430+60")

    sorting_label = Label(windowst, image=sorting_image)
    sorting_label.place(relwidth=1.0, relheight=1.0)

    def Bubble_sort():
        windowbs = Toplevel()
        windowbs.title("Bubble Sort")
        windowbs.geometry("750x450+380+160")

        def menuClear():
            radius1.set("")
            radius2.set("")
            radius3.set("")
            radius4.set("")
            result_var.set("")


        def bubble_sort(arr):
            n = len(arr)

            for i in range(n):
                swapped = False

                for j in range(0, n - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        swapped = True

                if not swapped:
                    break

        def calculate_sort():
            input_data = [entry1.get(), entry2.get(), entry3.get(), entry4.get()]
            try:
                data = [int(x) for x in input_data]
                bubble_sort(data)
                result_var.set("Sorted Array: " + " ".join(map(str, data)))
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter valid numbers in all 4 fields.")


        class PageManager:
            def __init__(self, root):
                self.root = root
                self.pages = []
                self.current_page_index = -1

            def add_page(self, page):
                self.pages.append(page)

            def show_page(self, page_index):
                if 0 <= page_index < len(self.pages):
                    if self.current_page_index >= 0:
                        self.pages[self.current_page_index].pack_forget()
                    self.pages[page_index].pack(fill="both", expand=True)
                    self.current_page_index = page_index
            def go_to_previous_page(self):
                if self.current_page_index > 0:
                    self.show_page(self.current_page_index - 1)

            def go_to_next_page(self):
                if self.current_page_index < len(self.pages) - 1:
                    self.show_page(self.current_page_index + 1)

        page_manager = PageManager(windowst)

        page1 = Frame(windowbs)
        Bubble_label = Label(page1, image=bubble_image1)
        Bubble_label.place(relwidth=1.0, relheight=1.0,)
        page1_label2 = Label(page1, text="มีหลักการจัดเรียงข้อมูล คือ ให้จับคู่ข้อมูลที่อยู่ในตำแหน่งติดกันแล้วเปรียบเทียบข้อมูลทีละคู่", font=("Angsana New", 16), fg="black", bg="white")
        page1_label2.place(relx=0.5, rely=0.3, anchor="center")
        page1_label3 = Label(page1, text="ทำการสลับตำแหน่งเมื่อพบว่าข้อมูลคู่นั้นไม่เรียงจากน้อยไปมากหรือมากไปน้อยตามที่กำหนด", font=("Angsana New", 16), fg="black", bg="white")
        page1_label3.place(relx=0.5, rely=0.4, anchor="center")
        page1_label4 = Label(page1, text="เมื่อสลับตำแหน่ง เรียบร้อยแล้วจะนำข้อมูลไปจับคู่กับข้อมูลในตำแหน่งถัดไปเพื่อเปรียบเทียบ", font=("Angsana New", 16), fg="black", bg="white")
        page1_label4.place(relx=0.5, rely=0.5, anchor="center")
        page1_label5 = Label(page1, text="เมื่อข้อมูลไม่เรียงลำดับ ตามที่ต้องการก็จะทำการสลับตำแหน่งอีกครั้ง ทำเช่นนี้ไปเรื่อยๆ", font=("Angsana New", 16), fg="black", bg="white")
        page1_label5.place(relx=0.5, rely=0.6, anchor="center")
        page1_label6 = Label(page1, text="จนถึงข้อมูลตำแหน่งสุดท้ายจะได้ ข้อมูลที่มีค่ามากที่สุดหรือน้อยที่สุดวางอยู่ในตำแหน่งสุดท้าย", font=("Angsana New", 16), fg="black", bg="white")
        page1_label6.place(relx=0.5, rely=0.7, anchor="center")
        next_button = tk.Button(page1, text="next>>", command=page_manager.go_to_next_page)
        next_button.place(relx=0.9, rely=0.9, anchor="center")

        page_manager.add_page(page1)
        
        page2 = Frame(windowbs)
        Bubble_label = Label(page2, image=bubble_image2)
        Bubble_label.place(relwidth=1.0, relheight=1.0,)
        previous_button = tk.Button(page2, text="<<prev", command=page_manager.go_to_previous_page)
        previous_button.place(relx=0.1, rely=0.9, anchor="center")
        next_button = tk.Button(page2, text="next>>", command=page_manager.go_to_next_page)
        next_button.place(relx=0.9, rely=0.9, anchor="center")

        page_manager.add_page(page2)

        def show_page4():
            windowbs.geometry("550x350+500+250")  # ปรับขนาดหน้าต่างเป็น 550x350
            page_manager.show_page(3)

        page3 = tk.Frame(windowbs)
        Bubble_label = Label(page3, image=bubble_image3)
        Bubble_label.place(relwidth=1.0, relheight=1.0,)
        nextto4_button = Button(page3, text="nex>>", command=show_page4)
        nextto4_button.place(relx=0.9, rely=0.9, anchor="center")
        previous_button = tk.Button(page3, text="<<prev", command=page_manager.go_to_previous_page)
        previous_button.place(relx=0.1, rely=0.9, anchor="center")

        page_manager.add_page(page3)

        page4 = tk.Frame(windowbs)
        Bubble_label = Label(page4, image=bubble_image5)
        Bubble_label.place(relwidth=1.0, relheight=1.0,)
        input_label = Label(page4, text="Enter numbers separated by spaces:",bg="white")
        input_label.place(relx=0.5, rely=0.3, anchor=CENTER)

        radius1 = StringVar()
        radius1.set("")
        entry1 = Entry(page4, width=10,textvariable=radius1)
        entry1.place(relx=0.4, rely=0.4, anchor=CENTER)
        radius2 = StringVar()
        radius2.set("")
        entry2 = Entry(page4, width=10,textvariable=radius2)
        entry2.place(relx=0.6, rely=0.4, anchor=CENTER)
        radius3 = StringVar()
        radius3.set("")
        entry3 = Entry(page4, width=10,textvariable=radius3)
        entry3.place(relx=0.4, rely=0.5, anchor=CENTER)
        radius4 = StringVar()
        radius4.set("")
        entry4 = Entry(page4, width=10,textvariable=radius4)
        entry4.place(relx=0.6, rely=0.5, anchor=CENTER)

        calculate_button = Button(page4, text="Sort", command=calculate_sort)
        calculate_button.place(relx=0.45, rely=0.6, anchor=CENTER)
        clear_button = Button(page4, text="Clear", command=menuClear)
        clear_button.place(relx=0.55, rely=0.6, anchor=CENTER)

        result_var = StringVar()
        result_label = Label(page4, textvariable=result_var,bg="white")
        result_label.place(relx=0.5, rely=0.7, anchor=CENTER)

        previous_button = tk.Button(page4, text="Exit", command=windowbs.destroy)
        previous_button.place(relx=0.5, rely=0.9, anchor=CENTER)

        page_manager.add_page(page4)
        
        page_manager.show_page(0)
        
        windowbs.mainloop()  
          
    def Insertion_sort():
        windowis = tk.Toplevel()
        windowis.title("Insertion Sort")
        windowis.geometry("650x650+430+60")


        # สร้าง Label สำหรับแสดงเนื้อหา

        class PageManager:
            def __init__(self, root):
                self.root = root
                self.pages = []
                self.current_page_index = -1

            def add_page(self, page):
                self.pages.append(page)

            def show_page(self, page_index):
                if 0 <= page_index < len(self.pages):
                    if self.current_page_index >= 0:
                        self.pages[self.current_page_index].pack_forget()
                    self.pages[page_index].pack(fill="both", expand=True)
                    self.current_page_index = page_index
            def go_to_previous_page(self):
                if self.current_page_index > 0:
                    self.show_page(self.current_page_index - 1)

            def go_to_next_page(self):
                if self.current_page_index < len(self.pages) - 1:
                    self.show_page(self.current_page_index + 1)

        page_manager = PageManager(windowis)

        # สร้างหน้า 1
        page1 = Frame(windowis)
        Insertion_label = Label(page1, image=Insertion_image)
        Insertion_label.place(relwidth=1.0, relheight=1.0,)
        page1_label1 = Label(page1, text="การเรียงข้อมูลแบบแทรก (insertion sort) ", font=("Angsana New", 20, 'bold'), fg="black", bg="white")
        page1_label1.place(relx=0.5, rely=0.1, anchor="center") 
        page1_label2 = Label(page1, text="ทำงานโดยจะแบ่งข้อมูลในรายการเป็นสองส่วนคือส่วนที่เรียงเเล้วและที่ยังไม่เรียง", font=("Angsana New", 17), fg="black", bg="white")
        page1_label2.place(relx=0.5, rely=0.2, anchor="center") 
        page1_label3 = Label(page1, text="เริ่มแรกส่วนที่เรียงแล้วก็จะมีอย่างน้อยหนึ่งตัว และจะเริ่มหยิบข้อมูลตัวหนึ่งของส่วนที่ยังไม่เรียง", font=("Angsana New", 17), fg="black", bg="white")
        page1_label3.place(relx=0.5, rely=0.3, anchor="center") 
        page1_label4 = Label(page1, text="มาเปรียบเทียบเพื่อหาตำแหน่งที่เหมาะสมในการแทรกลงในข้อมูลส่วนที่เรียงแล้ว", font=("Angsana New", 17), fg="black", bg="white")
        page1_label4.place(relx=0.05, rely=0.38, ) 
        page1_label5 = Label(page1, text="หน้า 1")
        page1_label5.place(relx=0.5, rely=0.9, anchor="center")


        page_manager.add_page(page1)

        # สร้างหน้า 2
        page2 = Frame(windowis)
        Insertion_label = Label(page2, image=Insertion_image)
        Insertion_label.place(relwidth=1.0, relheight=1.0,)
        Insertion_label1  = Label(page2, image=Insertion_image_page2_pic1)
        Insertion_label1.place(relx=0.5, rely=0.28, anchor="center")      
        Insertion_label2  = Label(page2, image=Insertion_image_page2_pic2)  
        Insertion_label2.place(relx=0.5, rely=0.45, anchor="center")          
        Insertion_label3  = Label(page2, image=Insertion_image_page2_pic3)
        Insertion_label3.place(relx=0.5, rely=0.68, anchor="center") 
        page2_label1 = Label(page2, text="ตัวอย่าง", font=("Angsana New", 20), fg="black", bg="white")
        page2_label1.place(relx=0.5, rely=0.1, anchor="center")
        page2_label2 = Label(page2, text="รอบที่ 1", font=("Angsana New", 20), fg="black", bg="white")
        page2_label2.place(relx=0.1, rely=0.2, anchor="center")
        page2_label4 = Label(page2, text="ยกตัวอย่างเลขมา4ชุด", font=("Angsana New", 18), fg="black", bg="white")
        page2_label4.place(relx=0.5, rely=0.2, anchor="center")
        page2_label3 = Label(page2, text="ขั้นตัวเลขพื่อตรวจสอบเลขหลังตัวขั้น", font=("Angsana New", 18), fg="black", bg="white")
        page2_label3.place(relx=0.5, rely=0.37, anchor="center")
        page2_label4 = Label(page2, text="ตรวจสอลเลขหลังตัวขั้นว่ามีค่าน้อยกว่าตัวหน้าขั้นหรือไม่", font=("Angsana New", 18), fg="black", bg="white")
        page2_label4.place(relx=0.5, rely=0.53, anchor="center")     
        page2_label4 = Label(page2, text="หากใช่จะย้ายตัวหลังไปยังข้างหน้าตัวขั้นเเต่หากไม่ก็ไม่ต้องทำอะไร", font=("Angsana New", 18), fg="black", bg="white")
        page2_label4.place(relx=0.5, rely=0.60, anchor="center")     
        page2_label6 = Label(page2, text="หน้า 2")
        page2_label6.place(relx=0.5, rely=0.9, anchor="center")
     
        page_manager.add_page(page2)

        # สร้างหน้า 3
        page3 = Frame(windowis)
        Insertion_label = Label(page3, image=Insertion_image)
        Insertion_label.place(relwidth=1.0, relheight=1.0,)
        Insertion_label1  = Label(page3, image=Insertion_image_page3_pic1)
        Insertion_label1.place(relx=0.5, rely=0.28, anchor="center")      
        Insertion_label2  = Label(page3, image=Insertion_image_page3_pic2)  
        Insertion_label2.place(relx=0.5, rely=0.45, anchor="center")          
        Insertion_label3  = Label(page3, image=Insertion_image_page3_pic3)
        Insertion_label3.place(relx=0.5, rely=0.68, anchor="center") 
        page2_label1 = Label(page3, text="ตัวอย่าง", font=("Angsana New", 20), fg="black", bg="white")
        page2_label1.place(relx=0.5, rely=0.1, anchor="center")
        page2_label2 = Label(page3, text="รอบที่ 2", font=("Angsana New", 20), fg="black", bg="white")
        page2_label2.place(relx=0.1, rely=0.2, anchor="center")
        page2_label4 = Label(page3, text="ย้ายตัวขั้นไปยังตำแหน่งต่อไป", font=("Angsana New", 18), fg="black", bg="white")
        page2_label4.place(relx=0.5, rely=0.2, anchor="center")
        page2_label3 = Label(page3, text="ตัวเลขมีค่าน้อยกว่าตัวหน้าขั้นทำการย้ายไปข้างหน้า", font=("Angsana New", 18), fg="black", bg="white")
        page2_label3.place(relx=0.5, rely=0.37, anchor="center")
        page2_label4 = Label(page3, text="ย้ายตัวเลขไปข้างหน้าตัวขั้น", font=("Angsana New", 18), fg="black", bg="white")
        page2_label4.place(relx=0.5, rely=0.53, anchor="center")     
        page2_label4 = Label(page3, text="ตัวเลขตำเเหน่งเดิมมีค่ามากกว่าจึงย้ายไปหลังตัวขั้น", font=("Angsana New", 18), fg="black", bg="white")
        page2_label4.place(relx=0.5, rely=0.60, anchor="center")    
        page2_label6 = Label(page3, text="หน้า 3")
        page2_label6.place(relx=0.5, rely=0.9, anchor="center")
        page_manager.add_page(page3)

        # สร้างหน้า 4
        page4 = Frame(windowis)
        Insertion_label = Label(page4, image=Insertion_image)
        Insertion_label.place(relwidth=1.0, relheight=1.0,)
        Insertion_label1  = Label(page4, image=Insertion_image_page2_pic1)
        Insertion_label1.place(relx=0.5, rely=0.28, anchor="center")      
        Insertion_label2  = Label(page4, image=Insertion_image_page4_pic2)  
        Insertion_label2.place(relx=0.5, rely=0.45, anchor="center")          
        Insertion_label3  = Label(page4, image=Insertion_image_page4_pic3)
        Insertion_label3.place(relx=0.5, rely=0.68, anchor="center") 
        page2_label1 = Label(page4, text="ตัวอย่าง", font=("Angsana New", 20), fg="black", bg="white")
        page2_label1.place(relx=0.5, rely=0.1, anchor="center")
        page2_label2 = Label(page4, text="รอบที่ 3", font=("Angsana New", 20), fg="black", bg="white")
        page2_label2.place(relx=0.1, rely=0.2, anchor="center")
        page2_label4 = Label(page4, text="ย้ายตัวขั้นไปยังตำแหน่งต่อไป", font=("Angsana New", 18), fg="black", bg="white")
        page2_label4.place(relx=0.5, rely=0.2, anchor="center")
        page2_label3 = Label(page4, text="ตัวเลขมีค่าน้อยกว่าตัวหน้าขั้นทำการย้ายไปข้างหน้า", font=("Angsana New", 18), fg="black", bg="white")
        page2_label3.place(relx=0.5, rely=0.37, anchor="center")
        page2_label4 = Label(page4, text="ย้ายตัวเลขไปข้างหน้าตัวขั้น", font=("Angsana New", 18), fg="black", bg="white")
        page2_label4.place(relx=0.5, rely=0.53, anchor="center")     
        page2_label4 = Label(page4, text="ตัวเลขตำเเหน่งเดิมมีค่ามากกว่าจึงย้ายไปหลังตัวขั้น", font=("Angsana New", 18), fg="black", bg="white")
        page2_label4.place(relx=0.5, rely=0.60, anchor="center")    
        page2_label6 = Label(page4, text="หน้า 4")
        page2_label6.place(relx=0.5, rely=0.9, anchor="center")
        page_manager.add_page(page4)

        # สร้างหน้า 5
        page5 = Frame(windowis)
        Insertion_label = Label(page5, image=Insertion_image)
        Insertion_label.place(relwidth=1.0, relheight=1.0,)
        def Num_Check(S):
            if S.isdigit():
                return True
            page5.bell()
            return False

        vcmd = (page5.register(Num_Check), '%S')

        label2 = Label(page5, text="โปรเเกรมตัวอย่าง", font=18, fg="black", bg="white")
        label2.place(relx=0.5, rely=0.05, anchor="center")

        label2 = Label(page5, text="ตำแหน่งที่ 1", font=18, fg="black", bg="white")
        label2.place(relx=0.15, rely=0.12, anchor="center")
        label3 = Label(page5, text="ตำแหน่งที่ 2", font=18, fg="black", bg="white")
        label3.place(relx=0.15, rely=0.22, anchor="center")
        label4 = Label(page5, text="ตำแหน่งที่ 3", font=18, fg="black", bg="white")
        label4.place(relx=0.15, rely=0.32, anchor="center")
        label5 = Label(page5, text="ตำแหน่งที่ 4", font=18, fg="black", bg="white")
        label5.place(relx=0.15, rely=0.42, anchor="center")
        label6 = Label(page5, text="ผลลัพท์", font=18, fg="black", bg="white")
        label6.place(relx=0.15, rely=0.52, anchor="center")

        Position_1_entry = Entry(page5,font=1, validate='key', vcmd=vcmd)
        Position_1_entry.place(relx=0.51, rely=0.12, anchor="center")
        Position_2_entry = Entry(page5,font=1,  validate='key', vcmd=vcmd)
        Position_2_entry.place(relx=0.51, rely=0.22, anchor="center")
        Position_3_entry = Entry(page5,font=1,  validate='key', vcmd=vcmd)
        Position_3_entry.place(relx=0.51, rely=0.32, anchor="center")
        Position_4_entry = Entry(page5,font=1,  validate='key', vcmd=vcmd)
        Position_4_entry.place(relx=0.51, rely=0.42, anchor="center")

        def insertion_sort(arr):
            for i in range(1, len(arr)):
                key = arr[i]
                j = i - 1
                while j >= 0 and key < arr[j]:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key

        def sort_and_display():
            try:
                positions = [int(Position_1_entry.get()), int(Position_2_entry.get()), int(Position_3_entry.get()), int(Position_4_entry.get())]

                # ทำการเรียงลำดับแบบ Insertion Sort
                insertion_sort(positions)

                # แสดงผลลัพธ์ที่เรียงลำดับใน textcircle1
                result.set(positions)
            except ValueError:
                messagebox.showerror(title="error", message="กรุณาป้อนข้อมูลให้ครบถ้วน")
        def menuClear():
            Position_1_entry.delete(0, 'end')
            Position_2_entry.delete(0, 'end')
            Position_3_entry.delete(0, 'end')
            Position_4_entry.delete(0, 'end')
            result.set("")  # เคลียร์ผลลัพธ์ที่แสดง


        # สร้าง Entry widget สำหรับแสดงผลลัพธ์
        result = StringVar()
        textcircle1 = Entry(page5, font=2, bg="#716C6A", textvariable=result)
        textcircle1["state"] = "readonly"
        textcircle1.place(relx=0.51, rely=0.52, anchor="center")

        # สร้างปุ่มสำหรับเรียงข้อมูลและแสดงผล
        sort_button = Button(page5, text="ผลลัพท์",font=1, command=sort_and_display)
        sort_button .place(relx=0.43, rely=0.62, anchor="center")
        btCal1 = Button(page5, text="ยกเลิก", font=1,  command=menuClear)
        btCal1.place(relx=0.55, rely=0.62, anchor="center")

        

        page_manager.add_page(page5)


        previous_button = tk.Button(windowis, text="ย้อนกลับ", command=page_manager.go_to_previous_page)
        next_button = tk.Button(windowis, text="ถัดไป", command=page_manager.go_to_next_page)

        # กำหนดตำแหน่งของปุ่มด้านขวาล่าง
        previous_button.place(relx=0.1, rely=0.9, anchor="center")
        next_button.place(relx=0.9, rely=0.9, anchor="center")

        page_manager.show_page(0)

        windowis.mainloop() 
          

    def Selection_sort():
        windowss = Toplevel()
        windowss.title("Selection Sort")
        windowss.geometry("750x450+380+160")

        selection_label = Label(windowss, image=selectio_image_page1)
        selection_label.place(relwidth=1.0, relheight=1.0)

        
        def Selection_sort(arr):
            for i in range(0, len(arr) - 1):
                cur_min_idx = i
                for j in range(i + 1, len(arr)):
                    if arr[j] < arr[cur_min_idx]:
                        cur_min_idx = j
                arr[i], arr[cur_min_idx] = arr[cur_min_idx], arr[i]  # สลับค่า

        def calculate_sort():
            input_data = input_entry.get()
            try:
                data = [int(x) for x in input_data.split()]
                Selection_sort(data)
                result_label.config(text="Sorted Array: " + " ".join(map(str, data)))
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter numbers separated by spaces.")


        class PageManager:
            def __init__(self, root):
                self.root = root
                self.pages = []
                self.current_page_index = -1

            def add_page(self, page):
                self.pages.append(page)

            def show_page(self, page_index):
                if 0 <= page_index < len(self.pages):
                    if self.current_page_index >= 0:
                        self.pages[self.current_page_index].pack_forget()
                    self.pages[page_index].pack(fill="both", expand=True)
                    self.current_page_index = page_index
            def go_to_previous_page(self):
                if self.current_page_index > 0:
                    self.show_page(self.current_page_index - 1)

            def go_to_next_page(self):
                if self.current_page_index < len(self.pages) - 1:
                    self.show_page(self.current_page_index + 1)
            

        page_manager = PageManager(windowss)

        # สร้างหน้า 1
        page1 = Frame(windowss)
        salculate_label = Label(page1, image=selectio_image_page1)
        salculate_label.place(relwidth=1.0, relheight=1.0,)


        page_manager.add_page(page1)

        # สร้างหน้า 2
        page2 = Frame(windowss)
        salculate_label = Label(page2, image=selectio_image_page2)
        salculate_label.place(relwidth=1.0, relheight=1.0,)

        page_manager.add_page(page2)

        # สร้างหน้า 3
        page3 = Frame(windowss)
        salculate_label = Label(page3, image=selectio_image_page3)
        salculate_label.place(relwidth=1.0, relheight=1.0,)
        page_manager.add_page(page3)

        # สร้างหน้า 4
        page4 = Frame(windowss)
        salculate_label = Label(page4, image=selectio_image_page4)
        salculate_label.place(relwidth=1.0, relheight=1.0,)
        page_manager.add_page(page4)
        
        # สร้างหน้า 5
        page5 = Frame(windowss)
        salculate_label = Label(page5, image=selectio_image_page5)
        salculate_label.place(relwidth=1.0, relheight=1.0,)
        page_manager.add_page(page5)

        # สร้างหน้า 6
        page6 = Frame(windowss)
        salculate_label = Label(page6, image=selectio_image_page6)
        salculate_label.place(relwidth=1.0, relheight=1.0,)

        salculate_label = Label(page6, text="Enter numbers separated by spaces:")
        salculate_label.place(relx=0.5, rely=0.3, anchor="center")

        radius1 = StringVar()
        radius1.set("")
        input_entry = Entry(page6, width=50)
        input_entry.place(relx=0.5, rely=0.4, anchor="center")

        calculate_button = Button(page6, text="Sort",font=1, command=calculate_sort)
        calculate_button.place(relx=0.45, rely=0.5, anchor="center")

        result_label = Label(page6, text="")
        result_label.place(relx=0.4, rely=0.6, anchor="center")

        def menuClear():
            result_label.destroy()
            input_entry.delete(0, 'end')

        page_manager.add_page(page6)


        btCal1 = Button(page6, text="Clear", font=1,  command=menuClear)
        btCal1.place(relx=0.55, rely=0.5, anchor="center")
        previous_button = tk.Button(windowss, text="ย้อนกลับ", command=page_manager.go_to_previous_page)
        next_button = tk.Button(windowss, text="ถัดไป", command=page_manager.go_to_next_page)

        # กำหนดตำแหน่งของปุ่มด้านขวาล่าง
        previous_button.place(relx=0.1, rely=0.9, anchor="center")
        next_button.place(relx=0.9, rely=0.9, anchor="center")


        page_manager.show_page(0)

        windowss.mainloop()

        
    def Merge_sort():
        windowms = Toplevel()
        windowms.title("Merge Sort")
        windowms.geometry("750x450+380+160")
        windowms.configure(background="white")

        sorting_label = Label(windowms, image=merge_image1)
        sorting_label.place(relwidth=1.0, relheight=1.0)

        def merge_sort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2
                left_half = arr[:mid]
                right_half = arr[mid:]

                merge_sort(left_half)
                merge_sort(right_half)

                i = j = k = 0
                while i < len(left_half) and j < len(right_half):
                    if left_half[i] < right_half[j]:
                        arr[k] = left_half[i]
                        i += 1
                    else:
                        arr[k] = right_half[j]
                        j += 1
                    k += 1

                while i < len(left_half):
                    arr[k] = left_half[i]
                    i += 1
                    k += 1

                while j < len(right_half):
                    arr[k] = right_half[j]
                    j += 1
                    k += 1

        def sort_button_clicked():
            input_text = input_entry.get()
            try:
                input_list = list(map(int, input_text.split()))
                merge_sort(input_list)
                result_label.config(text="รายการที่เรียงลำดับคือ: " + ' '.join(map(str, input_list)))
            except ValueError:
                result_label.config(text="โปรดป้อนรายการตัวเลขที่ถูกต้อง")
        class PageManager:
            def __init__(self, root):
                self.root = root
                self.pages = []
                self.current_page_index = -1

            def add_page(self, page):
                self.pages.append(page)

            def show_page(self, page_index):
                if 0 <= page_index < len(self.pages):
                    if self.current_page_index >= 0:
                        self.pages[self.current_page_index].pack_forget()
                    self.pages[page_index].pack(fill="both", expand=True)
                    self.current_page_index = page_index
            def go_to_previous_page(self):
                if self.current_page_index > 0:
                    self.show_page(self.current_page_index - 1)

            def go_to_next_page(self):
                if self.current_page_index < len(self.pages) - 1:
                    self.show_page(self.current_page_index + 1)
            

        page_manager = PageManager(windowms)


        page1 = Frame(windowms)
        Merge_label1 = Label(page1, image=merge_image1)
        Merge_label1.place(relwidth=1.0, relheight=1.0,)


        page_manager.add_page(page1)

        page2 = Frame(windowms)
        Merge_label2 = Label(page2, image=merge_image2)
        Merge_label2.place(relwidth=1.0, relheight=1.0,)

        page_manager.add_page(page2)

        page3 = Frame(windowms)
        Merge_label3 = Label(page3, image=merge_image3)
        Merge_label3.place(relwidth=1.0, relheight=1.0,)
        page_manager.add_page(page3)
        def menuClear():
            input_entry.delete(0, 'end')
            result_label.config(text="")

        page4 = Frame(windowms)
        Merge_label3 = Label(page4, image=merge_image4)
        Merge_label3.place(relwidth=1.0, relheight=1.0,)
        input_label = ttk.Label(page4, text="ป้อนรายการตัวเลข (คั่นด้วยช่องว่าง):")
        input_label.place(relx=0.5, rely=0.3, anchor=CENTER)
        input_entry = ttk.Entry(page4, width=30)
        input_entry.place(relx=0.5, rely=0.4, anchor=CENTER)
        sort_button = ttk.Button(page4, text="Sort", command=sort_button_clicked)
        sort_button.place(relx=0.40, rely=0.5, anchor=CENTER)
        result_label = ttk.Label(page4, text="")
        result_label.place(relx=0.5, rely=0.6, anchor=CENTER)
        clear_button = ttk.Button(page4, text="Clear",command=menuClear)
        clear_button.place(relx=0.60, rely=0.5, anchor=CENTER)
        page_manager.add_page(page4)

        previous_button = tk.Button(windowms, text="ย้อนกลับ", command=page_manager.go_to_previous_page)
        next_button = tk.Button(windowms, text="ถัดไป", command=page_manager.go_to_next_page)
        previous_button.place(relx=0.1, rely=0.9, anchor="center")
        next_button.place(relx=0.9, rely=0.9, anchor="center")
        
    
        page_manager.show_page(0)

        windowms.mainloop()

    btCal1 = ttk.Button(windowst, text="แบบฟองสบู่ Bubble Sort", style="Custom.TButton", command=Bubble_sort)
    btCal1.place(relx=0.5, rely=0.3, anchor=CENTER)

    btCal2 = ttk.Button(windowst, text="แบบแทรก Insertion Sort", style="Custom.TButton", command=Insertion_sort)
    btCal2.place(relx=0.5, rely=0.4, anchor=CENTER)

    btCal3 = ttk.Button(windowst, text="แบบเลือก Selection Sort", style="Custom.TButton", command=Selection_sort)
    btCal3.place(relx=0.5, rely=0.5, anchor=CENTER)

    btCal4 = ttk.Button(windowst, text="แบบรวม Merge Sort", style="Custom.TButton", command=Merge_sort)
    btCal4.place(relx=0.5, rely=0.6, anchor=CENTER)
    
    btCal5 = ttk.Button(windowst, text="ย้อนกลับ ", style="Custom.TButton", command=windowst.destroy)
    btCal5.place(relx=0.5, rely=0.7, anchor=CENTER)

    sorting_menu = Menu(windowst)
    sorting_menu.add_command(label="หน้าแรก")  # Placeholder function
    windowst.config(menu=sorting_menu)
    
    
    windowst.mainloop()
    

def Searching():
    windowsearch = Toplevel()
    windowsearch.title("searching")
    windowsearch.geometry("650x650+430+60")

    index_label = Label(windowsearch, image=index_image)
    index_label.pack(expand=YES)

    def Sequential_Search_ui():
            windowseq = tk.Toplevel()
            windowseq.title("Sequential_Search")
            windowseq.geometry("750x450+380+160")
            class PageManager:
                def __init__(self, root):
                    self.root = root
                    self.pages = []
                    self.current_page_index = -1

                def add_page(self, page):
                    self.pages.append(page)

                def show_page(self, page_index):
                    if 0 <= page_index < len(self.pages):
                        if self.current_page_index >= 0:
                            self.pages[self.current_page_index].pack_forget()
                        self.pages[page_index].pack(fill="both", expand=True)
                        self.current_page_index = page_index
                def go_to_previous_page(self):
                    if self.current_page_index > 0:
                        self.show_page(self.current_page_index - 1)

                def go_to_next_page(self):
                    if self.current_page_index < len(self.pages) - 1:
                        self.show_page(self.current_page_index + 1)

            page_manager = PageManager(windowseq)

    # สร้างหน้า 1
            page1 = Frame(windowseq)
            Sequential_label = Label(page1, image=searching_seq1)
            Sequential_label.place(relwidth=1.0, relheight=1.0,)
            page1_label5 = Label(page1, text="หน้า 1")
            page1_label5.place(relx=0.5, rely=0.9, anchor="center")


            page_manager.add_page(page1)

            # สร้างหน้า 2
            page2 = Frame(windowseq)
            Sequential_label = Label(page2, image=searching_seq2)
            Sequential_label.place(relwidth=1.0, relheight=1.0,)    
            page2_label6 = Label(page2, text="หน้า 2")
            page2_label6.place(relx=0.5, rely=0.9, anchor="center")
        
            page_manager.add_page(page2)

            # สร้างหน้า 3
            page3 = Frame(windowseq)
            Sequential_label = Label(page3, image=searching_seq3)
            Sequential_label.place(relwidth=1.0, relheight=1.0,)    
            page2_label6 = Label(page3, text="หน้า 3")
            page2_label6.place(relx=0.5, rely=0.9, anchor="center")
            page_manager.add_page(page3)

        # สร้างหน้า 4
            page4 = Frame(windowseq)
            Sequential_label_label = Label(page4, image=searching_seq4)
            Sequential_label_label.place(relwidth=1.0, relheight=1.0)

            def MoneyValidation(S):
                if S.isdigit() or S == "":
                    return True
                page4.bell()
                return False

            vcmd = (page4.register(MoneyValidation), '%S')

            def sequential_search(data, target):
                for index, item in enumerate(data):
                    if item == target:
                        return index
                return -1

            def validate_input(P):
                if P.isdigit() or P == "":
                    return True
                return False

            result_entry = StringVar()

            textcircle1 = Entry(page4, font=2, bg="#716C6A", textvariable=result_entry)
            textcircle1["state"] = "readonly"
            textcircle1.place(relx=0.5, rely=0.43, anchor="center")

            def sort_and_display():
                try:
                    target = int(Position_1_entry.get())
                    result = sequential_search(data, target)
                    if result != -1:
                        result_entry.set(f"ค้นเจอที่ Index {result}")
                    else:
                        result_entry.set("ไม่พบข้อมูล")
                except ValueError:
                    messagebox.showerror(title="error", message="กรุณาป้อนข้อมูลให้ครบถ้วน")



            data = [4, 5, 6, 7, 8, 9, 10, 15, 25]

            Position_1_entry = Entry(page4, font=2, validate='key', vcmd=vcmd)
            Position_1_entry.place(relx=0.5, rely=0.33, anchor=CENTER)

            # เพิ่มปุ่มยกเลิก
            def menuClear():
                Position_1_entry.delete(0, 'end')
                result_entry.set("")  

            # เพิ่มปุ่มค้นหา
            search_button = Button(page4, text="ค้นหา", font=1, command=sort_and_display)
            search_button.place(relx=0.43, rely=0.52, anchor=CENTER)
            btCal1 = Button(page4, text="ยกเลิก", font=1, command=menuClear)
            btCal1.place(relx=0.55, rely=0.52, anchor=CENTER)

            page_manager.add_page(page4)



            previous_button = tk.Button(windowseq, text="ย้อนกลับ", command=page_manager.go_to_previous_page)
            next_button = tk.Button(windowseq, text="ถัดไป", command=page_manager.go_to_next_page)

            # กำหนดตำแหน่งของปุ่มด้านขวาล่าง
            previous_button.place(relx=0.1, rely=0.9, anchor="center")
            next_button.place(relx=0.9, rely=0.9, anchor="center")

            page_manager.show_page(0)



        
            windowseq.mainloop()


    def Binary_Search():
        windowBs = Toplevel()
        windowBs.title("Binary Search")
        windowBs.geometry("750x450+380+160")
        windowBs.configure(background="white")

        def binary_search(arr, target):
            left, right = 0, len(arr) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return False

        def search_button_click():
            target_value = int(entry.get())
            result = binary_search(my_list, target_value)
            if result:
                result_label.config(text=f"ค่า {target_value} อยู่ในลิสต์")
            else:
                result_label.config(text=f"ค่า {target_value} ไม่อยู่ในลิสต์")

        # ตัวอย่างการใช้งาน
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        class PageManager:
            def __init__(self, root):
                self.root = root
                self.pages = []
                self.current_page_index = -1

            def add_page(self, page):
                self.pages.append(page)

            def show_page(self, page_index):
                if 0 <= page_index < len(self.pages):
                    if self.current_page_index >= 0:
                        self.pages[self.current_page_index].pack_forget()
                    self.pages[page_index].pack(fill="both", expand=True)
                    self.current_page_index = page_index
            def go_to_previous_page(self):
                if self.current_page_index > 0:
                    self.show_page(self.current_page_index - 1)

            def go_to_next_page(self):
                if self.current_page_index < len(self.pages) - 1:
                    self.show_page(self.current_page_index + 1)

        page_manager = PageManager(windowBs)

        # สร้างหน้า 1
        page1 = Frame(windowBs)
        Insertion_label = Label(page1, image=Binary_page1)
        Insertion_label.place(relwidth=1.0, relheight=1.0,)
        page_manager.add_page(page1)

        # สร้างหน้า 2
        page2 = Frame(windowBs)
        Insertion_label = Label(page2, image=Binary_page2)
        Insertion_label.place(relwidth=1.0, relheight=1.0,)
     
        page_manager.add_page(page2)

        # สร้างหน้า 3
       
        page3 = Frame(windowBs)
        Insertion_label = Label(page3, image=Binary_page3)
        Insertion_label.place(relwidth=1.0, relheight=1.0,)
        entry_label = tk.Label(page3, text="ป้อนค่าที่ต้องการค้นหา:")
        entry_label.place(relx=0.5, rely=0.3, anchor=CENTER)

        entry = tk.Entry(page3)
        entry.place(relx=0.5, rely=0.4, anchor=CENTER)
        def menuClear():
            entry.delete(0, 'end')
            result_label.destroy() 
        search_button = tk.Button(page3, text="ค้นหา", command=search_button_click)
        search_button.place(relx=0.45, rely=0.55, anchor=CENTER)

        result_label = tk.Label(page3, text="")
        result_label.place(relx=0.5, rely=0.7, anchor=CENTER)

        clear_button = tk.Button(page3, text="ยกเลิก", command=menuClear)
        clear_button.place(relx=0.55, rely=0.55, anchor=CENTER)

        page_manager.add_page(page3)

        previous_button = tk.Button(windowBs, text="ย้อนกลับ", command=page_manager.go_to_previous_page)
        next_button = tk.Button(windowBs, text="ถัดไป", command=page_manager.go_to_next_page)

        # กำหนดตำแหน่งของปุ่มด้านขวาล่าง
        previous_button.place(relx=0.2, rely=0.9, anchor="center")
        next_button.place(relx=0.8, rely=0.9, anchor="center")

        page_manager.show_page(0)
    
        windowBs.mainloop() 
          
        def numonly(S):
            if S.isdigit():
                return True
            windowBs.bell()
            return False
        vcmd = (windowBs.register(numonly), '%S')
        numbox = Entry(windowBs, bg='gray', validate='key', vcmd=vcmd)
        numbox.pack()
        windowBs.mainloop()
        label1=Label(windowBs,text="โปรเเกรมอธิบายและสาธิตการทำงาน",font=20,fg="black",bg="#c7c7c7") 
        label1.grid(row=0,column=0,columnspan=5,padx=110,pady=20)

    btCal1 = ttk.Button(windowsearch, text="Sequential Search", style="Custom.TButton",command=Sequential_Search_ui )
    btCal1.place(relx=0.5, rely=0.4, anchor=CENTER)
    btCal2 = ttk.Button(windowsearch, text="Binary Search", style="Custom.TButton",command=Binary_Search )
    btCal2.place(relx=0.5, rely=0.5, anchor=CENTER)
    btCal3 = ttk.Button(windowsearch, text="ย้อนกลับ ", style="Custom.TButton",command=windowsearch.destroy)
    btCal3.place(relx=0.5, rely=0.6, anchor=CENTER)

def menuInfo():
    windowInfo = Toplevel()
    windowInfo.title("sorting")
    windowInfo.geometry("1372x773+80+20")

    developer_label = Label(windowInfo, image=developer)
    developer_label.place(relwidth=1.0, relheight=1.0)

    windowInfo.mainloop()

def index():
    window.mainloop()



btCal1 = ttk.Button(window, text="การเรียงลำดับข้อมูล (Sorting)", style="Custom.TButton", command=Sorting)
btCal1.place(relx=0.5, rely=0.4, anchor=CENTER)
btCal2 = ttk.Button(window, text="การค้นหาข้อมูล (Searching)", style="Custom.TButton", command=Searching)
btCal2.place(relx=0.5, rely=0.5, anchor=CENTER)

btCal3 = ttk.Button(window, text="ผู้จัดทำ", style="Custom.TButton", command=menuInfo)
btCal3.place(relx=0.5, rely=0.6, anchor=CENTER)
btCal4 = ttk.Button(window, text="ออก", style="Custom.TButton", command=menuExit)
btCal4.place(relx=0.5, rely=0.7, anchor=CENTER)

window.mainloop()