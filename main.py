from bs4 import BeautifulSoup
import requests
from data_generator import *
from pdf_extraction import pdf_extraction
import os
import json
# from image_text_extractor import text_extractor
from tqdm import tqdm
from final_dataframe import FINAL_DATAFRAME_DICT

def creating_required_directories(clg_dir_name,output_dir):

    clg_dir_path=os.path.join(output_dir,clg_dir_name)
    clg_pdf_folder_path=os.path.join(clg_dir_path,'pdf')
    sanctioned_intake_folder=os.path.join(clg_dir_path,'sanctioned_intake')
    total_actual_ss_folder=os.path.join(clg_dir_path,'total_actual_ss')
    expenditure_folder=os.path.join(clg_dir_path,'expenditure')
    phd_student_folder=os.path.join(clg_dir_path,'phd_student')
    image_dir= os.path.join(clg_dir_path,'parm_image')
    if not os.path.exists(clg_dir_path):
        os.mkdir(clg_dir_path)
        os.mkdir(clg_pdf_folder_path)
        os.mkdir(sanctioned_intake_folder)
        os.mkdir(total_actual_ss_folder)
        os.mkdir(expenditure_folder)
        os.mkdir(phd_student_folder)
        os.mkdir(image_dir)
    else:
        print("DIR EXISIS --------------------------------------------------")


    clg_pdf_path=os.path.join(clg_pdf_folder_path,'data.pdf')
    clg_json_file_path= os.path.join(clg_dir_path,'clg_data.json')
    sanctioned_intake_table=os.path.join(sanctioned_intake_folder,'sanctioned_intake.csv')
    total_actual_ss_table=os.path.join(total_actual_ss_folder,'total_actual_ss.csv')
    expenditure_table=os.path.join(expenditure_folder,'expenditure.csv')
    phd_student_table=os.path.join(phd_student_folder,'phd_student.csv')
    image_file_path=os.path.join(image_dir,'parms.png')
    
    return clg_pdf_path,clg_json_file_path,sanctioned_intake_table,total_actual_ss_table,expenditure_table,phd_student_table,image_file_path





def extract_clg_name(text_string):
    string_list=text_string.split('|')
    string_list=string_list[0].split(',')
    name=string_list[0]
    return name 


def scores_extraction(html_tag):
    table_tag= html_tag.find(class_='table')
    table_body=table_tag.find("tbody")
    score_tags=table_body.find_all("td")
    scores=[tag.text for tag in score_tags if tag.name is not None]
    return scores


def get_pdf_url(html_tag):
    href_tag= html_tag.find_all("a")
    return href_tag[2].get('href')

def get_image_url(html_tag):
    href_tag= html_tag.find_all("a")
    return href_tag[3].get('href')

def download_file(url,file_path):
    response=requests.get(url)
    with open(file_path,'wb') as file:
        file.write(response.content)

def main():
    # nirf link
    output_dir='output'
    try:
        os.mkdir(output_dir)
    except:
    print("OUTPUT DIR ALREADY CREATED")
    with open('data.json','r') as json_file:
        table_structure=json.load(json_file)
    table_data=table_structure["data"]

    responsee= requests.get('https://www.nirfindia.org/2023/EngineeringRanking.html')

    html_text=responsee.text 
    soup= BeautifulSoup(html_text, 'html.parser')
    # class of pdf links



    table= soup.find(id="tbl_overall")
    college_tag_list=table.find_all("tr")

    college_tag_list=college_tag_list[1::3]




    for college in tqdm(college_tag_list):

        clg_details=college.children
        immediate_children = [child for child in clg_details if child.name is not None]
        # print(len(immediate_children))
        # extracting_clg_name


        # webpage details
        clg_name=extract_clg_name(immediate_children[1].text)
        clg_city=immediate_children[2].text
        clg_state=immediate_children[3].text
        clg_score= immediate_children[4].text
        TLR, RPC,GO, OI,PERCEPTION =scores_extraction(immediate_children[1])

        # print(f"""
        #     ----------------------
        #     name :{clg_name},
        #     city:{clg_city},
        #     state:{clg_state},
        #     score:{clg_score}
        #     TLR:{TLR},
        #     RPC:{RPC},
        #     GO:{GO},
        #     OI:{OI},
        #     PERCEPTION:{PERCEPTION}
        #     -----------------------
        #     """)

        
        #Creation of the file structure 
        clg_dir_name=clg_name.replace(' ','-')
        clg_pdf_path,clg_json_file_path,sanctioned_intake_table,total_actual_ss_table,expenditure_table,phd_student_table,image_file_path =creating_required_directories(clg_dir_name,output_dir)
    


        
        # pdf_downloading
        pdf_url= get_pdf_url(immediate_children[1])
        image_url= get_image_url(immediate_children[1])
        download_file(pdf_url,clg_pdf_path)
        download_file(image_url,image_file_path)
        
        #pdf reading
        pdf_content=pdf_extraction(clg_pdf_path)

        # Sanctioned_Intake
            # start 
            # end 
            # ------------------------> pdf_content
            # output ----------> string collection of data
        # saction_table_data=table_data['sanction_table']
        start="Academic Year 2021-22 2020-21 2019-20 2018-19 2017-18 2016-17"
        end="Total Actual Student Strength (Program(s) Offered by your Institution)"

        programme_names=saction_table_generator(pdf_content,start,end,sanctioned_intake_table)
        start='Government'
        end='Placement & Higher Studies'
        total_actual_ss_data=table_data['Total_actual_student_strength']
        total_actual_ss_data_column=total_actual_ss_data['horizontal_heading']
        total_actual_ss_generator(pdf_content,start,end, total_actual_ss_table, total_actual_ss_data_column,programme_names)
        financial_table_extractor(pdf_content,path=expenditure_table)

        start='Ph.D (Student pursuing doctoral program till 2021-22)'
        # try:
        phd_student_extraction(pdf_content,start,phd_student_table)
        # except:
            #print(clg_dir_name)
        # saving data in sanctioned_intake_folder

        website_detail={
            "name" :clg_name,
            "city":clg_city,
            "state":clg_state,
            "score":clg_score,
            "TLR":TLR,
            "RPC":RPC,
            "GO":GO,
            "OI":OI,
            "PERCEPTION":PERCEPTION,
            "FACULTY_MEMBERS":number_of_faculty_members(pdf_content)
            }

        with open(clg_json_file_path,'w') as json_file:
            json.dump(website_detail, json_file)
            

            # dir creation
        # Total_Actual_Student_Strength 


    
        
if __name__ =='__main__':
    main()





    


 





    




    

