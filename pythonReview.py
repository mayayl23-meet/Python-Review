def create_youtube_video(title,description):
	videodict = {"title":title, "description":description, "likes":0, "dislikes":0, "comments": {"username":{}}}
	return videodict

	

def like(youtubevideo):
	if "likes" in youtubevideo:
		youtubevideo["likes"] += 1

		return youtubevideo


def dislike(youtubevideo):
	if "dislikes" in youtubevideo:
		youtubevideo["dislikes"] += 1

		return youtubevideo



def add_comment(youtubevideo, username, comment_text):
	videodict=youtubevideo
	videodict['comments']['username'] = comment_text

	return youtubevideo

dict1 = create_youtube_video("a","b")
like(dict1)
dislike(dict1)
add_comment(dict1, "maya", "hello")

print(dict1)


newvideodict = {"title": 'How To Make Coffee', "description": 'a short video about how to make the best coffee', "likes": 495, "dislikes": 0, "comments":{"maya":{'so interesting'}}}

