def make_album(artist, title, num=None):
    album = {
        'artist': artist,
        'title': title
    }
    if (num):
        album['num'] = num
    return album

print(make_album('metallica', 'ride the lightning'))
print(make_album('beethoven', 'ninth symphony'))
print(make_album('willie nelson', 'red-headed stranger', 0))

print("Please input an artist and a title. If you want to end the input, please input q. ")
while True:
    artist = input("Please input an artist: ")
    if artist == 'q':
        break
    title = input("Please input a title: ")
    if artist == 'q':
        break
    print(make_album(artist, title))