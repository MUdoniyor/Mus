# Import the tkinter library and the cvd_predictor function from the cvd_model module
import tkinter as tk
from cvd_model import *


# Define a class called CVD_GUI for the credit card approval predictor application
class CVD_GUI:
    def __init__(self):

        # Create the main window for the GUI
        self.main_window = tk.Tk()
        self.main_window.title("CREDIT CARD APPROVAL PREDICTOR")

        # Create 17 frames to group widgets
        self.one_frame = tk.Frame()
        self.two_frame = tk.Frame()
        self.three_frame = tk.Frame()
        self.four_frame = tk.Frame()
        self.five_frame = tk.Frame()
        self.six_frame = tk.Frame()
        self.seven_frame = tk.Frame()
        self.eight_frame = tk.Frame()
        self.nine_frame = tk.Frame()
        self.ten_frame = tk.Frame()
        self.eleven_frame = tk.Frame()
        self.twelve_frame = tk.Frame()
        self.thirteen_frame = tk.Frame()
        self.fourteen_frame = tk.Frame()
        self.fifteen_frame = tk.Frame()
        self.sixteen_frame = tk.Frame()
        self.seventeen_frame = tk.Frame()


        # Create the widgets for one frame. (Title display)
        self.title_label = tk.Label(self.one_frame, text='CREDIT CARD APPROVAL PREDICTOR',fg="green", font=("Helvetica", 18, 'bold'))
        self.title_label.pack()


        # Create the widgets for two frame. (Gender input)
        self.gender_label = tk.Label(self.two_frame, text='Gender:')
        self.click_gender_var = tk.StringVar()
        self.click_gender_var.set("Male")
        self.gender_inp = tk.OptionMenu(self.two_frame,self.click_gender_var, "Male", "Female")
        self.gender_label.pack(side='left')
        self.gender_inp.pack(side='left')


        # Create the widgets for three frame. (Age input)
        self.age_label = tk.Label(self.three_frame, text='Age:')
        self.age_entry = tk.Entry(self.three_frame, bg="white", fg="black", width = 10)
        #self.age_entry.insert(0,'50')
        self.age_label.pack(side='left')
        self.age_entry.pack(side='left')


        # Create the widgets for four frame. (Debt input)
        self.debt_label = tk.Label(self.four_frame, text='Debt:')
        self.debt_entry = tk.Entry(self.four_frame, bg="white", fg="black")
        #self.debt_entry.insert(0,'150')
        self.debt_label.pack(side='left')
        self.debt_entry.pack(side='left')


        # Create the widgets for five frame. (Married input)
        self.married_label = tk.Label(self.five_frame, text='Married:')
        self.click_married_var = tk.StringVar()
        self.click_married_var.set("Single/Divorced/etc")
        self.married_inp = tk.OptionMenu(self.five_frame, self.click_married_var, "Single/Divorced/etc", "Married")
        self.married_label.pack(side='left')
        self.married_inp.pack(side='left')

        
        # Create the widgets for six frame. (Bank Customer input)
        self.bank_customer_label = tk.Label(self.six_frame, text='Bank Customer:')
        self.click_bank_customer_var = tk.StringVar()
        self.click_bank_customer_var.set("does not have a bank account")
        self.bank_customer_inp = tk.OptionMenu(self.six_frame, self.click_bank_customer_var, "does not have a bank account", "has a bank account")
        self.bank_customer_label.pack(side='left')
        self.bank_customer_inp.pack(side='left')


        # Create the widgets for seven frame. (Industry  input)
        self.industry_label = tk.Label(self.seven_frame, text='Industry:')
        self.click_industry_var = tk.StringVar()
        self.click_industry_var.set("Energy")
        self.industry_inp = tk.OptionMenu(self.seven_frame, self.click_industry_var,"Energy", "Materials", "Industrials", "Consumer Discretionary", "Consumer Staples", "Other")
        self.industry_label.pack(side='left')
        self.industry_inp.pack(side='left')


        # Create the widgets for eight frame. (Ethnicity  input)
        self.ethnicity_label = tk.Label(self.eight_frame, text='Ethnicity:')
        self.click_ethnicity_var = tk.StringVar()
        self.click_ethnicity_var.set("White")
        self.ethnicity_inp = tk.OptionMenu(self.eight_frame, self.click_ethnicity_var,"White", "Black", "Asian", "Latino", "Other")
        self.ethnicity_label.pack(side='left')
        self.ethnicity_inp.pack(side='left')


        # Create the widgets for nine frame. (Years Employed input)
        self.years_employed_label = tk.Label(self.nine_frame, text='Years Employed:')
        self.years_employed_entry = tk.Entry(self.nine_frame, bg="white", fg="black")
        #self.years_employed_entry.insert(0,'100')
        self.years_employed_label.pack(side='left')
        self.years_employed_entry.pack(side='left')


        # Create the widgets for ten frame. (Prior default input)
        self.prior_default_label = tk.Label(self.ten_frame, text='Prior default:')
        self.click_prior_default_var = tk.StringVar()
        self.click_prior_default_var.set("No")
        self.prior_default_inp = tk.OptionMenu(self.ten_frame, self.click_prior_default_var, "No", "Yes")
        self.prior_default_label.pack(side='left')
        self.prior_default_inp.pack(side='left')


        # Create the widgets for eleven frame. (Employed  input)
        self.employed_label = tk.Label(self.eleven_frame, text='Employed:')
        self.click_employed_var = tk.StringVar()
        self.click_employed_var.set("No")
        self.employed_inp = tk.OptionMenu(self.eleven_frame, self.click_employed_var, "No", "Yes")
        self.employed_label.pack(side='left')
        self.employed_inp.pack(side='left')


        # Create the widgets for twelve frame. (Credit Score input)
        self.credit_score_label = tk.Label(self.twelve_frame, text='Credit Score:')
        self.credit_score_entry = tk.Entry(self.twelve_frame, bg="white", fg="black")
        #self.credit_score_entry.insert(0,'100')
        self.credit_score_label.pack(side='left')
        self.credit_score_entry.pack(side='left')


        # Create the widgets for thirteen frame. (Drivers license input)
        self.drivers_license_label = tk.Label(self.thirteen_frame, text='Drivers license:')
        self.click_drivers_license_var = tk.StringVar()
        self.click_drivers_license_var.set("No")
        self.drivers_license_inp = tk.OptionMenu(self.thirteen_frame, self.click_drivers_license_var, "No", "Yes")
        self.drivers_license_label.pack(side='left')
        self.drivers_license_inp.pack(side='left')


        # Create the widgets for fourteen frame. (Citizen input)
        self.citizen_label = tk.Label(self.fourteen_frame, text='Citizen:')
        self.click_citizen_var = tk.StringVar()
        self.click_citizen_var.set("By birth")
        self.citizen_inp = tk.OptionMenu(self.fourteen_frame, self.click_citizen_var, "By birth", "By other means")
        self.citizen_label.pack(side='left')
        self.citizen_inp.pack(side='left')


        # Create the widgets for fifteen frame. (Zip Code input)
        self.zip_code_label = tk.Label(self.fifteen_frame, text='Zip Code:')
        self.zip_code_entry = tk.Entry(self.fifteen_frame, bg="white", fg="black")
        #self.zip_code_entry.insert(0,'100')
        self.zip_code_label.pack(side='left')
        self.zip_code_entry.pack(side='left')


        # Create the widgets for sixteen frame. (Income input)
        self.income_label = tk.Label(self.sixteen_frame, text='Income:')
        self.income_entry = tk.Entry(self.sixteen_frame, bg="white", fg="black")
        #self.income_entry.insert(0,'100')
        self.income_label.pack(side='left')
        self.income_entry.pack(side='left')



        #Create the widgets for seventeen frame = cca (Prediction of Credit Card Approval)
        self.cca_predict_ta = tk.Text(self.seventeen_frame,height = 10, width = 25,bg= 'light blue')

        #Create predict button and quit button
        self.btn_predict = tk.Button(self.seventeen_frame, text='Predict Credit Card Approval', command=self.predict_cca)
        self.btn_quit = tk.Button(self.seventeen_frame, text='Quit', command=self.main_window.destroy)


        self.cca_predict_ta.pack(side='left')
        self.btn_predict.pack()
        self.btn_quit.pack()

        # Pack the frames.
        self.one_frame.pack()
        self.two_frame.pack()
        self.three_frame.pack()
        self.four_frame.pack()
        self.five_frame.pack()
        self.six_frame.pack()
        self.seven_frame.pack()
        self.eight_frame.pack()
        self.nine_frame.pack()
        self.ten_frame.pack()
        self.eleven_frame.pack()
        self.twelve_frame.pack()
        self.thirteen_frame.pack()
        self.fourteen_frame.pack()
        self.fifteen_frame.pack()
        self.sixteen_frame.pack()
        self.seventeen_frame.pack()


        # Enter the tkinter main loop.
        tk.mainloop()

    def predict_cca(self):
        result_string = ""

        self.cca_predict_ta.delete(0.0, tk.END)

        creditor_gender = self.click_gender_var.get()
        if(creditor_gender == "Male"):
            creditor_gender = 1
        else:
            creditor_gender = 0

        creditor_age = self.age_entry.get()
        creditor_debt = self.debt_entry.get()

        creditor_married = self.click_married_var.get()
        if(creditor_married == "Single/Divorced/etc"):
            creditor_married = 0
        else:
            creditor_married = 1

        creditor_bank_customer = self.click_bank_customer_var.get()
        if(creditor_bank_customer == "does not have a bank account"):
            creditor_bank_customer = 0
        else:
            creditor_bank_customer = 1

        creditor_industry = self.click_industry_var.get()
        if(creditor_industry == "Energy"):
            creditor_industry = 0
        elif(creditor_industry == "Materials"):
            creditor_industry = 1
        elif(creditor_industry == "Industrials"):
            creditor_industry = 2
        elif(creditor_industry == "Consumer Discretionary"):
            creditor_industry = 3
        else:
            creditor_industry = 4

        creditor_ethnicity = self.click_ethnicity_var.get()
        if(creditor_ethnicity == "White"):
            creditor_ethnicity = 0
        elif(creditor_ethnicity == "Black"):
            creditor_ethnicity = 1
        elif(creditor_ethnicity == "Asian"):
            creditor_ethnicity = 2
        elif(creditor_ethnicity == "Latino"):
            creditor_ethnicity = 3
        else:
            creditor_ethnicity = 4


        creditor_years_employed = self.years_employed_entry.get()

        creditor_prior_default = self.click_prior_default_var.get()
        if(creditor_prior_default == "Yes"):
            creditor_prior_default = 1
        else:
            creditor_prior_default = 0

        creditor_employed = self.click_employed_var.get()
        if(creditor_employed == "Yes"):
            creditor_employed = 1
        else:
            creditor_employed = 0

        creditor_credit_score = self.credit_score_entry.get()

        creditor_drivers_license = self.click_drivers_license_var.get()
        if(creditor_drivers_license == "Yes"):
            creditor_drivers_license = 1
        else:
            creditor_drivers_license = 0

        creditor_citizen = self.click_citizen_var.get()
        if(creditor_citizen == "By birth"):
            creditor_citizen = 1
        else:
            creditor_citizen = 0

        creditor_zip_code = self.zip_code_entry.get()
        creditor_income = self.income_entry.get()




        result_string += "===creditor Diagnosis=== \n"
        creditor_info = (creditor_gender,creditor_age,creditor_debt,creditor_married,creditor_bank_customer, creditor_industry, creditor_ethnicity,creditor_years_employed,creditor_prior_default, creditor_employed, creditor_credit_score, creditor_drivers_license, creditor_citizen, creditor_zip_code, creditor_income)


        cca_prediction =  best_model.predict([creditor_info])
        disp_string = ("This prediction has an accuracy of:", str(model_accuracy))

        result = cca_prediction

        if(cca_prediction == [0]):
            result_string = (disp_string, '\n', "0 - Your credit card is not approved")
        else:
            result_string = (disp_string, '\n'+ "1 - Your credit card is approved")
        self.cca_predict_ta.insert('1.0',result_string)

        # Predicted:  1 Actual:  1 Data:  (1, 30, 0, 1, 1, 2, 0, 1, 1, 1, 1, 0, 0, 202, 0)
        # Predicted:  0 Actual:  0 Data:  (1, 21, 10, 0, 0, 5, 1, 1, 0, 0, 0, 0, 0, 260, 0)



my_cvd_GUI = CVD_GUI()

