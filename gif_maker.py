from moviepy.editor import VideoFileClip
movie_input_file = 'vid.mp4'
output_gif_file = 'vid.gif'

clip = VideoFileClip(movie_input_file)
clip.write_gif(output_gif_file)