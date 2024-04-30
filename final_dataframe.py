import os
import json
from image_text_extractor import text_extractor
from calculations import *
from functions import *
from tqdm import tqdm




FINAL_DATAFRAME_DICT={

    "College Name":[],
    "Total Sanctioned Intake(Nt)":[],
    "Total Actual Students(Ne)":[],
    "Total Ph.D Students(Np)":[],
    "N":[],
    "Total Faculties":[],
    "CE_2021-22":[],
    "CE_2020-21":[],
    "CE_2019-20":[],
    "OE_2021-22":[],
    "OE_2020-21":[],
    "OE_2019-20":[],

    "Total Capital Expenditure(BC)":[],
    "Total Operational Expenditure(BO)":[],
    "FSR_cal":[],
    "FRU_cal":[],
    #-----------------------------
    #TLR
    "SS_tv(20)":[],
    "FSR_tv(30)":[],
    "FQE_tv(20)":[],
    "FRU_tv(30)":[],
    "TLR_tv(100)":[],
    #-----------------------------
    #RP
    "PU_tv(35)":[],
    "QP_tv(40)":[],
    "IPR_tv(15)":[],
    "FPPP_tv(10)":[],
    "RP_tv(100)":[],
    #-----------------------------
    #GO
    "GPH_tv(40)":[],
    "GUE_tv(15)":[],
    "MS_tv(25)":[],
    "GPHD_tv(20)":[],
    "GO_tv(100)":[],
    #------------------------------
    #OI
    "RD_tv(30)":[],
    "WD_tv(30)":[],
    "ESCS_tv(20)":[],
    "PCS_tv(20)":[],
    "OI_tv(100)":[],
    #------------------------------
    #PR
    "PR_tv(100)":[],
    #------------------------------
    #Final Score
    "Score_tv(100)":[],
}

