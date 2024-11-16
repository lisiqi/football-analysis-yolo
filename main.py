from utils.video_utils import read_video, save_video

def main():
    # read video
    frames = read_video("input_videos/football.mp4")
    # save video
    save_video(frames, "output_videos/football_output.mp4")


if __name__ == "__main__":
    main()
