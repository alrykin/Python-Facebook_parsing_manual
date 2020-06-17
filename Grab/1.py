# -*- coding: utf-8 -*-
from grab import Grab
from tqdm import tqdm
import re
import time

# получаем количество страниц с объявлениями
def get_pages(g, url):

        
        while g.doc.select('//*[@id="reaction_profile_pager1"]/div/a').text() != ' ':
                More_url = g.doc.select('//*[@id="reaction_profile_pager1"]/div/a').attr('href')
                g.go(More_url)

        try:                
                pages = g.doc.select('//*[@id="reaction_profile_browser1"]/li/div/div/div/div[1]/div[2]/div/a').attr('href')
                pages.append(g.doc.select('//*[@id="reaction_profile_browser2"]/li/div/div/div/div[1]/div[2]/div/a').attr('href'))      
                pages.append(g.doc.select('//*[@id="reaction_profile_browser3"]/li/div/div/div/div[1]/div[2]/div/a').attr('href'))      
                pages.append(g.doc.select('//*[@id="reaction_profile_browser4"]/li/div/div/div/div[1]/div[2]/div/a').attr('href'))
        except:
                print(pages)
                return pages    

def get_url_List(name, searched_part_begin, searched_part_end):
        
        f = open(name + '.txt', 'r')
        adress = []
        str = f.read()
        while str.find(searched_part_begin) > -1:
            begin = str.find(searched_part_begin)+1
            end = str.find(searched_part_end,begin+6)
            if adress.count(str[begin:end]) == 0:
                adress.append(str[begin:end])
            str = str[end:]
        print(name)
        print(adress)
        f.close()
        return adress


def main():
        names = ['LOB19input','OLEROMinput','ISAACinput']
        for name in names:
                
                MarkLists = get_url_List(name, 'href="/ufi/reaction/profile/browser/?ft_ent_identifier=', '"')
                g = Grab()
                g.setup(encoding='utf-8', connect_timeout=3, timeout=5)

                f = open(name+'.csv', 'wt', encoding="utf-8")
                f.write('"url";"name";"@mail";"phone";"sites";"city";"birth data";"gender"'+'\n')
                for MarkList in MarkLists:
                        pages = get_pages(g, MarkList)
                        for page in tqdm(range(int(pages))):
                                g.go(page)
                                # получаем имя
                                p_name = g1.doc.select()('//*[@id="fb-timeline-cover-name"]/a').text()

                                # пробуем получить остальные данные
                                info_url = page.select('//*[@id="u_0_y"]/li[2]/a').attr('href')
                                g1 = Grab()
                                g1.go(info_url)
                                mainInfo_url = page.select('//*[@id="pagelet_timeline_app_collection_100001823140355:2327158227:8"]/ul/li/div/div[1]/div/div/ul/li[1]/a').attr('href')
                                g1.go(mainInfo_url)
                                if g1.doc.select('//*[@id="u_1i_0"]/div/div[2]/span/div[2]/span').exists():
                                                p_phone = g1.doc.select('//*[@id="u_1i_0"]/div/div[2]/span/div[2]/span').text()
                                else: p_phone = ''

                                if g1.doc.select('//*[@id="u_fetchstream_3_r"]/div/div[2]/span/div[2]/a').exists():
                                        p_email = g1.doc.select('//*[@id="u_fetchstream_3_r"]/div/div[2]/span/div[2]/a').text()
                                else: p_email = ''
                                
                                if g1.doc.select('//*[@id="u_fetchstream_3_t"]/div[2]/ul/li[3]/div/div[2]/span/div[2]').exists():
                                        p_DateOfBirth = g1.doc.select('//*[@id="u_fetchstream_3_t"]/div[2]/ul/li[3]/div/div[2]/span/div[2]').text()
                                else: p_DateOfBirth = ''

                                if g1.doc.select('//*[@id="u_x_1"]/div/div/div/div[1]/a').exists():
                                        p_city = g1.doc.select('//*[@id="u_x_1"]/div/div/div/div[1]/a').text()
                                else: p_city = ''

                                contactInfo_url = item.select('//*[@id="pagelet_timeline_app_collection_100001823140355:2327158227:8"]/ul/li/div/div[1]/div/div/ul/li[4]/a').attr('href')
                                g1.go(contactInfo_url)

                                if g1.doc.select('//*[@id="pagelet_basic"]/div/ul/li[2]/div/div[2]/div/div/span').exists():
                                        p_gender = g1.doc.select('//*[@id="pagelet_basic"]/div/ul/li[2]/div/div[2]/div/div/span').text()
                                else: p_gender = ''

                                if g1.doc.select('//*[@id="pagelet_contact"]/div/div[2]/div/ul/li/div/div[2]/div/div/span/ul/li/ul').exists():
                                        p_sites= g1.doc.select('//*[@id="pagelet_contact"]/div/div[2]/div/ul/li/div/div[2]/div/div/span/ul/li/ul').text()
                                else: p_sites = ''
                                f.write('"'+page+'";"'+p_name+'";"'+p_email+'";"'+p_phone+'";"'+p_sites+'";"'+p_city+'";"'+p_DateOfBirth+'"'+p_gender+'"'+'\n')
                        f.close()

                        
                                
                        

if __name__ == "__main__":
    main()
