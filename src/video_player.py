"""A video player class."""
import random

from .video_library import VideoLibrary

class VideoPlayer:
    """A class used to represent a Video Player."""

    cnt_video = None
    state = None
    playlist = {}
    flagged = {}

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        list_videos = self._video_library.get_all_videos()

        for row_videos in list_videos:
            video_id = row_videos.video_id

            if row_videos.video_id in self.flagged:
                print(f"{row_videos._title} ({video_id}) [{row_videos._tags}] - FLAGGED (reason: {self.flagged.get(video_id)})")
            else:
                print(f"{row_videos._title} ({video_id}) [{row_videos._tags}]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        video = self._video_library.get_video(video_id)

        if video == None:
            print("Cannot play video: Video does not exist")

        else:
            if video_id in self.flagged:
                print(f"Cannot play video: Video is currently flagged (reason: {self.flagged.get(video_id)})")

            else:
                if self.cnt_video != None:
                    self.stop_video()
                    print(f"Playing video: {video.title}")
                    self.cnt_video = video_id
                    self.state = "Play"

                else:
                    print(f"Playing video: {video.title}")
                    self.cnt_video = video_id
                    self.state = "Play"

    def stop_video(self):
        """Stops the current video."""
        video = self._video_library.get_video(self.cnt_video)

        if self.cnt_video == None:
            print("Cannot stop video: No video is currently playing")

        else:
            print(f"Stopping video: {video.title}")
            self.cnt_video = None
            self.state = None

    def play_random_video(self):
        """Plays a random video from the video library."""

        list_videos = self._video_library.get_all_videos()
        video = random.choice(list_videos)

        if video.video_id in self.flagged or self.cnt_video == video.video_id:
            self.play_random_video()
        else:
            self.play_video(video.video_id)

    def pause_video(self):
        """Pauses the current video."""

        video = self._video_library.get_video(self.cnt_video)

        if self.cnt_video == None:
            print("Cannot pause video: No video is currently playing")
        else:
            if self.state == "Pause":
                print(f"Video already paused: {video.title}")
                self.stop_video()
                self.state = None
            else:
                print(f"Pausing video: {video.title}")
                self.state = "Pause"

    def continue_video(self):
        """Resumes playing the current video."""

        video = self._video_library.get_video(self.cnt_video)

        if self.state == "Play":
            print("Cannot continue video: Video is not paused")

        elif self.state == "Pause":
            print(f"Continuing video: {video.title}")
            self.state = "Play"

        else:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""

        video = self._video_library.get_video(self.cnt_video)

        if self.state == "Play":
            print(f"Currently playing: {video.title} {video.video_id} {video.tags}")

        elif self.state == "Pause":
            print(f"Currently playing: {video.title} {video.video_id} {video.tags} - PAUSED")

        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        if playlist_name not in self.playlist:
            self.playlist.update({playlist_name: []})
            print(f"Successfully created new playlist: {playlist_name}")
        else:
            print("Cannot create playlist: A playlist with the same name already exists")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """

        video = self._video_library.get_video(video_id)

        if playlist_name not in self.playlist:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")

        else:
            if video == None:
                print(f"Cannot add video to {playlist_name}: Video does not exist")

            else:
               if video.video_id in self.flagged:
                   print(f"Cannot add video to {playlist_name}: Video is currently flagged (reason: {self.flagged.get(video_id)})")
               else:
                   if video_id in self.playlist[playlist_name]:
                       print(f"Cannot add video to {playlist_name}: Video already added")
                   else:
                       self.playlist[playlist_name].append(video_id)
                       print(f"Added video to {playlist_name}: {video.title}")

    def show_all_playlists(self):
        """Display all playlists."""

        if len(self.playlist) == 0:
            print("No playlists exist yet")
        else:
            print("Showing all playlists: ")
            for key in self.playlist:
                print(f"    {key}")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        if playlist_name in self.playlist:
            if len(self.playlist[playlist_name]) != 0:
                for values in self.playlist[playlist_name]:
                    video = self._video_library.get_video(values)
                    video_id = video.video_id

                    if video.video_id in self.flagged:
                        print(f"    {video.title} ({video_id}) [{video.tags}] - FLAGGED (reason: {self.flagged.get(video_id)})")
                    else:
                        print(f"    {video.title} ({video_id}) [{video.tags}]")
            else:
                print("    No videos are here yet")
        else:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """

        video = self._video_library.get_video(video_id)

        if playlist_name not in self.playlist:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")

        else:
            if video == None:
                print(f"Cannot remove video from {playlist_name}: Video does not exist")

            else:
                if video_id not in self.playlist[playlist_name]:
                    print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
                else:
                    self.playlist[playlist_name].remove(video_id)
                    print(f"Removed video from {playlist_name}: {video.title}")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        if playlist_name not in self.playlist:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
        else:
            self.playlist[playlist_name].clear()
            print(f"Successfully removed all videos from {playlist_name}")
            self.show_playlist(playlist_name)

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        if playlist_name not in self.playlist:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")
        else:
            del self.playlist[playlist_name]
            print(f"Deleted playlist: {playlist_name}")

    def play_input(self, video):
        """Input the corresponding number of a video."""

        new_input = input("Would you like to play any of the above? If yes, specify the number of the video. "
                           "If your answer is not a valid number, we will assumes it's a no. \n")

        if new_input in video:
            self.play_video(video.get(new_input))

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        list_videos = self._video_library.get_all_videos()
        search_set = set()
        search = []
        count = 0
        play = {}

        for row_videos in list_videos:
            video_id = row_videos._video_id
            search_set.add(video_id)
            search = [s for s in search_set if search_term.lower() in s]

            for each in search:
                if each in self.flagged:
                    search.remove(each)

        if search == []:
            print(f"No search results for {search_term}")

        else:
            for each in search:
                video = self._video_library.get_video(each)
                count += 1
                print(f"{count}) {video.title} ({video.video_id}) [{video.tags}]")
                play.update({str(count): video.video_id})
            self.play_input(play)

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """

        list_videos = self._video_library.get_all_videos()
        set_set = dict()
        search = []
        count = 0
        play = {}

        for row_videos in list_videos:
           tags = row_videos._tags
           video_id = row_videos._video_id
           set_set.update({video_id: list(tags)})

        for key, value in set_set.items():
            if video_tag in value:
                search.append(key)

                for each in search:
                    if each in self.flagged:
                        search.remove(each)

        if search == []:
            print(f"No search results for {video_tag}")

        else:
            for each in search:
                video = self._video_library.get_video(each)
                count += 1
                print(f"{count}) {video.title} ({video.video_id}) [{video.tags}]")
                play.update({str(count): video.video_id})
            self.play_input(play)

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """

        video = self._video_library.get_video(video_id)

        if flag_reason == "":
            flag_reason = "Not supplied"

        if video == None:
            print("Cannot flag video: Video does not exist")

        else:
            if video_id in self.flagged:
                print("Cannot flag video: Video is already flagged")

            else:
                if self.cnt_video != None:
                    self.stop_video()
                    print(f"Successfully flagged video: {video.title} (reason: {flag_reason})")
                    self.flagged.update({video_id: flag_reason})

                else:
                    print(f"Successfully flagged video: {video.title} (reason: {flag_reason})")
                    self.flagged.update({video_id: flag_reason})

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """

        video = self._video_library.get_video(video_id)

        if video == None:
            print("Cannot remove flag from video: Video does not exist")
        else:
            if video_id not in self.flagged:
                print("Cannot remove flag from video: Video is not flagged")
            else:
                print(f"Successfully removed flag from video: {video.title}")
                del self.flagged[video_id]
