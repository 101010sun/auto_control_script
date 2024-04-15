import json

class ControllerBase:
    def _get_json_data(self, key: str):
        with open("url_list.json", "r") as f:
            file = json.load(f)
            word = file[key]
            return word
        
    def watch_predefined_youtube_videos(self, playTime: int):
        return

    def download_web_file(self, waitTime: int):
        return

    def play_spotify_music(self, playTime: int):
        return

    def join_google_meet(self, playTime: int):
        return

    def send_gmail(self):
        return

    def view_specific_webpages(self, playTime: int):
        return

    def start_skype_call(self, playTime: int):
        return

    def upload_google_drive_file(self, waitTime: int):
        return

    def download_google_drive_file(self, waitTime: int):
        return

    def process_scenario(self, scenario: int):
        if scenario == 1:
            self.watch_predefined_youtube_videos(180)
        elif scenario == 2:
            self.download_web_file(180)
        elif scenario == 3:
            self.play_spotify_music(180)
        elif scenario == 4:
            self.join_google_meet(180)
        elif scenario == 5:
            self.send_gmail()
        elif scenario == 6:
            self.view_specific_webpages(180)
        elif scenario == 7:
            self.upload_google_drive_file(180)
        elif scenario == 8:
            self.download_google_drive_file(180)
        elif scenario == 9:
            self.start_skype_call(180)
