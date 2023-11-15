from cellphone_controller_samsungs20fe import SamSungS20FEController


def samsungS20fe():
    controller = SamSungS20FEController()
    # controller.watch_predefined_youtube_videos(5)
    # controller.download_web_file()
    # controller.play_spotify_music(60)
    # controller.join_google_meet(3)
    # controller.send_gmail()
    controller.view_specific_webpages(5)
    # controller.upload_google_drive_file()
    # controller.download_google_drive_file()


def main():
    samsungS20fe()


if __name__ == "__main__":
    main()