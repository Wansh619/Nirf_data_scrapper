import os 
import csv
import pandas as pd
import re
def saction_table_generator(
        pdf_content,
        start,
        end,
        path
        ):
    write =False
    content= pdf_content.split('\n')
    lines=[]
    dict_df={}
    for i in content:
        if i== start:
            write =True
        if i==end:
            break
        if write:
            lines.append(i)
            # print(i)
    # now since string collected then datacreation
    
    row_1=lines[0].split(' ')
    acadmic_pgrm_header=row_1[0]+" "+row_1[1]
    
    dict_df[acadmic_pgrm_header]= row_1[2:]
    other_rows=lines[1:]
    for row in other_rows:
        
        try:
            pgrm,values =row.split('] ')
            pgrm=pgrm+']'
            values=values.split(' ')
        except:
            splits=row.split(' ')
            pgrm,values =splits[0] ,splits[1:]
        dict_df[pgrm]=values

    df=pd.DataFrame(dict_df)
    df=df.set_index(acadmic_pgrm_header).T
    # print(df)
    # print(df.index)
    df.to_csv(path,index=True,index_label=acadmic_pgrm_header)
    return df.index
            

def total_actual_ss_generator(pdf_content,start,end, path, columns,prgm_list):
    write =False
    content= pdf_content.split('\n')
    dict_df={}
    lines=[]
    for i in content :
        if i==end:
            break
        if  i == start:
            write=True
            continue
        if write:
            lines.append(i)
    lines= lines[::2]
    # print(lines)
    # now since string collected then datacreation
    dict_df[columns[0]]=columns[1:]
    other_cols=lines
    # print(prgm_list)
    for idx,row in enumerate(lines) :
        # print(f"{idx}--------------->",row)
        if row != 'Program(s)]':
            try:
                _,values=row.split('Years ')
                values=values.split(' ')
            except:
                try:
                    _,values=row.split('Year ')
                    values=values.split(' ')
                except:
                    # print("================>",row.split(' '))
                    values=row.split(' ')
                    values=values[1:]
                    # print("================>",)
                    

            dict_df[prgm_list[idx]]=values
    
    df=pd.DataFrame(dict_df)
    index_header=df.columns[0]
    df=df.set_index(index_header).T
    # print(df)
    # print(df.index)
    df.to_csv(path,index=True,index_label=index_header)

    # print(df)


def number_of_faculty_members(pdf_content):
    content=pdf_content.split('\n')
    data=content[-1].split(' ')
    return data[-1]

# start:["Financial Year", "2021-22", "2020-21", "2019-20"]
def find_numbers(string):
    pattern = r'\d+'
    numbers = re.findall(pattern, string)
    return numbers


def financial_table_extractor(pdf_content, path):
    columns=["Financial Year", "2021-22", "2020-21", "2019-20"]
    finance_fields=[
        'Library ( Books, Journals and e-Resources only)',
        'New Equipment and software for Laboratories',
        'Engineering Workshops',
        'Other expenditure on creation of Capital Assets',
        'Salaries (Teaching and Non Teaching staff)',
        'Maintenance of Academic Infrastructure or consumables and',
        'Seminars/Conferences/Workshops'

    ]

    id=0
    content=pdf_content.split('\n')
    # print(content)
    data=[]
    for line in content:
        if id== len(finance_fields):
            break
        if  finance_fields[id] in  line:
            # print(line)
            numbers=find_numbers(line)
            data.append(numbers)
            # print(numbers)
            id=id+1

    # print(len(finance_fields),len(data))
    dict_db={}
    dict_db[columns[0]]=columns[1:]
    for idx, col in enumerate(finance_fields):
        dict_db[col]=data[idx]
    



    df=pd.DataFrame(dict_db)
    # for idx,i in enumerate(columns):
    #     if idx ==0:
    #         dict_db[i]=finance_fields
    index_header=df.columns[0]
    
    df=df.set_index(index_header).T    
    df.to_csv(path,index=True,index_label=index_header)
    # print(df)
        





def phd_student_extraction(pdf_content,start,path):
    content=pdf_content.split('\n')
    id=0
    for i in content:
        if start in i:
            break
        id+=1

    # print(f"""
    #       ============================
    #       {content[id]}
    #       =================
          
    #       """)

    dict_db={
        'Full Time':find_numbers(content[id+2]),
        'Part Time':find_numbers(content[id+3]),

    }
    # print(dict_db)
    df=pd.DataFrame(dict_db)
    # for idx,i in enumerate(columns):
    #     if idx ==0:
    #         dict_db[i]=finance_fields
    # print(df)
    df.to_csv(path,index=False)
        




if __name__=='__main__':
    with open('text2.txt','rb') as file:
        lines=file.read()
    decoded_string = lines.decode('utf-16le')
    # print(lines)
    









