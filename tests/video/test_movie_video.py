from panda3d.core import MovieVideo
from panda3d.core import Filename
from panda3d.core import MovieVideoCursor
import os
import pytest
from panda3d.core import PandaSystem
from panda3d.core import MovieTexture

def check_ffmpeg():
    movie_path = os.path.join(os.path.dirname(__file__), "small.mp4")
    movie_path = Filename.from_os_specific(movie_path) #platform independent path
    reference_file = MovieVideo.get(movie_path)
    reference_file.open()
    system = PandaSystem.get_global_ptr()
    has_ffmpeg = 'FFmpeg' in system.systems #checks whether ffmpeg is loaded
    if has_ffmpeg is True:
        return True
    else:
        return False

@pytest.mark.skipif(check_ffmpeg() is False, reason="skip when ffmpeg is not available")
class Test_Video_Movie():
    def test_cursor_check(self):
        movie_path = os.path.join(os.path.dirname(__file__), "small.mp4")
        movie_path = Filename.from_os_specific(movie_path) # enables Platform independent testing
        reference_file = MovieVideo.get(movie_path)
        assert reference_file.get_filename() == movie_path
        assert reference_file.open() is not None

    def test_video_length(self):
        movie_path = os.path.join(os.path.dirname(__file__), "small.mp4")
        movie_path = Filename.from_os_specific(movie_path) # enables Platform independent testing
        reference_file = MovieVideo.get(movie_path)
        cursor = reference_file.open()
        assert cursor.length() == 32.4800

    def test_video_size(self):
        movie_path = os.path.join(os.path.dirname(__file__), "small.mp4")
        movie_path = Filename.from_os_specific(movie_path) # enables Platform independent testing
        reference_file = MovieVideo.get(movie_path)
        cursor = reference_file.open()
        assert cursor.size_x() == 640 #found the height and width using mkvinfo
        assert cursor.size_y() == 360