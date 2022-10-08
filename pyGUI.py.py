import PySimpleGUI as sg
import pandas as pd

sg.theme('Dark Amber')

EXCEL_FILE='patient_records.xlsx'
df=pd.read_excel(EXCEL_FILE)

layout=[
    [sg.Text('please fill out the following fields: ')],
    [sg.Text('Name',size=(15,1)),sg.InputText(key='Name')],
    [sg.Text('Address',size=(15,1)),sg.InputText(key='Address')],
    [sg.Text('Gender',size=(15,1)),
                          sg.Checkbox('Male',key='MALE'),
                          sg.Checkbox('Female',key='FEMALE'),
                          sg.Checkbox('Others',key='OTHERS')],
    [sg.Text('No of Reports', size=(15,1)), sg.Spin([i for i in range(0,6)], initial_value=0, key='Reports')],                                               
    [sg.Submit(),sg.Button('Clear'),sg.Exit()]

]

window=sg.Window("Patient's data entry form", layout)

def clear_input():
    for key in values:
        window[key]('')
    return None

while True:
    event, values=window.read()
    if event == sg.WIN_CLOSED or event =='Exit':
        break
    if event =='Clear':
        clear_input()
    if event =='Submit':
        #print(event, values)
        df=df.append(values, ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Data saved!')
        clear_input()
window.close()