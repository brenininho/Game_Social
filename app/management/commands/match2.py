from time import sleep

from django.core.management import BaseCommand
from django.db.models import Count
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from app.models import Account, Participant, Summoner, Match, Item, Champion, Map, GameMode


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        path = "/home/breno/Área de Trabalho/Python Projects/GameAnalytics/chromedriver"
        page = 'https://www.leagueofgraphs.com/pt/'
        chrome_option = Options()
        # chrome_option.add_argument("--headless")
        # chrome_option.add_argument("--no-sadbox")
        # chrome_option.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(path, options=chrome_option)
        driver.get(page)
        accept_cookies = WebDriverWait(driver, 60).until(ec.presence_of_element_located((
            By.XPATH, '//*[@id="ncmp__tool"]/div/div/div[3]/div[1]/button[2]'
        )))
        accept_cookies.click()
        search_summoner = WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.XPATH, '//*[@id="homepageForm"]/input')))
        search_summoner.send_keys("brenininho2")

        search_button = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="homepageForm"]/button')))
        search_button.click()

        recent_matches = driver.find_element(By.CLASS_NAME, 'recentGamesTableHeaderTitle')

        recent_matches_filter = driver.find_element(By.CLASS_NAME, 'recentGamesFilterExpander')
        recent_matches_filter.click()

        recent_games_filter = driver.find_element(By.ID, 'recentGamesFilterQueueType')
        recent_games_filter.click()

        match_history = driver.find_element(By.TAG_NAME, 'tbody')
        trs = match_history.find_elements(By.TAG_NAME, 'tr')

        link_list = self.get_links(trs, match_history)
        print(link_list)
        for link in link_list:
            print(link)

        self.register_match(driver, link_list)

    def get_links(self, trs, match_history):
        link_list = []
        for tr in trs:
            if tr.get_attribute('class') != 'recentGamesTableHeader hide-for-dark' \
                    and tr.get_attribute('class') != 'recentGamesTableHeader filtersBlock':

                if tr.get_attribute('class') == 'see_more_ajax_button_row':

                    see_more = tr.find_element(By.CLASS_NAME, 'see_more_ajax_button')
                    see_more.click()
                    sleep(2)

                    trs = match_history.find_elements(By.TAG_NAME, 'tr')

                    links = self.get_links(trs, match_history)
                    for link in links:
                        if link not in link_list:
                            link_list.append(link)
                    break

                champion_cell = tr.find_element(By.CLASS_NAME, 'championCellLight')
                match_detail = WebDriverWait(champion_cell, 10).until(
                    ec.presence_of_element_located((By.TAG_NAME, 'a')))
                link = match_detail.get_attribute('href')
                if link not in link_list:
                    link_list.append(link)

        return link_list

    def register_match(self, driver, link_list):
        for link in link_list:
            driver.get(link)

            match_table = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.CLASS_NAME, 'data_table')))
            player_rows = match_table.find_elements(By.CLASS_NAME, "playerRow")

            participant_list = []
            for player_row in player_rows:
                # participant right register
                text_left = player_row.find_element(By.CLASS_NAME, "text-left")
                match_status_left = match_table.find_element(
                    By.XPATH, '//*[@id="mainContent"]/div[1]/div/div[1]/div/div[1]/table/tbody/tr[1]/th[1]/span[1]'
                )

                champion_img = text_left.find_element(By.TAG_NAME, "img")
                champion_name = champion_img.get_attribute('alt')  # champion name

                summoner_name_div = text_left.find_element(By.CLASS_NAME, "name")
                summoner_content = summoner_name_div.get_attribute('innerHTML')
                summoner_name = summoner_content.strip()  # summoner name
                champion_level = text_left.find_element(By.CLASS_NAME, "level").text  # champion level

                div_kda = player_row.find_element(By.CLASS_NAME, 'kda')
                kills_left = div_kda.find_element(By.CLASS_NAME, 'kills').text  # kills
                deaths_left = div_kda.find_element(By.CLASS_NAME, 'deaths').text  # deaths
                assists_left = div_kda.find_element(By.CLASS_NAME, 'assists').text  # assists

                td_items_left = player_row.find_element(By.CLASS_NAME, 'itemsColumn')
                imgs_left = td_items_left.find_elements(By.TAG_NAME, 'img')
                items_instance_left = []  # items
                for img in imgs_left:
                    item_name = img.get_attribute('alt')
                    try:
                        item_instance = Item.objects.get(name=item_name)
                        items_instance_left.append(item_instance.id)
                    except:
                        item_instance = Item.objects.create(name=item_name)
                        items_instance_left.append(item_instance.id)

                try:
                    summoner_instance_left = Summoner.objects.get(name=summoner_name)
                except:
                    summoner_instance_left = Summoner.objects.create(name=summoner_name)

                if match_status_left.text.casefold() == "vitória":
                    match_status_left = True
                else:
                    match_status_left = False

                try:
                    champion_instance = Champion.objects.get(name=champion_name)
                except:
                    champion_instance = Champion.objects.create(name=champion_name)

                participant_left_object = Participant.objects.filter(summoner=summoner_instance_left, kills=kills_left,
                                                                     assists=assists_left, deaths=deaths_left,
                                                                     champ_level=champion_level, champion=champion_instance,
                                                                     teamid="red", win=match_status_left,
                                                                     item__in=items_instance_left).annotate(num_tags=Count('item')).filter(num_tags=len(items_instance_left))

                if participant_left_object.exists():
                    participant_list.append(participant_left_object[0].id)
                    print('participante já existe')
                else:
                    try:
                        participant_left = Participant.objects.create(summoner=summoner_instance_left, kills=kills_left,
                                                                      assists=assists_left, deaths=deaths_left,
                                                                      champ_level=champion_level, champion=champion_instance,
                                                                      teamid="red", win=match_status_left)

                        participant_left.item.set(items_instance_left)

                        participant_list.append(participant_left.id)
                        pass
                    except Exception as e:
                        print(f"não foi possível registrar participante {e}")

                # ------------------------------------ Right Participant ------------------------------------

                # participant right register
                text_right = player_row.find_element(By.CLASS_NAME, "text-right")
                match_status_right = match_table.find_element(
                    By.XPATH, '//*[@id="mainContent"]/div[1]/div/div[1]/div/div[1]/table/tbody/tr[1]/th[1]/span[2]'
                )

                champion_img_right = text_right.find_element(By.TAG_NAME, "img")
                champion_name_right = champion_img_right.get_attribute('alt')  # champion name

                summoner_name_div_right = text_right.find_element(By.CLASS_NAME, "name")
                summoner_content_right = summoner_name_div_right.get_attribute('innerHTML')
                summoner_name_right = summoner_content_right.strip()  # summoner name
                champion_level_right = text_right.find_element(By.CLASS_NAME, "level").text  # champion level

                div_kda_right = player_row.find_element(
                    By.XPATH, '//*[@id="mainContent"]/div[1]/div/div[1]/div/div[1]/table/tbody/tr[2]/td[5]/div[1]'
                )
                kills_right = div_kda_right.find_element(By.CLASS_NAME, 'kills').text  # kills
                deaths_right = div_kda_right.find_element(By.CLASS_NAME, 'deaths').text  # deaths
                assists_right = div_kda_right.find_element(By.CLASS_NAME, 'assists').text  # assists

                td_items_right = player_row.find_element(By.CLASS_NAME, 'itemsColumn-200')
                imgs_right = td_items_right.find_elements(By.TAG_NAME, 'img')
                items_list_right = []  # items
                for img in imgs_right:
                    item_name = img.get_attribute('alt')
                    try:
                        item_instance_right = Item.objects.get(name=item_name)
                        items_list_right.append(item_instance_right.id)
                    except:
                        item_instance_right = Item.objects.create(name=item_name)
                        items_list_right.append(item_instance_right.id)

                try:
                    summoner_instance_right = Summoner.objects.get(name=summoner_name_right)
                except:
                    summoner_instance_right = Summoner.objects.create(name=summoner_name_right)

                if match_status_right.text.casefold() == "vitória":
                    match_status_right = True
                else:
                    match_status_right = False

                try:
                    champion_instance_right = Champion.objects.get(name=champion_name_right)
                except Exception as e:
                    champion_instance_right = Champion.objects.create(name=champion_name_right)
                    print(f'Champion registered: {champion_name_right}')
                participant_right_object = Participant.objects.filter(summoner=summoner_instance_right,
                                                                      kills=kills_right,
                                                                      assists=assists_right, deaths=deaths_right,
                                                                      champ_level=champion_level_right,
                                                                      champion=champion_instance_right,
                                                                      teamid="blue", win=match_status_right,
                                                                      item__in=items_list_right,).annotate(num_tags=Count('item')).filter(num_tags=len(items_list_right))
                if participant_right_object.exists():
                    participant_list.append(participant_right_object[0].id)
                    print('participante já existe')
                else:
                    try:
                        participant_right = Participant.objects.create(summoner=summoner_instance_right,
                                                                       kills=kills_right,
                                                                       assists=assists_right, deaths=deaths_right,
                                                                       champ_level=champion_level_right,
                                                                       champion=champion_instance_right,
                                                                       teamid="blue", win=match_status_right)

                        participant_right.item.set(items_list_right)
                        participant_list.append(participant_right.id)
                        pass
                    except Exception as e:
                        print(f"não foi possível registrar participante {e}")

            # game_mode = driver.find_element(
            #     By.XPATH, '//*[@id="mainContent"]/div[1]/div/div[1]/div/div[1]/table/tbody/tr[1]/th[3]/span[1]'
            # )
            game_mode = GameMode.objects.get(name="CLASSIC")
            platform = 'br1'
            default_map = Map.objects.get(name="Summoner's Rift", description="Current Version")

            match_object = Match.objects.filter(game_mode=game_mode, platform=platform, map=default_map,
                                                participant__in=participant_list).annotate(num_attr=Count('participant')).filter(num_attr=len(participant_list))

            if match_object.exists():
                print(f'This match already exists {match_object}')
            else:
                match_object = Match.objects.create(game_mode=game_mode, platform=platform, map=default_map)

                match_object.participant.set(participant_list)
                print(f"Match registered: {match_object}")

