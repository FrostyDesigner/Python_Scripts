import pandas
import os
import re

def parse_data(_src_file, _dest_file):
    #create empty dataframe
    df = pandas.DataFrame(columns=["_fullname","_filedate","_filesize"])
    # read the file back as a list of lines
    dest_file=_dest_file
    src_file=_src_file
    fin = open(src_file, "r")
    data_list = fin.readlines()
    fin.close()
    #type(data_list)
    #print(data_list)

    #loop attempt
    i=0
    cur_dir=None
    for line in data_list:
        # line=line.replace("\n","")
        line=line.strip(' \t\n\r')
        searchObj = re.search( r'\d\d/\d\d/\d\d\d\d\s\s\d\d:\d\d\s\w\w', line, re.M|re.I)
        #if value is not found in string...
        #if line.find("Directory of") == -1:
        #if value is found in string...
        if line.find("Directory of") >= 0:
            cur_dir=line.replace("Directory of ","")
            #print(cur_dir)
        #else if the search object is true
        elif searchObj:
            #we found the date but we need to remove the directories
            #.find returns index or -1 if None
            if line.find("  <DIR>  ") >= 0:
                # print("false - no wanty directories.")
                continue
            else:
                # !!! searchObj.group() is the returned matching results
                # print("regex!", searchObj.group())
                # but we want the entire line
                split_list=line.split(None,4)
                file_date=split_list[0]
                file_time=split_list[1]
                file_meridiem=split_list[2]
                file_size=split_list[3]
                file_name=split_list[4]
                full_name=os.path.join(cur_dir,file_name)
                df=df.append({"_fullname":full_name, "_filedate":file_date, "_filesize":file_size}, ignore_index=True)
                #print(df)
        # elif line =="":
        #     print("false - no wanty blank lines.")
        else:
            #print("Else!")
            continue
        i=i+1

    print(df)
    df.to_csv(dest_file)