def main():
    output_dir='output'
    clg_dirs=os.listdir(output_dir)
    for dir in tqdm(clg_dirs):
        json_file=os.path.join(output_dir,dir,'clg_data.json')
        sanction_intake_table=os.path.join(output_dir,dir,'sanctioned_intake','sanctioned_intake.csv')
        total_actual_ss=os.path.join(output_dir,dir,'total_actual_ss','total_actual_ss.csv')
        expenditure_table=os.path.join(output_dir,dir,'expenditure','expenditure.csv')
        phd_student=os.path.join(output_dir,dir,'phd_student','phd_student.csv')
        image_file=os.path.join(output_dir,dir,'parm_image','parms.png')
        with open(json_file) as file:
            clg_data=json.load(file)
        
        Nt=calculate_Nt(sanction_intake_table)
        Ne=calculate_Ne(total_actual_ss)
        Np=calculate_Np(phd_student)
        try:
            CE,OE=calculate_CE_OE(expenditure_table)
        except:
            print("not done")
        BC=0
        BO=0
        for i in CE.keys():
            try:
                FINAL_DATAFRAME_DICT['CE_'+str(i)].append(CE[i]/Nt)
            except Exception as e:
                # print("CE-----------",e)
                FINAL_DATAFRAME_DICT['CE_'+str(i)]=[CE[i]/Nt]
            BC+=float(CE[i]/(Nt*3))
        for i in OE.keys():
            try:
                FINAL_DATAFRAME_DICT['OE_'+str(i)].append(OE[i]/Nt)
            except Exception as e:
                # print("OE-----------",e)
                FINAL_DATAFRAME_DICT['OE_'+str(i)]=[OE[i]/Nt]
            BO+=float(OE[i]/(Nt*3))

        try:
            img_data=text_extractor(image_file)
        except Exception as e:
            print(e)

        FINAL_DATAFRAME_DICT['College Name'].append(clg_data['name'])
        FINAL_DATAFRAME_DICT['Total Sanctioned Intake(Nt)'].append(Nt)
        FINAL_DATAFRAME_DICT['Total Actual Students(Ne)'].append(Ne)
        FINAL_DATAFRAME_DICT['Total Ph.D Students(Np)'].append(Np)
        FINAL_DATAFRAME_DICT['Total Faculties'].append(clg_data['FACULTY_MEMBERS'])
        FINAL_DATAFRAME_DICT['Total Capital Expenditure(BC)'].append(BC)
        FINAL_DATAFRAME_DICT['Total Operational Expenditure(BO)'].append(BO)

        FINAL_DATAFRAME_DICT['N'].append(Nt+Np)
        FINAL_DATAFRAME_DICT['FSR_cal'].append(FSR(F = int (clg_data['FACULTY_MEMBERS']),N = Nt+Np))
        FINAL_DATAFRAME_DICT['FRU_cal'].append(FRU(BC,BO))
        #---------------------------------------------------------------------------
        #TLR
        FINAL_DATAFRAME_DICT["SS_tv(20)"].append(img_data['SS'])
        FINAL_DATAFRAME_DICT["FSR_tv(30)"].append(img_data['FSR'])
        FINAL_DATAFRAME_DICT["FQE_tv(20)"].append(img_data['FQE'])
        FINAL_DATAFRAME_DICT["FRU_tv(30)"].append(img_data['FRU'])

        tlr=float(img_data['SS'])+float(img_data['FSR'])+float(img_data['FQE'])+float(img_data['FRU'])
        FINAL_DATAFRAME_DICT["TLR_tv(100)"].append(tlr)
        #---------------------------------------------------------------------------
        #RP
        FINAL_DATAFRAME_DICT["PU_tv(35)"].append(img_data['PU'])
        FINAL_DATAFRAME_DICT["QP_tv(40)"].append(img_data['QP'])
        FINAL_DATAFRAME_DICT["IPR_tv(15)"].append(img_data['IPR'])
        FINAL_DATAFRAME_DICT["FPPP_tv(10)"].append(img_data['FPPP'])

        rp=float(img_data['PU'])+float(img_data['QP'])+float(img_data['IPR'])+float(img_data['FPPP'])
        FINAL_DATAFRAME_DICT["RP_tv(100)"].append(rp)
        #---------------------------------------------------------------------------
        #GO
        FINAL_DATAFRAME_DICT["GPH_tv(40)"].append(img_data['GPH'])
        FINAL_DATAFRAME_DICT["GUE_tv(15)"].append(img_data['GUE'])
        FINAL_DATAFRAME_DICT["MS_tv(25)"].append(img_data['MS'])
        FINAL_DATAFRAME_DICT["GPHD_tv(20)"].append(img_data['GPHD'])

        go=float(img_data['GPH'])+float(img_data['GUE'])+float(img_data['MS'])+float(img_data['GPHD'])
        FINAL_DATAFRAME_DICT["GO_tv(100)"].append(go)
        #---------------------------------------------------------------------------
        #OI
        FINAL_DATAFRAME_DICT["RD_tv(30)"].append(img_data['RD'])
        FINAL_DATAFRAME_DICT["WD_tv(30)"].append(img_data['WD'])
        FINAL_DATAFRAME_DICT["ESCS_tv(20)"].append(img_data['ESCS'])
        FINAL_DATAFRAME_DICT["PCS_tv(20)"].append(img_data['PCS'])

        oi=float(img_data['RD'])+float(img_data['WD'])+float(img_data['ESCS'])+float(img_data['PCS'])
        FINAL_DATAFRAME_DICT["OI_tv(100)"].append(oi)
        #----------------------------------------------------------------------------
        #PR
        FINAL_DATAFRAME_DICT["PR_tv(100)"].append(clg_data['PERCEPTION'])
        pr=float(clg_data['PERCEPTION'])
        #----------------------------------------------------------------------------
        #Score
        FINAL_DATAFRAME_DICT["Score_tv(100)"].append(0.3*tlr+0.3*rp+0.2*go+0.1*oi+0.1*pr)
    # for i in FINAL_DATAFRAME_DICT.keys():
        # print(f"{i}---------{len(FINAL_DATAFRAME_DICT[i])}")   
    output_data_frm=pd.DataFrame(FINAL_DATAFRAME_DICT)
    output_data_frm.to_csv('final_extracted_data.csv',index=False)


   
if __name__=='__main__':
    main()























