
class ControllerBase:
    def watch_predefined_youtube_videos(self, playTime: int):
        return 
    

    def download_web_file(self):
        return
    

    def play_spotify_music(self, playTime: int):
        return
    

    def join_google_meet(self):
        return


    def send_gmail(self):
        return
    

    def view_specific_webpages(self, playTime: int):
        return
    

    def start_skype_call(self, playTime: int):
        return
    

    def upload_google_drive_file(self):
        return


    def download_google_drive_file(self):
        return
    

    def process_scenario(self, scenario: int):
        if scenario == 1:
            self.watch_predefined_youtube_videos(10)
        elif scenario == 2:
            self.download_web_file()
        elif scenario == 3:
            self.play_spotify_music(5)
        elif scenario == 4:
            self.join_google_meet()
        elif scenario == 5:
            self.send_gmail()
        elif scenario == 6:
            self.view_specific_webpages(5)
        elif scenario == 7:
            self.upload_google_drive_file()
        elif scenario == 8:
            self.download_google_drive_file()
        elif scenario == 9:
            self.start_skype_call(5)
    
    