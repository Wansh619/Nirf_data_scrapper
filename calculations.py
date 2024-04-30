import pandas as pd

def calculate_Nt(path):
    Nt=0
    df= pd.read_csv(path)
    columns=df.columns[1:]

    for col in columns:
        for i in df[col]:
            # print(i)
            try:
                Nt+=int(i)
            except:
                Nt+=0
    return Nt



def calculate_Ne(path):
    Ne=0
    df= pd.read_csv(path)
    col='Total Students'

    for i in df[col]:
        try:
            Ne+=int(i)
        except:
            Ne+=0
    return Ne


def calculate_Np(path):
    Np=0
    df= pd.read_csv(path)
    columns=df.columns
    # print(columns)

    for col in columns:
        for i in df[col]:
            # print(i)
            try:
                Np+=int(i)
            except:
                Np+=0
    return Np





def calculate_CE_OE(path):
    df=pd.read_csv(path)
    # print(df.columns)
    columns=df.columns[1:]
    # col_BO=df.columns[1:]
    dict_CE={}
    dict_OE={}
    for col in columns:
        dict_CE[col]=0
        dict_OE[col]=0
        for i in df[col][0:2]:
            try:
                dict_CE[col]+=int(i)
            except:
                dict_CE[col]+=0
        for i in df[col][4:]:
            try:
                dict_OE[col]+=int(i)
            except:
                dict_OE[col]+=0
    # print(dict_OE,dict_CE)
    return dict_CE,dict_OE





if __name__=='__main__':
    print(calculate_BC_BO('output\Aligarh-Muslim-UniversityMore-DetailsClose-\expenditure\expenditure.csv'))