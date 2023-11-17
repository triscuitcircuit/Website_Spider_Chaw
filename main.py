import requests
import os
import argparse
def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--website", default="http://aturing.umcs.maine.edu/~sudarshan.chawathe",
                        help="The URL of Chaw's current website")
    parser.add_argument("--course", default="cos350",
                        help="Course number")
    parser.add_argument("--save_folder", default="previous_course",
                        help="Save folder name")

    args = parser.parse_args()

    website = args.website
    save_folder = args.save_folder
    course = args.course
    #Fall courses start in 09, Spring: 01
    semester_list = [
        "202309",
        "202209",
        "202109",
        "201601",
        "201701",
        "201801",
        "201901",
    ]

    if not os.path.exists(f"{save_folder}"):
        os.mkdir(f"{save_folder}")
        for folder in semester_list:
            os.mkdir(f"{save_folder}/{folder}")

    work_list = ["ce", "hw", "q", "mt"]

    counter = 0

    for year in semester_list:
        for selection in work_list:
            work_iter = 1
            link = (
                "{}/{}/{}/hwq/{}{:0>2}.pdf"
                .format(website, year,course,selection, work_iter))

            pdf_response = requests.get(link)
            while pdf_response.status_code == 200:
                counter += 1
                save_location = "{}/{}".format(save_folder, year)
                if not os.path.exists(save_location):
                    os.mkdir(save_location)
                with open('{}/{}-{}.pdf'.format(save_location, selection, work_iter), 'wb') as pdf_file:
                    pdf_file.write(pdf_response.content)
                work_iter += 1
                link = (
                    "{}/{}/{}/hwq/{}{:0>2}.pdf"
                    .format(website,year, course,selection, work_iter))
                pdf_response = requests.get(link)
    print(f"Saved {counter} files")
if __name__ == "__main__":
    main()