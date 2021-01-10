# import csv
# import pickle
# def get_csv():
#     # with open('book-list.csv', newline='') as csvfile:
#     #     book_list = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     #     for row in book_list:
#     #         print(', '.join(row))
#     # print(type(book_list))
#     titles = []
#     amazon_price= []
#     # titles_dict ={}
#     with open('book-list.csv') as csvfile:
#         reader = csv.DictReader(csvfile)
#         print(type(reader))
#         print(reader)
#         for row in reader:
#             # print(row['TITLE'])
#             titles.append(row['TITLE'])
#             amazon_price.append(row['$ AMAZON'])
#     # print(amazon_price)
#     cleaned_price_dict = set(amazon_price)
#     cleaned_price = list(cleaned_price_dict)
#     # print(cleaned_price)  
#     # print(titles)
#     # print(titles_dict)

#     # print(titles)
#     cd = set(titles)
#     # print(cd)
#     # words = titles.strip('')
#     # print(words)
#     cleaned_list = list(cd)
#     # print(cleaned_list)
#     # print(type(cleaned_list))
#     # list_dict = {}
#     # for item in cleaned_list:
#     #     for i in range(len(cleaned_list)):
#     #         list_dict['title'] = (item)

#     # print(list_dict)
#     # print(dict(cleaned_list))
#     # print(dict.fromvalue(cleaned_list, 'title'))

#     # title_dic = {titled : "title" for titled in cleaned_list}

#     # print(title_dic)

#     cleaned_list_dic = {'title': cleaned_list, 'amazon price': cleaned_price}
#     print(cleaned_list_dic)

#     # try: 
#     #     geeky_file = open('geekyfile.txt', 'wt') 
#     #     geeky_file.write(str(cleaned_list_dic)) 
#     #     geeky_file.close() 
    
#     # except: 
#     #     print("Unable to write to file")

# get_csv()