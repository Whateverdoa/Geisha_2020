

import pandas as pd

file_in = r"C:\Users\mike\PycharmProjects\Geisha_2020\source\file_in\2012000469_totaal.csv"
file_out= r"C:\Users\mike\PycharmProjects\Geisha_2020\source\file_out\2012000469.csv"

df = pd.read_csv(file_in,";", dtype="str", index_col='Artnr')

print(df.head(10))

artikel_nummers_verzameld=df.groupby('Artnr').sum()

artikel_nummers_verzameld.to_csv("arg.csv", encoding='utf-8')

df.Aantal.sum() # aantal totale order

aantal_rollen = len(df)
print(aantal_rollen)

print(df.columns)

indexlijst= df.index

print(indexlijst)

art_lijst = []
count = 1
art_lijst.append(f'{df.index[0]}')  # hard coded eerste regel
for i in range(1, aantal_rollen):

    if df.index[i] != df.index[i - 1]:
        count += 1

        art_lijst.append(f'{df.index[i]}')

print(art_lijst)
aantal_art = len(art_lijst)
print(aantal_art)
len(df.groupby('Artnr').sum())

# this returns the number of artnr
counter = 0
for num in range(1, aantal_rollen):
    counter += 1

    if df.index[num] != df.index[num - 1]:
        print(df.index[num])
        print(counter)
        counter = 0


# this generates the csv files
a = 0
b = 7
for x in range(0, aantal_art):
    df.iloc[a:b].to_csv(f"{x}.csv", ";")

    a += 7
    b += 7


def print__rolls(Aantal, beeld, colorname, Artnr, file_out):
    """
    Take line from list and build csv for that line
    """

    with open(file_out, "a", encoding="utf-8") as fn:
        # open a file to append the strings too
        # print(f".;stans.pdf\n", end='', file=fn)

        print(f'{Artnr} {colorname}: {Aantal} etiketten;leeg.pdf\n', end="", file=fn)
        # these  lines encapsulate the artikel en size
        print(f";{beeld}" * int(Aantal), end="", file=fn)
        # this line prints the actual beeld.pdf without extra

        print(f"{Artnr} {colorname}: {Aantal} etiketten;leeg.pdf\n", end="", file=fn)
        # these  lines encapsulate the artikel en size

        print(f";stans.pdf\n", end="", file=fn)
        # this line seperates the Sizes by a blanco etiket



def rolling_thunder(csv_in, fileout):
    """

    :param dataf: dataframe
    :param fileout: csv-file uit lijst
    :return: csv
    """

    new_input_list = []

    with open(csv_in) as input:
        num = 0
        for line in input:
            line_split = line.split(";")

            new_input_list.append(line_split)
            num += 1
    # print(new_input_list)
    list_length = len(new_input_list)

    beg = 1
    eind = 2

    # with open(fileout, 'a', encoding='utf-8') as fh:


        # print(";geel.pdf\n" * 8, end='', file=fh)
        # # this line seperates the Artikels by a a yellow "wikkel"
        # df_csv = pd.read_csv(csv_in, delimiter=";", usecols=['Artnr', 'beeld', 'Aantal', 'Size', 'ColorN'])
        # artikel_som = sum(df_csv.Aantal)
        # artikel = df_csv.Artnr[0]
        # print(f"{artikel_som} van {artikel};leeg.pdf\n", end='', file=fh)
        # print(";geel.pdf\n" * 8, end='', file=fh)

    with open(file_out, 'a', encoding='utf-8') as fh:
        for _ in range(list_length - 1):
            a = int(new_input_list[beg:eind][0][6])
            b = str(new_input_list[beg:eind][0][7])
            c = str(new_input_list[beg:eind][0][3])
            d = str(new_input_list[beg:eind][0][0])

            print__rolls(a, b, c, d, file_out)

            beg += 1
            eind += 1

    with open(file_out, 'a', encoding='utf-8') as geel:
        print(";geel.pdf\n" * 8, end='', file=geel)
        # this line seperates the Artikels by a a yellow "wikkel"
        df_csv = pd.read_csv(csv_in, delimiter=";", usecols=['Artnr', 'beeld', 'Aantal', 'Size', 'ColorN'])
        artikel_som = sum(df_csv.Aantal)
        artikel = df_csv.Artnr[0]
        print(f"{artikel_som} van {artikel};leeg.pdf\n", end='', file=geel)
        print(";geel.pdf\n" * 8, end='', file=geel)

txt_list = [f"{name}.csv" for name in range(aantal_art)]

# print(txt_list[0:24])
#
with open(file_out, "w") as fileout:
    print("aantal;beeld", file=fileout)

    for file in txt_list:
        rolling_thunder(file, file_out)

# open("tmp/df_csv_met_split_files.csv","w", encoding='utf-8')
# with open("tmp/df_csv_met_split_files.csv","a",encoding="utf-8") as hele_order:
#
#
#     for file in txt_list:
#         df_csv = pd.read_csv(file, delimiter=";", usecols=['Artnr', 'beeld', 'Aantal', 'Size', 'ColorN'])
#         new_df = f'{file}_{sum(df_csv.Aantal[0:7])}'
#         new_df_a = f'{file}_{sum(df_csv.Aantal[0:3])}_a'
#         new_df_b = f'{file}_{sum(df_csv.Aantal[3:5])}_b'
#         new_df_c = f'{file}_{sum(df_csv.Aantal[5:7])}_c'
#
#         if sum(df_csv.Aantal) > 5000:
#             print(f'csv_file: {file} ===> {df_csv.Artnr[0]} --> {sum(df_csv.Aantal)}')
#             new_df_a = pd.DataFrame(df_csv[0:3])
#             new_df_b = pd.DataFrame(df_csv[3:5])
#             new_df_c = pd.DataFrame(df_csv[5:7])
#             print(new_df_a, file=hele_order)
#             print(new_df_b)
#             print(new_df_c)
#
#     #         print(f'{df_csv.Artnr[0:3]} > {df_csv.Aantal[0:3]} --->  {sum(df_csv.Aantal[0:3])}-----> {df_csv.Size[0:3]}\n')
#     #         print()
#     #         print(f'{df_csv.Artnr[3:5]} > {df_csv.Aantal[3:5]} --->  {sum(df_csv.Aantal[3:5])}-----> {df_csv.Size[3:5]}\n')
#     #         print()
#     #         print(f'{df_csv.Artnr[5:7]} > {df_csv.Aantal[5:7]} --->  {sum(df_csv.Aantal[5:7])}-----> {df_csv.Size[5:7]}\n')
#     #         print()
#         else:
#             print(f'csv_file: {file} ===> {df_csv.Artnr[0]} --> {sum(df_csv.Aantal)}')
#             new_df = pd.DataFrame(df_csv[0:7])
#             print(new_df)
#
#


with open(file_out, "w") as fileout:
    print("aantal;beeld", file=fileout)

    for file in txt_list:
        rolling_thunder(file, file_out)
