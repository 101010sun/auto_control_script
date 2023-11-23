from cellphone import SamsungS20FEController
from computer import WindowsComputerController
import random


def samsungS20FE(scenario: int):
    controller = SamsungS20FEController()
    controller.enable_wifi()

    # if scenario == 1:
    #     controller.watch_predefined_youtube_videos(5)
    # elif scenario == 2:
    #     controller.download_web_file()
    # elif scenario == 3:
    #     controller.play_spotify_music(60)
    # elif scenario == 4:
    #     controller.join_google_meet(3)
    # elif scenario == 5:
    #     controller.send_gmail()
    # elif scenario == 6:
    #     controller.view_specific_webpages(5)
    # elif scenario == 7:
    #     controller.upload_google_drive_file()
    # elif scenario == 8:
    #     controller.download_google_drive_file()
    # elif scenario == 9:
    #     controller.start_skype_call(30)

    controller.disable_wifi()
    return


def windowsPC():
    controller = WindowsComputerController()
    # controller.start_skype_call(5)
    # controller.play_spotify_music(5)
    # controller.watch_predefined_youtube_videos(5)
    # controller.download_web_file()
    controller.join_google_meet()


def main():
    # scenario_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] # 總共9個場景
    # random_index = random.randint(0, len(scenario_list)-1)
    # value = scenario_list[random_index]
    # samsungS20FE(value)
    # scenario_list.remove(value)
    windowsPC()


if __name__ == "__main__":
    main()