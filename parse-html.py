from bs4 import BeautifulSoup
import os
import io
import re


dir_path = r'D:\python\reference\en'
out_dir = r'D:\python\reference_modification\en'

for root, dirs, files in os.walk(dir_path):
    for file_name in files:
        with io.open(os.path.join(root, file_name), encoding='utf-8') as html_file:
            soup = BeautifulSoup(html_file, 'html.parser')
            print(html_file)
            if soup.title:
                soup.title.decompose()
            if soup.find("div", {"id": "siteSub"}): #From cppreference.com
                soup.find("div", {"id": "siteSub"}).decompose()
            if soup.find("div", {"id": "catlinks"}): #Hidden category. With link to cppreverence.com
                soup.find("div", {"id": "catlinks"}).decompose()
            if soup.find("div", {"id": "contentSub"}): #For example "< cpp‎ | io" in top on a page
                soup.find("div", {"id": "contentSub"}).decompose()
            if soup.find("div", {"class": "t-navbar"}): #Navigation bar
                soup.find("div", {"class": "t-navbar"}).decompose()
            if soup.find("tr", {"class": "t-rev t-until-cxx11"}): #Remove string in a table with (Until C++11)
                soup.find("tr", {"class": "t-rev t-until-cxx11"}).decompose()
            if soup.find("span", {"id": "Example"}): #Remove string "Example"
                soup.find("span", {"id": "Example"}).decompose()
            if soup.find("div", {"class": "t-example"}): #Remove Examples
                soup.find("div", {"class": "t-example"}).decompose()
            if soup.find("span", {"id": "See_also"}): #Remove string "See also"
                soup.find("span", {"id": "See_also"}).decompose()
#            if soup.find("table", {"class": "t-dsc-begin"}): #table "t-dsc-begin" class occurs in many places. Delete?
#                soup.find("table", {"class": "t-dsc-begin"}).decompose()
            if soup.find("span", {"id": "Possible_implementation"}): ##Remove string "Possible implementation"
                soup.find("span", {"id": "Possible_implementation"}).decompose()
            if soup.find("table", {"class": "eq-fun-cpp-table"}): #Remove table after "Possible implementation"
                soup.find("table", {"class": "eq-fun-cpp-table"}).decompose()
            if soup.find("div", {"class": "printfooter"}): #Retrieved from + link to cppreverence.com
                soup.find("div", {"class": "printfooter"}).decompose()
            if soup.find("span", {"id": "Defect_reports"}): #Remove string "Defect reports"
                soup.find("span", {"id": "Defect_reports"}).decompose()
            if soup.find("table", {"class": "dsctable"}): #Remove table after "Defect reports"
                soup.find("table", {"class": "dsctable"}).decompose()
            if soup.find("span", {"id": "References"}): #Remove string "References"
                soup.find("span", {"id": "References"}).decompose()
            if soup.find("div", {"class": "t-ref-std-c++11"}): #Remove text after "References"
                soup.find("div", {"class": "t-ref-std-c++11"}).decompose()
            if soup.find("span", {"id": "Example_With_Comparator"}): # Remove string "Example With Comparator"
                soup.find("span", {"id": "Example_With_Comparator"}).decompose()
            if soup.find("div", {"class": "coliru-btn coliru-btn-run-init"}):
                soup.find("div", {"class": "coliru-btn coliru-btn-run-init"}).decompose()
#            if soup.find("pre", {"class": "de1"}): # Headers synopsys. Delete?
#               soup.find("pre", {"class": "de1"}).decompose()
            if soup.find_all("span", {"class": re.compile(r't-mark-rev t-since-(c|cxx)(11|14|17)')}): #Only text since C/C++ 11,14,17
                for i in soup.find_all("span", {"class": re.compile(r't-mark-rev t-since-(c|cxx)(11|14|17)')}):
                    i.decompose()
            if soup.find_all("span", {"class": re.compile(r't-mark-rev t-until-(c|cxx)(14|17)')}): #Only text until C/C++ 14,17
                for j in soup.find_all("span", {"class": re.compile(r't-mark-rev t-until-(c|cxx)(14|17)')}):
                    j.decompose()

        results_file = os.path.splitext(file_name)[0] + '.html'

        with io.open(os.path.join(root, file_name), 'w', encoding='utf-8') as outfile:
            outfile.write(soup.prettify())