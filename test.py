from dotenv import load_dotenv
from cellphone import SamsungS20FEController, OppoReno7Controller
from computer import AcerT9300Controller
from computer import AsusA550VController
from computer import MsiM16Controller
from base.logger import Logger
import os

# 載入環境變數
load_dotenv()

def samsungS20FE(scenario: int):
    samsung = os.environ.get("SAMSUNG_DEVICE_NAME")
    controller = SamsungS20FEController(samsung)
    controller.enable_wifi()

    if scenario == 1:
        controller.watch_predefined_youtube_videos(30)
    elif scenario == 2:
        controller.download_web_file(10)
    elif scenario == 3:
        controller.play_spotify_music(60)
    elif scenario == 4:
        controller.join_google_meet(30)
    elif scenario == 5:
        controller.send_gmail()
    elif scenario == 6:
        controller.view_specific_webpages(5)
    elif scenario == 7:
        controller.upload_google_drive_file(10)
    elif scenario == 8:
        controller.download_google_drive_file(10)
    elif scenario == 9:
        controller.start_skype_call(10)

    controller.disable_wifi()
    return


def oppoReno7(scenario: int):
    oppo = os.environ.get("OPPO_DEVICE_NAME")
    controller = OppoReno7Controller(oppo)
    controller.enable_wifi()

    if scenario == 1:
        controller.watch_predefined_youtube_videos(30)
    elif scenario == 2:
        controller.download_web_file(10)
    elif scenario == 3:
        controller.play_spotify_music(10)
    elif scenario == 4:
        controller.join_google_meet(30)
    elif scenario == 5:
        controller.send_gmail()
    elif scenario == 6:
        controller.view_specific_webpages(5)
    elif scenario == 7:
        controller.upload_google_drive_file(10)
    elif scenario == 8:
        controller.download_google_drive_file(10)
    elif scenario == 9:
        controller.start_skype_call(10)

    controller.disable_wifi()
    return


def acerT9300(scenario: int):
    controller = AcerT9300Controller()
    controller.enable_wifi()

    if scenario == 1:
        controller.watch_predefined_youtube_videos(10)
    elif scenario == 2:
        controller.download_web_file()
    elif scenario == 3:
        controller.play_spotify_music(5)
    elif scenario == 4:
        controller.join_google_meet()
    elif scenario == 5:
        controller.send_gmail()
    elif scenario == 6:
        controller.view_specific_webpages(5)
    elif scenario == 7:
        controller.upload_google_drive_file()
    elif scenario == 8:
        controller.download_google_drive_file()
    elif scenario == 9:
        controller.start_skype_call(5, 'acerT9300_tester')

    controller.disable_wifi()
    return


def asusA550v(scenario: int):
    controller = AsusA550VController()
    controller.enable_wifi()

    if scenario == 1:
        controller.watch_predefined_youtube_videos(10)
    elif scenario == 2:
        controller.download_web_file()
    elif scenario == 3:
        controller.play_spotify_music(5)
    elif scenario == 4:
        controller.join_google_meet()
    elif scenario == 5:
        controller.send_gmail()
    elif scenario == 6:
        controller.view_specific_webpages(5)
    elif scenario == 7:
        controller.upload_google_drive_file()
    elif scenario == 8:
        controller.download_google_drive_file()
    elif scenario == 9:
        controller.start_skype_call(5, 'asusA550v_tester')

    controller.disable_wifi()
    return


def msiM16(scenario: int):
    controller = MsiM16Controller()
    controller.get_cursor_position()
    # controller.enable_wifi()

    # if scenario == 1:
    #     controller.watch_predefined_youtube_videos(10)
    # elif scenario == 2:
    #     controller.download_web_file()
    # elif scenario == 3:
    #     controller.play_spotify_music(5)
    # elif scenario == 4:
    #     controller.join_google_meet()
    # elif scenario == 5:
    #     controller.send_gmail()
    # elif scenario == 6:
    #     controller.view_specific_webpages(5)
    # elif scenario == 7:
    #     controller.upload_google_drive_file()
    # elif scenario == 8:
    #     controller.download_google_drive_file()
    # elif scenario == 9:
    #     controller.start_skype_call(5, 'msiM16_tester')

    # controller.disable_wifi()
    return


def main():
    # scenario_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] # 總共9個場景

    # random_index = random.randint(0, len(scenario_list)-1)
    # value = scenario_list[random_index]
    # samsungS20FE(value)
    # scenario_list.remove(value)

    # random_index = random.randint(0, len(scenario_list)-1)
    # value = scenario_list[random_index]
    # oppoReno7(value)
    # scenario_list.remove(value)

    # random_index = random.randint(0, len(scenario_list)-1)
    # value = scenario_list[random_index]
    # acerT9300(value)
    # scenario_list.remove(value)

    # random_index = random.randint(0, len(scenario_list)-1)
    # value = scenario_list[random_index]
    # asusA550v(value)
    # scenario_list.remove(value)

    oppoReno7(4)
    # samsungS20FE(9)

if __name__ == "__main__":
    logger = Logger('WPA3DataSet', 'main')
    main()
